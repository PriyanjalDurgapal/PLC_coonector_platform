<script setup>

defineProps({

    logs:{
        type:Array,
        default:()=>[]
    }

})

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
text-sm
"
>


<thead
class="
bg-gray-100
"
>


<tr>

<th class="p-3 text-left">
Time
</th>


<th class="p-3 text-left">
User
</th>


<th class="p-3 text-left">
PLC
</th>


<th class="p-3 text-left">
Tag
</th>


<th class="p-3 text-left">
Operation
</th>


<th class="p-3 text-left">
Old Value
</th>


<th class="p-3 text-left">
New Value
</th>


</tr>


</thead>





<tbody>


<tr

v-for="log in logs"

:key="log.id"

class="
border-t
hover:bg-gray-50
"

>


<td class="p-3">

{{ 
new Date(
log.created_at
).toLocaleString()

}}

</td>





<td class="p-3">

{{log.user_name}}

</td>





<td class="p-3">

{{log.plc_name}}

</td>





<td class="p-3 font-medium">

{{log.tag_name}}

</td>





<td class="p-3">


<span

class="
px-3
py-1
rounded-full
bg-blue-100
text-blue-700
"

>

{{log.operation}}

</span>


</td>





<td class="p-3">

{{log.old_value ?? "-"}}

</td>





<td class="p-3">

{{log.new_value ?? "-"}}

</td>



</tr>






<tr

v-if="logs.length===0"

>

<td

colspan="7"

class="
text-center
p-5
text-gray-500
"

>

No logs found

</td>

</tr>



</tbody>


</table>


</div>


</template>