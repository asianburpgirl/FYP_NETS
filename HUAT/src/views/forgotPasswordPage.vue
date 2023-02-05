<template>
  <base-layout
    pageTitle="Forgot Password"
    needToolBar="y"
    needBackButton="y"
    pageToGoBack="/"
  >
    <ion-grid class="ion-padding">
      Enter the email associated with your account and we will send you a link
      to reset your account:
      <ion-item fill="solid" ref="item" class="ion-padding-top">
        <ion-input
          :clearInput="true"
          placeholder="Email"
          v-model="email"
        ></ion-input>
      </ion-item>
      <ion-item lines="none" >
        <ion-note color="danger" v-if="isEmailValid == 2">Invalid email!</ion-note>
        <ion-note color="danger" v-if="emailNoExist == true">Your email does not exist in our database</ion-note>
      </ion-item>

      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" @click="forgotPassword(email)"
          >Continue</ion-button
        >
      </ion-row>
    </ion-grid>

    <ion-modal :is-open="successOpen" class="ion-padding">
      <ion-content class="ion-padding-top ion-padding">
        An email to reset your password has been sent to the email. Do follow the instructions on the email. 
        <br>
        Bringing you back to Login page.....
 
        <ion-button
          shape="round"
          @click="
            routeToLoginPage();
          "
          expand="block"
          size="large"
          >Login</ion-button
        >
        
      </ion-content>
    </ion-modal>
  </base-layout>
</template>

<script lang="ts">
import { IonInput, IonItem,IonModal, IonContent } from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonInput,
        IonItem,
        IonModal,
    IonContent
  },
  data() {
    return {
      email: "",
        isEmailValid: 0,
        successOpen: false,
      emailNoExist : false,
    };
  },
    methods: {
        routeToLoginPage() {
            this.$router
            .push({
              path: "/",
            })
            .then(() => {
              this.$router.go(0);
            });
          location.reload();
        },
     setSuccessOpen(open: boolean) {
         this.successOpen = open;
       this.$router
            .push({
              path: "/",
            })
            .then(() => {
              this.$router.go(0);
            });
          location.reload();
    },
    forgotPassword(email: string) {
      if (email.match("@")) {
        this.isEmailValid = 1;
        const emailNameOnly = this.email.split("@")[0];
        const emailAccountOnly = this.email.split("@")[1];

        const url =
          "http://127.0.0.1:5002/checkUserExist?email=" +
          emailNameOnly +
          "&account=" +
          emailAccountOnly;
        
        axios.get(url).then((response) => {
          const responseMessage = response.data.message;
          if (responseMessage == "User exists") {
              this.successOpen = true
              const timer: ReturnType<typeof setTimeout> = setTimeout(() => this.setSuccessOpen(false), 2000);
          }

          if (responseMessage == "User not found") {
              this.emailNoExist = true
          }
        
        });
      } else {
        this.isEmailValid = 2;
      }
    },
   
  },

});
</script>

<style scoped></style>
