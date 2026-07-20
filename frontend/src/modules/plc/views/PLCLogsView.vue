<script setup>

import {
    ref,
    onMounted
} from "vue"



import {
    usePLCTagStore
} from "../stores/plcTagStore"



import PLCLogTable
from "../components/PLCLogTable.vue"




const tagStore =
    usePLCTagStore()



const logs =
    ref([])





async function load(){


    logs.value =
        await tagStore.loadLogs()


    console.log(
        "LOGS:",
        logs.value
    )


}






onMounted(()=>{

    load()

})


</script>





<template>


<div
class="
p-6
space-y-6
"
>



<div
class="
flex
justify-between
items-center
"
>



<div>

<h1
class="
text-2xl
font-bold
"
>

PLC Operation Logs

</h1>


<p
class="
text-gray-500
"
>

Track PLC changes and operations

</p>


</div>





<button

@click="load"

class="
bg-blue-600
text-white
px-4
py-2
rounded-lg
"

>

Refresh

</button>



</div>







<PLCLogTable

:logs="logs"

/>






</div>


</template>