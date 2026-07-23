<script setup>

const props = defineProps({

    object: {

        type: Object,

        default: null,

    },

})

const emit = defineEmits([

    "save",

])

function save(){

    emit(

        "save",

        props.object,

    )

}

</script>

<template>

<div

v-if="object"

class="
w-80
h-full
bg-white
border-l
shadow-lg
p-5
overflow-y-auto
space-y-6
"

>

<h2

class="
text-xl
font-bold
"

>

Properties

</h2>





<!-- GENERAL -->

<div>

<h3

class="
font-semibold
mb-3
"

>

General

</h3>



<div class="space-y-3">

<div>

<label class="text-sm">

Label

</label>

<input

v-model="object.label"

class="
w-full
border
rounded
px-3
py-2
"

/>

</div>



<div>

<label class="text-sm">

SVG Type

</label>

<input

v-model="object.svg_type"

disabled

class="
w-full
border
rounded
px-3
py-2
bg-gray-100
"

/>

</div>



<div>

<label class="text-sm">

PLC Address

</label>

<input

v-model="object.address"

disabled

class="
w-full
border
rounded
px-3
py-2
bg-gray-100
"

/>

</div>

</div>

</div>





<!-- POSITION -->

<div>

<h3

class="
font-semibold
mb-3
"

>

Position

</h3>



<div class="grid grid-cols-2 gap-3">

<div>

<label>X</label>

<input

v-model.number="object.x"

type="number"

class="
w-full
border
rounded
px-3
py-2
"

/>

</div>



<div>

<label>Y</label>

<input

v-model.number="object.y"

type="number"

class="
w-full
border
rounded
px-3
py-2
"

/>

</div>

</div>





<div class="mt-3">

<label>

Rotation

</label>

<input

v-model.number="object.rotation"

type="number"

class="
w-full
border
rounded
px-3
py-2
"

/>

</div>





<div class="mt-3">

<label>

Scale

</label>

<input

v-model.number="object.scale"

type="number"

step="0.1"

class="
w-full
border
rounded
px-3
py-2
"

/>

</div>

</div>





<!-- COLORS -->

<div>

<h3

class="
font-semibold
mb-3
"

>

Colors

</h3>



<div>

<label>

ON Color

</label>

<input

type="color"

v-model="object.on_color"

class="w-full h-10"

>

</div>



<div class="mt-3">

<label>

OFF Color

</label>

<input

type="color"

v-model="object.off_color"

class="w-full h-10"

>

</div>

</div>





<!-- LIVE -->

<div>

<h3

class="
font-semibold
mb-3
"

>

Live Data

</h3>

<p>

Value :

<strong>

{{ object.value }}

{{ object.unit }}

</strong>

</p>

</div>





<button

@click="save"

class="
w-full
bg-green-600
text-white
py-3
rounded-lg
hover:bg-green-700
"

>

Save

</button>

</div>

</template>