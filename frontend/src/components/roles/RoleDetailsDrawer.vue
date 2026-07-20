<script setup>

import {
    X,
    ShieldCheck,
    Calendar,
    LockKeyhole
} from "lucide-vue-next"


import {
    ref,
    onMounted
} from "vue"


import { rolesApi } from "../../api/roles"





const props = defineProps({

    role: {

        type:Object,

        required:true

    }

})





const emit = defineEmits([

    "close"

])






const permissions = ref([])

const loading = ref(false)









// =========================
// Load Permissions
// =========================

const loadPermissions = async()=>{


    loading.value=true


    try{


        permissions.value =

            await rolesApi.getRolePermissions(

                props.role.id

            )



    }


    catch(error){


        console.error(

            "Permission loading error:",

            error

        )


    }


    finally{


        loading.value=false


    }


}







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

bg-slate-950/40

backdrop-blur-sm
"

>



<!-- Drawer -->


<div

class="
absolute

right-0

top-0

h-full

w-full

max-w-md

overflow-y-auto

border-l

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

{{role.name}}

</h2>


<p class="text-sm text-slate-500">

Role Details

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









<!-- Content -->


<div class="space-y-6 p-6">






<!-- Type -->


<div>


<p

class="
mb-2

text-sm

text-slate-500
"

>

Type

</p>



<span

:class="[

'rounded-full px-3 py-1 text-xs font-medium',

role.is_system

?

'bg-purple-100 text-purple-700 dark:bg-purple-950 dark:text-purple-300'

:

'bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300'

]"

>


{{role.is_system ? "System Role" : "Custom Role"}}


</span>


</div>








<!-- Description -->


<div>


<p

class="
mb-2

text-sm

text-slate-500
"

>

Description

</p>


<p

class="
rounded-xl

bg-slate-50

p-4

text-sm

text-slate-700

dark:bg-slate-800

dark:text-slate-300
"

>

{{role.description || "No description"}}

</p>


</div>









<!-- Dates -->


<div class="space-y-3">


<div

class="
flex

items-center

gap-3

text-sm

text-slate-600

dark:text-slate-300
"

>

<Calendar :size="17"/>


Created:

{{new Date(role.created_at).toLocaleString()}}


</div>





<div

class="
flex

items-center

gap-3

text-sm

text-slate-600

dark:text-slate-300
"

>

<Calendar :size="17"/>


Updated:

{{new Date(role.updated_at).toLocaleString()}}


</div>


</div>









<!-- Permissions -->


<div>


<div

class="
mb-3

flex

items-center

gap-2

font-semibold

dark:text-white
"

>


<LockKeyhole :size="18"/>


Permissions


</div>





<div

v-if="loading"

class="
text-sm

text-slate-500
"

>

Loading permissions...

</div>







<div

v-else-if="!permissions.length"

class="
rounded-xl

bg-slate-50

p-4

text-sm

text-slate-500

dark:bg-slate-800
"

>

No permissions assigned.

</div>







<div

v-else

class="
space-y-2
"

>


<div

v-for="permission in permissions"

:key="permission.id"

class="
rounded-xl

border

border-slate-200

p-3

dark:border-slate-700
"

>


<p

class="
text-sm

font-medium

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


</div>


</div>







</div>


</div>


</div>


</template>