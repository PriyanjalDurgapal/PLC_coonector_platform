<script setup>


import {
    ref
} from "vue"


import {
    Save
} from "lucide-vue-next"


import {
    usePLCTagStore
} from "../stores/plcTagStore"




const props = defineProps({

    tag:{
        type:Object,
        required:true
    }

})



const tagStore =
    usePLCTagStore()



const colors = ref({

    on_color:
        props.tag.on_color,

    off_color:
        props.tag.off_color,

    low_color:
        props.tag.low_color,

    medium_color:
        props.tag.medium_color,

    high_color:
        props.tag.high_color

})





async function saveColors(){


    await tagStore.updateTag(

        props.tag.id,

        colors.value

    )


}




</script>





<template>


<div
class="
space-y-3
"
>



<div
class="
grid
grid-cols-2
gap-3
"
>



<!-- ON -->

<div>


<label class="text-sm">
ON
</label>


<div class="flex gap-2">


<input

type="color"

v-model="
colors.on_color
"

/>


<input

v-model="
colors.on_color
"

class="
border
rounded
px-2
w-28
"

/>


</div>


</div>





<!-- OFF -->


<div>


<label class="text-sm">
OFF
</label>


<div class="flex gap-2">


<input

type="color"

v-model="
colors.off_color
"

/>


<input

v-model="
colors.off_color
"

class="
border
rounded
px-2
w-28
"

/>


</div>


</div>







<!-- LOW -->


<div>


<label class="text-sm">
LOW
</label>


<div class="flex gap-2">


<input

type="color"

v-model="
colors.low_color
"

/>


<input

v-model="
colors.low_color
"

class="
border
rounded
px-2
w-28
"

/>


</div>


</div>







<!-- MEDIUM -->


<div>


<label class="text-sm">
MEDIUM
</label>


<div class="flex gap-2">


<input

type="color"

v-model="
colors.medium_color
"

/>


<input

v-model="
colors.medium_color
"

class="
border
rounded
px-2
w-28
"

/>


</div>


</div>







<!-- HIGH -->


<div>


<label class="text-sm">
HIGH
</label>


<div class="flex gap-2">


<input

type="color"

v-model="
colors.high_color
"

/>


<input

v-model="
colors.high_color
"

class="
border
rounded
px-2
w-28
"

/>


</div>


</div>



</div>





<button

@click="saveColors"

class="
mt-3
flex
items-center
gap-2
bg-blue-600
text-white
px-4
py-2
rounded-lg
"

>


<Save size="16"/>

Save Colors


</button>




</div>



</template>