import api from "./axios";


const backupService = {


  // Get available backups
  async getBackups(){

    return api.get("/backups/");

  },


  // Create backup
  async createBackup(data){

    return api.post(
      "/backups/create/",
      data
    );

  },


  // Restore backup
  async restoreBackup(data){

    return api.post(
      "/backups/restore/",
      data
    );

  },


};


export default backupService;