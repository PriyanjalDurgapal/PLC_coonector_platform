import api from "./axios"

export const dashboardApi = {

    async getUsersCount() {

        const response = await api.get(
            "/users/?page_size=1"
        )

        return response.data.count

    },

    async getRolesCount() {

        const response = await api.get(
            "/rbac/roles/"
        )

        return response.data.data.length

    },

}