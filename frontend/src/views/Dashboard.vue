<script setup>
import { ref, onMounted } from "vue"

import {
    Users,
    Shield,
    Cpu,
    Activity,
} from "lucide-vue-next"

import { useAuthStore } from "../stores/auth"

import DashboardCard from "../components/dashboard/DashboardCard.vue"

import { dashboardApi } from "../api/dashboard"

const auth = useAuthStore()

const loading = ref(true)

const stats = ref({

    users: 0,

    roles: 0,

    plc: "Coming Soon",

    activeUsers: 0,

})

const loadDashboard = async () => {

    loading.value = true

    try {

        const [

            users,

            roles,

        ] = await Promise.all([

            dashboardApi.getUsersCount(),

            dashboardApi.getRolesCount(),

        ])

        stats.value.users = users

        stats.value.roles = roles

        stats.value.plc = "Coming Soon"

        // Temporary until activity tracking is implemented
        stats.value.activeUsers = users

    }

    catch (error) {

        console.error("Dashboard Error:", error)

    }

    finally {

        loading.value = false

    }

}

onMounted(() => {

    loadDashboard()

})
</script>

<template>

<div class="space-y-8">

    <!-- ========================= -->
    <!-- Welcome -->
    <!-- ========================= -->

    <section>

        <h1

            class="
            text-3xl
            font-bold

            text-slate-900
            dark:text-white
            "

        >

            Welcome,

            {{ auth.user?.username || "Administrator" }}

            

        </h1>

        <p

            class="
            mt-2

            text-slate-500
            dark:text-slate-400
            "

        >

            Monitor and manage your Taikisha Industrial Platform.

        </p>

    </section>

    <!-- ========================= -->
    <!-- Statistics -->
    <!-- ========================= -->

    <section

        class="
        grid

        gap-6

        sm:grid-cols-2
        xl:grid-cols-4
        "

    >

        <DashboardCard

            title="Total Users"

            :value="loading ? '...' : stats.users"

            subtitle="Registered Users"

            :icon="Users"

            color="blue"

        />

        <DashboardCard

            title="Roles"

            :value="loading ? '...' : stats.roles"

            subtitle="Available Roles"

            :icon="Shield"

            color="purple"

        />

        <DashboardCard

            title="PLC Status"

            :value="loading ? '...' : stats.plc"

            subtitle="Connection Status"

            :icon="Cpu"

            color="green"

        />

        <DashboardCard

            title="Active Users"

            :value="loading ? '...' : stats.activeUsers"

            subtitle="Current Session"

            :icon="Activity"

            color="orange"

        />

    </section>

    <!-- ========================= -->
    <!-- Coming Soon -->
    <!-- ========================= -->

    <section

        class="
        rounded-2xl

        border
        border-dashed
        border-slate-300

        bg-white

        p-10

        text-center

        dark:border-slate-700
        dark:bg-slate-900
        "

    >

        <h2

            class="
            text-xl
            font-semibold

            text-slate-900
            dark:text-white
            "

        >

            Dashboard Modules Coming Soon

        </h2>

        <p

            class="
            mt-3

            text-slate-500
            dark:text-slate-400
            "

        >

            Upcoming widgets will include Recent Activity, PLC Status,
            Quick Actions, System Health, Charts, and Analytics.

        </p>

    </section>

</div>

</template>