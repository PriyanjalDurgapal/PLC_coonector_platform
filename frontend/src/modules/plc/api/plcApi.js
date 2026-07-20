import api from "../../../api/axios"

export const plcApi = {


    // =========================
    // PLC LIST
    // =========================

    async getPLCs(){

        const response = await api.get(
            "/plc/"
        )

        return response.data.data

    },



    // =========================
    // CONNECT PLC
    // =========================

    async connectPLC(id){

        const response = await api.post(
            `/plc/${id}/connect/`
        )

        return response.data

    },



    // =========================
    // DISCONNECT PLC
    // =========================

    async disconnectPLC(id){

        const response = await api.post(
            `/plc/${id}/disconnect/`
        )

        return response.data

    },



    // =========================
    // STATUS
    // =========================

    async getStatus(id){

        const response = await api.get(
            `/plc/${id}/status/`
        )

        return response.data

    }

}