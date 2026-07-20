<script setup>
import {
    Menu,
} from "lucide-vue-next"

import Breadcrumb from "./Breadcrumb.vue"
import SearchBox from "./SearchBox.vue"
import UserMenu from "./UserMenu.vue"

import ThemeToggle from "../ThemeToggle.vue"

import { useLayoutStore } from "../../stores/layout"

const layout = useLayoutStore()
</script>

<template>

<header

class="
flex
h-20

items-center
justify-between

border-b
border-slate-200

bg-white

px-4
sm:px-6
lg:px-8

dark:border-slate-800
dark:bg-slate-900
"

>

    <!-- ========================= -->
    <!-- Left -->
    <!-- ========================= -->

    <div class="flex items-center gap-4">

        <!-- Mobile Menu -->

        <button

            @click="layout.toggleMobileSidebar"

            class="
            flex

            h-10
            w-10

            items-center
            justify-center

            rounded-lg

            border

            border-slate-200

            transition

            hover:bg-slate-100

            lg:hidden

            dark:border-slate-700
            dark:hover:bg-slate-800
            "

        >

            <Menu :size="20" />

        </button>

        <Breadcrumb />

    </div>

    <!-- ========================= -->
    <!-- Right -->
    <!-- ========================= -->

    <div
        class="
        flex
        items-center
        gap-3
        sm:gap-4
        lg:gap-5
        "
    >

        <!-- Search -->

        <div class="hidden md:block">

            <SearchBox />

        </div>

        <!-- Theme -->

        <ThemeToggle />

        <!-- User -->

        <UserMenu />

    </div>

</header>

</template>