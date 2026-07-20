import api from "./axios"

export const usersApi = {

    // =========================
    // List Users
    // =========================

    async getUsers(params = {}) {

        const response = await api.get(
            "/users/",
            {
                params,
            }
        )

        return response.data

    },

    // =========================
    // User Details
    // =========================

    async getUser(id) {

        const response = await api.get(
            `/users/${id}/`
        )

        return response.data

    },

    // =========================
    // Create User
    // =========================

    async createUser(data) {

        const response = await api.post(
            "/users/",
            data
        )

        return response.data

    },

    // =========================
    // Update User
    // =========================

    async updateUser(id, data) {

        const response = await api.put(
            `/users/${id}/`,
            data
        )

        return response.data

    },

    // =========================
    // Delete User
    // =========================

    async deleteUser(id) {

        const response = await api.delete(
            `/users/${id}/`
        )

        return response.data

    },

}