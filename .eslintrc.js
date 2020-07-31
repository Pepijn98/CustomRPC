module.exports = {
    plugins: ["@typescript-eslint/eslint-plugin"],
    extends: [
        "erb/typescript",
        "plugin:@typescript-eslint/eslint-recommended",
        "plugin:@typescript-eslint/recommended",
        "plugin:prettier/recommended",
        "prettier/@typescript-eslint"
    ],
    parserOptions: {
        ecmaVersion: 2020,
        sourceType: "module",
        project: "./tsconfig.json",
        tsconfigRootDir: __dirname,
        createDefaultProgram: true
    },
    settings: {
        "import/resolver": {
            // See https://github.com/benmosher/eslint-plugin-import/issues/1396#issuecomment-575727774 for line below
            node: {},
            webpack: {
                config: require.resolve("./configs/webpack.config.eslint.js")
            }
        },
        "import/parsers": {
            "@typescript-eslint/parser": [".ts", ".tsx"]
        }
    },
    rules: {
        // A temporary hack related to IDE not resolving correct package.json
        "import/no-extraneous-dependencies": "off",
        "eol-last": ["error", "always"],
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/no-var-requires": "off",
        "@typescript-eslint/explicit-module-boundary-types": "off",
        "react/jsx-indent": ["error", 4],
        "react/jsx-indent-props": ["error", 4],
        "react/jsx-closing-bracket-location": [1, "after-props"],
        "indent": [
            "error",
            4,
            {
                SwitchCase: 1
            }
        ],
        "no-console": "off",
        "no-undef": "off",
        "quotes": [
            "error",
            "double",
            {
                avoidEscape: true
            }
        ],
        "semi": ["error", "always"],
        "semi-spacing": "error",
        "semi-style": ["error", "last"]
    }
};
