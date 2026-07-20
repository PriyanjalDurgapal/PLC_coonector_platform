<script setup>

import {
    MoreVertical,
    Eye,
    Pencil,
    KeyRound,
    Trash2
} from "lucide-vue-next"

import {
    ref,
    onMounted,
    onBeforeUnmount
} from "vue"


const props = defineProps({

    user:{
        type:Object,
        required:true
    }

})


const emit = defineEmits([

    "view",

    "edit",

    "reset-password",

    "delete"

])


const open = ref(false)



const toggle = ()=>{

    open.value = !open.value

}



const close = ()=>{

    open.value=false

}



const handleOutside = (event)=>{

    if(!event.target.closest(".action-menu")){

        close()

    }

}



onMounted(()=>{

    document.addEventListener(
        "click",
        handleOutside
    )

})


onBeforeUnmount(()=>{

    document.removeEventListener(
        "click",
        handleOutside
    )

})


</script>


<template>


<div class="relative action-menu">


<button

@click.stop="toggle"

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





<div

v-if="open"

class="
absolute
right-0
top-10

z-50

w-48

overflow-hidden

rounded-xl

border

border-slate-200

bg-white

shadow-xl

dark:border-slate-700

dark:bg-slate-900
"

>


<button

@click="
emit('view');
close()
"

class="menu-item"

>

<Eye :size="16"/>

View Profile

</button>





<button

@click="
emit('edit');
close()
"

class="menu-item"

>

<Pencil :size="16"/>

Edit User

</button>





<button

@click="
emit('reset-password');
close()
"

class="menu-item"

>

<KeyRound :size="16"/>

Reset Password

</button>





<div
class="
my-1
border-t
border-slate-200
dark:border-slate-700
"
></div>





<button

@click="
emit('delete');
close()
"

class="
menu-item

text-red-600

hover:bg-red-50

dark:hover:bg-red-950
"

>

<Trash2 :size="16"/>

Delete User

</button>


</div>


</div>


</template>



<style scoped>

.menu-item{

display:flex;

align-items:center;

gap:10px;

width:100%;

padding:10px 14px;

font-size:14px;

text-align:left;

color:inherit;

transition:.2s;

}


.menu-item:hover{

background:#f1f5f9;

}


</style>