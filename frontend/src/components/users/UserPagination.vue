<script setup>

import {
    ChevronLeft,
    ChevronRight,
} from "lucide-vue-next"



const props = defineProps({

    pagination: {

        type: Object,

        required: true,

    },


    currentPage: {

        type: Number,

        default: 1,

    }

})



const emit = defineEmits([

    "change-page"

])




// =========================
// Change Page
// =========================

const changePage = (page)=>{


    if(page < 1){

        return

    }


    emit(
        "change-page",
        page
    )


}



</script>



<template>


<div

class="
flex

flex-col

gap-4

rounded-2xl

border

border-slate-200

bg-white

p-4

sm:flex-row

sm:items-center

sm:justify-between

dark:border-slate-800

dark:bg-slate-900
"

>



<!-- Total -->

<div

class="
text-sm

text-slate-500

dark:text-slate-400
"

>


Showing page

<span

class="
font-semibold

text-slate-900

dark:text-white
"

>

{{ currentPage }}

</span>


&nbsp; • &nbsp;


Total Users:

<span

class="
font-semibold

text-slate-900

dark:text-white
"

>

{{ pagination.count }}

</span>


</div>







<!-- Buttons -->

<div

class="
flex

items-center

gap-3
"

>


<button


@click="changePage(currentPage - 1)"


:disabled="!pagination.previous"



class="
flex

items-center

gap-2

rounded-xl

border

border-slate-200

px-4

py-2

text-sm

transition

hover:bg-slate-100

disabled:cursor-not-allowed

disabled:opacity-50

dark:border-slate-700

dark:hover:bg-slate-800
"

>


<ChevronLeft :size="16"/>


Previous


</button>






<button


@click="changePage(currentPage + 1)"


:disabled="!pagination.next"



class="
flex

items-center

gap-2

rounded-xl

border

border-slate-200

px-4

py-2

text-sm

transition

hover:bg-slate-100

disabled:cursor-not-allowed

disabled:opacity-50

dark:border-slate-700

dark:hover:bg-slate-800
"

>


Next


<ChevronRight :size="16"/>


</button>



</div>



</div>



</template>