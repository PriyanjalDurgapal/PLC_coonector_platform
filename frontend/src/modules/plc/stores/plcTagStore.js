import { defineStore } from "pinia"

import { plcTagApi } from "../api/tagApi"



export const usePLCTagStore = defineStore(
    "plcTag",
    {


        state:()=>({

            tags: [],


            liveValues:{},


            loading:false,


            saving:false,


            error:null,


            refreshTimer:null,


        }),






        getters:{


            // Get live PLC value using address

            getTagValue:(state)=>(tag)=>{


                return (
                    state.liveValues[tag.address]
                        ?.value
                    ??
                    null
                )


            },



        },








        actions:{



            // ==================================
            // LOAD ALL TAGS
            // ==================================


            async loadTags(params={}){


                this.loading = true


                try{


                    const response =
                        await plcTagApi.getTags(
                            params
                        )



                    this.tags =
                        response.data.results



                }

                catch(error){


                    this.error =
                        error.response?.data
                        ||
                        error.message



                }

                finally{


                    this.loading=false


                }


            },









            // ==================================
            // CREATE TAG
            // ==================================


            async createTag(data){


                this.saving=true



                try{


                    await plcTagApi.createTag(
                        data
                    )



                    await this.loadTags()



                }

                finally{


                    this.saving=false


                }


            },









            // ==================================
            // UPDATE TAG
            // ==================================


            async updateTag(id,data){


                this.saving=true



                try{


                    await plcTagApi.updateTag(

                        id,

                        data

                    )



                    await this.loadTags()



                }


                finally{


                    this.saving=false


                }


            },









            // ==================================
            // DELETE TAG
            // ==================================


            async deleteTag(id){


                await plcTagApi.deleteTag(
                    id
                )



                await this.loadTags()



            },









            // ==================================
            // READ SINGLE TAG FROM PLC
            // ==================================


            async readTag(id){


                return await plcTagApi.readTag(

                    id

                )


            },









            // ==================================
            // WRITE VALUE TO PLC
            // ==================================


            async writeTag(id,value){


                const response =
                    await plcTagApi.writeTag(

                        id,

                        value

                    )



                return response


            },


async loadLogs(){

    try{

        const response =
            await plcTagApi.getLogs()


        return response.data


    }
    catch(error){

        console.error(
            "Log loading error",
            error
        )


        return []

    }

},






            // ==================================
            // LOAD LIVE PLC VALUES
            // ==================================


            async loadLiveValues(plcId){


                try{


                    const response =
                        await plcTagApi.getLiveValues(

                            plcId

                        )





                    const values={}





                    response.data.forEach(item=>{


                        values[item.address]=item



                    })





                    this.liveValues =
                        values





                }

                catch(error){


                    console.error(

                        "Live value error",

                        error

                    )


                }


            },









            // ==================================
            // AUTO REFRESH
            // ==================================


            startAutoRefresh(plcId){



                this.stopAutoRefresh()





                this.refreshTimer = setInterval(()=>{


                    this.loadLiveValues(

                        plcId

                    )



                },1000)



            },
            









            // ==================================
            // STOP AUTO REFRESH
            // ==================================


            stopAutoRefresh(){



                if(this.refreshTimer){



                    clearInterval(

                        this.refreshTimer

                    )



                    this.refreshTimer=null



                }


            },





        }



    }

)