<template>
  <ion-page>
    <ion-content class="ion-padding">
      <ion-grid class="ion-padding">
        <ion-row class="ion-justify-content-center">
          <ion-img src="assets/images/parking.png"></ion-img>
        </ion-row>
        <h1><b><i>Where do you want to drive to?</i></b></h1>
        <p><i>Let's make this your least expensive journey ever.</i></p>
        <ion-button expand="block" shape="round" @click="routeUser('login')">Get Started</ion-button>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import {
  IonButton,
  IonGrid,
  IonContent,
  IonPage,
  IonImg,
  IonRow,
} from "@ionic/vue";

export default defineComponent({
  components: { IonContent, IonPage, IonGrid, IonButton, IonImg, IonRow },
  methods: {
    routeUser(route: string) {
      this.$router.push({
        path: "/" + route,
      });
    },
  },
});
</script>

<style scoped>
h1 {
  padding-top: 40px;
  font-size: 40px;
}

ion-img {
  padding-top: 100px;
  width: 70%;
}
</style>
