<script setup>
import { ref, onMounted } from "vue";
import { ChevronRight } from "lucide-vue-next";

import BackupCreateCard from "../components/backup/BackupCreateCard.vue";
import BackupCreateModal from "../components/backup/BackupCreateModal.vue";
import BackupTable from "../components/backup/BackupTable.vue";
import RestoreBackupModal from "../components/backup/RestoreBackupModal.vue";
import EmptyBackupState from "../components/backup/EmptyBackupState.vue";

import { useBackupStore } from "../stores/backupStore";


const backupStore = useBackupStore();


const showCreateModal = ref(false);

const showRestoreModal = ref(false);

const selectedBackup = ref(null);



onMounted(async () => {

  await backupStore.loadBackups();

});



// ---------------------------
// CREATE BACKUP
// ---------------------------

function handleCreateBackup(){

  showCreateModal.value = true;

}



function closeCreateModal(){

  showCreateModal.value = false;

}



async function handleCreateSubmit(data){

  try {

    showCreateModal.value = false;


    await backupStore.createBackup(data);


  }
  catch(error){

    console.error(
      "Backup creation failed:",
      error
    );

  }

}





// ---------------------------
// RESTORE BACKUP
// ---------------------------


function handleRestoreClick(backup){

  selectedBackup.value = backup;

  showRestoreModal.value = true;

}



async function handleRestore(data){

  try {


    await backupStore.restoreBackup(data);



    showRestoreModal.value = false;


    selectedBackup.value = null;


  }
  catch(error){


    console.error(
      "Restore failed:",
      error
    );


  }

}




function closeRestoreModal(){

  showRestoreModal.value = false;

  selectedBackup.value = null;

}

</script>




<template>

<main class="min-h-screen bg-slate-50">


<div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">



<!-- Breadcrumb -->

<nav class="mb-4 flex items-center gap-2 text-sm text-slate-500">


<span>
Settings
</span>


<ChevronRight class="h-4 w-4"/>


<span class="font-medium text-slate-900">
Database Backup
</span>


</nav>






<!-- Header -->


<header class="mb-8">


<h1 class="text-3xl font-bold tracking-tight text-slate-900">
Database Backup
</h1>


<p class="mt-2 text-slate-600">
Create and restore PostgreSQL database backups.
</p>


</header>







<!-- Create Backup Card -->


<BackupCreateCard
@create="handleCreateBackup"
/>







<!-- Backup Table -->


<div class="mt-8">



<BackupTable

v-if="
!backupStore.loading &&
backupStore.backups.length
"

:backups="backupStore.backups"

@restore="handleRestoreClick"

/>





<EmptyBackupState

v-else-if="
!backupStore.loading
"

/>





<div

v-else

class="rounded-xl border border-slate-200 bg-white py-20 text-center"

>


<p class="text-slate-500">
Loading backups...
</p>


</div>




</div>








<!-- CREATE MODAL -->


<BackupCreateModal

:show="showCreateModal"

@close="closeCreateModal"

@submit="handleCreateSubmit"

/>








<!-- RESTORE MODAL -->


<RestoreBackupModal

:show="showRestoreModal"

:backup="selectedBackup"

@close="closeRestoreModal"

@restore="handleRestore"

/>




</div>


</main>


</template>