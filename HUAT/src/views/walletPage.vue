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
              <ion-button color="dark">
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
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton } from '@ionic/vue';
import { defineComponent } from 'vue';
import { add, card, home, star, wallet } from 'ionicons/icons';
import axios from "axios";

export default defineComponent({
    components: { IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton },
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
        getBalance() {
        this.userData = JSON.parse(localStorage.getItem("userData"));
        
        const url = "http://127.0.0.1:5002/getBalance/" + this.userData.userID;
        axios
            .get(url)
            .then((response) => {
            this.balance = response.data.data.balance
            })
            .catch((error) => {
            console.log(error.message);
            });
        },
      purchaseBook() {
        fetch('http://localhost:4242/create-payment-intent', {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          
          body: JSON.stringify({ item:123 }),
        })
        .then((result) => result.json())
        .then((data) => {
          // Redirect to Stripe Checkout
          return this.stripe.redirectToCheckout({ sessionId: 123 });
        })
        .then((res) => {
          console.log(res);
        });
      },
      getStripePublishableKey() {
          fetch('http://localhost:4242/config')
          .then((result) => result.json())
          .then((data) => {
              // Initialize Stripe.js
              this.stripe = Stripe(data.publicKey); // eslint-disable-line no-undef
          });
      },
      created() {
          this.getStripePublishableKey();
      },
      mounted(){
        const recaptchaScript = document.createElement('script')
        recaptchaScript.setAttribute('src', 'https://js.stripe.com/v3/')
        document.head.appendChild(recaptchaScript)
        this.getBalance();
      }
  }
})

</script>

<style>
h1 {
  font-size: 50px;
}
</style>

