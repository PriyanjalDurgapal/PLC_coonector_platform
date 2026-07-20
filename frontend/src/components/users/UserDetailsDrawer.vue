<script setup>

import {
    X,
    User,
    Mail,
    BadgeCheck,
    ShieldCheck,
    Calendar,
    BriefcaseBusiness
} from "lucide-vue-next"


const props = defineProps({

    user:{
        type:Object,
        required:true
    }

})


const emit = defineEmits([

    "close"

])



</script>


<template>


<div>


<!-- Overlay -->

<div

class="
fixed
inset-0

z-40

bg-black/40

backdrop-blur-sm
"

@click="emit('close')"

></div>





<!-- Drawer -->


<div

class="
fixed

right-0

top-0

z-50

h-screen

w-full

max-w-md

overflow-y-auto

border-l

border-slate-200

bg-white

shadow-2xl

dark:border-slate-800

dark:bg-slate-900

animate-slide
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


<div>

<h2

class="
text-xl

font-bold

text-slate-900

dark:text-white
"

>

User Profile

</h2>


<p

class="
text-sm

text-slate-500
"

>

User details and permissions

</p>


</div>





<button

@click="emit('close')"

class="
rounded-xl

p-2

text-slate-500

transition

hover:bg-slate-100

dark:hover:bg-slate-800
"

>

<X :size="20"/>

</button>


</div>









<!-- Content -->


<div class="space-y-6 p-6">





<!-- Avatar -->


<div

class="
flex

items-center

gap-4
"

>


<div

class="
flex

h-16

w-16

items-center

justify-center

rounded-full

bg-blue-100

text-blue-600

dark:bg-blue-950

dark:text-blue-400
"

>

<User :size="30"/>

</div>




<div>


<h3

class="
text-lg

font-semibold

dark:text-white
"

>

{{user.username}}

</h3>


<p

class="
text-sm

text-slate-500
"

>

User ID: {{user.id}}

</p>


</div>


</div>









<!-- Information Card -->


<div

class="
space-y-4

rounded-2xl

border

border-slate-200

p-5

dark:border-slate-700
"

>


<h4

class="
font-semibold

dark:text-white
"

>

Account Information

</h4>




<div class="flex gap-3">


<Mail
:size="18"
class="text-slate-400"
/>


<div>

<p class="text-xs text-slate-500">

Email

</p>

<p class="text-sm dark:text-white">

{{user.email || "-"}}

</p>


</div>


</div>






<div class="flex gap-3">


<BriefcaseBusiness
:size="18"
class="text-slate-400"
/>


<div>

<p class="text-xs text-slate-500">

Employee ID

</p>

<p class="text-sm dark:text-white">

{{user.employee_id || "-"}}

</p>


</div>


</div>






<div class="flex gap-3">


<BadgeCheck
:size="18"
class="text-slate-400"
/>


<div>

<p class="text-xs text-slate-500">

Account Status

</p>



<span

:class="[

'inline-flex rounded-full px-3 py-1 text-xs font-medium',

user.is_active

?

'bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300'

:

'bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300'

]"

>

{{user.is_active ? "Active":"Inactive"}}

</span>


</div>


</div>





</div>









<!-- Roles -->


<div

class="
rounded-2xl

border

border-slate-200

p-5

dark:border-slate-700
"

>


<h4

class="
mb-4

flex

items-center

gap-2

font-semibold

dark:text-white
"

>

<ShieldCheck :size="18"/>

Roles

</h4>





<div

v-if="user.roles?.length"

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

{{role}}

</span>


</div>





<p

v-else

class="
text-sm

text-slate-500
"

>

No roles assigned.

</p>


</div>









<!-- Permission Info -->


<div

class="
rounded-2xl

border

border-slate-200

p-5

dark:border-slate-700
"

>


<h4

class="
mb-3

font-semibold

dark:text-white
"

>

Access

</h4>



<div class="flex items-center gap-3">


<Calendar
:size="18"
class="text-slate-400"
/>


<p

class="
text-sm

dark:text-white
"

>

{{user.is_staff ? "Staff User":"Normal User"}}

</p>


</div>


</div>





</div>





</div>


</div>


</template>





<style scoped>

.animate-slide{

animation:slide .25s ease-out;

}


@keyframes slide{


from{

transform:translateX(100%);

}


to{

transform:translateX(0);

}


}

</style>