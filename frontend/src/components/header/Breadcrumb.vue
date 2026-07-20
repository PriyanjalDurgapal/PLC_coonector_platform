<script setup>

import { computed } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()

const title = computed(() => route.name)

</script>

<template>

<div>

    <h1
        class="
        text-2xl
        font-bold

        text-slate-900
        dark:text-white
        "
    >

        {{ title }}

    </h1>

</div>

</template>