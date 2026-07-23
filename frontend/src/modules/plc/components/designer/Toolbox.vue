<script setup>

const emit = defineEmits([
    "select-tool"
])


function selectTool(type){

    emit(
        "select-tool",
        type
    )

}

</script>


<template>

<div
class="
absolute
top-5
left-5
z-[100]
bg-white
shadow-lg
rounded-lg
p-4
w-48
"
>


<h2
class="
font-bold
mb-4
"
>
Equipment
</h2>



<div class="space-y-3">


<button

@click="selectTool('motor')"

class="
w-full
bg-blue-600
text-white
rounded
p-2
hover:bg-blue-700
cursor-pointer
"

>
+ Motor
</button>



<button

@click="selectTool('pump')"

class="
w-full
bg-blue-600
text-white
rounded
p-2
hover:bg-blue-700
cursor-pointer
"

>
+ Pump
</button>



<button

@click="selectTool('tank')"

class="
w-full
bg-blue-600
text-white
rounded
p-2
hover:bg-blue-700
cursor-pointer
"

>
+ Tank
</button>



<button

@click="selectTool('valve')"

class="
w-full
bg-blue-600
text-white
rounded
p-2
hover:bg-blue-700
cursor-pointer
"

>
+ Valve
</button>



<button

@click="selectTool('fan')"

class="
w-full
bg-blue-600
text-white
rounded
p-2
hover:bg-blue-700
cursor-pointer
"

>
+ Fan
</button>



</div>


</div>


</template>