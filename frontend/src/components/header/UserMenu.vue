<script setup>
import {
    LogOut,
    User,
} from "lucide-vue-next"

import { useRouter } from "vue-router"
import { useAuthStore } from "../../stores/auth"

const auth = useAuthStore()
const router = useRouter()

const logout = () => {

    auth.logout()

    router.push("/login")

}
</script>

<template>

<div
class="
flex
items-center
gap-3
"
>

    <!-- Avatar -->

    <div

        class="
        flex

        h-10
        w-10

        items-center
        justify-center

        rounded-full

        bg-blue-100
        text-blue-600

        dark:bg-blue-900/40
        dark:text-blue-400
        "

    >

        <User :size="18" />

    </div>

    <!-- User Info -->

    <div

        class="
        hidden
        sm:block

        text-right
        "

    >

        <p

            class="
            font-semibold

            text-slate-900
            dark:text-white
            "

        >

            {{ auth.user?.username || "Administrator" }}

        </p>

        <p

            class="
            max-w-[180px]

            truncate

            text-sm

            text-slate-500
            "

        >

            {{ auth.user?.email }}

        </p>

    </div>

    <!-- Logout -->

    <button

        @click="logout"

        class="
        flex

        h-10
        w-10

        items-center
        justify-center

        rounded-xl

        border
        border-slate-200

        text-slate-600

        transition-all
        duration-200

        hover:border-red-200
        hover:bg-red-50
        hover:text-red-600

        dark:border-slate-700
        dark:text-slate-300
        dark:hover:border-red-900
        dark:hover:bg-red-950/40
        dark:hover:text-red-400
        "

    >

        <LogOut :size="18" />

    </button>

</div>

</template>