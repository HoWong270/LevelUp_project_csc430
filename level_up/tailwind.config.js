    /** @type {import('tailwindcss').Config} */
    module.exports = {
        content: [  "./templates/**/*.html",
        ],
        safelist: ['button', 'primary', 'secondary', 'danger','mb-4'],
        theme: {},
        plugins: [
          require("@tailwindcss/forms"),
          require("@tailwindcss/typography"),
        ],
      }