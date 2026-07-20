<script setup>

import {
    ref,
    onMounted,
    onUnmounted
} from "vue"



import {
    usePLCTagStore
} from "../stores/plcTagStore"



import PLCTagTable 
from "../components/PLCTagTable.vue"



import PLCTagEditModal 
from "../components/PLCTagEditModal.vue"



import PLCTagCreateModal 
from "../components/PLCTagCreateModal.vue"






const tagStore =
    usePLCTagStore()





// PLC ID

const plcId = 1







// ============================
// MODALS
// ============================


const editOpen = ref(false)


const createOpen = ref(false)



const selectedTag = ref(null)










// ============================
// REFRESH LIVE PLC VALUES
// ============================


async function refresh(){


    await tagStore.loadLiveValues(

        plcId

    )


}









// ============================
// OPEN EDIT
// ============================


function editTag(tag){


    selectedTag.value = tag


    editOpen.value = true


}










// ============================
// DELETE TAG
// ============================


async function deleteTag(tag){



    const confirmDelete =

        confirm(

            `Delete ${tag.name}?`

        )




    if(!confirmDelete){

        return

    }





    await tagStore.deleteTag(

        tag.id

    )



}









// ============================
// MOUNT
// ============================


onMounted(async()=>{


    await tagStore.loadTags()



    await refresh()



    tagStore.startAutoRefresh(

        plcId

    )


})









// ============================
// UNMOUNT
// ============================


onUnmounted(()=>{


    tagStore.stopAutoRefresh()



})



</script>








<template>


<div
class="
p-6
space-y-6
"
>





<!-- HEADER -->


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

PLC Tags

</h1>



<p
class="
text-gray-500
"
>

Real time PLC monitoring and control

</p>


</div>






<div
class="
flex
gap-3
"
>





<!-- ADD TAG -->


<button

@click="createOpen=true"

class="
px-4
py-2
rounded-lg
bg-green-600
text-white
hover:bg-green-700
"

>

+ Add Tag

</button>







<!-- REFRESH -->


<button

@click="refresh"

class="
px-4
py-2
rounded-lg
bg-blue-600
text-white
hover:bg-blue-700
"

>

Refresh

</button>





</div>





</div>









<!-- TABLE -->


<PLCTagTable


@edit="editTag"


@delete="deleteTag"



/>









<!-- CREATE MODAL -->


<PLCTagCreateModal


:show="createOpen"


@close="createOpen=false"



/>









<!-- EDIT MODAL -->


<PLCTagEditModal


:show="editOpen"


:tag="selectedTag"


@close="editOpen=false"



/>







</div>



</template>