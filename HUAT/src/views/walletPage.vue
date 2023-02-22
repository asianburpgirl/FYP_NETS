<template>
  <base-layout pageTitle="My Wallet" needToolBar="y">
    <div class="ion-text-center">
      <h2>Amount</h2>
      <h1>${{ balance }}</h1>
      <ion-card>
        <ion-grid>
          <ion-row>
            <!-- <ion-col>
              <ion-button color="dark">
                <ion-icon :icon="addOutline" > </ion-icon>
              </ion-button>
              <p>Pay</p>
            </ion-col> -->
            <ion-col>
              <ion-button color="dark" @click='routeUser("payment")'>
                 <ion-icon :icon="wallet" > </ion-icon>
              </ion-button>
              <p>Top Up</p>
            </ion-col>
            <ion-col>
              <ion-button color="dark">
                <ion-icon :icon="card" />
              </ion-button>
              <p>Card</p>
            </ion-col>
          </ion-row>
          <ion-row>
            <!-- <ion-col>
              <ion-button color="dark">
                <ion-icon :icon="addOutline" > </ion-icon>
              </ion-button>
              <p>Pay</p>
            </ion-col> -->
            <ion-col>
              <ion-button color="dark">
                $10
              </ion-button>
            </ion-col>
            <ion-col>
              <ion-button color="dark">
                $20
              </ion-button>
            </ion-col>
            <ion-col>
              <ion-button color="dark">
                $30
              </ion-button>
            </ion-col>
          </ion-row>
        </ion-grid>
      </ion-card>
      <ion-list lines="none">
        <ion-list-header align="left">
          <ion-label>Transaction History</ion-label>
        </ion-list-header>
        <ion-item>
          <ion-label>Top Up Account</ion-label>
          <ion-label align="end">$5</ion-label>
        </ion-item>
        <ion-item>
          <ion-label>Top Up Account</ion-label>
          <ion-label align="end">$20</ion-label>
        </ion-item>
        <ion-item>
          <ion-label>Top Up Account</ion-label>
          <ion-label align="end">$25</ion-label>
        </ion-item>
      </ion-list>
    </div>
  </base-layout>
</template>

<script>
import { IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton } from '@ionic/vue';
import { defineComponent } from 'vue';
import { card, wallet } from 'ionicons/icons';
import axios from "axios";

export default defineComponent({
    components: { IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton},
  setup() {
    return { card,wallet };
  },
  data() {
    return {
      stripe: null,
      balance: 0,
      userData: {}
    }
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
    },
    getBalance() {
      const url = "http://localhost:5002/getBalance/" + this.userData.userID;
      axios.get(url)
      .then((response) => {
        // console.log(response)
        this.balance = response.data.data.balance
      })
      .catch((error) => {
        console.log(error.message);
      });
    },
    routeUser(route) {
      this.$router.push({
        path: '/' + route,
      });
    },
  },
  mounted(){
    this.loadUserData(),
    this.getBalance()
  }
})
</script>

<style>
h1 {
  font-size: 50px;
}
</style>