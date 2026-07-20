<script setup>

const props = defineProps({

    value:{
        type:Boolean,
        default:false
    },

    onColor:{
        type:String,
        default:"#22C55E"
    },

    offColor:{
        type:String,
        default:"#6B7280"
    }

})


</script>



<template>

<div

class="
w-20
h-20
rounded-full
flex
items-center
justify-center
text-white
font-bold
shadow-lg
"

:style="{

backgroundColor:
value
?
onColor
:
offColor

}"

>


{{ value ? "ON" : "OFF" }}


</div>


</template>