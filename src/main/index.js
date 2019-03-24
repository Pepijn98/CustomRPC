import {
    BrowserWindow,
    app,
    ipcMain
} from "electron";

const config = require("electron-json-config");
const DiscordRPC = require("discord-rpc");
const rpc = new DiscordRPC.Client({ transport: "ipc" });
let activity = {};
let clientId = "416357849153929226";

const dialog = require("electron").dialog || require("electron").remote.dialog;

/**
 * Set `__static` path to static files in production
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html
 */
if (process.env.NODE_ENV !== "development") {
    global.__static = require("path").join(__dirname, "/static").replace(/\\/g, "\\\\");
}

let forceQuit = false;
let mainWindow = null;
const winURL = process.env.NODE_ENV === "development" ? "http://localhost:9080" : `file://${__dirname}/index.html`;

function createWindow() {
    /**
     * Initial window options
     */
    mainWindow = new BrowserWindow({
        height: 563,
        useContentSize: true,
        width: 1000,
        resizable: false
    });

    mainWindow.loadURL(winURL);

    mainWindow.on("close", (e) => {
        if (!forceQuit) {
            e.preventDefault();

            dialog.showMessageBox({
                type: "question",
                title: "Question",
                message: "Save Data",
                detail: "Do you want to save the current date for next time?",
                buttons: ["Yes", "No"]
            }, (response) => {
                if (response === 0) {
                    mainWindow.webContents.send("close:request");
                } else {
                    forceQuit = true;
                    rpc.destroy();
                    app.quit();
                }
            });
        }
    });

    mainWindow.on("closed", () => {
        mainWindow = null;
    });
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});

app.on("activate", () => {
    if (mainWindow === null) {
        createWindow();
    }
});

const validateData = (data) => {
    if (!data.rpcData.details) {
        dialog.showMessageBox({
            type: "warning",
            title: "Warning",
            message: "Invalid Property",
            detail: "Details is required to set a rich presence activity",
            buttons: ["Ok"]
        });

        return false;
    }

    if (!data.rpcData.state) {
        dialog.showMessageBox({
            type: "warning",
            title: "Warning",
            message: "Invalid Property",
            detail: "State is required to set a rich presence activity",
            buttons: ["Ok"]
        });

        return false;
    }

    activity = {
        details: data.rpcData.details,
        state: data.rpcData.state,
        largeImageKey: "large_image",
        instance: false
    };

    if (data.custom.appId) {
        clientId = data.custom.appId;

        if (data.custom.largeImageName) {
            activity.largeImageKey = data.custom.largeImageName;
        }

        if (data.custom.smallImageName) {
            activity.smallImageKey = data.custom.smallImageName;
        }
    }

    if (data.rpcData.largeImageText) {
        activity.largeImageText = data.rpcData.largeImageText;
    }

    if (data.rpcData.smallImageText) {
        activity.smallImageText = data.rpcData.smallImageText;
    }

    return activity;
};

const isEmpty = (obj) => {
    for (let key in obj) {
        if (obj.hasOwnProperty(key))
            return false;
    }
    return true;
};

ipcMain.on("app:ready", (event) => {
    const data = config.all();
    if (!data || isEmpty(data)) {
        return null;
    }

    event.sender.send("app:data", data);
});

ipcMain.on("rpc:start", async (event, data) => {
    const a = validateData(data);
    if (!a) {
        event.sender.send("start:failed");
        return null;
    }

    await rpc.login({ clientId }).catch(console.error);

    rpc.setActivity(a);

    event.sender.send("start:success");
});

ipcMain.on("rpc:update", (_, data) => {
    const a = validateData(data);
    if (!a) return null;

    rpc.setActivity(a);
});

ipcMain.on("rpc:stop", () => {
    rpc.clearActivity();
});

ipcMain.on("close:response", (_, data) => {
    config.purge();
    config.setBulk(data);

    forceQuit = true;
    rpc.destroy();
    app.quit();
});

/**
 * Auto Updater
 *
 * Uncomment the following code below and install `electron-updater` to
 * support auto updating. Code Signing with a valid certificate is required.
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-electron-builder.html#auto-updating
 */

// import { autoUpdater } from 'electron-updater'
// autoUpdater.on('update-downloaded', () => {
// autoUpdater.quitAndInstall()
// })
// app.on('ready', () => {
// if (process.env.NODE_ENV === 'production') autoUpdater.checkForUpdates()
// })
