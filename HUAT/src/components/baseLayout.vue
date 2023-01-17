<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-title>
          {{ pageTitle }}
        </ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
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
} from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  props: ["pageTitle"],
  components: {
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
  },
});
</script>

<style scoped></style>
