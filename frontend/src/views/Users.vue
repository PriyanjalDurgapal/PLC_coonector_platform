<script setup>

import {
    onMounted,
    ref
} from "vue"


import { Plus } from "lucide-vue-next"


import { usersApi } from "../api/users"


import UserToolbar from "../components/users/UserToolbar.vue"

import UserTable from "../components/users/UserTable.vue"

import UserPagination from "../components/users/UserPagination.vue"

import UserFormModal from "../components/users/UserFormModal.vue"

import EditUserModal from "../components/users/EditUserModal.vue"

import UserDetailsDrawer from "../components/users/UserDetailsDrawer.vue"

import DeleteUserModal from "../components/users/DeleteUserModal.vue"





const loading = ref(false)





// =========================
// Create Modal
// =========================

const showUserModal = ref(false)





// =========================
// Edit Modal
// =========================

const showEditModal = ref(false)

const selectedUser = ref(null)







// =========================
// Details Drawer
// =========================

const showDetailsDrawer = ref(false)

const detailsUser = ref(null)







// =========================
// Delete Modal
// =========================

const showDeleteModal = ref(false)

const deleteUserTarget = ref(null)








const users = ref([])



const pagination = ref({

    count:0,

    next:null,

    previous:null,

})





const filters = ref({

    page:1,

    search:"",

    role:"",

    is_active:"",

})









// =========================
// Load Users
// =========================

const loadUsers = async()=>{


    loading.value=true



    try{


        const response =
            await usersApi.getUsers(
                filters.value
            )



        users.value =
            response.results?.data || []




        pagination.value = {


            count:
                response.count || 0,


            next:
                response.next,


            previous:
                response.previous,


        }



    }


    catch(error){


        console.error(

            "Users loading error:",

            error

        )


    }


    finally{


        loading.value=false


    }


}









// =========================
// Filters
// =========================

const updateFilters = (newFilters)=>{


    filters.value = {


        ...filters.value,


        ...newFilters,


        page:1


    }



    loadUsers()


}









// =========================
// Pagination
// =========================

const changePage = (page)=>{


    filters.value.page = page


    loadUsers()


}









// =========================
// Create User
// =========================

const userCreated = ()=>{


    showUserModal.value=false


    loadUsers()


}









// =========================
// Edit User
// =========================

const editUser = (user)=>{


    selectedUser.value = user


    showEditModal.value = true


}






const closeEditModal = ()=>{


    showEditModal.value=false


    selectedUser.value=null


}






const userUpdated = ()=>{


    closeEditModal()


    loadUsers()


}









// =========================
// View User
// =========================

const viewUser = (user)=>{


    detailsUser.value = user


    showDetailsDrawer.value = true


}






const closeDetailsDrawer = ()=>{


    showDetailsDrawer.value=false


    detailsUser.value=null


}









// =========================
// Delete User
// =========================

const deleteUser = (user)=>{


    deleteUserTarget.value = user


    showDeleteModal.value = true


}






const closeDeleteModal = ()=>{


    showDeleteModal.value = false


    deleteUserTarget.value = null


}






const confirmDelete = async()=>{


    try{


        await usersApi.deleteUser(

            deleteUserTarget.value.id

        )


        closeDeleteModal()


        loadUsers()



    }


    catch(error){


        console.error(

            "Delete User Error:",

            error

        )


    }


}









onMounted(()=>{


    loadUsers()


})



</script>





<template>


<div class="space-y-6">





<!-- Header -->

<div

class="
flex

flex-col

gap-4

md:flex-row

md:items-center

md:justify-between
"

>


<div>


<h1

class="
text-3xl

font-bold

text-slate-900

dark:text-white
"

>

Users

</h1>



<p

class="
mt-1

text-slate-500

dark:text-slate-400
"

>

Manage platform users.

</p>


</div>






<button

@click="showUserModal=true"

class="
inline-flex

items-center

gap-2

rounded-xl

bg-blue-600

px-5

py-3

font-medium

text-white

transition

hover:bg-blue-700
"

>


<Plus :size="18"/>


Add User


</button>


</div>









<UserToolbar

@filter-change="updateFilters"

/>









<UserTable

:users="users"

:loading="loading"

@view="viewUser"

@edit="editUser"

@delete="deleteUser"

/>









<UserPagination

:pagination="pagination"

:current-page="filters.page"

@change-page="changePage"

/>









<UserFormModal

v-if="showUserModal"

@close="showUserModal=false"

@created="userCreated"

/>









<EditUserModal

v-if="showEditModal"

:user="selectedUser"

@close="closeEditModal"

@updated="userUpdated"

/>









<UserDetailsDrawer

v-if="showDetailsDrawer"

:user="detailsUser"

@close="closeDetailsDrawer"

/>









<DeleteUserModal

v-if="showDeleteModal"

:user="deleteUserTarget"

@close="closeDeleteModal"

@confirm="confirmDelete"

/>







</div>


</template>