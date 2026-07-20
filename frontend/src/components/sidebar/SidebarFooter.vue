<script setup>
import {
    User,
} from "lucide-vue-next"

import { useAuthStore } from "../../stores/auth"

defineProps({

    collapsed: {

        type: Boolean,

        default: false,

    },

})

const auth = useAuthStore()
</script>

<template>

<div

class="
border-t
border-slate-200

p-4

dark:border-slate-800
"

>

    <div

        class="
        flex
        items-center

        rounded-xl

        bg-slate-50

        p-3

        dark:bg-slate-800/50
        "

        :class="
            collapsed
                ? 'justify-center'
                : 'gap-3'
        "

    >

        <!-- Avatar -->

        <div

            class="
            flex

            h-11
            w-11

            shrink-0

            items-center
            justify-center

            rounded-full

            bg-blue-600

            text-white
            "

        >

            <User :size="18" />

        </div>

        <!-- User Info -->

        <Transition name="fade">

            <div

                v-if="!collapsed"

                class="min-w-0"

            >

                <p

                    class="
                    truncate

                    font-semibold

                    text-slate-900
                    dark:text-white
                    "

                >

                    {{ auth.user?.username || "Administrator" }}

                </p>

                <p

                    class="
                    truncate

                    text-sm

                    text-slate-500
                    "

                >

                    {{ auth.user?.email || "admin@example.com" }}

                </p>

            </div>

        </Transition>

    </div>

</div>

</template>

<style scoped>

.fade-enter-active,
.fade-leave-active {

    transition: opacity .2s ease;

}

.fade-enter-from,
.fade-leave-to {

    opacity: 0;

}

</style>