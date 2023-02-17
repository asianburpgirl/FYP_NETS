<template>
  <base-layout >
    <ion-grid scroll-y="false">
      <ion-row class="ion-justify-content-center">
        <img src='assets/images/nets.png' />
      </ion-row>

      <ion-row class="ion-justify-content-center">
        <icon-col size="9" class="pageHeader"> Login </icon-col>
      </ion-row>

      <!-- username -->
      <ion-item fill="solid" ref="item">
        <!-- <ion-input :clearInput="true" placeholder="Username:" type="email" @ionInput="validate"></ion-input> -->
        <ion-input
          :clearInput="true"
          placeholder="Username"
          v-model="username"
        ></ion-input>
      </ion-item>
      
      <!-- password -->
      <ion-item>
        <ion-input
          :clearInput="true"
          type="password"
          placeholder="Password"
          v-model="password"
        ></ion-input>
      </ion-item>
      
      <ion-row class="ion-padding-top">
        <ion-col>
          <div class="myLine ion-justify-content-start">
            <ion-item lines="none">
              <ion-checkbox></ion-checkbox>
              <ion-label> Remember me</ion-label>
            </ion-item>
            <!-- <ion-button class="hyperlinkButton" >Forgot Password</ion-button> -->
            <a float-right class="myLine2" href="/forgotPassword">Forgot password?</a>
          </div>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top">
        <ion-col>
          <div class="ion-text-center">
            <a href="/register"> Do not have an account? Sign up now! </a>
          </div>
        </ion-col>
      </ion-row>
      
      <!-- login -->
      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" @click="validateLogin()">Login</ion-button>
      </ion-row>
      <!-- login error message -->
  

      <!-- Password error message -->
      <ion-item lines="none">
          <ion-note color="danger">
            <ul>
              <li v-if="usernameError != '' ">{{ usernameError }}</li>
              <li v-if="passwordError != '' ">{{ passwordError }}</li>
            </ul>
          </ion-note>
      </ion-item>

      <!-- username error message -->
      <!-- <ion-item lines="none" v-if="">
          <ion-note color="danger">
            <ul>
              <li>{{ usernameError }}</li>
            </ul>
          </ion-note>
      </ion-item> -->


      <ion-item lines="none">
          <ion-note color="danger">
            <ul id="hi">
            </ul>
          </ion-note>
      </ion-item>

    </ion-grid>
  </base-layout>
</template> 

<script>
import {
  IonRow,
  IonInput,
  IonItem,
  IonButton,
  IonCheckbox,
  IonLabel,
  IonNote,
  IonCol,
  IonGrid
} from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";
import axios from 'axios';

export default defineComponent({
  components: {
    IonRow,
    IonGrid,
    IonCol,
    IonNote,
    IonInput,
    IonItem,
    IonButton,
    IonCheckbox,
    IonLabel,
  },
  data() {
    return {
      username: "",
      password: "",
      passwordError: "",
      usernameError: "",
      loginError: "",
    };
  },
  methods: {
    init() {
      localStorage.setItem("userData", "");
    },
    validateLogin() {
      let data = "";
      let config = {};

      if(this.username != "" && this.password != ""){
        // console.log("username and password avail")
        data = JSON.stringify({
          "username": this.username,
          "password": this.password
        });

        // contains the configuration that was sent along with the request
        config = {
          method: 'post',
          mode: 'cors',
          url: 'http://localhost:5002/userlogin',
          headers: {
              'Content-Type': 'application/json'
          },
          data: data
        }

        const router = this.$router;

        const response =  axios(config)
            .then(function (response) {
                localStorage.setItem("userData", JSON.stringify(response.data.data));
                // console.log(response.data);
                router.push("tabs");
                return response.data
            })
            .catch(function (error) {
                error = "Incorrect login details. Please try again"
                document.getElementById("hi").innerText = error
                console.log(error)
                // return error
            });

        return response;

      } else {
        if (this.username == '') {
          this.usernameError = "Username cannot be empty";
        } 
        if (this.password == ''){
          this.passwordError = "Password cannot be empty";
        }
      }      
    },
  },
  mounted() {
    this.init()
  }
});
</script>

<style scoped>
ion-content {
  --overflow: hidden;
}

img {
  /* --padding-top: 100px;  this is for ion content*/
  padding-top: 100px;
  width: 290px;
}
.pageHeader {
  padding-top: 60px;
  padding-bottom: 60px;
  font-size: 35px;
  color: #484747;
  font-weight: 700;
}

ion-checkbox {
  --size: 14px;
}

.myLine {
  display: flex;
  align-items: center;
  /* font-size: 14px; */
}

.myLine2 {
  display: flex;
  align-items: center;
  /* padding-left: 10px; */
}

/* .hyperlinkButton{
  --color: black;
  --background: transparent;
  --size: 10px;
  font-size: 14px
  
} */
</style>
<!-- purpose filtering: focus -->
<!-- purpose marketing: attract -->
<!-- purpose sales: convert customers -->
