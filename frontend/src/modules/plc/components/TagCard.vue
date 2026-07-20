<script setup>


import BoolIndicator 
from "./BoolIndicator.vue"



const props = defineProps({

tag:{
    type:Object,
    required:true
},


value:{
    default:null
}


})





function getColor(){


if(props.tag.data_type==="BOOL"){

return props.value
?
props.tag.on_color
:
props.tag.off_color

}




if(props.value < 50){

return props.tag.low_color

}


if(props.value < 80){

return props.tag.medium_color

}


return props.tag.high_color


}


</script>






<template>


<div

class="
bg-white
rounded-xl
p-5
shadow
border
space-y-4
"

>


<div>


<h2 class="font-bold text-lg">

{{tag.name}}

</h2>


<p class="text-gray-500">

{{tag.address}}

</p>


</div>





<div

v-if="tag.data_type==='BOOL'"

class="
flex
justify-center
"

>


<BoolIndicator

:value="value"

:onColor="tag.on_color"

:offColor="tag.off_color"

/>


</div>








<div

v-else

class="
text-center
"

>


<div

class="
text-4xl
font-bold
"

:style="{

color:getColor()

}"

>


{{value ?? "--"}}


</div>



<p>

{{tag.unit}}

</p>


</div>




</div>


</template>