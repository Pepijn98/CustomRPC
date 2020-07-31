/* eslint-disable react/jsx-props-no-spreading, react/button-has-type, react/no-string-refs */

import React, { Component } from "react";
import styles from "./Button.css";

type Props = {
    type: "button" | "submit" | "reset" | undefined;
    onClick: () => void;
};

class Button extends Component<Props> {
    render() {
        const { type, onClick, children, ...props } = this.props;

        return (
            <button ref="element" type={type || "button"} onClick={onClick} className={styles["btn-linux"]} {...props}>
                {children}
            </button>
        );
    }
}

export default Button;
