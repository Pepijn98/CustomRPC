import React from "react";
import App from "./app";
import { Renderer } from "@nodegui/react-nodegui";

process.title = "My NodeGui App";
Renderer.render(<App />);
// This is for hot reloading (this will be stripped off in production by webpack)
if (module.hot) {
    module.hot.accept(["./app"], function () {
        Renderer.forceUpdate();
    });
}
