import "./assets/main.css";
import "@mdi/font/css/materialdesignicons.min.css";
import * as ROSLib from "roslib";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";

const ros = new ROSLib.Ros({encoding: "ascii"});

ros.connect("ws://localhost:9090");

const app = createApp(App);
app.use(createPinia());
app.mount("#app");