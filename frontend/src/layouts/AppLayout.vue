<script setup>
import { RouterView } from "vue-router"

import { useLayoutStore } from "../stores/layout"

import AppSidebar from "../components/sidebar/AppSidebar.vue"
import AppHeader from "../components/header/AppHeader.vue"

const layout = useLayoutStore()
</script>

<template>
    <div
        class="
        flex
        h-screen
        overflow-hidden

        bg-slate-50
        dark:bg-slate-950
        "
    >
        <!-- ========================= -->
        <!-- Mobile Overlay -->
        <!-- ========================= -->

        <Transition name="fade">

            <div

                v-if="layout.sidebarOpen"

                @click="layout.closeSidebar"

                class="
                fixed
                inset-0

                z-40

                bg-black/50

                lg:hidden
                "

            />

        </Transition>

        <!-- ========================= -->
        <!-- Sidebar -->
        <!-- ========================= -->

        <AppSidebar />

        <!-- ========================= -->
        <!-- Main Content -->
        <!-- ========================= -->

        <div
    :class="[
        'flex min-w-0 flex-1 flex-col transition-all duration-300',

        layout.sidebarCollapsed
            ? 'lg:ml-20'
            : 'lg:ml-72',
    ]"
>

            <AppHeader />

            <main

                class="
                flex-1

                overflow-y-auto

                p-4
                sm:p-6
                lg:p-8
                "

            >

                <RouterView />

            </main>

        </div>

    </div>
</template>

<style scoped>

.fade-enter-active,
.fade-leave-active{

    transition:opacity .25s ease;

}

.fade-enter-from,
.fade-leave-to{

    opacity:0;

}

</style>