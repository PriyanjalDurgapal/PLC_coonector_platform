<script setup>

import { ref } from "vue"
import { useRouter } from "vue-router"

import { User, Lock, Eye, EyeOff, LoaderCircle } from "lucide-vue-next"

import Logo from "./Logo.vue"

import { useAuthStore } from "../stores/auth"

const auth = useAuthStore()
const router = useRouter()

const username = ref("")
const password = ref("")
const loading = ref(false)
const error = ref("")
const showPassword = ref(false)

const submit = async () => {
  try {

    loading.value = true
    error.value = ""

    await auth.login({
      username: username.value,
      password: password.value,
    })

    await auth.getCurrentUser()

    router.push("/dashboard")

  } catch {

    error.value = "Invalid username or password."

  } finally {

    loading.value = false

  }
}

</script>

<template>

<div
class="
w-full
max-w-md
rounded-3xl

border
border-slate-200/70
dark:border-slate-700/70

bg-white/80
dark:bg-slate-900/80

backdrop-blur-xl

shadow-2xl

p-8

transition-all
duration-300
">

    <Logo />

    <div class="mt-4 text-center">

        <h1 class="text-4xl font-bold text-slate-900 dark:text-white">
            Welcome Back
        </h1>

        <p class="mt-2 text-sm text-slate-500 dark:text-slate-400">
            Sign in to continue to your dashboard
        </p>

    </div>

    <form
        @submit.prevent="submit"
        class="mt-8 space-y-5"
    >

        <!-- Username -->

        <div class="relative">

            <User
                class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
                :size="18"
            />

            <input
                v-model="username"
                type="text"
                placeholder="Username"
                class="w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent py-3 pl-11 pr-4 outline-none focus:border-blue-500"
            />

        </div>

        <!-- Password -->

        <div class="relative">

            <Lock
                class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
                :size="18"
            />

            <input
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="Password"
                class="w-full rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent py-3 pl-11 pr-12 outline-none focus:border-blue-500"
            />

            <button
                type="button"
                @click="showPassword=!showPassword"
                class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400"
            >

                <Eye
                    v-if="!showPassword"
                    :size="18"
                />

                <EyeOff
                    v-else
                    :size="18"
                />

            </button>

        </div>

        <p
            v-if="error"
            class="text-sm text-red-500"
        >
            {{ error }}
        </p>

        <button
            :disabled="loading"
            class="
            flex
            w-full
            items-center
            justify-center

            rounded-xl

            bg-gradient-to-r
            from-blue-600
            to-violet-600

            py-3

            font-semibold
            text-white

            transition

            hover:opacity-90

            disabled:cursor-not-allowed
            disabled:opacity-60
            "
        >

            <LoaderCircle
                v-if="loading"
                class="mr-2 animate-spin"
                :size="18"
            />

            {{ loading ? "Signing In..." : "Sign In" }}

        </button>

    </form>

</div>

</template>