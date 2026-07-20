<template>
  <div class="fixed inset-0 -z-10 overflow-hidden">

    <!-- Background -->
    <div class="absolute inset-0 bg-slate-50 dark:bg-slate-950 transition-colors duration-300"></div>

    <!-- Grid -->
    <div
      class="absolute inset-0 opacity-60 dark:opacity-20"
      style="
        background-image:
          linear-gradient(to right, rgba(148,163,184,.15) 1px, transparent 1px),
          linear-gradient(to bottom, rgba(148,163,184,.15) 1px, transparent 1px);
        background-size:40px 40px;
      "
    ></div>

    <!-- Blue Glow -->
    <div
      class="absolute -top-40 -left-40 h-96 w-96 rounded-full bg-blue-500/20 blur-3xl"
    ></div>

    <!-- Purple Glow -->
    <div
      class="absolute bottom-0 right-0 h-96 w-96 rounded-full bg-violet-500/20 blur-3xl"
    ></div>

  </div>
</template>