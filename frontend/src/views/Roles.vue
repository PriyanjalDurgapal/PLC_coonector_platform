<script setup>

import {
    onMounted,
    ref
} from "vue"


import {
    Plus
} from "lucide-vue-next"


import { rolesApi } from "../api/roles"



import RoleFormModal from "../components/roles/RoleFormModal.vue"

import RoleDetailsDrawer from "../components/roles/RoleDetailsDrawer.vue"

import RolePermissionModal from "../components/roles/RolePermissionModal.vue"





const loading = ref(false)



const roles = ref([])



// Create

const showCreateModal = ref(false)


// Details

const showDetails = ref(false)

const selectedRole = ref(null)



// Permissions

const showPermissionModal = ref(false)








// =========================
// Load Roles
// =========================

const loadRoles = async()=>{


    loading.value=true


    try{


        roles.value =

            await rolesApi.getRoles()



    }

    catch(error){


        console.error(

            "Roles loading error",

            error

        )


    }


    finally{


        loading.value=false


    }


}









// =========================
// Create
// =========================

const roleCreated = ()=>{


    showCreateModal.value=false


    loadRoles()


}









// =========================
// View
// =========================

const viewRole = (role)=>{


    selectedRole.value = role


    showDetails.value=true


}








// =========================
// Permission
// =========================

const managePermissions = (role)=>{


    selectedRole.value = role


    showPermissionModal.value=true


}







const closeAll = ()=>{


    selectedRole.value=null


}






const permissionsUpdated = ()=>{


    showPermissionModal.value=false


    loadRoles()


}






onMounted(()=>{


    loadRoles()


})


</script>








<template>


<div class="space-y-6">







<!-- Header -->


<div

class="
flex

items-center

justify-between
"

>


<div>


<h1

class="
text-3xl

font-bold

text-slate-900

dark:text-white
"

>

Roles

</h1>



<p class="text-slate-500">

Manage user roles and permissions.

</p>


</div>







<button

@click="showCreateModal=true"

class="
flex

items-center

gap-2

rounded-xl

bg-blue-600

px-5

py-3

text-white

hover:bg-blue-700
"

>


<Plus :size="18"/>


Create Role


</button>



</div>









<!-- Loading -->


<div

v-if="loading"

class="
rounded-2xl

bg-white

p-10

text-center

dark:bg-slate-900
"

>

Loading roles...

</div>









<!-- Empty -->


<div

v-else-if="!roles.length"

class="
rounded-2xl

bg-white

p-10

text-center

dark:bg-slate-900
"

>

No roles found.

</div>









<!-- Role Cards -->


<div

v-else

class="
grid

gap-5

md:grid-cols-2

xl:grid-cols-3
"

>


<div

v-for="role in roles"

:key="role.id"

class="
rounded-2xl

border

border-slate-200

bg-white

p-6

dark:border-slate-800

dark:bg-slate-900
"

>


<div class="flex items-start justify-between">


<div>


<h2

class="
text-lg

font-bold

dark:text-white
"

>

{{role.name}}

</h2>


<p

class="
mt-2

text-sm

text-slate-500
"

>

{{role.description || "No description"}}

</p>


</div>




<span

class="
rounded-full

bg-blue-100

px-3

py-1

text-xs

text-blue-700
"

>

{{role.is_system ? "System" : "Custom"}}

</span>


</div>








<div

class="
mt-6

flex

gap-3
"

>


<button

@click="viewRole(role)"

class="
rounded-xl

bg-slate-100

px-4

py-2

text-sm

dark:bg-slate-800

dark:text-white
"

>

View


</button>







<button

@click="managePermissions(role)"

class="
rounded-xl

bg-blue-600

px-4

py-2

text-sm

text-white
"

>

Permissions


</button>


</div>



</div>


</div>









<!-- Create -->


<RoleFormModal

v-if="showCreateModal"

@close="showCreateModal=false"

@created="roleCreated"

/>








<!-- Details -->


<RoleDetailsDrawer

v-if="showDetails"

:role="selectedRole"

@close="showDetails=false"

/>








<!-- Permissions -->


<RolePermissionModal

v-if="showPermissionModal"

:role="selectedRole"

@close="showPermissionModal=false"

@updated="permissionsUpdated"

/>





</div>


</template>