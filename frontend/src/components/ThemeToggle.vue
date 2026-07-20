<script setup>
import { Moon, Sun } from "lucide-vue-next"
import { useThemeStore } from "../stores/theme"

const theme = useThemeStore()
</script>

<template>
  <button
    @click="theme.toggle"
    class="
      inline-flex
      h-10
      w-10
      items-center
      justify-center

      rounded-xl

      border
      border-slate-200

      bg-white

      text-slate-600

      transition-all
      duration-200

      hover:bg-slate-100

      dark:border-slate-700
      dark:bg-slate-800
      dark:text-slate-300
      dark:hover:bg-slate-700
    "
  >
    <Moon
      v-if="theme.mode === 'light'"
      :size="18"
    />

    <Sun
      v-else
      :size="18"
    />
  </button>
</template>