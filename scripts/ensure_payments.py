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

def run_migration():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        schema_path = os.path.join('database_schemas', '04_add_payments.sql')
        with open(schema_path, 'r') as f:
            sql = f.read()
            
        print(f"Executing migration: {schema_path}")
        cur.execute(sql)
        conn.commit()
        print("Migration successful.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    run_migration()
