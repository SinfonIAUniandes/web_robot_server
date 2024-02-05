import "./assets/main.css";
import "@mdi/font/css/materialdesignicons.min.css";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";

const app = createApp(App);

app.use(createPinia());

app.mount("#app");
