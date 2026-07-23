<script setup>

import Toolbox from "../components/designer/Toolbox.vue"

import Canvas from "../components/designer/Canvas.vue"

import PropertiesPanel from "../components/designer/PropertiesPanel.vue"

</script>

<template>

<div
class="flex h-screen bg-gray-100">

    <!-- Left -->

    <div
    class="w-64 border-r bg-white">

        <Toolbox/>

    </div>



    <!-- Center -->

    <div
    class="flex-1">

        <Canvas/>

    </div>



    <!-- Right -->

    <div
    class="w-80 border-l bg-white">

        <PropertiesPanel/>

    </div>

</div>

</template>