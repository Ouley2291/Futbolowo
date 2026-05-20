tailwind.config = {
    theme: {
        extend: {
            colors: {
                forest: {
                    950: '#030d06',
                    900: '#071810',
                    800: '#0d2b1a',
                    700: '#133d25',
                    600: '#1a5233',
                    500: '#216640',
                    400: '#2e8b57',
                    300: '#3dab6b',
                    200: '#6fcf97',
                    100: '#a8e6c1',
                    50:  '#d4f5e3',
                },
            },
            fontFamily: {
                display: ['"Bebas Neue"', 'sans-serif'],
                body:    ['"DM Sans"', 'sans-serif'],
            },
            keyframes: {
                pulsedot: {
                    '0%, 100%': { opacity: '1',  transform: 'scale(1)'   },
                    '50%': { opacity: '0.4', transform: 'scale(0.65)' },
                },
            },
            animation: {
                pulsedot: 'pulsedot 1.4s ease-in-out infinite',
            },
        },
    },
};
