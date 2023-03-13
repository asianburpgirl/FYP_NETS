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

      <ion-row  class="ion-padding">
        <ion-col  @click="routeNets('Nets')"> 

        
              <img src='assets/images/nets.png'/>
              
            
          </ion-col>
      
      
        <ion-col> 
          <ion-button expand="block" size="large" @click="routeStripe('Stripe')">Others</ion-button>
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
  IonButtons,
  IonCol,
  IonRow
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
    IonButtons,
    IonCol,
    IonRow
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