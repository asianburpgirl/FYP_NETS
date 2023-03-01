<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title class="ion-text-center">Bookings</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
      <ion-button
        shape="round"
        expand="block"
        size="large"
        @click="routeUser('nearbyMe')"
        >Nearby Me</ion-button
      >

      <ion-button
        shape="round"
        expand="block"
        size="large"
        @click="routeUser('map')"
        >Map</ion-button
      >
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonHeader,
  IonTitle,
  IonContent,
  IonToolbar,
  // IonButtons,
  // IonBackButton,
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
    // IonButtons,
    // IonBackButton,
  },

  methods: {
    routeUser(route) {
      this.$router.push({
        path: "/" + route,
      });
    },
    getBalance() {
      this.userData = JSON.parse(localStorage.getItem("userData"));

      const url = "http://127.0.0.1:5002/getBalance/" + this.userData.userID;
      axios
        .get(url)
        .then((response) => {
          console.log(response);
          this.balance = response.data.data.balance;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  mounted() {
    this.getBalance();
  },
});
</script>

<style scoped></style>
