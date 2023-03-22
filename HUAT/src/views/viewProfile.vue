<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/tabs/profile"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Edit Profile</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-list lines="none">
        <ion-item>
          <ion-label position="stacked">Email</ion-label>
          <ion-input
            :clear-input="true"
            placeholder="Enter new email"
          ></ion-input>
        </ion-item>

        <ion-item>
          <ion-label position="stacked">Phone Number</ion-label>
          <ion-input
            :clear-on-edit="true"
            placeholder="Enter new phone number"
          ></ion-input>
        </ion-item>

        <ion-item>
          <ion-label position="stacked">Password</ion-label>
          <ion-input
            type="password"
            placeholder="Enter new password"
          ></ion-input>
        </ion-item>
      </ion-list>
      <div class="ion-text-center ion-padding-top">
        <ion-button expand="block"> Save </ion-button>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import {
  IonContent,
  IonPage,
  IonHeader,
  IonLabel,
  IonItem,
  IonList,
  IonButton,
  IonInput,
  IonBackButton,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { add, card, home, star, wallet } from "ionicons/icons";

export default defineComponent({
  components: {
    IonContent,
    IonPage,
    IonHeader,
    IonLabel,
    IonItem,
    IonList,
    IonButton,
    IonInput,
    IonBackButton,
  },
});
</script>

<style scoped>
h1 {
  font-size: 50px;
}
</style>
