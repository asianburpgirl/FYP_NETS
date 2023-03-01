<template>
  <base-layout pageTitle="My Wallet" needToolBar="y">
    <!-- <h2>Amount</h2> -->
    <ion-card color="primary">
      <ion-card-header>
        <ion-card-title>${{ balance }}</ion-card-title>
        <br>
        <ion-card-subtitle
          >Top up easily with our in-built payment</ion-card-subtitle
        >
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
      <ion-item v-for="eachBooking in transactionDetails" :key="eachBooking">
        <!-- <ion-label color="{{ eachBooking.color }}">Booking</ion-label> -->
        <ion-label :color="eachBooking.color">Booking</ion-label>
        <ion-label :color="eachBooking.color" class="ion-text-center">{{
          eachBooking.bookingDate
        }}</ion-label>
        <ion-label :color="eachBooking.color" class="ion-text-right"
          >- ${{ eachBooking.amount }}</ion-label
        >
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
    };
  },
  methods: {
    formatMoney(myFloat) {
      // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
      myFloat = myFloat.toString();
      let newFloat = myFloat.split(".");
      if (newFloat[1].length == 1) {
        newFloat[1] += "0";
      }
      newFloat = newFloat.join(".");
      return newFloat;
    },
    getUserBooking() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
      const url = "http://127.0.0.1:5001/bookings/" + this.userData.userID;
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
      const url = "http://localhost:5002/getBalance/" + this.userData.userID;
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
  },
  mounted() {
    this.loadUserData(), this.getBalance();
    this.getUserBooking();
  },
});
</script>

<style scoped>
h1 {
  font-size: 50px;
}
</style>
