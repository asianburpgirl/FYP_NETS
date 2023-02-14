<template>
    <base-layout>
        <ion-page>
            <ion-header>
                <ion-toolbar>
                    <ion-title class="ion-text-center">My Wallet</ion-title>
                </ion-toolbar>
            </ion-header>
    
            <ion-content class="ion-padding">
                <div class="ion-text-center">
                    <h1>Amount</h1>
                    <ion-card>
                        <ion-grid>
                            <ion-row>
                                <ion-col>
                                    <ion-button color="dark">
                                        <ion-icon :icon="add" />
                                    </ion-button>
                                    <p>Pay</p>
                                </ion-col>
                                <ion-col>
                                    <ion-button color="dark">
                                        <ion-icon :icon="wallet" />
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
            </ion-content>
        </ion-page>
    </base-layout>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton } from '@ionic/vue';
import { defineComponent } from 'vue';
import { add, card, home, star, wallet } from 'ionicons/icons';

// export default defineComponent({
//     components: { IonPage, IonContent, IonHeader, IonTitle, IonToolbar, IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton },
// });
export default defineComponent({
  data() {
      return {
          stripe: null,
      }
  },
  methods: {
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
      }
  }
})
</script>

<style>
h1 {
    font-size: 50px;
}
</style>

