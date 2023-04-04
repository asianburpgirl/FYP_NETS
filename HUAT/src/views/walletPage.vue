<template>
    <base-layout pageTitle="My Wallet" needToolBar="y">
        <ion-card color="primary">
            <ion-card-header>
                <ion-card-title >${{ formatMoney(balance) }}</ion-card-title>
                <br>
                <ion-card-subtitle>Top up easily with our in-built payment</ion-card-subtitle>
            </ion-card-header>
        </ion-card>
    
        <ion-grid class="ion-padding">
            <ion-button expand="block" color="dark" @click="routeUser('payment')">
                <ion-icon :icon="wallet"> </ion-icon>
            </ion-button>
            <!-- <ion-button expand="block" color="primary">
              <ion-icon :icon="card" />
            </ion-button> -->
        </ion-grid>
        <ion-list lines="none">
            <ion-list-header align="left">
                <ion-label><b>Transaction History</b></ion-label>
            </ion-list-header>
            <ion-item>
                <ion-label>ID</ion-label>
                <ion-label>Date</ion-label>
                <ion-label >Amount</ion-label>
                <ion-label>Type</ion-label>
            </ion-item>
    
            <ion-item v-for="eachTrans in trans" :key="eachTrans">
                <ion-label>{{eachTrans.transID}}</ion-label>
                <ion-label>{{ eachTrans.transDateClean }}</ion-label>
                
                <ion-label v-if="eachTrans.type == 'Topup'" :color="eachTrans.colortopup"> ${{ eachTrans.amount }}</ion-label>
                <ion-label v-if="eachTrans.type == 'Deduct'" :color="eachTrans.colordeduct" >- ${{ eachTrans.amount }}</ion-label>
                <ion-label> {{eachTrans.type}}</ion-label>
                
            </ion-item>
        </ion-list>
    </base-layout>
</template>

<script>
import {
    IonGrid,
    IonCard,
    IonIcon,
    IonButton,
    IonLabel,
    IonList,
    IonItem,
    IonListHeader,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle
} from "@ionic/vue";
import { defineComponent } from "vue";
import { card, wallet } from "ionicons/icons";
import axios from "axios";

export default defineComponent({
    components: {
        IonGrid,
        IonCard,
        IonIcon,
        IonButton,
        IonLabel,
        IonList,
        IonItem,
        IonListHeader,
        IonCardHeader,
        IonCardSubtitle,
        IonCardTitle
    },
    setup() {
        return { card, wallet };
    },
    data() {
        return {
            stripe: null,
            balance: 0,
            userData: {},
            transactionDetails: [],
            trans: [],
        };
    },
    methods: {
        formatMoney(myFloat) {
            // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
            myFloat = myFloat.toString();
            const dotExists = myFloat.includes(".");
            let newFloat = myFloat;
            if (dotExists) {
                newFloat = myFloat.split(".");
                if (newFloat[1].length == 1) {
                    newFloat[1] += "0";
                } else if (newFloat[1].length == 0) {
                    newFloat[1] += "00";
                }
                newFloat = newFloat.join(".");
            } else {
                newFloat += ".00";
            }

            return newFloat;
        },
        getUserBooking() {
            this.userData = JSON.parse(localStorage.getItem("userData"));
            const url = "http://13.55.33.68:5001/bookings/" + this.userData.userID;
            axios
                .get(url)
                .then((response) => {
                    let data = response.data.data.bookings;
                    data = data.reverse();
                    for (const eachBooking of data) {
                        this.transactionDetails.push({
                            bookingDate: eachBooking.bookingDateTime.slice(4, 17),
                            bookingID: eachBooking.bookingID,
                            amount: this.formatMoney(eachBooking.bookingAmt),
                            color: "danger", // for dynamically chaning of color. maybe top up can use "success"
                        });
                    }
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
        loadUserData() {
            this.userData = JSON.parse(localStorage.getItem("userData"));
        },
        getBalance() {
            const url = "http://13.55.33.68:5002/getBalance/" + this.userData.userID;
            axios
                .get(url)
                .then((response) => {
                    // console.log(response)
                    this.balance = response.data.data.balance;
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
        routeUser(route) {
            this.$router.push({
                path: "/" + route,
            });
        },
        getTrans() {
            this.userData = JSON.parse(localStorage.getItem("userData"));
            const url = "http://13.55.33.68:5006/transaction/" + this.userData.userID;
            axios
                .get(url)
                .then((response) => {
                    for (const eachTrans in response.data.data.bookings) {
                        const formattedDate = 
                        this.trans.push({
                            amount: this.formatMoney(response.data.data.bookings[eachTrans]['amount']),
                            transID: response.data.data.bookings[eachTrans]['transID'],
                            transDateClean: response.data.data.bookings[eachTrans]['transDate'].slice(4, 11),
                            transDate: response.data.data.bookings[eachTrans]['transDate'],
                            type: response.data.data.bookings[eachTrans]['transType'],
                            colordeduct: "danger",
                            colortopup: "success",
                            // colorrefund: "medium",       
                        });
                        this.trans= this.trans.sort(function(a, b) {
                            const keyA = a.transDate;
                            const keyB = b.transDate;
                            if (keyA > keyB) return -1;
                            if (keyA < keyB) return 1;
                            return 0;
                        });
                    }
                    // this.balance = response.data.data.balance;
                })
                .catch((error) => {
                    console.log(error.message);
                });
        }
    },
    mounted() {
        this.loadUserData(), 
        this.getBalance();
        this.getUserBooking();
        this.getTrans()
    },
});
</script>

<style scoped>
h1 {
    font-size: 50px;
}
</style>
