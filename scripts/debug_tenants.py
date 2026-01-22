import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        port=os.environ.get('DB_PORT')
    )
    return conn

def check_tenants():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        print("--- Checking Tenant Data ---")
        cur.execute("SELECT id, full_name, email, room_number, bed_number FROM tenants")
        tenants = cur.fetchall()
        
        if not tenants:
            print("No tenants found.")
        else:
            print(f"{'Name':<20} | {'Email':<30} | {'Room':<10} | {'Bed':<10}")
            print("-" * 80)
            for t in tenants:
                print(f"{t[1]:<20} | {t[2]:<30} | {str(t[3]):<10} | {str(t[4]):<10}")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    check_tenants()
