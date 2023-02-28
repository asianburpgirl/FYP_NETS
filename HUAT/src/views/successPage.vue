<template>
  <ion-page class="ion-padding">
    <ion-content class="ion-padding">
      <p>Payment has been made. Thank you</p>
      <ion-button color="primary" routerLink="/tabs/wallet" routerDirection="forward">Back to Wallet</ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import { 
  IonButton
} from '@ionic/vue';
import { defineComponent } from 'vue'
  
export default defineComponent({
  components: { 
    IonButton
  },
  data() {
    return {
      userData: {},
    }
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
    }
  },
  mounted() {
    this.loadUserData()
  }
});
</script>