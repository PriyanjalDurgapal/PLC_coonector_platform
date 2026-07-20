<script setup>
import { Database } from "lucide-vue-next";

const emit = defineEmits([
  "create",
]);

function openCreateModal() {
  emit("create");
}
</script>

<template>
  <section
    class="rounded-xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-200 hover:shadow-md"
  >
    <div
      class="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between"
    >

      <!-- Left -->
      <div class="flex items-start gap-4">

        <div
          class="flex h-14 w-14 items-center justify-center rounded-xl bg-indigo-50"
        >
          <Database class="h-7 w-7 text-indigo-600" />
        </div>


        <div>

          <h2 class="text-xl font-semibold text-slate-900">
            Create Backup
          </h2>


          <p class="mt-2 max-w-xl text-sm leading-6 text-slate-600">
            Create a compressed PostgreSQL database backup.
            Enter database credentials to generate a backup file.
          </p>

        </div>

      </div>


      <!-- Button -->
      <button
        @click="openCreateModal"
        class="inline-flex w-full items-center justify-center gap-2 rounded-lg bg-indigo-600 px-5 py-3 text-sm font-medium text-white shadow-sm transition-all duration-200 hover:bg-indigo-700 hover:shadow-md active:scale-[0.98] lg:w-auto"
      >

        <Database class="h-5 w-5" />

        <span>
          Create Backup
        </span>

      </button>


    </div>
  </section>
</template>