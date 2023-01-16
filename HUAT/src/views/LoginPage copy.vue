<template>
  <ion-content class="ion-padding">

    <ion-grid>
      <ion-row>
        <img :src="require('../images/nets.png')" />
      </ion-row>
    </ion-grid>

    <ion-grid>
      <ion-row class="ion-justify-content-center">
        <icon-col size="9" class="pageHeader"> Login </icon-col>
      </ion-row>
    </ion-grid>

    <ion-item clas="paddingTop">
      <ion-input :clearInput="true" placeholder="Username:"></ion-input>
    </ion-item>

    <ion-item>
      <ion-input :clearInput="true" type="password" placeholder="Password:"></ion-input>
    </ion-item>

    <!-- <ion-item fill="solid" ref="item">
      <ion-label position="floating">Email</ion-label>
      <ion-input type="email" @ionInput="validate" @ionBlur="markTouched"></ion-input> 
      <ion-note slot="helper">Enter a valid email</ion-note>
      <ion-note s`lot="error">Invalid email</ion-note>
  </ion-item> -->

  </ion-content>
</template>

<script lang="ts">

import { IonGrid, IonRow , IonInput, IonItem} from "@ionic/vue"; // IonCol, IonList
import { defineComponent } from "vue";

export default defineComponent({
  components: { IonGrid, IonRow,  IonInput, IonItem }, //IonCol, IonList


});


</script>

<style scoped>
ion-col {
  background-color: #135d54;
  border: solid 1px #fff;
  color: #fff;
  text-align: center;
}

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
  --placeholder-color: #484747;
  --placeholder-opacity: 1;
  color: #484747;
}


</style>


<!-- <ion-input type="email" @ionInput="validate" @ionBlur="markTouched"></ion-input> -->
<!-- <ion-note slot="helper">Enter a valid email</ion-note> -->