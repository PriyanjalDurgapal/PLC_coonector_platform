<script setup>

import {
    X,
    Save,
    ShieldCheck
} from "lucide-vue-next"


import {
    ref,
    watch,
    onMounted
} from "vue"


import { rolesApi } from "../../api/roles"





const props = defineProps({

    role:{

        type:Object,

        required:true

    }

})





const emit = defineEmits([

    "close",

    "updated"

])







const loading = ref(false)

const permissionsLoading = ref(false)


const error = ref("")



const permissions = ref([])


const selectedPermissions = ref([])








// =========================
// Load Permissions
// =========================

const loadPermissions = async()=>{


    permissionsLoading.value=true


    try{


        permissions.value =
            await rolesApi.getPermissions()



    }


    catch(err){


        console.error(
            "Permission loading error",
            err
        )


    }


    finally{


        permissionsLoading.value=false


    }


}









// =========================
// Load Role Permissions
// =========================

const loadRolePermissions = async()=>{


    try{


        const data =
            await rolesApi.getRolePermissions(
                props.role.id
            )



        selectedPermissions.value =

            data.map(
                permission =>
                    Number(permission.id)
            )


    }


    catch(err){


        console.error(
            "Role permissions error",
            err
        )


    }


}









// =========================
// Save
// =========================

const submit = async()=>{


    loading.value=true


    error.value=""


    try{


        await rolesApi.assignPermissions(

            props.role.id,

            selectedPermissions.value

        )



        emit("updated")



    }


    catch(err){


        console.error(
            err.response?.data
        )


        error.value =
            "Failed to assign permissions"


    }


    finally{


        loading.value=false


    }


}








watch(

    ()=>props.role,

    ()=>{


        if(props.role){

            loadRolePermissions()

        }


    },

    {
        immediate:true
    }

)






onMounted(()=>{

    loadPermissions()

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

max-w-3xl

max-h-[85vh]

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

<ShieldCheck :size="22"/>

</div>



<div>


<h2

class="
text-xl

font-bold

dark:text-white
"

>

Assign Permissions

</h2>


<p class="text-sm text-slate-500">

{{role.name}}

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





<div

v-if="error"

class="
rounded-xl

bg-red-50

p-3

text-sm

text-red-600
"

>

{{error}}

</div>








<div

v-if="permissionsLoading"

class="
p-10

text-center

text-slate-500
"

>

Loading permissions...

</div>








<div

v-else

class="
grid

grid-cols-1

gap-3

overflow-y-auto

md:grid-cols-2

max-h-[450px]
"

>



<label

v-for="permission in permissions"

:key="permission.id"

class="
cursor-pointer
"

>


<input

type="checkbox"

:value="permission.id"

v-model="selectedPermissions"

class="hidden peer"

/>




<div

class="
rounded-xl

border

border-slate-200

p-4

transition

peer-checked:border-blue-600

peer-checked:bg-blue-50

dark:border-slate-700

dark:peer-checked:bg-blue-950
"

>


<p

class="
font-medium

text-slate-900

dark:text-white
"

>

{{permission.name}}

</p>



<p

class="
text-xs

text-slate-500
"

>

{{permission.codename}}

</p>


</div>


</label>


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
"

>


<Save :size="17"/>


{{loading ? "Saving..." : "Save Permissions"}}


</button>



</div>




</form>


</div>


</div>


</template>