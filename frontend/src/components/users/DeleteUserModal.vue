<script setup>

import {
    X,
    Trash2
} from "lucide-vue-next"


import { ref } from "vue"


const props = defineProps({

    user:{
        type:Object,
        required:true
    }

})


const emit = defineEmits([
    "close",
    "confirm"
])


const loading = ref(false)



const confirmDelete = ()=>{

    loading.value=true

    emit(
        "confirm"
    )

}


</script>



<template>


<div

class="
fixed
inset-0
z-50

flex
items-center
justify-center

bg-black/50

backdrop-blur-sm

px-4
"

>


<div

class="
w-full
max-w-md

rounded-3xl

bg-white

p-6

shadow-2xl

dark:bg-slate-900
"

>


<!-- Header -->

<div

class="
flex
items-center
justify-between
mb-6
"

>


<div

class="
flex
items-center
gap-3
"

>


<div

class="
flex
h-12
w-12
items-center
justify-center

rounded-2xl

bg-red-100

text-red-600
"

>

<Trash2/>

</div>



<div>

<h2 class="font-bold text-xl dark:text-white">

Delete User

</h2>


<p class="text-sm text-slate-500">

This action cannot be undone

</p>


</div>


</div>





<button

@click="emit('close')"

>

<X/>

</button>


</div>





<p class="
text-slate-600
dark:text-slate-300
mb-6
">


Are you sure you want to delete

<strong>

{{user.username}}

</strong>

?


</p>






<div

class="
flex
justify-end
gap-3
"

>


<button

@click="emit('close')"

class="
rounded-xl
px-5
py-2

hover:bg-slate-100
"

>

Cancel

</button>





<button

@click="confirmDelete"

:disabled="loading"

class="
rounded-xl

bg-red-600

px-5

py-2

text-white

hover:bg-red-700
"

>


{{loading ? "Deleting..." : "Delete"}}


</button>



</div>




</div>


</div>


</template>