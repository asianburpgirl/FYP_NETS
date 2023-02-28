<template>
<ion-page class="ion-padding">
    <ion-header>
        <ion-toolbar>
            <ion-buttons slot="start">
                <ion-back-button defaultHref="/tabs/wallet"></ion-back-button>
            </ion-buttons>
            <ion-title class="ion-text-center">NETS Top-up amount</ion-title>
        </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
        <img src='assets/images/nets.png' />
        <ion-button shape="round" expand="block" size="large" @click="routeTen()">$10</ion-button>
        <ion-button shape="round" expand="block" size="large" @click="routeTwenty()">$20</ion-button>
        <ion-button shape="round" expand="block" size="large" @click="routeThirty()">$30</ion-button>
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
        routeTen(route) {
            const url = "http://localhost:5002/addTen/" + this.userData.userID + "/" + parseInt(this.userData.balance);
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
        
            this.$router.push({
                path: '/tabs/wallet',
            });
        },
        routeTwenty() {
            console.log(this.userData)
            const url = "http://localhost:5002/addTwenty/" + this.userData.userID + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                userID: this.userData.userID,
                balance: this.userData.balance
            })
            .then((response) => {
                this.userData = JSON.parse(localStorage.getItem("userData"));
                console.log(this.userData)
                this.userData.balance = response.data.data
                localStorage.setItem("userData", JSON.stringify(this.userData));
            })
            .catch((error) => {
                console.log(error.message);
            });
            
            
            this.$router.push({
                path: '/tabs/wallet',
            });
         
        },
        routeThirty(route) {
            const url = "http://localhost:5002/addThirty/" + this.userData.userID + "/" + parseInt(this.userData.balance);
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
        
            this.$router.push({
                path: '/tabs/wallet',
            });
        },
    },
    mounted() {
      this.loadUserData()
    }
  });
  </script>