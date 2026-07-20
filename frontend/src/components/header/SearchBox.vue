<script setup>
import { Search } from "lucide-vue-next"
</script>

<template>

<div
class="
relative

w-44
sm:w-56
md:w-72
xl:w-96
"

>

    <Search

        :size="18"

        class="
        absolute

        left-3
        top-1/2

        -translate-y-1/2

        text-slate-400
        "

    />

    <input

        type="text"

        placeholder="Search..."

        class="
        w-full

        rounded-xl

        border
        border-slate-200

        bg-white

        py-2.5
        pl-10
        pr-4

        text-sm

        text-slate-700
        placeholder:text-slate-400

        outline-none

        transition-all
        duration-200

        focus:border-blue-500
        focus:ring-2
        focus:ring-blue-500/20

        dark:border-slate-700
        dark:bg-slate-900
        dark:text-slate-100
        dark:placeholder:text-slate-500
        "

    />

</div>

</template>