<template>
  <base-layout :pageTitle="`Welcome, ${userData.name}!`" needToolBar="y">
  <p>email: {{ userData.email }}</p>
  <p>phoneNum: {{ userData.phoneNum }}</p>
  <p>userID: {{ userData.userID }}</p>

    <!-- <ion-grid>
      <ion-row class="ion-align-items-center">
        <ion-col>
          <ion-button expand="block">Subscription Plans</ion-button>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col>
          <ion-button expand="block">Find me a carpark</ion-button>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col>
          <ion-button expand="block" href="/viewBooking"
            >My Bookings</ion-button
          >
        </ion-col>
      </ion-row>
    </ion-grid> -->

    <ion-grid>
      <ion-row class="ion-align-items-center ion-padding-top">
        <ion-col>
         Available Carparks
        </ion-col>
      </ion-row>

      <ion-row class="ion-align-items-center ion-padding-top">
        <ion-col>
         Current available sthsth
        </ion-col>
      </ion-row>

    </ion-grid>
  </base-layout>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      userData: {}
    }
  },
  methods: {
    loadUserData(){
      this.userData = JSON.parse(localStorage.getItem("userData"));
    },
  },
  // Calls function on page load
  mounted(){
    this.loadUserData();
  }
});
</script>
