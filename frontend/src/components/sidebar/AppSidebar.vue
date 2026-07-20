<script setup>
import {
    LayoutDashboard,
    Users,
    Shield,
    Cpu,
    Settings,
    Factory,
    PanelLeftClose,
    PanelLeftOpen,
    X,
} from "lucide-vue-next"

import { computed } from "vue"

import { useLayoutStore } from "../../stores/layout"

import SidebarItem from "./SidebarItem.vue"
import SidebarFooter from "./SidebarFooter.vue"

const layout = useLayoutStore()

const showLabels = computed(() => {

    if (typeof window !== "undefined") {

        if (window.innerWidth < 1024) {

            return true

        }

    }

    return !layout.sidebarCollapsed

})

</script>

<template>

<aside

:class="[

'fixed left-0 top-0 z-50 flex h-screen flex-col border-r border-slate-200 bg-white shadow-xl transition-all duration-300 dark:border-slate-800 dark:bg-slate-900',

layout.sidebarCollapsed
? 'lg:w-20'
: 'lg:w-72',

'w-72',

layout.sidebarOpen
? 'translate-x-0'
: '-translate-x-full lg:translate-x-0'

]"

>

    <!-- ========================= -->
    <!-- Header -->
    <!-- ========================= -->

    <div

    class="
    flex
    items-center
    justify-between

    border-b
    border-slate-200

    p-5

    dark:border-slate-800
    "

    >

        <div

        v-if="showLabels"

        class="flex items-center gap-3"

        >

            <div

            class="
            flex
            h-10
            w-10

            items-center
            justify-center

            rounded-xl

            bg-blue-600
            text-white
            "

            >

                <Factory :size="20" />

            </div>

            <div>

                <h1

                class="
                text-lg
                font-bold
                tracking-wide

                text-slate-900
                dark:text-white
                "

                >

                    TAIKISHA

                </h1>

                <p

                class="
                text-xs
                text-slate-500
                "

                >

                    Industrial Platform

                </p>

            </div>

        </div>

        <!-- Desktop Collapse -->

        <button

        @click="layout.toggleSidebar"

        class="
        hidden
        lg:flex

        rounded-lg

        p-2

        transition

        hover:bg-slate-100

        dark:hover:bg-slate-800
        "

        >

            <PanelLeftClose

                v-if="!layout.sidebarCollapsed"

                :size="20"

            />

            <PanelLeftOpen

                v-else

                :size="20"

            />

        </button>

        <!-- Mobile Close -->

        <button

        @click="layout.closeMobileSidebar"

        class="
        rounded-lg

        p-2

        transition

        hover:bg-slate-100

        lg:hidden

        dark:hover:bg-slate-800
        "

        >

            <X :size="20" />

        </button>

    </div>

    <!-- ========================= -->
    <!-- Navigation -->
    <!-- ========================= -->

    <nav

    class="
    flex-1

    space-y-2

    overflow-y-auto

    p-4
    "

    >

        <SidebarItem

            title="Dashboard"
            to="/dashboard"

            :icon="LayoutDashboard"

            :collapsed="!showLabels"

        />

        <SidebarItem

            title="Users"
            to="/users"

            :icon="Users"

            :collapsed="!showLabels"

        />
        

        <SidebarItem

            title="Roles"
            to="/roles"

            :icon="Shield"

            :collapsed="!showLabels"

        />

        <SidebarItem

            title="PLC"
            to="/plc"

            :icon="Cpu"

            :collapsed="!showLabels"

        />

        <SidebarItem

            title="plc-tags"
            to="/plc/tags"

            :icon="Settings"

            :collapsed="!showLabels"

        />
         <SidebarItem

            title="plc-visualtize"
            to="/plc/visualization"

            :icon="Settings"

            :collapsed="!showLabels"

        />
        <SidebarItem

            title="plc-logs"
            to="/plc/logs"

            :icon="Settings"

            :collapsed="!showLabels"

        />
        <SidebarItem

            title="Backup"
            to="/backup"

            :icon="Settings"

            :collapsed="!showLabels"

        />

    </nav>

    <SidebarFooter :collapsed="!showLabels" />

</aside>

</template>