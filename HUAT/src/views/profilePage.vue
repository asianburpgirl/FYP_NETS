<template>
    <ion-page>
      <ion-header>
          <ion-toolbar>
              <ion-title size="large" class="ion-text-center">My Account</ion-title>
          </ion-toolbar>
      </ion-header>
  
      <ion-content>
          <ion-grid>
          <ion-row class="ion-padding-horizontal ion-padding-top">
            <ion-col>
              <ion-avatar>
                <img
                  alt="Silhouette of a person's head"
                  src="https://ionicframework.com/docs/img/demos/avatar.svg"
                />
              </ion-avatar>
            </ion-col>
            <ion-col size="10">
              <ion-item button detail="true">
                <ion-label>
                  <h2>Mary Tan</h2>
                  <p>Edit Profile</p>
                </ion-label>
              </ion-item>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col class="ion-margin-horizontal">
              <h3>My Wallet</h3>
              <ion-icon :icon="wallet" />
              <ion-badge color="danger" style="position: absolute"
                >$100</ion-badge
              >
            </ion-col>
            <ion-col class="ion-margin-vertical">
              <ion-item lines="none" class="ion-padding-top">
                <ion-badge slot="end" color="danger">Top Up</ion-badge>
              </ion-item>
            </ion-col>
          </ion-row>
          <hr />
        </ion-grid>
  
        <ion-list class="ion-margin">
          <ion-item button detail="true">
            <ion-label>View Bookings</ion-label>
          </ion-item>
          <ion-item button detail="true">
            <ion-label>Setting</ion-label>
          </ion-item>
          <ion-item button detail="true">
            <ion-label>Language</ion-label>
          </ion-item>
          <ion-item button detail="true">
            <ion-label>Feedback</ion-label>
          </ion-item>
          <ion-item button detail="true">
            <ion-label>Help Centre</ion-label>
          </ion-item>
        </ion-list>
  
      </ion-content>
    </ion-page>
  </template>
  
  <script setup lang="ts">
  import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonIcon,
    IonCard,
    IonCardHeader,
    IonButton
  } from "@ionic/vue";
  // import ExploreContainer from '@/components/ExploreContainer.vue';
  import { defineComponent } from "vue";
  import { wallet } from "ionicons/icons";
  </script>
  
<style scoped>
/* iOS places the subtitle above the title */
ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
}
ion-icon {
  font-size: 60px;
}
hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}
</style> 
