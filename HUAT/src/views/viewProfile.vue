<template>
  <base-layout
    pageTitle="Edit Profile"
    pageToGoBack="/tabs/profile"
    needBackButton="y"
    needToolBar="y"
  >
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
        <ion-input type="password" placeholder="Enter new password"></ion-input>
      </ion-item>
    </ion-list>
    <div class="ion-text-center ion-padding-top">
      <ion-button shape="round" expand="block"> Save </ion-button>
    </div>
  </base-layout>
</template>

<script lang="ts">
import {
    IonLabel,
    IonItem,
    IonList,
    IonButton,
    IonInput
  
} from "@ionic/vue";
import { defineComponent } from "vue";
import { add, card, home, star, wallet } from "ionicons/icons";

export default defineComponent({
  components: {
    IonLabel,
    IonItem,
    IonList,
    IonButton,
    IonInput
  },
});
</script>

<style scoped>
h1 {
  font-size: 50px;
}
</style>
