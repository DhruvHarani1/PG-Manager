module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/**/*.py',
    './src/**/*.html',
  ],
  theme: {
    extend: {
      animation: {
        shine: 'shine 1s',
      },
      keyframes: {
        shine: {
          '100%': { left: '125%' },
        },
      },
    },
  },
  plugins: [],
};
