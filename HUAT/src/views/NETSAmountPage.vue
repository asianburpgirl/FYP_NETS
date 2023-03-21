<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button defaultHref="/tabs/wallet"></ion-back-button>
                </ion-buttons>
                <ion-title class="ion-text-center">NETS Top-up amount</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
            <ion-img src='assets/images/nets.png'></ion-img>
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
    IonImg,
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
        IonImg,
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
            const url = "http://localhost:5002/addTen/" + parseInt(this.userData.userID) + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                    userID: parseInt(this.userData.userID),
                    balance: parseInt(this.userData.balance)
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
            const url = "http://localhost:5002/addTwenty/" + parseInt(this.userData.userID) + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                    userID: parseInt(this.userData.userID),
                    balance: parseInt(this.userData.balance)
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
            const url = "http://localhost:5002/addThirty/" + parseInt(this.userData.userID) + "/" + parseInt(this.userData.balance);
            axios.put(url, {
                    userID: parseInt(this.userData.userID),
                    balance: parseInt(this.userData.balance)
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
            const url = "http://127.0.0.1:5006/topup"
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