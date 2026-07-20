<script setup>

import { onMounted } from "vue"

import { storeToRefs } from "pinia"

import { usePLCStore } from "../stores/plcStore"


const plcStore = usePLCStore()


const {
    plcs,
    loading,
    error,
    connected,
    status,
} = storeToRefs(plcStore)



onMounted(() => {

    plcStore.fetchPLCs()

})



function connect(id){

    plcStore.connectPLC(id)

}



function disconnect(id){

    plcStore.disconnectPLC(id)

}

</script>



<template>

<div class="p-6">


    <div class="mb-6">

        <h1 class="text-2xl font-semibold">
            PLC Management
        </h1>

        <p class="text-slate-500">
            Manage PLC connections and status
        </p>

    </div>



    <div
        v-if="loading"
        class="text-center py-10"
    >

        Loading PLCs...

    </div>



    <div
        v-if="error"
        class="mb-4 rounded-lg bg-red-100 p-4 text-red-700"
    >

        {{ error }}

    </div>




    <div
        class="grid gap-5 md:grid-cols-2 lg:grid-cols-3"
    >


        <div
            v-for="plc in plcs"
            :key="plc.id"
            class="
                rounded-xl
                border
                bg-white
                p-5
                shadow-sm
            "
        >


            <h2 class="text-lg font-semibold">

                {{ plc.name }}

            </h2>



            <div class="mt-3 space-y-2 text-sm">


                <p>

                    IP:
                    <span class="font-medium">
                        {{ plc.ip_address }}
                    </span>

                </p>


                <p>

                    Port:
                    <span class="font-medium">
                        {{ plc.port }}
                    </span>

                </p>



                <p>

                    Status:

                    <span
                        v-if="connected"
                        class="text-green-600"
                    >
                        Connected
                    </span>


                    <span
                        v-else
                        class="text-red-600"
                    >
                        Disconnected
                    </span>


                </p>


            </div>



            <div
                class="mt-5 flex gap-3"
            >


                <button

                    @click="connect(plc.id)"

                    class="
                        rounded-lg
                        bg-green-600
                        px-4
                        py-2
                        text-white
                    "

                >

                    Connect

                </button>




                <button

                    @click="disconnect(plc.id)"

                    class="
                        rounded-lg
                        bg-red-600
                        px-4
                        py-2
                        text-white
                    "

                >

                    Disconnect

                </button>


            </div>


        </div>


    </div>



</div>

</template>