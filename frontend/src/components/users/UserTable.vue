<script setup>

import {
    MoreVertical,
    Mail,
    User
} from "lucide-vue-next"

import { ref } from "vue"



const props = defineProps({

    users: {

        type: Array,

        default: () => []

    },


    loading: {

        type: Boolean,

        default: false

    }

})




const emit = defineEmits([

    "view",

    "edit",

    "delete"

])





const activeMenu = ref(null)





// =========================
// Dropdown
// =========================

const openMenu = (id)=>{


    activeMenu.value =
        activeMenu.value === id
        ? null
        : id


}






// =========================
// Actions
// =========================

const viewUser = (user)=>{


    activeMenu.value = null


    emit(
        "view",
        user
    )


}



const editUser = (user)=>{


    activeMenu.value = null


    emit(
        "edit",
        user
    )


}




const deleteUser = (user)=>{


    activeMenu.value = null


    emit(
        "delete",
        user
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

Loading users...

</div>







<!-- Empty -->

<div

v-else-if="!users.length"

class="
p-10

text-center

text-slate-500
"

>

No users found.

</div>







<!-- Table -->

<div

v-else

class="
overflow-x-auto
"

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

User

</th>


<th class="px-6 py-4 font-semibold">

Email

</th>


<th class="px-6 py-4 font-semibold">

Employee ID

</th>


<th class="px-6 py-4 font-semibold">

Roles

</th>


<th class="px-6 py-4 font-semibold">

Status

</th>


<th class="px-6 py-4 text-right font-semibold">

Action

</th>


</tr>


</thead>







<tbody>


<tr

v-for="user in users"

:key="user.id"

class="
border-b

border-slate-100

transition

hover:bg-slate-50

dark:border-slate-800

dark:hover:bg-slate-800/50
"

>





<!-- User -->


<td

class="
px-6
py-4
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

<User :size="18"/>

</div>




<div>


<p

class="
font-medium

text-slate-900

dark:text-white
"

>

{{ user.username }}

</p>


<p

class="
text-xs

text-slate-500
"

>

ID: {{ user.id }}

</p>


</div>


</div>


</td>







<!-- Email -->


<td

class="
px-6
py-4
"

>


<div

class="
flex

items-center

gap-2

text-slate-600

dark:text-slate-300
"

>


<Mail :size="16"/>


{{ user.email }}


</div>


</td>







<!-- Employee -->


<td

class="
px-6

py-4

text-slate-600

dark:text-slate-300
"

>


{{ user.employee_id || "-" }}


</td>







<!-- Roles -->


<td

class="
px-6
py-4
"

>


<div

class="
flex

flex-wrap

gap-2
"

>


<span

v-for="role in user.roles"

:key="role"

class="
rounded-full

bg-blue-100

px-3

py-1

text-xs

font-medium

text-blue-700

dark:bg-blue-950

dark:text-blue-300
"

>

{{ role }}


</span>


</div>


</td>







<!-- Status -->


<td

class="
px-6

py-4
"

>


<span

:class="[

'rounded-full px-3 py-1 text-xs font-medium',

user.is_active

?

'bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300'

:

'bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300'

]"

>


{{

user.is_active

?

"Active"

:

"Inactive"

}}



</span>


</td>









<!-- Actions -->


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

@click="openMenu(user.id)"

class="
rounded-lg

p-2

text-slate-500

transition

hover:bg-slate-100

dark:hover:bg-slate-800
"

>


<MoreVertical :size="18"/>


</button>








<!-- Dropdown -->


<div

v-if="activeMenu === user.id"

class="
absolute

right-0

z-30

mt-2

w-40

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

@click="viewUser(user)"

class="
w-full

rounded-lg

px-3

py-2

text-left

text-sm

text-slate-700

hover:bg-slate-100

dark:text-slate-200

dark:hover:bg-slate-800
"

>

View

</button>





<button

@click="editUser(user)"

class="
w-full

rounded-lg

px-3

py-2

text-left

text-sm

text-slate-700

hover:bg-slate-100

dark:text-slate-200

dark:hover:bg-slate-800
"

>

Edit

</button>





<button

@click="deleteUser(user)"

class="
w-full

rounded-lg

px-3

py-2

text-left

text-sm

text-red-600

hover:bg-red-50

dark:hover:bg-red-950
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