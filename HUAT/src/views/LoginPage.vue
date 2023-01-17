<template>
  <ion-content class="ion-padding">
    <ion-grid>
      <ion-row class="ion-justify-content-center">
        <img :src="require('../images/nets.png')" />
      </ion-row>

      <ion-row class="ion-justify-content-center">
        <icon-col size="9" class="pageHeader"> Login </icon-col>
      </ion-row>

      <ion-item fill="solid" ref="item" class="paddingTop">
        <!-- <ion-input :clearInput="true" placeholder="Username:" type="email" @ionInput="validate"></ion-input> -->
        <ion-input :clearInput="true" placeholder="Username:" type="email"></ion-input>
        <ion-note slot="error">Invalid email</ion-note>
      </ion-item>

      <ion-item>
        <ion-input :clearInput="true" type="password" placeholder="Password:"></ion-input>
      </ion-item>

      <ion-row class="ion-padding-top ">
        <ion-col>
          <div class="myLine ion-justify-content-center">
            <ion-item lines="none">
              <ion-checkbox></ion-checkbox>
              <ion-label> Remember me</ion-label>
            </ion-item>
            <div float-right class="myLine2">Forgot password</div>
          </div>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top">
        <ion-col>
          <div class="ion-text-center">New User? Sign up now!</div>
        </ion-col>
      </ion-row>

      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" routerLink="/tabs/">Login</ion-button>
      </ion-row>
    </ion-grid>
  </ion-content>
</template>

<script lang="ts">
import { IonRow, IonInput, IonItem, IonButton, IonCheckbox, IonLabel, IonNote } from "@ionic/vue"; // IonCol, IonList
import { Method } from "ionicons/dist/types/stencil-public-runtime";
import { defineComponent } from "vue";

export default defineComponent({
  components: { IonRow, IonInput, IonItem, IonButton, IonCheckbox,IonLabel, IonNote  }, //IonCol, IonList
  // methods:{
  //   validateEmail(email: string) {
  //       return email.match(/^(?=.{1,254}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/);
  //     },

  //     validate(ev: { target: { value: any; }; }) {
  //       const value = ev.target.value;

  //       this.$refs.item.$el.classList.remove('ion-valid');
  //       this.$refs.item.$el.classList.remove('ion-invalid');

  //       if (value === '') return;

  //       this.validateEmail(value)
  //         ? this.$refs.item.$el.classList.add('ion-valid')
  //         : this.$refs.item.$el.classList.add('ion-invalid');
  //     },

  //     markTouched() {
  //       this.$refs.item.$el.classList.add('ion-touched')
  //     }
  // }
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
