<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button defaultHref="/tabs/wallet"></ion-back-button>
                </ion-buttons>
                <ion-title class="ion-text-center">Top-up amount</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
            <!-- <img src='assets/images/stripe.png' /> -->
            <ion-row class="ion-padding-top">
                <ion-col>
                    <ion-button expand="block" @click="routeTen()">$10</ion-button>
                </ion-col>
                <ion-col>
                    <ion-button expand="block" @click="routeTwenty()">$20</ion-button>
                </ion-col>
                <ion-col>
                    <ion-button expand="block" @click="routeThirty()">$30</ion-button>
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
        routeTen() {
            const routeData = 'https://buy.stripe.com/test_8wMaGm2Di8m1fXq6oq';
            window.open(routeData, '_blank');

            const url = "http://localhost:5002/addTen/" + this.userData.userID + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                    userID: this.userData.userID,
                    balance: this.userData.balance
                })
                .then((response) => {
                    this.userData = JSON.parse(localStorage.getItem("userData"));
                    this.userData.balance = response.data.data
                    this.addTopup(10)
                    localStorage.setItem("userData", JSON.stringify(this.userData));
                    this.$router.push('/success').then(() => window.location.reload())
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
        routeTwenty() {
            const routeData = 'https://buy.stripe.com/test_5kA6q60va0TzbHaaEH';
            window.open(routeData, '_blank');

            const url = "http://localhost:5002/addTwenty/" + this.userData.userID + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                    userID: this.userData.userID,
                    balance: this.userData.balance
                })
                .then((response) => {
                    this.userData = JSON.parse(localStorage.getItem("userData"));
                    this.userData.balance = response.data.data
                    this.addTopup(20)
                    localStorage.setItem("userData", JSON.stringify(this.userData));
                    this.$router.push('/success').then(() => window.location.reload())
                    
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
        routeThirty() {
            const routeData = 'https://buy.stripe.com/test_6oEbKq2DifOt12w4gk';
            window.open(routeData, '_blank');

            const url = "http://localhost:5002/addThirty/" + this.userData.userID + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                    userID: this.userData.userID,
                    balance: this.userData.balance
                })
                .then((response) => {
                    this.userData = JSON.parse(localStorage.getItem("userData"));
                    this.userData.balance = response.data.data
                    this.addTopup(30)
                    localStorage.setItem("userData", JSON.stringify(this.userData));
                    this.$router.push('/success').then(() => window.location.reload())
                   
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
        addTopup(amount) {
            const url = "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5006/topup"
                axios
                .post(url, {
                    "amount": amount,
                    "userID": this.userData.userID
                })
                .then((response) => {
                    console.log(response)
                })
            },
    },
    mounted() {
        this.loadUserData()
    }
});
</script>