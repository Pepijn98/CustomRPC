/* eslint-disable sort-imports */
import "./assets/element-variables.scss";

import ElementUI from "element-ui";
import Vue from "vue";
import axios from "axios";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";

import App from "./App";
import router from "./router";
import store from "./store";

if (!process.env.IS_WEB) Vue.use(require("vue-electron"));
Vue.http = Vue.prototype.$http = axios;
Vue.config.productionTip = false;

library.add(fab, far, fas);
Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.use(ElementUI);

new Vue({
    components: { App },
    router,
    store,
    template: "<App/>"
}).$mount("#app");
