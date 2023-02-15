import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import TabsPage from '../views/BottomTabs.vue';
import LoginPage from '../views/LoginPage.vue';
import viewBooking from '../views/viewBooking.vue';
import buySubscription from '../views/buySubscription.vue';
import nearbymePage from '../views/nearbymePage.vue';
import register from '../views/registerPage.vue';
import viewProfile from '../views/viewProfile.vue';
import BarChart from '../views/BarChart.vue';
import forgotPassword from '../views/forgotPasswordPage.vue';
import mapPage from '../views/mapPage.vue';

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
        component: () => import('@/views/HomePage.vue')
      },
      {
        path: 'wallet',
        component: () => import('@/views/walletPage.vue'),
        children: [
          {
            path: '/successPage',
            component: () => import('@/views/successPage.vue')
          }
        ] 
      },
      {
        path: 'plans',
        component: () => import('@/views/plansPage.vue')
      },
      {
        path: 'profile',
        component: () => import('@/views/profilePage.vue')
      },
      {
        path: 'bookings',
        component: () => import('@/views/bookingPage.vue')
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
  },
  {
    path: '/register',
    component: register
  },
  {
    path: '/viewProfile',
    component: viewProfile
  },
  {
    path: '/BarChart',
    component: BarChart
  },
  {
    path: '/forgotPassword',
    component: forgotPassword
  },
  {
    path: '/map',
    component: mapPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
