<script setup>
import {
  AlertTriangle,
  RotateCcw,
  Database,
  User,
  Server,
  Lock,
} from "lucide-vue-next";

import { reactive } from "vue";


const props = defineProps({

  show:{
    type:Boolean,
    default:false
  },

  backup:{
    type:Object,
    default:null
  }

});


const emit = defineEmits([
  "close",
  "restore"
]);


const form = reactive({

  db_name:"",
  db_user:"",
  db_host:"localhost",
  db_password:""

});



function closeModal(){

  emit("close");

}



function restore(){

  emit(
    "restore",
    {
      backup_file: props.backup?.filename,

      db_name: form.db_name,

      db_user: form.db_user,

      db_host: form.db_host,

      db_password: form.db_password
    }
  );

}

</script>


<template>

<Transition
enter-active-class="transition duration-200 ease-out"
enter-from-class="opacity-0"
enter-to-class="opacity-100"
leave-active-class="transition duration-150 ease-in"
leave-from-class="opacity-100"
leave-to-class="opacity-0"
>


<div
v-if="show"
class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
>


<div
class="w-full max-w-lg rounded-xl bg-white shadow-xl"
>



<!-- Header -->

<div
class="flex items-center justify-between border-b border-slate-200 p-6"
>


<div class="flex items-center gap-3">


<div
class="flex h-12 w-12 items-center justify-center rounded-full bg-amber-100"
>

<AlertTriangle
class="h-6 w-6 text-amber-600"
/>

</div>


<div>

<h2 class="text-lg font-semibold text-slate-900">
Restore Backup
</h2>

<p class="text-sm text-slate-500">
Enter database details
</p>


</div>


</div>


</div>





<!-- Body -->

<div class="space-y-4 p-6">


<!-- Backup File -->

<div
class="rounded-lg border border-slate-200 bg-slate-50 p-4"
>

<p class="text-xs uppercase text-slate-500">
Backup File
</p>


<p class="mt-1 break-all text-sm font-medium text-slate-900">
{{ backup?.filename }}
</p>


</div>





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
class="flex flex-col-reverse gap-3 border-t border-slate-200 p-6 sm:flex-row sm:justify-end"
>


<button
@click="closeModal"
class="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100"
>

Cancel

</button>




<button
@click="restore"
class="inline-flex items-center justify-center gap-2 rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white hover:bg-indigo-700"
>


<RotateCcw class="h-4 w-4"/>


Restore Backup


</button>


</div>



</div>


</div>


</Transition>


</template>