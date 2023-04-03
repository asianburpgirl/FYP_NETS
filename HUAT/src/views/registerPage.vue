<template>
  <base-layout pageTitle="Registration" needToolBar="y">
    <ion-grid>
      <ion-row class="ion-justify-content-center">
        <!-- <img :src="require('../images/nets.png')" /> -->
        <img src="assets/images/carparkism.png" />
      </ion-row>

      <ion-row class="ion-justify-content-center ion-padding">
        <ion-col size="12" class="pageHeader">Get Started Now</ion-col>
        <ion-col size="12">
          <p>
            It's free to join and gain full access to our features to carpark
            slot booking!
          </p></ion-col
        >
      </ion-row>

      <!-- username -->
      <ion-list class="ion-padding-bottom">
        <ion-item>
          <!-- <ion-label position="stacked">Username:</ion-label> -->
          <ion-input
            :clear-input="true"
            placeholder="Username"
            v-model="userName"
            @change="validateUsername(userName)"
          ></ion-input>
        </ion-item>
        <!-- username error message -->
        <ion-item lines="none" v-if="isUsernameValid == 2">
          <ion-note color="danger">Your username is too long!</ion-note>
        </ion-item>

        <!-- name -->
        <ion-item>
          <!-- <ion-label position="stacked">Name:</ion-label> -->
          <ion-input
            :clear-input="true"
            placeholder="Name"
            v-model="name"
            @change="validateName(name)"
          >
          </ion-input>
        </ion-item>
        <!-- name error message -->
        <ion-item lines="none" v-if="isNameValid == 2">
          <ion-note color="danger">Your name is too long!</ion-note>
        </ion-item>

        <!-- email -->
        <ion-item>
          <!-- <ion-label position="stacked">Email:</ion-label> -->
          <ion-input
            :clear-input="true"
            placeholder="Email"
            type="email"
            v-model="email"
            @change="validateEmail(email)"
          >
          </ion-input>
        </ion-item>
        <!-- email error message -->
        <ion-item lines="none" v-if="isEmailValid == 2">
          <ion-note color="danger">Invalid email!</ion-note>
        </ion-item>

        <!-- password -->
        <ion-item>
          <!-- <ion-label position="stacked">Password:</ion-label> -->
          <ion-input
            :clear-input="true"
            type="password"
            placeholder="Password"
            v-model="password"
            @change="validatePassword(password)"
          ></ion-input>
        </ion-item>
        <!-- password error message -->
        <ion-item lines="none" v-if="passwordErrors.length != 0">
          <ion-note color="danger">
            <ul v-for="error of passwordErrors" :key="error">
              <li>{{ error }}</li>
            </ul>
          </ion-note>
        </ion-item>

        <!-- reconfirm password -->
        <ion-item>
          <!-- <ion-label position="stacked">Reconfirm password:</ion-label> -->
          <ion-input
            :clear-input="true"
            type="password"
            placeholder="Confirm Password"
            v-model="reconfirmPassword"
            @change="validateReconfirmPassword(reconfirmPassword)"
          ></ion-input>
        </ion-item>
        <!-- reconfirm password error message -->
        <ion-item lines="none" v-if="isReconfirmPasswordValid == 2">
          <ion-note color="danger">Your password do not match!</ion-note>
        </ion-item>

        <!-- phone num -->
        <ion-item>
          <!-- <ion-label position="stacked">Phone number:</ion-label> -->
          <ion-input
            :clear-input="true"
            type="tel"
            placeholder="Phone Number"
            v-model="phoneNumber"
            @change="validatePhone(phoneNumber)"
          ></ion-input>
        </ion-item>
        <!-- phone num error message -->
        <ion-item lines="none" v-if="isPhoneValid == 2">
          <ion-note color="danger">Invalid phone number!</ion-note>
        </ion-item>
      </ion-list>
      <div class="ion-padding ion-justify-content-center">
        <ion-button
          expand="block"
          shape="round"
          :disabled="disabledRegisterButton == 1"
          @click="registerUser"
          >Sign Up</ion-button
        >
        <div class="ion-text-center ion-padding-top">
          <a href="/login"><i>Already have an account? Sign in here!</i></a>
        </div>
      </div>
    </ion-grid>
  </base-layout>
</template>

<script lang="ts">
import { List } from "@ionic/core/dist/types/components/list/list";
import { defineComponent } from "vue";

import {
  IonGrid,
  IonRow,
  IonInput,
  IonItem,
  IonButton,
  // IonLabel,
  IonNote,
  IonList,
  IonCol,
} from "@ionic/vue";
import { construct } from "ionicons/icons";
import axios from "axios";

export default defineComponent({
  components: {
    IonGrid,
    IonRow,
    IonInput,
    IonItem,
    IonButton,
    // IonLabel,
    IonNote,
    IonList,
    IonCol,
  },
  data() {
    return {
      userName: "",
      name: "",
      email: "",
      password: "",
      reconfirmPassword: "",
      phoneNumber: "",

      // if using boolean, the error msgs will appear when user first load.
      // 0 = neutral (first load), 1 = valid (accept field), 2 = not valid (error message)
      isUsernameValid: 0,
      isNameValid: 0,
      isEmailValid: 0,
      isReconfirmPasswordValid: 0,
      isPhoneValid: 0,

      //password need a list since there are multiple requiremnts to a password,
      passwordErrors: Array<string>(),

      disabledRegisterButton: 1,
    };
  },
  methods: {
    validateEmail(email: string) {
      //user enter valid address (with a @)
      if (email.match("@")) {
        this.isEmailValid = 1;
        this.registerButton();
      } else {
        this.isEmailValid = 2;
      }
      //  copied from ionic website, not sure what it is but i think its @ in computer language. same as console.log(email.match('@'))
      // console.log(email.match(/^(?=.{1,254}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/))
    },
    validateUsername(username: string) {
      //valid path. username less than 128 characters
      if (username.length < 128) {
        this.isUsernameValid = 1;
        this.registerButton();
      } else {
        this.isUsernameValid = 2;
      }
    },
    validateName(name: string) {
      //valid path. name less than 128 characters
      if (name.length < 128) {
        this.isNameValid = 1;
        this.registerButton();
      } else {
        this.isNameValid = 2;
      }
    },
    validatePassword(password: string) {
      this.passwordErrors = Array<string>(); // empty array to delete all errors
      // error if password is too short
      if (password.length < 8) {
        this.passwordErrors.push(
          "Password length must be more than 8 characters"
        );
      }
      // check if there is at least a lower letter in password
      const capsAllPassword = password.toUpperCase();
      if (password == capsAllPassword) {
        this.passwordErrors.push("Password must have at least a lower letter");
      }
      // check if there is at least a capital letter in password
      const lowerAllPassword = password.toLowerCase();
      if (password == lowerAllPassword) {
        this.passwordErrors.push("Password must have at least an upper letter");
      }
      this.registerButton();
    },
    validateReconfirmPassword(reconfirmPassword: string) {
      //valid path. reconfirm password same as password
      if (reconfirmPassword == this.password) {
        this.isReconfirmPasswordValid = 1;
        //issue if user enter reconfirm password first, then enter password.
        // even if same passwords, will have
        this.registerButton();
      } else {
        this.isReconfirmPasswordValid = 2;
      }
    },
    validatePhone(phoneNum: string) {
      //valid path. phone number is 8 numbers
      if (phoneNum.length == 8) {
        this.isPhoneValid = 1;
        this.registerButton();
      } else {
        this.isPhoneValid = 2;
      }
    },
    registerButton() {
      // only let user register if they are no errors
      if (
        this.isPhoneValid == 1 &&
        this.isReconfirmPasswordValid == 1 &&
        this.isNameValid == 1 &&
        this.isEmailValid == 1
      ) {
        this.disabledRegisterButton = 0;
      }
    },
    registerUser() {
      const url = "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5002/users"; // hardcoded
      axios
        .post(url, {
          email: this.email,
          name: this.name,
          phoneNum: this.phoneNumber,
          username: this.userName,
          password: this.password,
        })
        .then((response) => {
          console.log(response);
          this.$router.push({
            path: "/",
          });
        });
    },
  },
});
</script>

<style scoped>
img {
  /* --padding-top: 100px;  this is for ion content*/
  padding-top: 45px;
  width: 290px;
}
.pageHeader {
  text-align: center;
  font-size: 20px;
  color: #484747;
  font-weight: 700;
}

p {
  font-size: 13px;
}

ion-checkbox {
  --size: 20px;
}

ion-note {
  font-size: small;
}

.ion-padding {
  padding-bottom: 0px;
  padding-top: 0px;
}

a{
   text-decoration: none;
   font-size: 12px;
}
</style>
