<script setup>

import {
    MoreVertical,
    ShieldCheck
} from "lucide-vue-next"

import { ref } from "vue"



defineProps({

    roles: {

        type: Array,

        default:()=>[]

    },


    loading: {

        type:Boolean,

        default:false

    }

})



const emit = defineEmits([

    "view",

    "permissions",

    "edit",

    "delete"

])



const activeMenu = ref(null)



const openMenu = (id)=>{


    activeMenu.value =
        activeMenu.value === id
        ? null
        : id

}




const viewRole = (role)=>{

    activeMenu.value=null

    emit(
        "view",
        role
    )

}



const permissionRole = (role)=>{

    activeMenu.value=null

    emit(
        "permissions",
        role
    )

}



const editRole = (role)=>{

    activeMenu.value=null

    emit(
        "edit",
        role
    )

}



const deleteRole = (role)=>{

    activeMenu.value=null

    emit(
        "delete",
        role
    )

}


</script>





<template>


<div

class="
overflow-hidden

rounded-2xl

border

border-slate-200

bg-white

dark:border-slate-800

dark:bg-slate-900
"

>



<!-- Loading -->

<div

v-if="loading"

class="
p-10
text-center
text-slate-500
"

>

Loading roles...

</div>





<!-- Empty -->

<div

v-else-if="!roles.length"

class="
p-10
text-center
text-slate-500
"

>

No roles found.

</div>







<div

v-else

class="overflow-x-auto"

>


<table

class="
w-full
text-left
text-sm
"

>


<thead

class="
border-b

border-slate-200

bg-slate-50

dark:border-slate-800

dark:bg-slate-950
"

>


<tr>


<th class="px-6 py-4 font-semibold">

Role

</th>



<th class="px-6 py-4 font-semibold">

Description

</th>



<th class="px-6 py-4 font-semibold">

Type

</th>



<th class="px-6 py-4 font-semibold">

Created

</th>



<th class="px-6 py-4 text-right font-semibold">

Action

</th>


</tr>


</thead>






<tbody>


<tr

v-for="role in roles"

:key="role.id"

class="
border-b

border-slate-100

transition

hover:bg-slate-50

dark:border-slate-800

dark:hover:bg-slate-800/50
"

>






<!-- Role -->


<td class="px-6 py-4">


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
h-10
w-10

items-center
justify-center

rounded-full

bg-blue-100

text-blue-600

dark:bg-blue-950

dark:text-blue-400
"

>

<ShieldCheck :size="18"/>

</div>




<div>


<p

class="
font-medium

text-slate-900

dark:text-white
"

>

{{role.name}}

</p>


<p class="text-xs text-slate-500">

ID: {{role.id}}

</p>


</div>


</div>


</td>








<!-- Description -->


<td

class="
px-6
py-4

text-slate-600

dark:text-slate-300
"

>

{{role.description || "-"}}

</td>








<!-- Type -->


<td class="px-6 py-4">


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


{{

role.is_system

?

"System"

:

"Custom"

}}


</span>


</td>








<!-- Date -->


<td

class="
px-6
py-4

text-slate-500
"

>


{{

new Date(role.created_at)

.toLocaleDateString()

}}


</td>








<!-- Action -->


<td

class="
px-6
py-4
text-right
"

>


<div

class="
relative
inline-block
"

>


<button

@click="openMenu(role.id)"

class="
rounded-lg
p-2

text-slate-500

hover:bg-slate-100

dark:hover:bg-slate-800
"

>


<MoreVertical :size="18"/>


</button>







<div

v-if="activeMenu===role.id"

class="
absolute

right-0

z-30

mt-2

w-48

rounded-xl

border

border-slate-200

bg-white

p-2

shadow-xl

dark:border-slate-700

dark:bg-slate-900
"

>


<button

@click="viewRole(role)"

class="
menu-item
"

>

View

</button>




<button

@click="permissionRole(role)"

class="
menu-item
"

>

Permissions

</button>




<button

@click="editRole(role)"

class="
menu-item
"

>

Edit

</button>





<button

@click="deleteRole(role)"

class="
menu-item

text-red-600
"

>

Delete

</button>



</div>



</div>


</td>







</tr>


</tbody>


</table>


</div>


</div>


</template>





<style scoped>


.menu-item{

width:100%;

text-align:left;

padding:8px 12px;

border-radius:8px;

font-size:14px;

color:rgb(51 65 85);

}



.menu-item:hover{

background:rgb(241 245 249);

}



</style>