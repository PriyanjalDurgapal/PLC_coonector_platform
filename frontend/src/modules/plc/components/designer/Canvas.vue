<script setup>

import {
    ref,
    onMounted,
    onUnmounted,
} from "vue"


import {
    storeToRefs,
} from "pinia"


import {
    useVisualizationStore
} from "../../stores/plcVisualizationStore"



import {
    usePLCTagStore
} from "../../stores/plcTagStore"



import Toolbar from "../Toolbar.vue"

import TagSelectionModal from "../TagSelectionModal.vue"

import PropertyPanel from "../PropertyPanel.vue"



import Motor from "./Motor.vue"
import Pump from "./Pump.vue"
import Tank from "./Tank.vue"
import Button from "./Button.vue"





// ============================
// STORES
// ============================


const visualizationStore =
    useVisualizationStore()



const plcTagStore =
    usePLCTagStore()



const {
    objects
} = storeToRefs(
    visualizationStore
)







// ============================
// COMPONENT MAP
// ============================


const componentMap = {

    motor: Motor,

    pump: Pump,

    tank: Tank,

    button: Button,

}







// ============================
// STATES
// ============================


const selectedObject = ref(null)


const currentTool = ref(null)


const showTagModal = ref(false)


const selectedTag = ref(null)


const plcTags = ref([])








// ============================
// DRAG
// ============================


const dragging = ref(null)


const offset = ref({

    x:0,

    y:0

})








// ============================
// GET TAG ID
// ============================

function getTagId(object){


    if(
        typeof object.tag === "object"
        &&
        object.tag !== null
    ){

        return object.tag.id

    }


    return object.tag


}









// ============================
// TOOL CLICK
// ============================


function selectTool(tool){


    console.log(
        "TOOL:",
        tool
    )


    currentTool.value = tool


    loadTags()


    showTagModal.value=true


}








// ============================
// LOAD TAGS
// ============================


async function loadTags(){


    try{


        await plcTagStore.loadTags()



        plcTags.value =
            plcTagStore.tags



        console.log(
            "TAGS:",
            plcTags.value
        )


    }

    catch(error){


        console.error(
            "TAG ERROR",
            error
        )


    }


}








// ============================
// TAG SELECT
// ============================


async function tagSelected(tag){


    console.log(
        "SELECTED TAG",
        tag
    )



    const object = {


        tag: tag.id,


        svg_type: currentTool.value,


        label: tag.name,


        address: tag.address,


        value: tag.value ?? 0,


        unit:
        currentTool.value === "motor"
        ?
        "RPM"
        :
        "",


        on_color: object.on_color,

off_color: object.off_color,

low_color: object.low_color,

medium_color: object.medium_color,

high_color: object.high_color,



        x:200,


        y:200,


        rotation:0,


        scale:1,


        visible:true


    }



    try{


        const response =
            await visualizationStore.createObject(
                object
            )



        console.log(
            "CREATED:",
            response
        )



        showTagModal.value=false

        currentTool.value=null

        selectedTag.value=null



    }


   catch(error){

    console.error(
        "CREATE SVG ERROR",
        error
    )

    const message =
        error.response?.data?.tag?.[0]
        ||
        error.response?.data?.detail
        ||
        "Failed to create visualization object."

    alert(message)

}


}







// ============================
// READ SVG VALUE
// ============================


async function readSVGValue(object){


    try{


        console.log(
            "READ OBJECT:",
            object
        )



        const tagId =
            getTagId(object)



        const response =
            await plcTagStore.readTag(
                tagId
            )



        console.log(
            "READ RESPONSE:",
            response
        )



        if(response.value !== undefined){


            object.value =
                response.value


        }



    }


    catch(error){


        console.error(
            "READ ERROR",
            error
        )


    }


}









// ============================
// WRITE SVG VALUE
// ============================


// ============================
// WRITE SVG VALUE
// ============================

async function writeSVGValue(object){

    console.log("WRITE OBJECT:", object)

    if(!object || !object.tag){

        console.error("INVALID OBJECT")

        return

    }

    let value

    // ==========================
    // BOOL BUTTON
    // ==========================
    if(object.data_type === "BOOL"){

        // Button.vue already toggled the value
        value = Number(object.value)

    }

    // ==========================
    // OTHER DATA TYPES
    // ==========================
    else{

        const input = window.prompt(
            "Enter PLC Value",
            String(object.value)
        )

        if(input === null){
            return
        }

        value = input.trim()

        if(value.toLowerCase() === "true"){
            value = true
        }
        else if(value.toLowerCase() === "false"){
            value = false
        }
        else if(!isNaN(value)){
            value = Number(value)
        }

        // Update UI immediately
        object.value = value

    }

    try{

        const response = await plcTagStore.writeTag(
            object.tag,
            value
        )

        console.log("WRITE RESPONSE:", response)

        if(!response.success){

            // Rollback if write failed
            if(object.data_type === "BOOL"){
                object.value =
                    object.value === 1 ? 0 : 1
            }

        }

    }
    catch(error){

        console.error(error)

        // Rollback on error
        if(object.data_type === "BOOL"){
            object.value =
                object.value === 1 ? 0 : 1
        }

    }

}



// ============================
// SELECT OBJECT
// ============================


function selectObject(object){


    selectedObject.value =
        object


}








// ============================
// DRAG
// ============================


function startDrag(event,object){


    dragging.value =
        object



    offset.value.x =
        event.clientX - object.x



    offset.value.y =
        event.clientY - object.y


}






function drag(event){


    if(!dragging.value){

        return

    }



    dragging.value.x =

        event.clientX -
        offset.value.x



    dragging.value.y =

        event.clientY -
        offset.value.y



}






function stopDrag(){


    dragging.value=null


}








// ============================
// SAVE
// ============================


async function saveLayout(){


    for(
        const object of objects.value
    ){


        await visualizationStore.saveObject(
            object
        )


    }



    alert(
        "Layout Saved"
    )


}








// ============================
// DELETE
// ============================


async function deleteObject(object){


    await visualizationStore.deleteObject(

        object.id

    )


    selectedObject.value=null


}








// ============================
// MOUNT
// ============================


onMounted(async()=>{


    await visualizationStore.loadObjects()



    objects.value =
        objects.value.map(object=>{


            return {


                ...object,


                label:
                object.label ||
                object.tag_name,



                value:
                Number(object.value) || 0,



                unit:
                object.unit ||
                "",



                on_color:
                object.on_color ||
                "#22C55E",



                off_color:
                object.off_color ||
                "#6B7280",



                x:
                object.x===0
                ?150
                :object.x,



                y:
                object.y===0
                ?150
                :object.y



            }


        })





    window.addEventListener(
        "mousemove",
        drag
    )


    window.addEventListener(
        "mouseup",
        stopDrag
    )


})








onUnmounted(()=>{


    window.removeEventListener(
        "mousemove",
        drag
    )


    window.removeEventListener(
        "mouseup",
        stopDrag
    )


})


</script>





<template>

<div

class="
relative
w-full
h-screen
overflow-hidden
bg-slate-100
"

>


<div

class="
absolute
top-0
left-0
z-50
bg-white
shadow
"

>

<Toolbar

@select-tool="selectTool"

/>

</div>





<button

@click="saveLayout"

class="
absolute
top-5
right-5
z-50
bg-green-600
text-white
px-5
py-2
rounded-lg
"

>

Save Layout

</button>





<div

class="
absolute
inset-0
z-10
"

>



<div

class="
absolute
inset-0
pointer-events-none
"

style="
background-image:
linear-gradient(#d1d5db 1px,transparent 1px),
linear-gradient(90deg,#d1d5db 1px,transparent 1px);

background-size:25px 25px;
"

></div>





<component

v-for="object in objects"

:key="object.id"

:is="componentMap[object.svg_type]"

:object="object"

@click.stop="selectObject(object)"

@mousedown.stop="startDrag($event,object)"

@read="readSVGValue"

@write="writeSVGValue"

/>



</div>






<div

v-if="selectedObject"

class="
absolute
bottom-5
left-5
z-[9999]
pointer-events-auto
"

@click.stop

@mousedown.stop

>


<PropertyPanel

:object="selectedObject"

@save="saveLayout"

@delete="deleteObject"

/>



</div>







<TagSelectionModal

v-if="showTagModal"

:tags="plcTags"

@select="tagSelected"

@close="showTagModal=false"

/>





</div>

</template>