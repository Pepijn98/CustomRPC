<template>
    <main>
        <el-collapse v-model="activeNames">
            <el-collapse-item title="Rich Presence Data" name="1">
                <div class="collapse-item-inner">
                    <el-input v-model="rpcData.details" placeholder="details" clearable />
                    <el-input v-model="rpcData.state" placeholder="state" clearable />
                    <el-input v-model="rpcData.largeImageText" placeholder="large image text" clearable />
                    <el-input v-model="rpcData.smallImageText" placeholder="small image text" clearable />
                </div>
            </el-collapse-item>
            <el-collapse-item title="Custom Discord App" name="2">
                <div class="collapse-item-inner">
                    <el-input v-model="custom.appId" placeholder="app id" clearable />
                    <el-input v-model="custom.largeImageName" placeholder="large image name" clearable />
                    <el-input v-model="custom.smallImageName" placeholder="small image name" clearable />
                </div>
            </el-collapse-item>
        </el-collapse>
        <div class="action-buttons">
            <el-button type="danger" round @click="stop"><font-awesome-icon icon="stop" />&nbsp; Stop</el-button>
            <el-button v-if="isActive === false" type="primary" round @click="start"><font-awesome-icon icon="play" />&nbsp; Start</el-button>
            <el-button v-else type="primary" round @click="update"><font-awesome-icon icon="sync-alt" />&nbsp; Update</el-button>
        </div>
    </main>
</template>

<script>
export default {
    name: "MainPage",
    data() {
        return {
            activeNames: ["1", "2"],
            isActive: false,
            rpcData: {
                details: "",
                state: "",
                largeImageText: "",
                smallImageText: ""
            },
            custom: {
                appId: "",
                largeImageName: "",
                smallImageName: ""
            }
        };
    },
    mounted() {
        this.$electron.ipcRenderer.on("app:data", (_, data) => {
            this.$data.rpcData = {
                details: data.details,
                state: data.state,
                largeImageText: data.largeImageText,
                smallImageText: data.smallImageText
            };

            this.$data.custom = {
                appId: data.appId,
                largeImageName: data.largeImageKey,
                smallImageName: data.smallImageKey
            };
        });

        this.$electron.ipcRenderer.on("start:success", () => {
            console.log("Active is true");
            this.$data.isActive = true;
        });

        this.$electron.ipcRenderer.on("start:failed", () => {
            this.$data.isActive = false;
        });

        this.$electron.ipcRenderer.send("app:ready");
    },
    methods: {
        start() {
            const data = {
                rpcData: this.$data.rpcData,
                custom: this.$data.custom
            };
            this.$electron.ipcRenderer.send("rpc:start", data);
        },
        update() {
            const data = {
                rpcData: this.$data.rpcData,
                custom: this.$data.custom
            };
            this.$electron.ipcRenderer.send("rpc:update", data);
        },
        stop() {
            this.$electron.ipcRenderer.send("rpc:stop");
        }
    }
};
</script>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css?family=Ubuntu');

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    html {
        background: #21252B;
    }

    body { font-family: 'Ubuntu', sans-serif; }

    main {
        width: 90%;
        margin: auto;
        .el-collapse {
            border-top: 0;
            .el-collapse-item__header {
                font-weight: bold;
                font-size: 16px;
            }
            .collapse-item-inner {
                width: 80%;
                margin: auto;
                .el-input {
                    margin-bottom: 10px;
                }
            }
        }
        .action-buttons {
            width: 30%;
            margin: 10px auto auto;
            text-align: center;
        }
    }
</style>
