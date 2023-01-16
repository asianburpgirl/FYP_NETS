import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import TabsPage from '../views/TabsPage.vue';
import LoginPage from '../views/LoginPage.vue';
import viewBooking from '../views/viewBooking.vue';
import HomePage from '../views/HomePage.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: LoginPage
  },
  // {
  //   path: '/tabs/',
  //   component: TabsPage,
  //   children: [
  //     {
  //       path: '',
  //       redirect: '/tabs/tab1'
  //     },
  //     {
  //       path: 'tab1',
  //       component: () => import('@/views/Tab1Page.vue')
  //     },
  //     {
  //       path: 'tab2',
  //       component: () => import('@/views/Tab2Page.vue')
  //     },
  //     {
  //       path: 'tab3',
  //       component: () => import('@/views/Tab3Page.vue')
  //     },
  //     {
  //       path: 'tab4',
  //       component: () => import('@/views/Tab4Page.vue')
  //     },
  //     {
  //       path: 'tab5',
  //       component: () => import('@/views/Tab5Page.vue')
  //     },
  //   ]
  // },
  {
    path: '/viewBooking',
    component: viewBooking
  },
  {
    path: '/login',
    component: LoginPage
  },
  {
    path: '/home',
    component: HomePage
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
