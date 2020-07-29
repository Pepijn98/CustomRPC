module.exports = {
    root: true,
    env: {
        node: true
    },
    parserOptions: {
        ecmaVersion: 10,
        parser: "@typescript-eslint/parser"
    },
    plugins: ["@typescript-eslint/eslint-plugin"],
    extends: ["plugin:@typescript-eslint/eslint-recommended", "plugin:@typescript-eslint/recommended", "prettier", "prettier/@typescript-eslint", "react-app"],
    rules: {
        // TypeScript eslint options
        "@typescript-eslint/explicit-function-return-type": [
            "error",
            {
                allowExpressions: true
            }
        ],
        "@typescript-eslint/interface-name-prefix": "off",
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/no-non-null-assertion": "off",
        "@typescript-eslint/no-unused-vars": "off",
        "@typescript-eslint/no-var-requires": "off",

        // General eslint options
        "eol-last": ["error", "always"],
        "indent": [
            "error",
            4,
            {
                SwitchCase: 1
            }
        ],
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
