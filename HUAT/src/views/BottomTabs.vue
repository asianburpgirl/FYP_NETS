<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="home" href="/tabs/home">
          <ion-icon :icon="home" />
          <ion-label>Home</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="wallet" href="/tabs/wallet">
          <ion-icon :icon="card" />
          <ion-label>Wallet</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="plans" href="/tabs/plans">
          <ion-icon :icon="albums" />
          <ion-label> Plans</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="booking" href="/tabs/bookings">
          <ion-icon :icon="map" />
          <ion-label>Bookings</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="profile" href="/tabs/profile">
          <ion-icon :icon="person" />
          <ion-label>Profile</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script setup lang="ts">
import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
import { albums, card, ellipse, home, map, person, square, triangle } from 'ionicons/icons';
</script>
