<script setup>

import {
    Search,
    RotateCcw,
} from "lucide-vue-next"

import { ref, watch } from "vue"


const emit = defineEmits([

    "filter-change"

])


const search = ref("")


const status = ref("")


const role = ref("")


// Send filters to parent

const emitFilters = () => {


    emit(
        "filter-change",
        {

            search: search.value,

            is_active: status.value,

            role: role.value,

            page: 1,

        }
    )


}


// Search debounce

let timeout = null


watch(search, ()=>{


    clearTimeout(timeout)


    timeout = setTimeout(()=>{


        emitFilters()


    },500)


})


// Status change

watch(status, ()=>{


    emitFilters()


})


// Role change

watch(role, ()=>{


    emitFilters()


})


// Reset

const resetFilters = ()=>{


    search.value = ""

    status.value = ""

    role.value = ""

    emitFilters()


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

p-5

md:flex-row

md:items-center

dark:border-slate-800

dark:bg-slate-900
"

>


    <!-- Search -->

    <div
    class="
    relative

    flex-1
    "
    >

        <Search

        class="
        absolute

        left-3

        top-1/2

        -translate-y-1/2

        text-slate-400
        "

        :size="18"

        />


        <input

        v-model="search"

        type="text"

        placeholder="Search users..."

        class="
        w-full

        rounded-xl

        border

        border-slate-200

        bg-white

        py-2.5

        pl-10

        pr-4

        text-sm

        outline-none

        transition

        focus:border-blue-500

        dark:border-slate-700

        dark:bg-slate-950

        dark:text-white
        "

        />

    </div>



    <!-- Status -->

    <select

    v-model="status"

    class="
    rounded-xl

    border

    border-slate-200

    bg-white

    px-4

    py-2.5

    text-sm

    outline-none

    dark:border-slate-700

    dark:bg-slate-950

    dark:text-white
    "

    >

        <option value="">
            All Status
        </option>


        <option value="true">
            Active
        </option>


        <option value="false">
            Inactive
        </option>


    </select>



    <!-- Role -->

    <select

    v-model="role"

    class="
    rounded-xl

    border

    border-slate-200

    bg-white

    px-4

    py-2.5

    text-sm

    outline-none

    dark:border-slate-700

    dark:bg-slate-950

    dark:text-white
    "

    >

        <option value="">
            All Roles
        </option>


        <option value="1">
            Administrator
        </option>


    </select>



    <!-- Reset -->

    <button

    @click="resetFilters"

    class="
    flex

    items-center

    justify-center

    gap-2

    rounded-xl

    border

    border-slate-200

    px-4

    py-2.5

    text-sm

    transition

    hover:bg-slate-100

    dark:border-slate-700

    dark:hover:bg-slate-800
    "

    >

        <RotateCcw :size="16"/>

        Reset

    </button>


</div>


</template>