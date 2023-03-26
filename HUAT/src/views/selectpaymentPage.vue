<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/tabs/wallet"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Payment</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
      <ion-list>
        <ion-item button @click="routeNets('Nets')">
          <ion-label>NETS</ion-label>
        </ion-item>
        <!-- <ion-item @click="routeNets('Nets')">
          <img src="assets/images/nets.png" />
        </ion-item> -->
        <ion-item button @click="routeStripe('Stripe')">
          <ion-label>Others</ion-label>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  // IonButton,
  IonPage,
  IonHeader,
  IonTitle,
  IonContent,
  IonToolbar,
  IonBackButton,
  IonButtons,
  // IonCol,
  // IonRow,
  IonList,
  IonItem,
  IonLabel
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    // IonButton,
    IonBackButton,
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
    IonButtons,
    // IonCol,
    // IonRow,
    IonList,
    IonItem,
    IonLabel
  },
  data() {
    return {
      stripe: null,
      balance: 0,
      userData: {},
    };
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
    },
    routeNets(route) {
      this.$router.push({
        path: "/" + route,
      });
    },
    routeStripe(route) {
      this.$router.push({
        path: "/" + route,
      });
    },
  },
  mounted() {
    this.loadUserData();
  },
});
</script>

<style></style>
