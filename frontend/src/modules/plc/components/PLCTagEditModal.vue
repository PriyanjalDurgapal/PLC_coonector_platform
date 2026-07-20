<script setup>

import {
    ref,
    watch
} from "vue"


import {
    X,
    Save
} from "lucide-vue-next"


import {
    usePLCTagStore
} from "../stores/plcTagStore"



const props = defineProps({

    show:{
        type:Boolean,
        default:false
    },


    tag:{
        type:Object,
        default:null
    }

})



const emit = defineEmits([

    "close"

])



const tagStore =
    usePLCTagStore()



const form = ref({

    name:"",
    address:"",
    data_type:"INT",
    unit:"",
    description:"",
    is_writable:false,
    is_active:true,

    on_color:"#22C55E",
    off_color:"#6B7280",
    low_color:"#22C55E",
    medium_color:"#FACC15",
    high_color:"#EF4444"

})





watch(

()=>props.tag,

(tag)=>{


    if(tag){

        form.value = {

            name:
                tag.name,


            address:
                tag.address,


            data_type:
                tag.data_type,


            unit:
                tag.unit || "",


            description:
                tag.description || "",


            is_writable:
                tag.is_writable,


            is_active:
                tag.is_active,


            on_color:
                tag.on_color,


            off_color:
                tag.off_color,


            low_color:
                tag.low_color,


            medium_color:
                tag.medium_color,


            high_color:
                tag.high_color

        }

    }


},

{
    immediate:true
}

)






async function save(){


    await tagStore.updateTag(

        props.tag.id,

        form.value

    )



    emit("close")


}





</script>





<template>


<div

v-if="show"

class="
fixed
inset-0
bg-black/40
flex
items-center
justify-center
z-50
"


>



<div

class="
bg-white
rounded-xl
w-[600px]
p-6
space-y-5
"

>



<!-- HEADER -->

<div
class="
flex
justify-between
items-center
"
>


<h2 class="text-xl font-bold">

Edit PLC Tag

</h2>



<button

@click="emit('close')"

>

<X/>

</button>


</div>







<!-- FORM -->


<div
class="
grid
grid-cols-2
gap-4
"
>




<input

v-model="form.name"

placeholder="Tag Name"

class="
border
rounded
p-2
"

/>



<input

v-model="form.address"

placeholder="Address"

class="
border
rounded
p-2
"

/>







<select

v-model="form.data_type"

class="
border
rounded
p-2
"

>


<option>
BOOL
</option>


<option>
INT
</option>


<option>
STRING
</option>


<option>
FLOAT
</option>


</select>





<input

v-model="form.unit"

placeholder="Unit"

class="
border
rounded
p-2
"

/>



</div>








<textarea

v-model="form.description"

placeholder="Description"

class="
border
rounded
p-2
w-full
"

/>








<div
class="
flex
gap-6
"
>


<label>

<input

type="checkbox"

v-model="form.is_writable"

/>

Writable


</label>



<label>

<input

type="checkbox"

v-model="form.is_active"

/>

Active


</label>


</div>








<!-- COLORS -->


<div>


<h3 class="font-semibold mb-3">

Colors

</h3>



<div

class="
grid
grid-cols-5
gap-3
"

>


<div>


<label class="text-xs">
ON
</label>


<input

type="color"

v-model="form.on_color"

/>


</div>




<div>


<label class="text-xs">
OFF
</label>


<input

type="color"

v-model="form.off_color"

/>


</div>




<div>


<label class="text-xs">
LOW
</label>


<input

type="color"

v-model="form.low_color"

/>


</div>




<div>


<label class="text-xs">
MEDIUM
</label>


<input

type="color"

v-model="form.medium_color"

/>


</div>




<div>


<label class="text-xs">
HIGH
</label>


<input

type="color"

v-model="form.high_color"

/>


</div>



</div>


</div>







<!-- SAVE -->


<button

@click="save"

class="
bg-blue-600
text-white
px-5
py-2
rounded-lg
flex
items-center
gap-2
"

>


<Save size="18"/>

Save Changes


</button>





</div>


</div>


</template>