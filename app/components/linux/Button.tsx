/* eslint-disable react/jsx-props-no-spreading, react/button-has-type, react/no-string-refs */

import React, { Component } from "react";
import styles from "./Button.css";

type Props = {
    type: "button" | "submit" | "reset" | undefined;
    color: string;
    style: any;
    onClick: () => void;
};

class Button extends Component<Props> {
    render() {
        const { type, color, onClick, children, style, ...props } = this.props;

        return (
            // prettier-ignore
            // eslint-disable-next-line prettier/prettier
            <button
                ref="element"
                type={type || "button"}
                onClick={onClick}
                className={styles["btn-linux"]}
                style={{ backgroundColor: color, ...style }}
                {...props}>
                {children}
            </button>
        );
    }
}

export default Button;
