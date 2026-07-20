import { defineStore } from "pinia"

import { plcApi } from "../api/plcApi"



export const usePLCStore = defineStore(
    "plc",
    {


        state: () => ({

            plcs: [],

            selectedPLC: null,

            connected: false,

            loading: false,

            error: null,

            status: null,

        }),



        actions: {


            // =========================
            // GET PLC LIST
            // =========================

            async fetchPLCs(){

                try {

                    this.loading = true
                    this.error = null


                    this.plcs =
                        await plcApi.getPLCs()


                }
                catch(error){

                    this.error =
                        error.response?.data?.message
                        ||
                        "Failed to load PLCs"

                }
                finally{

                    this.loading = false

                }

            },



            // =========================
            // CONNECT PLC
            // =========================

            async connectPLC(id){

                try{

                    this.loading = true


                    const response =
                        await plcApi.connectPLC(id)


                    this.connected =
                        response.success


                    await this.getStatus(id)


                }
                catch(error){

                    this.error =
                        error.response?.data?.message
                        ||
                        "PLC connection failed"

                }
                finally{

                    this.loading = false

                }

            },



            // =========================
            // DISCONNECT PLC
            // =========================

            async disconnectPLC(id){

                try{

                    const response =
                        await plcApi.disconnectPLC(id)


                    this.connected =
                        false


                    this.status =
                        response


                }
                catch(error){

                    this.error =
                        error.response?.data?.message
                        ||
                        "Disconnect failed"

                }

            },



            // =========================
            // STATUS
            // =========================

            async getStatus(id){

                try{

                    const response =
                        await plcApi.getStatus(id)


                    this.status =
                        response


                    this.connected =
                        response.connected


                }
                catch(error){

                    this.error =
                        "Status failed"

                }

            }


        }

    }
)