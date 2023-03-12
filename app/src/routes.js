
import Reports_page from './components/Reports_page.vue'
import Timelogs_page from './components/Timelogs_page.vue'
import Test_page from './components/Test_page.vue'
import Home from './components/Home.vue'
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        name:'Home',
        component:Home,
        path:'/'
    },
    {
        name:'Test_page',
        component:Test_page,
        path:'/test'
    },
    {
        name:'Timelogs_page',
        component:Timelogs_page,
        path:'/timelogs'
    },

    {

        name: 'Reports_page',
        component: Reports_page,
        path: '/reports'

    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router;