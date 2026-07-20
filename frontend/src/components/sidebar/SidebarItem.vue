<script setup>
import { RouterLink } from "vue-router"
import { useLayoutStore } from "../../stores/layout"

const props = defineProps({

    title: {
        type: String,
        required: true,
    },

    to: {
        type: String,
        required: true,
    },

    icon: {
        type: Object,
        required: true,
    },

    collapsed: {
        type: Boolean,
        default: false,
    },

})

const layout = useLayoutStore()

const handleClick = () => {

    // Close drawer on mobile

    if (window.innerWidth < 1024) {

        layout.closeMobileSidebar()

    }

}
</script>

<template>

<RouterLink

    :to="to"

    @click="handleClick"

    class="
    group

    flex
    items-center

    rounded-xl

    py-3

    text-slate-600

    transition-all
    duration-200

    hover:bg-slate-100
    hover:text-blue-600

    dark:text-slate-300
    dark:hover:bg-slate-800
    dark:hover:text-blue-400
    "

    :class="

        collapsed
            ? 'justify-center px-0'
            : 'gap-3 px-4'

    "

    active-class="
    bg-blue-50
    text-blue-600

    dark:bg-blue-950/40
    dark:text-blue-400
    "

>

    <!-- Icon -->

    <component

        :is="icon"

        :size="20"

        class="shrink-0"

    />

    <!-- Label -->

    <Transition name="fade">

        <span

            v-if="!collapsed"

            class="
            whitespace-nowrap

            font-medium
            "

        >

            {{ title }}

        </span>

    </Transition>

</RouterLink>

</template>

<style scoped>

.fade-enter-active,
.fade-leave-active{

    transition:opacity .2s ease;

}

.fade-enter-from,
.fade-leave-to{

    opacity:0;

}

</style>