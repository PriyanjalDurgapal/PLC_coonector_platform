<script setup>

const emit = defineEmits([
    "select-tool",
])

const tools = [

    {
        name: "Motor",
        type: "motor",
    },

    {
        name: "Pump",
        type: "pump",
    },

    {
        name: "Tank",
        type: "tank",
    },

    {
        name: "Button",
        type: "button",
    },

    
]

function selectTool(tool){

    emit(
        "select-tool",
        tool.type,
    )

}

</script>

<template>

<div
class="
flex
gap-3
p-4
bg-white
border-b
"
>

<button

v-for="tool in tools"

:key="tool.type"

@click="selectTool(tool)"

class="
px-4
py-2
rounded-lg
bg-blue-600
text-white
hover:bg-blue-700
"

>

+ {{ tool.name }}

</button>

</div>

</template>