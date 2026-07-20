<script setup>

import {
    ref
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
    }

})



const emit = defineEmits([

    "close"

])



const tagStore =
    usePLCTagStore()





const form = ref({

    plc:1,

    name:"",

    address:"",

    data_type:"INT",

    unit:"",

    description:"",


    is_writable:true,

    is_active:true,


    on_color:"#22C55E",

    off_color:"#6B7280",

    low_color:"#22C55E",

    medium_color:"#FACC15",

    high_color:"#EF4444"


})







async function save(){



    await tagStore.createTag(

        form.value

    )



    emit("close")



}






function reset(){


    form.value={

        plc:1,

        name:"",

        address:"",

        data_type:"INT",

        unit:"",

        description:"",

        is_writable:true,

        is_active:true,


        on_color:"#22C55E",

        off_color:"#6B7280",

        low_color:"#22C55E",

        medium_color:"#FACC15",

        high_color:"#EF4444"

    }


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
p-6
w-[650px]
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

Add PLC Tag

</h2>


<button
@click="emit('close')"
>

<X/>

</button>


</div>






<!-- BASIC INFO -->


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

placeholder="PLC Address (D100,M100)"

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

placeholder="Unit (RPM, mm)"

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

<label>
ON
</label>

<input

type="color"

v-model="form.on_color"

/>

</div>




<div>

<label>
OFF
</label>

<input

type="color"

v-model="form.off_color"

/>

</div>





<div>

<label>
LOW
</label>

<input

type="color"

v-model="form.low_color"

/>

</div>





<div>

<label>
MEDIUM
</label>

<input

type="color"

v-model="form.medium_color"

/>

</div>





<div>

<label>
HIGH
</label>

<input

type="color"

v-model="form.high_color"

/>

</div>



</div>


</div>








<button

@click="save"

class="
bg-blue-600
text-white
px-5
py-2
rounded-lg
flex
gap-2
items-center
"

>


<Save size="18"/>

Create Tag


</button>







</div>


</div>


</template>