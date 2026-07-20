import { createApp } from "vue"
import { createPinia } from "pinia"

import App from "./App.vue"
import router from "./router"

import { useThemeStore } from "./stores/theme"
import { useAuthStore } from "./stores/auth"

import "./style.css"

async function bootstrap() {

    const app = createApp(App)

    const pinia = createPinia()

    app.use(pinia)

    // Initialize Theme
    const theme = useThemeStore()
    theme.init()

    // Initialize Authentication
    const auth = useAuthStore()
    await auth.initialize()

    // Register Router
    app.use(router)

    // Mount App
    app.mount("#app")

}

bootstrap()