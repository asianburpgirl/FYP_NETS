<template>
  <base-layout>
    <ion-grid>
      <ion-row class="ion-justify-content-center">
        <img :src="require('../images/nets.png')" />
      </ion-row>

      <ion-row class="ion-justify-content-center">
        <icon-col size="9" class="pageHeader"> Registration </icon-col>
      </ion-row>

      <!-- username -->
      <ion-list>
        <ion-item>
          <ion-label position="stacked">Username:</ion-label>
          <ion-input
            :clear-input="true"
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
          <ion-label position="stacked">Name:</ion-label>
          <ion-input
            :clear-input="true"
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
          <ion-label position="stacked">Email:</ion-label>
          <ion-input
            :clear-input="true"
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
          <ion-label position="stacked">Password:</ion-label>
          <ion-input
            :clear-input="true"
            type="password"
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
          <ion-label position="stacked">Reconfirm password:</ion-label>
          <ion-input
            :clear-input="true"
            type="password"
            v-model="reconfirmPassword"
            @change="validateReconfirmPassword(reconfirmPassword)"
          ></ion-input>
        </ion-item>
        <!-- reconfirm password error message -->
        <ion-item lines="none" v-if="isReconfirmPasswordValid == 2">
            <ion-note color="danger" >Your password do not match!</ion-note>
        </ion-item>

        <!-- phone num -->
        <ion-item>
          <ion-label position="stacked">Phone number:</ion-label>
          <ion-input
            :clear-input="true"
            type="tel"
            v-model="phoneNumber"
            @change="validatePhone(phoneNumber)"
          ></ion-input>
        </ion-item>
        <!-- phone num error message -->
        <ion-item lines="none" v-if="isPhoneValid == 2">
            <ion-note color="danger" >Invalid phone number!</ion-note>
        </ion-item>

        <ion-row class="ion-padding-top ion-justify-content-center">
          <ion-button shape="round" :disabled="disabledRegisterButton==1" routerLink="/tabs/">Register</ion-button>
        </ion-row>
      </ion-list>
    </ion-grid>
  </base-layout>
</template>

<script lang="ts">
import { List } from "@ionic/core/dist/types/components/list/list";
import { defineComponent } from 'vue';

import {
  IonRow,
  IonInput,
  IonItem,
  IonButton,
  IonLabel,
  IonNote,
} from "@ionic/vue";
import { construct } from "ionicons/icons";

export default defineComponent( {
  components: {
    IonRow,
    IonInput,
    IonItem,
    IonButton,
    IonLabel,
    IonNote,
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
        this.registerButton()
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
        this.registerButton()
      } else {
        this.isUsernameValid = 2;
      }
    },
    validateName(name: string) {
      //valid path. name less than 128 characters
      if (name.length < 128) {
        this.isNameValid = 1;
        this.registerButton()
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
      const capsAllPassword = password.toUpperCase()
      if (password == capsAllPassword) {
        this.passwordErrors.push(
          "Password must have at least a lower letter"
        );
      }
      // check if there is at least a capital letter in password
      const lowerAllPassword = password.toLowerCase()
      if (password == lowerAllPassword) {
        this.passwordErrors.push(
          "Password must have at least an upper letter"
        );
      }
      this.registerButton()
    },
    validateReconfirmPassword(reconfirmPassword: string) { 
      //valid path. reconfirm password same as password
      if (reconfirmPassword == this.password ) {
        this.isReconfirmPasswordValid = 1;
        //issue if user enter reconfirm password first, then enter password.
        // even if same passwords, will have 
        this.registerButton()
      } else {
        this.isReconfirmPasswordValid = 2;
      }
    },
    validatePhone(phoneNum: string) { 
      //valid path. phone number is 8 numbers
      if (phoneNum.length == 8 ) {
        this.isPhoneValid = 1;
        this.registerButton()
      } else {
        this.isPhoneValid = 2;
      }
    },
    registerButton(){
      // only let user register if they are no errors 
      // disabledRegisterButton
      console.log(this.isPhoneValid== 1)
      console.log( this.isReconfirmPasswordValid ==1 ) 
      console.log(this.isNameValid==1)
      console.log(this.isEmailValid == 1)
      if (this.isPhoneValid== 1 && this.isReconfirmPasswordValid== 1 && this.isNameValid==1 && this.isEmailValid == 1){
        this.disabledRegisterButton = 0
      }
      // this.$router.push({
      //   path: '/tabs/',
      // });
    }
    
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
  padding: 45px;
  font-size: 35px;
  color: #484747;
  font-weight: 700;
}

ion-checkbox {
  --size: 20px;
}

ion-note {
  font-size: small;
}
</style>
