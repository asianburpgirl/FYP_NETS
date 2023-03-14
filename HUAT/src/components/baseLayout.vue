<template>
  <ion-page>
    <ion-header>
      <ion-toolbar v-if="needToolBar">
        <ion-buttons v-if="needBackButton">
          <ion-back-button :default-href="pageToGoBack"></ion-back-button>
        </ion-buttons>

        <ion-title class="ion-text-center">
          {{ pageTitle }}
        </ion-title>

      </ion-toolbar>
    </ion-header>
 
    <ion-content class="ion-padding">
      <slot />
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import {
  IonPage,
  IonHeader,
  IonTitle,
  IonContent,
  IonToolbar,
  IonButtons,
  IonBackButton
} from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    pageTitle: String,
    needBackButton: String,
    pageToGoBack: String,
    needToolBar : String
  },
  components: {
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
    IonButtons,
    IonBackButton
  },
});
</script>

<style scoped></style>
