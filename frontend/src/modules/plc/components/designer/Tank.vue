<script setup>

import { computed } from "vue"


const props = defineProps({

object:{
type:Object,
required:true
}

})


const emit = defineEmits([

"mousedown",

"read",

"write"

])



const level = computed(()=>{

return Number(props.object.value) || 0

})



function tankClicked(){

emit(
"read",
props.object
)

}



function tankMouseDown(event){

emit(
"mousedown",
event
)

}



function writeValue(){

console.log(
"TANK WRITE",
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
"

@click.stop

:style="{

left:object.x+'px',

top:object.y+'px',

transform:
`scale(${object.scale}) rotate(${object.rotation}deg)`

}"

>


<svg

viewBox="0 0 120 180"

class="w-48 cursor-move"

@click.stop="tankClicked"

@mousedown.stop="tankMouseDown"

>


<!-- LEVEL -->

<rect

x="25"

y="30"

width="70"

height="100"

fill="#ddd"

stroke="black"

/>


<rect

x="25"

y="130"

width="70"

:height="level"

fill="#22C55E"

/>



<text

x="60"

y="80"

text-anchor="middle"

font-size="10"

>

{{level}} %

</text>



<text

x="60"

y="150"

text-anchor="middle"

font-size="10"

>

{{object.label}}

</text>


</svg>



<button

@click.stop="writeValue"

class="
mt-2
bg-blue-600
text-white
px-4
py-2
rounded
"

>

Write

</button>


</div>


</template>