<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar>
        <ion-tab-button tab="home" href="/adminTabs/adminHome">
          <ion-icon :icon="home" />
          <ion-label>Home</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="booking" href="/adminTabs/adminBookings">
          <ion-icon :icon="albums" />
          <ion-label>Bookings</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="users" href="/adminTabs/adminUsers">
          <ion-icon :icon="star" />
          <ion-label>Users</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="person" href="/adminTabs/adminProfile">
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
import { albums, card, home, person, star } from "ionicons/icons";
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
    return { card, albums, home, person, star };
  },
});
</script>
