    /** @type {import('tailwindcss').Config} */
    module.exports = {
        content: [  "./templates/**/*.html",
                    "./static/**/*.js",
                    "./**/*.py"
        ],
        safelist: ['button', 'primary', 'secondary', 'danger'],
        theme: {
          extend: {},
        },
        plugins: [
          require("@tailwindcss/forms"),
          require("@tailwindcss/typography"),
        ],
      }