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



const inputValue =
    ref("")





function currentValue(){


    return (
        tagStore.getTagValue(
            props.tag
        )
        ??
        "-"
    )


}





async function writeValue(){


    if(
        inputValue.value === ""
    ){

        return

    }



    await tagStore.writeTag(

        props.tag.id,

        inputValue.value

    )



    inputValue.value = ""



}





async function toggle(){


    const value =
        currentValue()



    await tagStore.writeTag(

        props.tag.id,

        !value

    )


}





</script>





<template>



<div>


<!-- BOOL -->

<button

v-if="
tag.data_type === 'BOOL'
"

@click="toggle"


class="
px-4
py-2
rounded-full
text-white
font-semibold
flex
items-center
justify-center
"

:style="{

backgroundColor:

currentValue()

?

tag.on_color

:

tag.off_color

}"

>


{{
currentValue()
?
"ON"
:
"OFF"
}}


</button>







<!-- INT -->

<div

v-else-if="
tag.data_type === 'INT'
"

class="
flex
gap-2
"

>


<input

v-model="inputValue"

type="number"

class="
border
rounded
px-2
py-1
w-24
"

placeholder="value"

/>



<button

v-if="tag.is_writable"

@click="writeValue"

class="
bg-green-600
text-white
rounded
px-3
"

>

<Save size="16"/>

</button>


</div>








<!-- STRING -->


<div

v-else-if="
tag.data_type === 'STRING'
"

class="
flex
gap-2
"

>


<input

v-model="inputValue"

type="text"

class="
border
rounded
px-2
py-1
w-32
"

placeholder="text"

/>



<button

v-if="tag.is_writable"

@click="writeValue"

class="
bg-green-600
text-white
rounded
px-3
"

>

<Save size="16"/>

</button>


</div>





</div>



</template>