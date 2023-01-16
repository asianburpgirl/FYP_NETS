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

      <ion-row>
        <ion-col>
          <ion-item>
            <ion-checkbox></ion-checkbox>
            <ion-label>Remember me</ion-label>
          </ion-item>
        </ion-col>
      </ion-row>
      
      <ion-row>
        <ion-col> Forgot Password? </ion-col>
      </ion-row>

      <ion-row>
        New User? Sign up now!
      </ion-row>

      <ion-button>Login </ion-button>
      <!-- PLS HELP CENTER THIS -->
    </ion-grid>
  </ion-content>
</template>

<script lang="ts">
import { IonGrid, IonRow, IonInput, IonItem } from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";

export default defineComponent({
  components: { IonGrid, IonRow, IonInput, IonItem }, //IonCol, IonList
 
});
</script>

<style scoped>


img {
  /* --padding-top: 100px;  this is for ion content*/
  padding-top: 100px;
}
.pageHeader {
  padding: 60px;
  font-size: 40px;
  color: #484747;
  font-weight: 700;
}

ion-input {
  --placeholder-color: #ffffff;
  --placeholder-opacity: 1;
  /* color: #dbdbdb; */
}


ion-button{
  padding:60px,
  
}
</style>

