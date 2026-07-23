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


    const value =
        props.object.value



    if(typeof value === "boolean"){

        return value

    }



    return Number(value) > 0


})







function motorClicked(){


    emit(
        "read",
        props.object
    )


}







function motorMouseDown(event){


    emit(
        "mousedown",
        event
    )


}







function writeValue(){


    console.log(
        "WRITE BUTTON CLICKED",
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

left: object.x + 'px',

top: object.y + 'px',

transform:
`rotate(${object.rotation}deg) scale(${object.scale})`,

transformOrigin:'center'

}"

>



<svg

viewBox="0 0 130 150"

class="w-56 cursor-move"

@click.stop="motorClicked"

@mousedown.stop="motorMouseDown"

>



<!-- STATUS -->

<circle

cx="65"

cy="12"

r="6"

:fill="
running
?
object.on_color
:
object.off_color
"

/>





<!-- MOTOR BODY -->

<rect

x="15"

y="30"

width="100"

height="60"

rx="4"

:fill="
running
?
object.on_color
:
'#D3D3D3'
"

stroke="black"

/>





<!-- SHAFT -->

<rect

x="58"

y="95"

width="14"

height="18"

fill="#D3D3D3"

/>






<!-- LABEL -->

<text

x="65"

y="56"

text-anchor="middle"

font-size="10"

font-weight="bold"

fill="black"

>

{{object.label}}

</text>





<!-- ADDRESS -->

<text

x="65"

y="70"

text-anchor="middle"

font-size="8"

fill="#666"

>

{{object.address}}

</text>






<!-- VALUE -->

<text

x="65"

y="128"

text-anchor="middle"

font-size="10"

font-weight="bold"

>

{{object.value}} {{object.unit}}

</text>



</svg>








<!-- WRITE BUTTON -->

<button

type="button"

@click.stop="writeValue"

class="
relative
z-[999999]
mt-2
bg-blue-600
text-white
px-4
py-2
rounded
text-sm
cursor-pointer
pointer-events-auto
"

>

Write

</button>





</div>


</template>