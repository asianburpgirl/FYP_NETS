<template>
  <base-layout needToolBar="y" needBackButton="y" pageToGoBack="/">
    <!-- <ion-row class="ion-justify-content-center">
      <ion-img src="assets/images/forget_password.png" />
    </ion-row> -->
    <ion-grid class="ion-padding">
      <h1>Reset Password</h1>
      <p>
        Enter the email associated with your account and we will send you a link
        to reset your account:
      </p>
      <ion-input
        lines="solid"
        :clearInput="true"
        placeholder="Email"
        v-model="email"
      ></ion-input>
      <ion-item lines="none"> </ion-item>

      <div class="ion-justify-content-center">
        <ion-button expand="block" @click="forgotPassword(email)"
          >Send Link</ion-button
        >
      </div>
      <div class="ion-padding-top">
        <p v-if="isEmailValid == 2" class="error-message">Invalid email!</p>
        <p v-if="emailNoExist == true" class="error-message">
          Your email does not exist in our database.
        </p>
      </div>
    </ion-grid>

    <ion-modal :is-open="successOpen" class="ion-padding">
      <ion-content class="ion-padding">
        <ion-grid>
          <ion-img src="../../public/assets/images/mail.png"></ion-img>
          <p>
            An email to reset your password has been sent to the email. Do
            follow the instructions on the email.
          </p>
          <p>Bringing you back to Login page...</p>
          <ion-row class="ion-justify-content-center">
            <ion-col>
              <ion-button @click="routeToLoginPage()">Login</ion-button>
            </ion-col>
          </ion-row>
        </ion-grid>
      </ion-content>
    </ion-modal>
  </base-layout>
</template>

<script lang="ts">
import {
  IonInput,
  IonModal,
  IonContent,
  IonGrid,
  IonButton,
  IonItem,
  IonImg,
  IonRow,
  IonCol,
} from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonInput,
    IonModal,
    IonContent,
    IonGrid,
    IonButton,
    IonItem,
    IonImg,
    IonRow,
    IonCol,
  },
  data() {
    return {
      email: "",
      isEmailValid: 0,
      successOpen: false,
      emailNoExist: false,
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
          "http://13.55.33.68:5002/checkUserExist?email=" +
          emailNameOnly +
          "&account=" +
          emailAccountOnly;

        axios.get(url).then((response) => {
          const responseMessage = response.data.message;
          if (responseMessage == "User exists") {
            this.successOpen = true;
            const timer: ReturnType<typeof setTimeout> = setTimeout(
              () => this.setSuccessOpen(false),
              10000
            );
          }

          if (responseMessage == "User not found") {
            this.emailNoExist = true;
          }
        });
      } else {
        this.isEmailValid = 2;
      }
    },
  },
});
</script>

<style scoped>
ion-img {
  width: 70%;
  height: 70%;
  margin-bottom: 10px;
}

p {
  font-size: 15px;
  font-style: italic;
}

.error-message {
  color: #eb445a;
}
</style>
