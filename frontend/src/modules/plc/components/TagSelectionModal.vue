<script setup>

import {
    ref
} from "vue"



const props = defineProps({

    tags:{
        type:Array,
        default:()=>[]
    }

})



const emit = defineEmits([

    "select",

    "close"

])



const selectedTag = ref(null)





function selectTag(){


    if(!selectedTag.value){

        return

    }



    emit(
        "select",
        selectedTag.value
    )


}





function closeModal(){

    emit(
        "close"
    )

}


</script>





<template>


<div

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
shadow-xl
w-96
p-5
"

>


<h2

class="
text-lg
font-bold
mb-4
"

>

Select PLC Tag

</h2>





<div

class="
space-y-2
max-h-80
overflow-y-auto
"

>



<label

v-for="tag in tags"

:key="tag.id"

class="
flex
items-center
gap-3
border
p-3
rounded
cursor-pointer
hover:bg-gray-100
"

>


<input

type="radio"

:value="tag"

v-model="selectedTag"

/>




<div>


<p

class="font-semibold"

>

{{ tag.name }}

</p>



<p

class="text-sm text-gray-500"

>

{{ tag.address }}

({{ tag.data_type }})

</p>


</div>



</label>



</div>






<div

class="
flex
justify-end
gap-3
mt-5
"

>


<button

@click="closeModal"

class="
px-4
py-2
border
rounded
"

>

Cancel

</button>





<button

@click="selectTag"

class="
px-4
py-2
bg-blue-600
text-white
rounded
"

>

Select

</button>



</div>





</div>


</div>


</template>