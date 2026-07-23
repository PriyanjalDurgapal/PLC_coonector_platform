<script setup>
import { computed, ref } from "vue";
import {
  Search,
  RotateCcw,
  Database,
  Trash2,
} from "lucide-vue-next";

const props = defineProps({
  backups: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits([
  "restore",
  "delete",
]);

const search = ref("");

const filteredBackups = computed(() => {
  if (!search.value) return props.backups;

  return props.backups.filter((backup) =>
    backup.filename.toLowerCase().includes(search.value.toLowerCase())
  );
});
</script>

<template>
  <section class="rounded-xl border border-slate-200 bg-white shadow-sm">

    <!-- Header -->
    <div
      class="flex flex-col gap-4 border-b border-slate-200 p-6 md:flex-row md:items-center md:justify-between"
    >
      <div>
        <h2 class="text-lg font-semibold text-slate-900">
          Available Backups
        </h2>

        <p class="mt-1 text-sm text-slate-500">
          Manage and restore existing database backups.
        </p>
      </div>

      <div class="relative w-full md:w-80">
        <Search
          class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400"
        />

        <input
          v-model="search"
          type="text"
          placeholder="Search backups..."
          class="w-full rounded-lg border border-slate-300 py-2 pl-10 pr-4 text-sm outline-none transition focus:border-indigo-500"
        />
      </div>
    </div>

    <!-- Empty State -->
    <div
      v-if="filteredBackups.length === 0"
      class="flex flex-col items-center justify-center py-16"
    >
      <Database class="mb-4 h-12 w-12 text-slate-300" />

      <h3 class="text-lg font-semibold text-slate-700">
        No backups found
      </h3>

      <p class="mt-2 text-sm text-slate-500">
        Create your first database backup.
      </p>
    </div>

    <!-- Desktop Table -->
    <div v-else class="hidden overflow-x-auto md:block">

      <table class="w-full">

        <thead>

          <tr class="border-b border-slate-200 bg-slate-50">

            <th class="px-6 py-4 text-left text-sm font-semibold text-slate-700">
              Backup Filename
            </th>

            <th class="px-6 py-4 text-left text-sm font-semibold text-slate-700">
              Created On
            </th>

            <th class="px-6 py-4 text-right text-sm font-semibold text-slate-700">
              Action
            </th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="backup in filteredBackups"
            :key="backup.filename"
            class="border-b border-slate-100 transition hover:bg-slate-50"
          >

            <td class="px-6 py-5 font-medium text-slate-800">
              {{ backup.filename }}
            </td>

            <td class="px-6 py-5 text-slate-500">
              {{ backup.createdOn }}
            </td>

            <td class="px-6 py-5 text-right">

              <div class="inline-flex items-center gap-2">

                <button
                  @click="$emit('restore', backup)"
                  class="inline-flex items-center gap-2 rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:border-indigo-500 hover:text-indigo-600"
                >
                  <RotateCcw class="h-4 w-4" />
                  Restore
                </button>

                <button
                  @click="$emit('delete', backup)"
                  class="inline-flex items-center gap-2 rounded-lg border border-red-300 px-4 py-2 text-sm font-medium text-red-600 transition hover:bg-red-50"
                >
                  <Trash2 class="h-4 w-4" />
                  Delete
                </button>

              </div>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

    <!-- Mobile Cards -->
    <div class="space-y-4 p-4 md:hidden">

      <div
        v-for="backup in filteredBackups"
        :key="backup.filename"
        class="rounded-xl border border-slate-200 p-4"
      >
        <h3 class="break-all font-semibold text-slate-900">
          {{ backup.filename }}
        </h3>

        <p class="mt-2 text-sm text-slate-500">
          {{ backup.createdOn }}
        </p>

        <div class="mt-4 flex gap-2">

          <button
            @click="$emit('restore', backup)"
            class="inline-flex flex-1 items-center justify-center gap-2 rounded-lg border border-slate-300 py-2 text-sm font-medium text-slate-700 transition hover:border-indigo-500 hover:text-indigo-600"
          >
            <RotateCcw class="h-4 w-4" />
            Restore
          </button>

          <button
            @click="$emit('delete', backup)"
            class="inline-flex flex-1 items-center justify-center gap-2 rounded-lg border border-red-300 py-2 text-sm font-medium text-red-600 transition hover:bg-red-50"
          >
            <Trash2 class="h-4 w-4" />
            Delete
          </button>

        </div>

      </div>

    </div>

  </section>
</template>