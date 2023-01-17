import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import TabsPage from '../views/BottomTabs.vue';
import LoginPage from '../views/loginPage.vue';
import viewBooking from '../views/viewBooking.vue';
import buySubscription from '../views/buySubscription.vue';
import nearbymePage from '../views/nearbymePage.vue';

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
    path: '/nearbyme',
    component: nearbymePage
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
