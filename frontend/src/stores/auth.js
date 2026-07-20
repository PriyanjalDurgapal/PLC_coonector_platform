import { defineStore } from "pinia"
import api from "../api/axios"

export const useAuthStore = defineStore("auth", {

    state: () => ({

        user: null,

        access: localStorage.getItem("access"),

        refresh: localStorage.getItem("refresh"),

    }),

    getters: {

        isAuthenticated: (state) => !!state.access,

    },

    actions: {

        async login(credentials) {

        const response = await api.post(
            "/auth/login/",
            credentials
        )

        const data = response.data.data

        this.access = data.access
        this.refresh = data.refresh

        localStorage.setItem(
            "access",
            data.access
        )

        localStorage.setItem(
            "refresh",
            data.refresh
        )

        api.defaults.headers.common.Authorization =
            `Bearer ${data.access}`

        // Always load the latest user information
        await this.getCurrentUser()

        return data

    },

        async getCurrentUser() {

            const response = await api.get(
                "/auth/me/"
            )

            this.user = response.data.data

            return this.user
        },

        async initialize() {

            if (!this.access) {
                return false
            }

            api.defaults.headers.common.Authorization =
                `Bearer ${this.access}`

            try {

                await this.getCurrentUser()

                return true

            } catch (error) {

                this.logout()

                return false

            }

        },

        logout() {

            this.user = null
            this.access = null
            this.refresh = null

            localStorage.removeItem("access")
            localStorage.removeItem("refresh")

            delete api.defaults.headers.common.Authorization

        }

    }

})