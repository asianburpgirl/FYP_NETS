<template>
  <base-layout >
    <ion-grid scroll-y="false">
      <ion-row class="ion-justify-content-center">
        <img :src="require('../images/nets.png')" />
      </ion-row>

      <ion-row class="ion-justify-content-center">
        <icon-col size="9" class="pageHeader"> Login </icon-col>
      </ion-row>

      <ion-item fill="solid" ref="item" class="paddingTop">
        <!-- <ion-input :clearInput="true" placeholder="Username:" type="email" @ionInput="validate"></ion-input> -->
        <ion-input
          :clearInput="true"
          placeholder="Username:"
          type="email"
        ></ion-input>
        <ion-note slot="error">Invalid email</ion-note>
      </ion-item>

      <ion-item>
        <ion-input
          :clearInput="true"
          type="password"
          placeholder="Password:"
        ></ion-input>
      </ion-item>

      <ion-row class="ion-padding-top">
        <ion-col>
          <div class="myLine ion-justify-content-center">
            <ion-item lines="none">
              <ion-checkbox></ion-checkbox>
              <ion-label> Remember me</ion-label>
            </ion-item>
            <!-- <ion-button class="hyperlinkButton" >Forgot Password</ion-button> -->
            <a float-right class="myLine2" href="/tabs/">Forgot password</a>
          </div>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-col class="ion-text-center">
            <a href="/register"> New User? Sign up now! </a>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" routerLink="/tabs/">Login</ion-button>
      </ion-row>
    </ion-grid>
  </base-layout>
</template>

<script lang="ts">
import {
  IonRow,
  IonInput,
  IonItem,
  IonButton,
  IonCheckbox,
  IonLabel,
  IonNote,
} from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";

export default defineComponent({
  
});
</script>

<style scoped>
ion-content {
  --overflow: hidden;
}

img {
  /* --padding-top: 100px;  this is for ion content*/
  padding-top: 110px;
  width: 290px;
}
.pageHeader {
  padding: 110px;
  font-size: 35px;
  color: #484747;
  font-weight: 700;
}

ion-checkbox {
  --size: 20px;
}

.myLine {
  display: flex;
  align-items: center;
  font-size: 14px;
}

.myLine2 {
  display: flex;
  align-items: center;
  padding-left: 10px;
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
