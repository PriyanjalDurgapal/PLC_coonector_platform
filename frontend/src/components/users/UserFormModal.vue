<script setup>

import {
    X,
    Save,
    UserPlus,
    ShieldCheck
} from "lucide-vue-next"


import {
    onMounted,
    reactive,
    ref
} from "vue"


import { usersApi } from "../../api/users"

import { rolesApi } from "../../api/roles"




const emit = defineEmits([

    "close",

    "created"

])




const loading = ref(false)

const rolesLoading = ref(false)



const roles = ref([])


const error = ref("")






const form = reactive({

    username:"",

    email:"",

    password:"",

    employee_id:"",

    is_active:true,

    roles:[]

})







// =========================
// Load Roles
// =========================

const loadRoles = async()=>{


    rolesLoading.value = true


    try{


        roles.value =
            await rolesApi.getRoles()


    }


    catch(err){


        console.error(
            "Roles Error:",
            err.response?.data
        )


    }


    finally{


        rolesLoading.value = false


    }


}








// =========================
// Error Formatter
// =========================

const getErrorMessage = (err)=>{


    console.error(
        "Create User Error:",
        err.response?.data
    )



    const data = err.response?.data



    if(!data){

        return "Server connection failed"

    }




    if(data.detail){

        return data.detail

    }




    if(data.message){

        return data.message

    }





    if(typeof data === "object"){


        return Object.values(data)

        .flat()

        .join(", ")


    }




    return "Something went wrong"



}







// =========================
// Submit
// =========================

const submit = async()=>{


    error.value = ""



    if(
        !form.username ||
        !form.email ||
        !form.password
    ){

        error.value =
            "Username, email and password are required"

        return

    }



    loading.value = true



    try{


        await usersApi.createUser({

            username:
                form.username,


            email:
                form.email,


            password:
                form.password,


            employee_id:
                form.employee_id || null,


            is_active:
                form.is_active,


            roles:
                form.roles


        })



        emit("created")



    }



    catch(err){


        error.value =
            getErrorMessage(err)



    }



    finally{


        loading.value = false


    }



}







onMounted(()=>{


    loadRoles()


})



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

animate-scale
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


<div class="flex items-center gap-3">


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

<UserPlus :size="22"/>

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

Create User

</h2>


<p

class="
text-sm
text-slate-500
"

>

Add a new platform user

</p>


</div>


</div>





<button

@click="emit('close')"

class="
rounded-xl

p-2

text-slate-500

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

dark:text-red-400
"

>

{{ error }}

</div>







<!-- Account -->

<div>


<p

class="
mb-4
flex
items-center
gap-2
font-semibold
text-slate-900
dark:text-white
"

>

<UserPlus :size="17"/>

Account Information

</p>



<div class="grid gap-4 md:grid-cols-2">


<input

v-model="form.username"

placeholder="Username"

class="input"

/>




<input

v-model="form.email"

type="email"

placeholder="Email address"

class="input"

/>


</div>


</div>







<!-- Password -->

<div>


<p

class="
mb-4
font-semibold
text-slate-900
dark:text-white
"

>

Security

</p>


<input

v-model="form.password"

type="password"

placeholder="Password"

class="input"

/>


</div>







<!-- Employee -->


<div>


<p

class="
mb-4
font-semibold
text-slate-900
dark:text-white
"

>

Employee Details

</p>



<input

v-model="form.employee_id"

placeholder="Employee ID"

class="input"

/>


</div>







<!-- Roles -->


<div>


<p

class="
mb-3
flex
items-center
gap-2
font-semibold
text-slate-900
dark:text-white
"

>

<ShieldCheck :size="17"/>

Assign Roles

</p>





<div

v-if="rolesLoading"

class="text-sm text-slate-500"

>

Loading roles...

</div>





<div

v-else

class="flex flex-wrap gap-3"

>


<label

v-for="role in roles"

:key="role.id"

class="cursor-pointer"

>


<input

type="checkbox"

:value="role.id"

v-model="form.roles"

class="hidden peer"

/>



<div

class="
rounded-xl
border
border-slate-200

px-4
py-2

text-sm

transition

peer-checked:border-blue-600

peer-checked:bg-blue-600

peer-checked:text-white

dark:border-slate-700
"

>

{{ role.name }}

</div>



</label>



</div>



</div>







<!-- Active -->


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

Account Status

</p>


<p class="text-sm text-slate-500">

Enable login access

</p>


</div>



<input

v-model="form.is_active"

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

border-slate-200

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

text-slate-600

hover:bg-slate-100

dark:text-slate-300

dark:hover:bg-slate-800
"

>

Cancel

</button>






<button

type="submit"

:disabled="loading"

class="
flex
items-center
gap-2

rounded-xl

bg-blue-600

px-6
py-2.5

font-medium

text-white

transition

hover:bg-blue-700

disabled:opacity-50
"

>

<Save :size="17"/>


{{ loading ? "Creating..." : "Create User" }}


</button>



</div>




</form>



</div>


</div>



</template>





<style scoped>

.animate-scale{

animation:scale .2s ease-out;

}



@keyframes scale{


from{

transform:scale(.95);

opacity:0;

}


to{

transform:scale(1);

opacity:1;

}


}

</style>