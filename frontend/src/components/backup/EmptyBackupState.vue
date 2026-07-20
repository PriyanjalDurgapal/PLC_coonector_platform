<script setup>
import { Database } from "lucide-vue-next";
</script>

<template>
  <div class="flex flex-col items-center justify-center px-6 py-16 text-center">
    <!-- Icon -->
    <div
      class="mb-6 flex h-16 w-16 items-center justify-center rounded-full bg-slate-100"
    >
      <Database class="h-8 w-8 text-slate-400" />
    </div>

    <!-- Title -->
    <h3 class="text-lg font-semibold text-slate-900">
      No Backups Found
    </h3>

    <!-- Description -->
    <p class="mt-2 max-w-md text-sm leading-6 text-slate-500">
      No database backups are currently available.
      Create your first backup to securely store your PostgreSQL database.
    </p>
  </div>
</template>