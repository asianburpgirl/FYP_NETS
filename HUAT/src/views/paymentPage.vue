<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/tabs/wallet"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Payment</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
      <ion-button shape="round" expand="block" size="large" @click="routeNets('Nets')">NETS</ion-button>
      <ion-button shape="round" expand="block" size="large" @click="routeStripe()">Stripe</ion-button>
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
    routeStripe() {
      const routeData = 'https://buy.stripe.com/test_8wMaGm2Di8m1fXq6oq';
      window.open(routeData, '_blank');

      const url = "http://localhost:5002/addTen/" + this.userData.userID + "/" + this.userData.balance;
      axios.put(url, {
        userID: this.userData.userID,
        balance: this.userData.balance
      })
      .then((response) => {
        this.userData = JSON.parse(localStorage.getItem("userData"));
        this.userData.balance = response.data.data
        localStorage.setItem("userData", JSON.stringify(this.userData));
      })
      .catch((error) => {
        console.log(error.message);
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