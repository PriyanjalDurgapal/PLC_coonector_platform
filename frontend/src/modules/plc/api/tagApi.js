import api from "../../../api/axios"

export const plcTagApi = {

    // ==========================
    // PLC TAGS
    // ==========================

    async getTags(params = {}) {

        const response = await api.get(
            "/plc/tags/",
            {
                params,
            }
        )

        return response.data
    },

    async getTag(id) {

        const response = await api.get(
            `/plc/tags/${id}/`
        )

        return response.data
    },

    async createTag(data) {

        const response = await api.post(
            "/plc/tags/",
            data
        )

        return response.data
    },

    async updateTag(id, data) {

        const response = await api.put(
            `/plc/tags/${id}/`,
            data
        )

        return response.data
    },

    async deleteTag(id) {

        const response = await api.delete(
            `/plc/tags/${id}/`
        )

        return response.data
    },



    // ==========================
    // READ SINGLE TAG
    // ==========================

    async readTag(id) {

        const response = await api.get(
            `/plc/tags/${id}/read/`
        )

        return response.data
    },



    // ==========================
    // WRITE TAG
    // ==========================

    async writeTag(id, value) {

        const response = await api.post(
            `/plc/tags/${id}/write/`,
            {
                value,
            }
        )

        return response.data
    },



    // ==========================
    // LIVE VALUES
    // ==========================

    async getLiveValues(plcId) {

        const response = await api.get(
            `/plc/${plcId}/tags/live/`
        )

        return response.data
    },



    // ==========================
    // OPERATION LOGS
    // ==========================

    async getLogs() {

        const response = await api.get(
            "/plc/logs/"
        )

        return response.data
    },
    

}

