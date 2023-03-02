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
      <ion-row>
        <ion-col>
          <ion-button expand="block" size="large" @click="routeNets('Nets')">NETS</ion-button>
        </ion-col>
        <ion-col> 
          <ion-button expand="block" size="large" @click="routeStripe('Stripe')">Stripe</ion-button>
        </ion-col>
      </ion-row>
    </ion-content>
  </ion-page>
</template>


<script>
import { 
  IonButton, 
  IonPage,
  IonHeader,
  IonTitle,
  IonContent,
  IonToolbar,
  IonBackButton,
} from '@ionic/vue';
import { defineComponent } from 'vue'
import axios from "axios";

export default defineComponent({
  components: { 
    IonButton,
    IonBackButton,
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
  },
  data() {
    return {
      stripe: null,
      balance: 0,
      userData: {}
    }
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
    },
    routeNets(route) {
      this.$router.push({
        path: '/' + route,
      });
    },
    routeStripe(route) {
      this.$router.push({
        path: '/' + route,
      });
    }
  },
  mounted() {
    this.loadUserData()
  }
});
</script>

<style>
</style>