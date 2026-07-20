import {
    createRouter,
    createWebHistory
} from "vue-router"


import Login from "../views/Login.vue"

import AdminLayout from "../layouts/AppLayout.vue"

import Dashboard from "../views/Dashboard.vue"
import PLCLogsView from "../modules/plc/views/PLCLogsView.vue"

import Users from "../views/Users.vue"
import Roles from "../views/Roles.vue"
import PLCTagView from "../modules/plc/views/PLCTagView.vue"
import PLCListView from "../modules/plc/views/PLCListView.vue"
import PLCVisualizationView from "../modules/plc/views/PLCVisualizationView.vue"


import DatabaseBackupView from "../views/DatabaseBackupView.vue"
const routes = [


    {
        path: "/login",

        name: "Login",

        component: Login,

        meta:{
            guest:true
        }

    },
    


    {
        path:"/",

        component: AdminLayout,

        meta:{
            requiresAuth:true
        },

        children:[


            {
                path:"dashboard",

                name:"Dashboard",

                component:Dashboard

            },


            {
                path:"users",

                name:"Users",

                component:Users

            },
            {
    path: "/roles",
    name: "roles",
    component: Roles,
    meta:{
        requiresAuth:true
    }
},
{
    path: "/plc",
    name: "plc",
    component: PLCListView,
},
{
    path:"/plc/tags",
    name:"plc-tags",
    component:PLCTagView
},{

 path:"/plc/visualization",
 component:PLCVisualizationView
},
{
    path:"/plc/logs",
    component:PLCLogsView
},
{
    path:"/backup",
    component:DatabaseBackupView
},



        ]

    },


]


const router = createRouter({

    history:createWebHistory(),

    routes

})



router.beforeEach((to)=>{


    const token =
        localStorage.getItem("access")


    if(

        to.meta.requiresAuth
        &&
        !token

    ){

        return "/login"

    }


    if(

        to.meta.guest
        &&
        token

    ){

        return "/dashboard"

    }


    return true

})



export default router