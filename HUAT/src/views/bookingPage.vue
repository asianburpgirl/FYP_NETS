<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-title size="large" class="ion-text-center">Bookings</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding-top">
      <ion-button shape="round" expand="block" size="large" @click='routeUser("nearbyMe")'>Book</ion-button>

      <ion-button shape="round" expand="block" size="large" @click='routeUser("map")'
        >Subscription</ion-button
      >
    </ion-content>
  </ion-page>
</template>
<ion-content class="ion-padding"></ion-content>

<script lang="ts">
import {} from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: {},

  methods: {
    routeUser(route: string) {
            this.$router.push({
                path: '/' + route,
            });
        }
  }
});
</script>

<style scoped>

</style>
