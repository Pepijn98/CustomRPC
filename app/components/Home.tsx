/* eslint-disable global-require, prefer-const */

import React from "react";
import styles from "./Home.css";

export default function Home(): JSX.Element {
    let ui: any;
    let primaryColor = "#66a3df";
    let dangerColor = "#e10000";
    // let temp = "win32";
    // switch (temp) {
    switch (process.platform) {
        case "darwin":
            primaryColor = "blue";
            ui = require("react-desktop/macOs");
            break;
        case "win32":
            ui = require("react-desktop/windows");
            break;
        default:
            ui = require("./linux");
            break;
    }

    const { Button } = ui;

    return (
        <div className={styles.container} data-tid="container">
            <h2>Home</h2>
            <Button color={primaryColor} onClick={() => console.log("Clicked")}>
                Start
            </Button>
            <Button color={dangerColor} onClick={() => console.log("Clicked")} style={{ marginLeft: "5px" }}>
                Stop
            </Button>
        </div>
    );
}
