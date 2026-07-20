<script setup>
import {
  X,
  Database,
  Server,
  User,
  Lock,
} from "lucide-vue-next";


const props = defineProps({

  show:{
    type:Boolean,
    default:false
  }

});


const emit = defineEmits([
  "close",
  "submit"
]);


const form = {
  db_name:"",
  db_user:"",
  db_host:"localhost",
  db_password:""
};


function submitBackup(){

  emit(
    "submit",
    {
      ...form
    }
  );

}


function closeModal(){

  emit("close");

}

</script>


<template>

<Transition name="fade">

<div
v-if="show"
class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
>


<div
class="w-full max-w-lg rounded-xl bg-white shadow-xl"
>


<!-- Header -->

<div
class="flex items-center justify-between border-b border-slate-200 px-6 py-4"
>


<div class="flex items-center gap-3">

<div
class="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-50"
>

<Database
class="h-5 w-5 text-indigo-600"
/>

</div>


<div>

<h2
class="text-lg font-semibold text-slate-900"
>
Create Backup
</h2>

<p
class="text-sm text-slate-500"
>
Enter database details
</p>


</div>

</div>



<button
@click="closeModal"
class="rounded-lg p-2 hover:bg-slate-100"
>

<X
class="h-5 w-5 text-slate-500"
/>

</button>


</div>



<!-- Form -->

<div class="space-y-4 p-6">


<!-- Database Name -->

<div>

<label class="mb-1 block text-sm font-medium text-slate-700">
Database Name
</label>


<div class="relative">

<Database
class="absolute left-3 top-3 h-4 w-4 text-slate-400"
/>


<input
v-model="form.db_name"
type="text"
placeholder="Database name"
class="w-full rounded-lg border border-slate-300 py-2 pl-10 pr-3 text-sm outline-none focus:border-indigo-500"
/>


</div>

</div>



<!-- User -->

<div>

<label class="mb-1 block text-sm font-medium text-slate-700">
Database User
</label>


<div class="relative">

<User
class="absolute left-3 top-3 h-4 w-4 text-slate-400"
/>


<input
v-model="form.db_user"
type="text"
placeholder="Database user"
class="w-full rounded-lg border border-slate-300 py-2 pl-10 pr-3 text-sm outline-none focus:border-indigo-500"
/>


</div>

</div>




<!-- Host -->

<div>

<label class="mb-1 block text-sm font-medium text-slate-700">
Database Host
</label>


<div class="relative">

<Server
class="absolute left-3 top-3 h-4 w-4 text-slate-400"
/>


<input
v-model="form.db_host"
type="text"
placeholder="localhost"
class="w-full rounded-lg border border-slate-300 py-2 pl-10 pr-3 text-sm outline-none focus:border-indigo-500"
/>


</div>

</div>




<!-- Password -->

<div>

<label class="mb-1 block text-sm font-medium text-slate-700">
Database Password
</label>


<div class="relative">

<Lock
class="absolute left-3 top-3 h-4 w-4 text-slate-400"
/>


<input
v-model="form.db_password"
type="password"
placeholder="Password"
class="w-full rounded-lg border border-slate-300 py-2 pl-10 pr-3 text-sm outline-none focus:border-indigo-500"
/>


</div>

</div>



</div>




<!-- Footer -->

<div
class="flex justify-end gap-3 border-t border-slate-200 px-6 py-4"
>


<button
@click="closeModal"
class="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100"
>

Cancel

</button>



<button
@click="submitBackup"
class="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white hover:bg-indigo-700"
>

Create Backup

</button>


</div>



</div>


</div>

</Transition>


</template>