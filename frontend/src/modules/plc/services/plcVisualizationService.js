import api from "../../../api/axios"


export default {


    // ==================================
    // GET ALL VISUALIZATION OBJECTS
    // ==================================

    async getObjects(){

        const response = await api.get(
            "/plc/visualizations/"
        )


        return response.data

    },




    // ==================================
    // CREATE OBJECT
    // ==================================

    async createObject(data){


        const response =
            await api.post(

                "/plc/visualizations/",

                data

            )


        return response.data

    },





    // ==================================
    // UPDATE POSITION
    // ==================================

    async updateObject(id,data){


        const response =
            await api.patch(

                `/plc/visualizations/${id}/`,

                data

            )


        return response.data

    },





    // ==================================
    // DELETE OBJECT
    // ==================================

    async deleteObject(id){


        const response =
            await api.delete(

                `/plc/visualizations/${id}/`

            )


        return response.data

    }



}