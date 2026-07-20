<script setup>

import {
    X,
    Save,
    ShieldPlus
} from "lucide-vue-next"


import {
    reactive,
    ref
} from "vue"


import { rolesApi } from "../../api/roles"





const emit = defineEmits([

    "close",

    "created"

])





const loading = ref(false)

const error = ref("")






const form = reactive({

    name:"",

    description:"",

    is_system:false

})







// =========================
// Error Handler
// =========================

const getErrorMessage = (err)=>{


    const data =
        err.response?.data



    console.log(
        "Role Error:",
        data
    )



    if(!data)

        return "Server connection failed"



    if(data.detail)

        return data.detail



    if(data.message)

        return data.message



    if(typeof data==="object"){


        return Object.values(data)

        .flat()

        .join(", ")

    }



    return "Something went wrong"


}









// =========================
// Create Role
// =========================

const submit = async()=>{


    loading.value=true


    error.value=""



    try{


        await rolesApi.createRole({

            name:
                form.name,


            description:
                form.description,


            is_system:
                form.is_system

        })



        emit("created")



    }


    catch(err){


        error.value =
            getErrorMessage(err)


    }


    finally{


        loading.value=false


    }


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

bg-slate-950/60

backdrop-blur-sm

px-4
"

>



<div

class="
w-full

max-w-xl

overflow-hidden

rounded-3xl

border

border-slate-200

bg-white

shadow-2xl

dark:border-slate-800

dark:bg-slate-900
"

>







<!-- Header -->


<div

class="
flex

items-center

justify-between

border-b

border-slate-200

p-6

dark:border-slate-800
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

h-11

w-11

items-center

justify-center

rounded-2xl

bg-blue-600

text-white
"

>

<ShieldPlus :size="22"/>

</div>




<div>


<h2

class="
text-xl

font-bold

text-slate-900

dark:text-white
"

>

Create Role

</h2>


<p class="text-sm text-slate-500">

Add new system role

</p>


</div>


</div>






<button

@click="emit('close')"

class="
rounded-xl

p-2

hover:bg-slate-100

dark:hover:bg-slate-800
"

>


<X :size="20"/>


</button>



</div>










<form

@submit.prevent="submit"

class="space-y-6 p-6"

>





<!-- Error -->


<div

v-if="error"

class="
rounded-xl

bg-red-50

p-3

text-sm

text-red-600

dark:bg-red-950/30
"

>

{{error}}

</div>









<!-- Name -->


<div>


<label

class="
mb-2

block

font-medium

dark:text-white
"

>

Role Name

</label>


<input

v-model="form.name"

class="input"

placeholder="Example: Production Manager"

required

/>


</div>









<!-- Description -->


<div>


<label

class="
mb-2

block

font-medium

dark:text-white
"

>

Description

</label>


<textarea

v-model="form.description"

rows="4"

class="input"

placeholder="Role description"

></textarea>


</div>









<!-- System Role -->


<div

class="
flex

items-center

justify-between

rounded-xl

border

border-slate-200

p-4

dark:border-slate-700
"

>


<div>


<p class="font-medium dark:text-white">

System Role

</p>


<p class="text-sm text-slate-500">

Protected system role

</p>


</div>




<input

v-model="form.is_system"

type="checkbox"

class="
h-5

w-5

accent-blue-600
"

/>



</div>









<!-- Footer -->


<div

class="
flex

justify-end

gap-3

border-t

pt-5

dark:border-slate-800
"

>



<button

type="button"

@click="emit('close')"

class="
rounded-xl

px-5

py-2.5

hover:bg-slate-100

dark:hover:bg-slate-800
"

>

Cancel

</button>








<button

:disabled="loading"

class="
flex

items-center

gap-2

rounded-xl

bg-blue-600

px-6

py-2.5

text-white

hover:bg-blue-700

disabled:opacity-50
"

>


<Save :size="17"/>


{{loading ? "Creating..." : "Create Role"}}


</button>



</div>




</form>



</div>


</div>


</template>