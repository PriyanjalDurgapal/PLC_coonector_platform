<script setup>

import {
    computed
} from "vue"


import {
    Pencil,
    Trash2
} from "lucide-vue-next"


import {
    usePLCTagStore
} from "../stores/plcTagStore"


import PLCTagControl from "./PLCTagControl.vue"



const emit = defineEmits([

    "edit",

    "delete"

])



const tagStore = usePLCTagStore()



const tags = computed(()=>{

    return tagStore.tags

})





function getValue(tag){


    const liveValue =
        tagStore.getTagValue(tag)


    if(liveValue !== null){

        return liveValue

    }


    return "-"

}





function editTag(tag){

    emit(
        "edit",
        tag
    )

}





function deleteTag(tag){

    emit(
        "delete",
        tag
    )

}



</script>





<template>


<div
class="
bg-white
rounded-xl
shadow
overflow-hidden
"
>



<table
class="
w-full
"
>


<thead
class="
bg-gray-100
"
>


<tr>


<th class="p-3 text-left">
Tag Name
</th>


<th class="p-3">
Address
</th>


<th class="p-3">
Type
</th>


<th class="p-3">
PLC Value
</th>


<th class="p-3">
Unit
</th>


<th class="p-3">
Colors
</th>


<th class="p-3">
Control
</th>


<th class="p-3">
Actions
</th>


</tr>


</thead>






<tbody>


<tr

v-for="tag in tags"

:key="tag.id"

class="
border-b
hover:bg-gray-50
"

>



<!-- TAG NAME -->

<td
class="
p-3
"
>


<div
class="
font-semibold
"
>

{{tag.name}}

</div>


<div
class="
text-xs
text-gray-500
"
>

{{tag.description}}

</div>


</td>





<!-- ADDRESS -->


<td class="p-3 text-center">


{{tag.address}}


</td>







<!-- DATA TYPE -->


<td class="p-3 text-center">


<span
class="
px-2
py-1
rounded
bg-gray-100
text-sm
"
>

{{tag.data_type}}

</span>


</td>








<!-- LIVE VALUE -->


<td class="p-3 text-center">


<span
class="
font-bold
text-lg
"
>


{{getValue(tag)}}


</span>


</td>









<!-- UNIT -->


<td class="p-3 text-center">


{{tag.unit || "-"}}


</td>









<!-- COLORS -->


<td class="p-3">


<div
class="
flex
gap-2
justify-center
"
>


<div

class="
w-7
h-7
rounded
border
"

:title="'ON '+tag.on_color"

:style="{

backgroundColor:
tag.on_color

}"

></div>





<div

class="
w-7
h-7
rounded
border
"

:title="'OFF '+tag.off_color"

:style="{

backgroundColor:
tag.off_color

}"

></div>





<div

class="
w-7
h-7
rounded
border
"

:title="'LOW '+tag.low_color"

:style="{

backgroundColor:
tag.low_color

}"

></div>





<div

class="
w-7
h-7
rounded
border
"

:title="'HIGH '+tag.high_color"

:style="{

backgroundColor:
tag.high_color

}"

></div>




</div>


</td>









<!-- CONTROL -->


<td class="p-3">


<PLCTagControl

:tag="tag"

/>


</td>









<!-- ACTIONS -->


<td class="p-3">


<div
class="
flex
justify-center
gap-2
"
>


<button

@click="editTag(tag)"

class="
p-2
rounded
hover:bg-blue-100
text-blue-600
"

>


<Pencil size="18"/>


</button>






<button

@click="deleteTag(tag)"

class="
p-2
rounded
hover:bg-red-100
text-red-600
"

>


<Trash2 size="18"/>


</button>





</div>


</td>







</tr>





<tr

v-if="tags.length===0"

>


<td

colspan="8"

class="
p-10
text-center
text-gray-500
"

>

No PLC Tags Found


</td>


</tr>





</tbody>



</table>



</div>



</template>