<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar>
        <ion-tab-button tab="home" href="/tabs/home">
          <ion-icon :icon="home" />
          <ion-label>Home</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="wallet" href="/tabs/wallet">
          <ion-icon :icon="card" />
          <ion-label>Wallet</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="booking" href="/tabs/bookings">
          <ion-icon :icon="map" />
          <ion-label>Bookings</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="plans" href="/tabs/plans">
          <ion-icon :icon="albums" />
          <ion-label> Plans</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="profile" href="/tabs/profile">
          <ion-icon :icon="person" />
          <ion-label>Profile</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script>
import {
  IonTabBar,
  IonTabButton,
  IonTabs,
  IonLabel,
  IonIcon,
  IonPage,
  IonRouterOutlet,
} from "@ionic/vue";
import { albums, card, home, map, person } from "ionicons/icons";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonTabBar,
    IonTabButton,
    IonTabs,
    IonLabel,
    IonIcon,
    IonPage,
    IonRouterOutlet,
  },
  setup() {
    return { card, albums, home, map, person };
  },
});
</script>
