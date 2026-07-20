import { defineStore } from "pinia"

export const useLayoutStore = defineStore("layout", {

    state: () => ({

        // =========================
        // Desktop Sidebar
        // =========================

        sidebarCollapsed: false,

        // =========================
        // Mobile Drawer
        // =========================

        sidebarOpen: false,

    }),

    actions: {

        // =========================
        // Desktop
        // =========================

        toggleSidebar() {

            this.sidebarCollapsed =
                !this.sidebarCollapsed

        },

        // =========================
        // Mobile
        // =========================

        openMobileSidebar() {

            this.sidebarOpen = true

        },

        closeMobileSidebar() {

            this.sidebarOpen = false

        },

        toggleMobileSidebar() {

            this.sidebarOpen =
                !this.sidebarOpen

        },

    },

})