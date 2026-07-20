<script setup>
defineProps({

    title: {
        type: String,
        required: true,
    },

    value: {
        type: [String, Number],
        required: true,
    },

    subtitle: {
        type: String,
        default: "",
    },

    icon: {
        type: Object,
        required: true,
    },

    color: {
        type: String,
        default: "blue",
    },

})
</script>

<template>

<div

class="
group

rounded-2xl

border
border-slate-200

bg-white

p-6

shadow-sm

transition-all
duration-300

hover:-translate-y-1
hover:shadow-lg

dark:border-slate-800
dark:bg-slate-900
"

>

    <div class="flex items-start justify-between">

        <div>

            <p

                class="
                text-sm
                font-medium

                text-slate-500
                "

            >

                {{ title }}

            </p>

            <h2

                class="
                mt-3

                text-3xl
                font-bold

                text-slate-900
                dark:text-white
                "

            >

                {{ value }}

            </h2>

            <p

                v-if="subtitle"

                class="
                mt-2

                text-sm

                text-slate-500
                "

            >

                {{ subtitle }}

            </p>

        </div>

        <div

            :class="[
                'flex h-14 w-14 items-center justify-center rounded-2xl',

                {
                    'bg-blue-100 text-blue-600 dark:bg-blue-900/30 dark:text-blue-400':
                        color === 'blue',

                    'bg-green-100 text-green-600 dark:bg-green-900/30 dark:text-green-400':
                        color === 'green',

                    'bg-orange-100 text-orange-600 dark:bg-orange-900/30 dark:text-orange-400':
                        color === 'orange',

                    'bg-purple-100 text-purple-600 dark:bg-purple-900/30 dark:text-purple-400':
                        color === 'purple',
                },
            ]"

        >

            <component

                :is="icon"

                :size="28"

            />

        </div>

    </div>

</div>

</template>