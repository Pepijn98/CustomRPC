import Router from "vue-router";
import Vue from "vue";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            name: "main",
            component: require("@/components/MainPage").default
        },
        {
            path: "*",
            redirect: "/"
        }
    ]
});
