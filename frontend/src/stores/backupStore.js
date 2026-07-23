import { defineStore } from "pinia";
import { ref } from "vue";

import backupService from "../api/backupService";

export const useBackupStore = defineStore(
  "backup",
  () => {


    const backups = ref([]);

    const loading = ref(false);

    const creating = ref(false);

    const restoring = ref(false);

    const error = ref(null);



    // Load backups
    async function loadBackups(){

      loading.value = true;

      error.value = null;


      try{

        const response =
          await backupService.getBackups();


        backups.value =
          response.data.data || response.data;


      }
      catch(err){

        error.value =
          err.response?.data?.message ||
          err.message;

      }
      finally{

        loading.value = false;

      }

    }





    // Create backup
    async function createBackup(data){

      creating.value = true;

      error.value = null;


      try{


        const response =
          await backupService.createBackup(data);



        // reload list after creating

        await loadBackups();


        return response.data;


      }
      catch(err){

        error.value =
          err.response?.data?.message ||
          err.message;


        throw err;

      }
      finally{

        creating.value = false;

      }


    }




    // Delete backup
    async function deleteBackup(filename){

      error.value = null;

      try{

        const response =
          await backupService.deleteBackup(filename);

        await loadBackups();

        return response.data;

      }
      catch(err){

        error.value =
          err.response?.data?.message ||
          err.message;

        throw new Error(error.value);

      }

    }





    // Restore backup
    async function restoreBackup(data){


      restoring.value = true;

      error.value = null;


      try{


        const response =
          await backupService.restoreBackup(data);



        await loadBackups();


        return response.data;


      }
      catch(err){


        error.value =
          err.response?.data?.message ||
          "Database restore failed.";


        throw new Error(error.value);


      }
      finally{

        restoring.value = false;

      }


    }




    return {


      backups,

      loading,

      creating,

      restoring,

      error,


      loadBackups,

      createBackup,

      restoreBackup,

      deleteBackup,


    };


  }
);