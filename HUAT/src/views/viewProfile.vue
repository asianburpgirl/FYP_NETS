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

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton } from '@ionic/vue';
import { defineComponent } from 'vue';
import { add, card, home, star, wallet } from 'ionicons/icons';

// export default defineComponent({
//     components: { IonPage, IonContent, IonHeader, IonTitle, IonToolbar, IonGrid, IonCard, IonIcon, IonRow, IonCol, IonButton },
// });
</script>

<style>
h1 {
    font-size: 50px;
}
</style>

