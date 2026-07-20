import api from "./axios"



export const rolesApi = {



    // =========================
    // Get Roles
    // =========================

    async getRoles(){

        const response =
            await api.get(
                "/rbac/roles/"
            )


        return response.data.data

    },





    // =========================
    // Create Role
    // =========================

    async createRole(data){


        const response =
            await api.post(
                "/rbac/roles/",
                data
            )


        return response.data.data

    },






    // =========================
    // Get Permissions
    // =========================

    async getPermissions(){


        const response =
            await api.get(
                "/rbac/permissions/"
            )


        return response.data.data

    },






    // =========================
    // Get Role Permissions
    // =========================

    async getRolePermissions(roleId){


        const response =
            await api.get(
                `/rbac/roles/${roleId}/permissions/`
            )


        return response.data.data

    },







    // =========================
    // Assign Permissions
    // =========================

    async assignPermissions(
        roleId,
        permissions
    ){


        const response =
            await api.post(

                `/rbac/roles/${roleId}/permissions/`,

                {
                    permissions
                }

            )


        return response.data

    }


}