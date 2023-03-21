<template>
  <base-layout needToolBar="y" pageTitle="Payment Successful">
    <div class="ion-padding">
      <p>Payment has been made. Thank you!</p>
      <ion-button
        color="primary"
        routerLink="/tabs/wallet"
        routerDirection="forward"
        >Back to Wallet</ion-button
      >
    </div>
  </base-layout>
</template>

<script>
import { IonButton } from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonButton,
  },
  data() {
    return {
      userData: {},
    };
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
    },
  },
  mounted() {
    this.loadUserData();
  },
});
</script>
