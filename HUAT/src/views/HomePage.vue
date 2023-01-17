<template>
  <base-layout pageTitle="Welcome, John Tan!" needToolBar="y">
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

<style scoped>


</style>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
} from "@ionic/vue";
import { person } from "ionicons/icons";
// import ExploreContainer from '@components/ExploreContainer.vue';
</script>
