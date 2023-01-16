import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import TabsPage from '../views/TabsPage.vue';
import LoginPage from '../views/LoginPage.vue';
import viewBooking from '../views/viewBooking.vue';
import HomePage from '../views/HomePage.vue';
import buySubscription from '../views/buySubscription.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: LoginPage
  },
  {
    path: '/tabs/',
    component: TabsPage,
    children: [
      {
        path: '',
        redirect: '/tabs/home'
      },
      {
        path: 'home',
        component: () => import('@/views/homePage.vue')
      },
      {
        path: 'wallet',
        component: () => import('@/views/walletPage.vue')
      },
      {
        path: 'plans',
        component: () => import('@/views/plansPage.vue')
      },
      {
        path: 'map',
        component: () => import('@/views/mapPage.vue')
      },
      {
        path: 'profile',
        component: () => import('@/views/profilePage.vue')
      },
    ]
  },
  {
    path: '/viewBooking',
    component: viewBooking
  },
  {
    path: '/login',
    component: LoginPage
  },
  {
    path: '/buySubscription',
    component: buySubscription
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
