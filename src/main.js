import {createApp } from "vue"

import App from "./App.vue"
import BikeItem from "../components/BikeItem.vue"

const app = createApp(App)

app.component("bike-item",BikeItem)
app.mount("#app")


