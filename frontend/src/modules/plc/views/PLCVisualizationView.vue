<script setup>


import {
onMounted,
onUnmounted
}
from "vue"



import {
usePLCTagStore
}
from "../stores/plcTagStore"



import TagCard from "../components/TagCard.vue"




const tagStore =
usePLCTagStore()



const plcId=1







onMounted(async()=>{


await tagStore.loadTags()



await tagStore.loadLiveValues(
plcId
)



tagStore.startAutoRefresh(
plcId
)


})







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


<h1

class="
text-3xl
font-bold
"

>

PLC Visualization

</h1>






<div

class="
grid
grid-cols-1
md:grid-cols-3
gap-6
"

>



<TagCard


v-for="tag in tagStore.tags"


:key="tag.id"


:tag="tag"


:value="tagStore.getTagValue(tag)"


/>



</div>




</div>


</template>