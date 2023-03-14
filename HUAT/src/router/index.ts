import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import TabsPage from "../views/BottomTabs.vue";
import LoginPage from "../views/LoginPage.vue";
import viewBooking from "../views/viewBooking.vue";
import buySubscription from "../views/buySubscription.vue";
import nearbymePage from "../views/nearbymePage.vue";
import register from "../views/registerPage.vue";
import viewProfile from "../views/viewProfile.vue";
import BarChart from "../views/BarChart.vue";
import forgotPassword from "../views/forgotPasswordPage.vue";
import mapPage from "../views/mapPage.vue";
import selectpaymentPage from "../views/selectpaymentPage.vue";
import NETSAmountPage from "../views/NETSAmountPage.vue";
import StripeAmountPage from "../views/StripeAmountPage.vue";
import successPage from "../views/successPage.vue";
import AdminPage from "../views/AdminPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: LoginPage,
  },
  {
    path: "/admin",
    component: AdminPage,
  },
  {
    path: "/tabs/",
    component: TabsPage,
    children: [
      {
        path: "",
        redirect: "/tabs/home",
      },
      {
        path: "home",
        component: () => import("@/views/HomePage.vue"),
      },
      {
        path: "wallet",
        component: () => import("@/views/walletPage.vue"),
      },
      {
        path: "plans",
        component: () => import("@/views/plansPage.vue"),
      },
      {
        path: "profile",
        component: () => import("@/views/profilePage.vue"),
      },
      {
        path: "bookings",
        component: () => import("@/views/bookingPage.vue"),
      },
    ],
  },
  {
    path: "/viewBooking",
    component: viewBooking,
  },
  {
    path: "/nearbyme",
    component: nearbymePage,
  },
  {
    path: "/buySubscription",
    component: buySubscription,
  },
  {
    path: "/register",
    component: register,
  },
  {
    path: "/viewProfile",
    component: viewProfile,
  },
  {
    path: "/BarChart",
    component: BarChart,
  },
  {
    path: "/forgotPassword",
    component: forgotPassword,
  },
  {
    path: "/map",
    component: mapPage,
  },
  {
    path: "/payment",
    component: selectpaymentPage,
  },
  {
    path: "/Nets",
    component: NETSAmountPage,
  },
  {
    path: "/Stripe",
    component: StripeAmountPage,
  },
  {
    path: "/success",
    component: successPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// router.beforeEach((to, from, next) => {
//   const authUser = JSON.parse(localStorage.getItem("userData")!);
//   console.log(authUser.role);
//   if (to.meta.requiresAuth) {
//     if (to.meta.adminAuth) {
//       if (authUser.role === "Admin"){
//         next("/admin");
//       }else{
//         next("/tabs/home");
//       }
//     } 
//     else if (to.meta.userAuth) {
//       if (authUser.role === "User"){
//         next("/tabs/home");
//       }else{
//         next("/admin");
//       }
//     }
//   } 
//   else {
//     next();
//   }
// });

export default router;
