<script setup>

import {
    X,
    Save,
    UserCog,
    ShieldCheck
} from "lucide-vue-next"


import {
    reactive,
    ref,
    watch,
    onMounted
} from "vue"


import { usersApi } from "../../api/users"

import { rolesApi } from "../../api/roles"





const props = defineProps({

    user: {

        type:Object,

        required:true

    }

})



const emit = defineEmits([

    "close",

    "updated"

])





const loading = ref(false)

const rolesLoading = ref(false)


const roles = ref([])


const error = ref("")







const form = reactive({

    username:"",

    email:"",

    employee_id:"",

    is_active:true,

    roles:[]

})









// =========================
// Load Existing User
// =========================

const loadUser = ()=>{


    if(!props.user)
        return



    form.username =
        props.user.username || ""



    form.email =
        props.user.email || ""



    form.employee_id =
        props.user.employee_id || ""



    form.is_active =
        props.user.is_active



    /*
        Important:
        API gives role names:

        [
          "Administrator"
        ]

        Convert them to IDs after roles load
    */


    form.roles = []

}










// =========================
// Load Roles
// =========================

const loadRoles = async()=>{


    rolesLoading.value=true



    try{


        roles.value =
            await rolesApi.getRoles()



        /*
          Match user role names
          with role ids
        */


        if(props.user?.roles){


            form.roles = roles.value

            .filter(role =>
                props.user.roles.includes(
                    role.name
                )
            )

            .map(role =>
                Number(role.id)
            )


        }



    }


    catch(err){


        console.error(
            "Role loading error",
            err
        )


    }


    finally{


        rolesLoading.value=false


    }


}









// =========================
// Error Handler
// =========================

const getErrorMessage = (err)=>{


    const data =
        err.response?.data



    console.log(
        "Backend Error:",
        data
    )



    if(!data)

        return "Server connection failed"



    if(data.detail)

        return data.detail



    if(data.message)

        return data.message



    if(typeof data === "object"){


        return Object.values(data)

        .flat()

        .join(", ")


    }



    return "Something went wrong"


}









// =========================
// Submit Update
// =========================

const submit = async()=>{


    loading.value=true


    error.value=""



    try{


        await usersApi.updateUser(

            props.user.id,

            {


                username:
                    form.username,


                email:
                    form.email,


                employee_id:
                    form.employee_id || null,


                is_active:
                    form.is_active,


                roles:
                    form.roles.map(
                        id=>Number(id)
                    )


            }

        )



        emit("updated")



    }


    catch(err){


        error.value =
            getErrorMessage(err)


    }


    finally{


        loading.value=false


    }


}








watch(

    ()=>props.user,

    ()=>{


        loadUser()


    },

    {
        immediate:true
    }

)






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

<UserCog :size="22"/>

</div>



<div>


<h2 class="text-xl font-bold dark:text-white">

Edit User

</h2>


<p class="text-sm text-slate-500">

Update user information

</p>


</div>


</div>



<button

@click="emit('close')"

class="rounded-xl p-2 hover:bg-slate-100 dark:hover:bg-slate-800"

>

<X :size="20"/>

</button>


</div>







<form

@submit.prevent="submit"

class="space-y-6 p-6"

>




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








<div>


<p class="mb-4 font-semibold dark:text-white">

Account Information

</p>


<div class="grid gap-4 md:grid-cols-2">


<input

v-model="form.username"

class="input"

placeholder="Username"

/>



<input

v-model="form.email"

class="input"

placeholder="Email"

/>



</div>


</div>









<div>


<p class="mb-4 font-semibold dark:text-white">

Employee Details

</p>


<input

v-model="form.employee_id"

class="input"

placeholder="Employee ID"

/>


</div>








<div>


<p

class="
mb-3
flex
items-center
gap-2
font-semibold
dark:text-white
"

>

<ShieldCheck :size="17"/>

Roles

</p>





<div v-if="rolesLoading">

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
px-4
py-2
text-sm

peer-checked:bg-blue-600
peer-checked:text-white
peer-checked:border-blue-600
"

>

{{role.name}}

</div>


</label>


</div>


</div>








<div

class="
flex
items-center
justify-between

rounded-xl

border

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

class="h-5 w-5 accent-blue-600"

/>


</div>








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

class="rounded-xl px-5 py-2.5 hover:bg-slate-100"

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
"

>

<Save :size="17"/>


{{loading ? "Updating..." : "Update User"}}


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