<template>
  <ion-content class="ion-padding">
    <ion-grid>
      <ion-row>
        <img :src="require('../images/nets.png')" />
      </ion-row>

      <ion-row class="ion-justify-content-center">
        <icon-col size="9" class="pageHeader"> Login </icon-col>
      </ion-row>

      <ion-item clas="paddingTop">
        <ion-input :clearInput="true" placeholder="Username:"></ion-input>
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
          <div float-left class="myLine">
            <ion-item lines="none">
              <ion-checkbox></ion-checkbox>
              <ion-label> Remember me</ion-label>
            </ion-item>
            <div float-right class="myLine2">
              Forgot password
            </div>
          </div>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top">
        <ion-col>
          <div class="ion-text-center">New User? Sign up now!</div>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round">Login</ion-button>
      </ion-row>
      
      
    </ion-grid>
  </ion-content>
</template>

<script lang="ts">
import { IonRow, IonInput, IonItem, IonButton } from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";

export default defineComponent({
  components: { IonRow, IonInput, IonItem, IonButton }, //IonCol, IonList
});
</script>

<style scoped>
img {
  /* --padding-top: 100px;  this is for ion content*/
  padding-top: 70px;
}
.pageHeader {
  padding: 70px;
  font-size: 40px;
  color: #484747;
  font-weight: 700;
}

ion-checkbox {
  --size: 20px;
}


ion-label {
  font-size: 1000px;
}
.myLine {
  display: flex;
  align-items: center;
}

.myLine2 {
  display: flex;
  align-items: center;
  padding-left: 10px;
}
</style>
