<template>
    <base-layout>
        <ion-grid scroll-y="false">
            <ion-row class="ion-justify-content-center">
              <img src='assets/images/nets.png'/>
            </ion-row>
            <div class="ion-padding ion-text-center">
              <p class="pageHeader">Login</p>
            </div>

            <ion-list>
                <ion-item fill="solid" ref="item">
                    <!-- <ion-input :clearInput="true" placeholder="Username:" type="email" @ionInput="validate"></ion-input> -->
                    <ion-input :clearInput="true" placeholder="Username" v-model="username"></ion-input>
                </ion-item>
    
                <!-- password -->
                <ion-item>
                    <ion-input :clearInput="true" type="password" placeholder="Password" v-model="password">
                    </ion-input>
                </ion-item>
            </ion-list>
            <!-- username -->
    
            <div class="myLine ion-justify-content-center">
              <a href="/forgotPassword" class=""><i>Forgot password?</i></a>
            </div>
            <!-- <ion-row class="ion-padding-top">
                <ion-col>
                    <div class="myLine ion-justify-content-start">
                        <ion-item lines="none">
                            <ion-checkbox></ion-checkbox>
                            <ion-label> Remember me</ion-label>
                        </ion-item>
                        <ion-button class="hyperlinkButton" >Forgot Password</ion-button>
                        <a float-right class="myLine2" href="/forgotPassword">Forgot password?</a>
                    </div>
                </ion-col>
            </ion-row> -->
    
            <div class="ion-text-center ion-padding-top">
                <a href="/register"> Do not have an account? Sign up now! </a>
            </div>

            <!-- login -->
            <div class="ion-padding-top">
                <ion-button expand="block" @click="validateLogin()">Login</ion-button>
            </div>

            <!-- login error message -->
            <!-- Password error message -->
            <!-- User does not exist error message -->
            <ion-note color="danger" class="ion-text-center">
                <p v-if="usernameError != '' ">{{ usernameError }}</p>
                <p v-if="passwordError != '' ">{{ passwordError }}</p>
            </ion-note>
            
            <ion-note color="danger" class="ion-text-center">
                <p id="NoUserFound"></p>
            </ion-note>

            <!-- username error message -->
            <!-- <ion-item lines="none" v-if="">
              <ion-note color="danger">
                <ul>
                  <li>{{ usernameError }}</li>
                </ul>
              </ion-note>
          </ion-item> -->
        </ion-grid>
    </base-layout>
</template>

<script>
import {
    IonRow,
    IonInput,
    IonItem,
    IonButton,
    // IonCheckbox,
    // IonLabel,
    IonList,
    IonNote,
    // IonCol,
    IonGrid,
    // IonIcon
} from "@ionic/vue"; // IonCol, IonList
// import {eye} from "ionicons/icons";
import { defineComponent } from "vue";
import axios from 'axios';

export default defineComponent({
    components: {
        IonRow,
        IonGrid,
        IonList,
        // IonCol,
        IonNote,
        IonInput,
        IonItem,
        IonButton,
        // IonIcon
        // IonCheckbox,
        // IonLabel,
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

            if (this.username != "" && this.password != "") {
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

                const response = axios(config)
                    .then(function(response) {
                        localStorage.setItem("userData", JSON.stringify(response.data.data));
                        // console.log(response.data);
                        router.push("tabs");
                        return response.data
                    })
                    .catch(function(error) {
                        error = "User not found. Please Try Again!"
                        document.getElementById("NoUserFound").innerText = error
                        console.log(error)
                        // return error
                    });

                return response;

            } else {
                if (this.username == '') {
                    this.usernameError = "Username cannot be empty";
                }
                if (this.password == '') {
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
    /* text-align: center; */
}

.pageHeader {
    /* padding-top: 60px; */
    /* padding-bottom: 60px; */
    font-size: 35px;
    color: #484747;
    font-weight: 700;
}

.myLine {
    display: flex;
    padding-top: 10px;
    align-items: end;
}

a{
   text-decoration: none;
   font-size: 12px;
}
</style>

