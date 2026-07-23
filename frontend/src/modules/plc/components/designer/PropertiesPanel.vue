<script setup>

import {
    computed,
} from "vue"



const props = defineProps({

    object: {

        type: Object,

        required: true,

    },

})



const emit = defineEmits([

    "save",

    "delete",

])





const label = computed({

    get(){

        return props.object.label

    },

    set(value){

        props.object.label = value

    }

})



const x = computed({

    get(){

        return props.object.x

    },

    set(value){

        props.object.x = Number(value)

    }

})



const y = computed({

    get(){

        return props.object.y

    },

    set(value){

        props.object.y = Number(value)

    }

})



const rotation = computed({

    get(){

        return props.object.rotation

    },

    set(value){

        props.object.rotation = Number(value)

    }

})



const scale = computed({

    get(){

        return props.object.scale

    },

    set(value){

        props.object.scale = Number(value)

    }

})





function save(){

    emit(
        "save"
    )

}





function remove(){

    emit(
        "delete",
        props.object
    )

}


</script>





<template>


<div

class="
bg-white
rounded-lg
border
shadow
p-4
w-72
"

>


<h2

class="
text-lg
font-bold
mb-4
"

>

Properties

</h2>





<div class="space-y-3">



<div>

<label class="text-sm">

Label

</label>


<input

v-model="label"

class="
w-full
border
rounded
px-2
py-1
"

/>

</div>






<div>

<label class="text-sm">

PLC Address

</label>


<input

:value="object.address"

disabled

class="
w-full
border
rounded
px-2
py-1
bg-gray-100
"

/>

</div>






<div>

<label class="text-sm">

X Position

</label>


<input

v-model="x"

type="number"

class="
w-full
border
rounded
px-2
py-1
"

/>

</div>






<div>

<label class="text-sm">

Y Position

</label>


<input

v-model="y"

type="number"

class="
w-full
border
rounded
px-2
py-1
"

/>

</div>






<div>

<label class="text-sm">

Rotation

</label>


<input

v-model="rotation"

type="number"

class="
w-full
border
rounded
px-2
py-1
"

/>

</div>






<div>

<label class="text-sm">

Scale

</label>


<input

v-model="scale"

type="number"

step="0.1"

class="
w-full
border
rounded
px-2
py-1
"

/>

</div>






<div class="pt-3 flex gap-2">


<button

@click="save"

class="
flex-1
bg-green-600
text-white
py-2
rounded
"

>

Save

</button>





<button

@click="remove"

class="
flex-1
bg-red-600
text-white
py-2
rounded
"

>

Delete

</button>



</div>


</div>


</div>


</template>