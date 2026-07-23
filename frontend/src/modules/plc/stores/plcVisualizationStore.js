import { defineStore } from "pinia"

import visualizationService 
from "../services/plcVisualizationService"
import { plcTagApi } from "../api/tagApi"

export const useVisualizationStore = defineStore(

"visualization",

{

state:()=>({

    objects:[],

    loading:false,

    error:null,

}),





actions:{


    // ==================================
// READ SVG TAG
// ==================================

async readSVGTag(tagId){


    const response =
        await plcTagApi.readTag(
            tagId
        )


    return response


},




// ==================================
// WRITE SVG TAG
// ==================================

async writeSVGTag(tagId,value){


    const response =
        await plcTagApi.writeTag(

            tagId,

            value

        )


    return response


},


// ==================================
// LOAD VISUALIZATION OBJECTS
// ==================================

async loadObjects(){


    this.loading = true


    try{


        const response =
            await visualizationService.getObjects()



        console.log(
            "Visualization API:",
            response
        )



        this.objects =
            response.data.results.map(object => ({


                ...object,


                // if label empty use tag name

                label:
                    object.label ||
                    object.tag_name,



                // default colors

                on_color:
                    object.on_color ||
                    "#22C55E",



                off_color:
                    object.off_color ||
                    "#6B7280",



                // default unit

                unit:
                    object.unit ||
                    "RPM",



                // convert value

                value:
                    Number(object.value) ||
                    0



            }))



        console.log(
            "Canvas Objects:",
            this.objects
        )


    }



    catch(error){


        console.error(
            "Visualization Load Error",
            error
        )


        this.error =
            error.message


    }



    finally{


        this.loading=false


    }


},







// ==================================
// CREATE OBJECT
// ==================================

async createObject(data){


    const newObject =
        await visualizationService.createObject(
            data
        )


    console.log(
        "NEW SVG OBJECT:",
        newObject
    )



    this.objects.push({

        ...newObject,


        label:
        newObject.label ||
        newObject.tag_name,



        value:
        Number(newObject.value) || 0,



        unit:
        newObject.unit ||
        "RPM",



        on_color:
        newObject.on_color ||
        "#22C55E",



        off_color:
        newObject.off_color ||
        "#6B7280"


    })



    return newObject

},





// ==================================
// UPDATE POSITION
// ==================================

async saveObject(object){



    await visualizationService.updateObject(

        object.id,

        {

            x:object.x,

            y:object.y,

            rotation:object.rotation,

            scale:object.scale,

        }

    )


},







// ==================================
// DELETE OBJECT
// ==================================

async deleteObject(id){



    await visualizationService.deleteObject(

        id

    )



    this.objects =
        this.objects.filter(

            object =>
            object.id !== id

        )


},



}



})