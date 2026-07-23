<script setup>

import { computed } from "vue"


const props = defineProps({

    object:{
        type:Object,
        required:true,
    }

})


const emit = defineEmits([

    "mousedown",

    "read",

    "write"

])



const running = computed(()=>{

    const value = props.object.value


    if(typeof value === "boolean"){

        return value

    }


    return Number(value) > 0

})



function pumpClicked(){

    emit(
        "read",
        props.object
    )

}



function pumpMouseDown(event){

    emit(
        "mousedown",
        event
    )

}



function writeValue(){

    console.log(
        "PUMP WRITE",
        props.object
    )


    emit(
        "write",
        props.object
    )

}

</script>



<template>


<div

class="
absolute
select-none
flex
flex-col
items-center
pointer-events-auto
"

@click.stop

:style="{

left:object.x+'px',

top:object.y+'px',

transform:
`rotate(${object.rotation}deg) scale(${object.scale})`

}"

>


<svg

viewBox="0 0 140 140"

class="w-56 cursor-move"

@click.stop="pumpClicked"

@mousedown.stop="pumpMouseDown"

>


<!-- STATUS -->

<circle

cx="70"

cy="15"

r="6"

:fill="
running
?
object.on_color
:
object.off_color
"

/>



<!-- PUMP BODY -->

<circle

cx="70"

cy="65"

r="35"

:fill="
running
?
object.on_color
:
'#D3D3D3'
"

stroke="black"

/>



<!-- CENTER -->

<circle

cx="70"

cy="65"

r="10"

fill="white"

/>



<!-- LABEL -->

<text

x="70"

y="115"

text-anchor="middle"

font-size="10"

font-weight="bold"

>

{{object.label}}

</text>



<text

x="70"

y="128"

text-anchor="middle"

font-size="8"

fill="#666"

>

{{object.address}}

</text>



</svg>



<button

type="button"

@click.stop="writeValue"

class="
mt-2
bg-blue-600
text-white
px-4
py-2
rounded
text-sm
cursor-pointer
"

>

Write

</button>


</div>


</template>