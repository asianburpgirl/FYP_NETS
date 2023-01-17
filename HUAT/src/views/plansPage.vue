<template>
  <!-- <base-layout pageTitle="Subscription Plans" pageToGoBack="/tabs/"> -->
  <base-layout pageTitle="Subscription Plans" pageToGoBack="/tabs/" >
  
      <ion-card>
        <!-- <ion-img src="assets/images/ion.jpg"></ion-img> -->
        <ion-grid>
          <ion-card-header>
            <ion-card-title>Basic Plan</ion-card-title>
            <ion-card-subtitle>Free 1 hour parking</ion-card-subtitle>
            <ion-card-subtitle>Free parking on birthday</ion-card-subtitle>
            <br />
            <ion-card-subtitle align="right"
              >Valid till 25/9/23</ion-card-subtitle
            >
          </ion-card-header>
        </ion-grid>
      </ion-card>
      <ion-card>
        <!-- <ion-img src="assets/images/ion.jpg"></ion-img> -->
        <ion-grid>
          <ion-card-header>
            <ion-card-title>Premium Plan</ion-card-title>
            <ion-card-subtitle>Free 2 hour parking</ion-card-subtitle>
            <ion-card-subtitle>Free parking once a month</ion-card-subtitle>
            <ion-card-subtitle
              >Pay parking fees at the end of the month</ion-card-subtitle
            >
            <br />
            <ion-item lines="none">
              <ion-button
                slot="end"
                color="success"
                size="large"
                href="/buySubscription"
                >Buy</ion-button
              >
            </ion-item>
          </ion-card-header>
        </ion-grid>
      </ion-card>

  </base-layout>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
} from "@ionic/vue";
// import ExploreContainer from '@/components/ExploreContainer.vue';
</script>

<style scoped>
.item-inner {
  padding: 0;
}
</style>
