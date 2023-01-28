<template>
    <base-layout>
        <ion-page>
            <ion-header>
                <ion-toolbar>
                    <ion-title class="ion-text-left">Edit Profile</ion-title>
                </ion-toolbar>
            </ion-header>
    
            
                    <ion-list lines="none">
                        <ion-list-header align="left">
                            <ion-label>Enter your updated particulars and hit on the save button</ion-label>
                        </ion-list-header>
                        <ion-item>
                            <ion-label position="stacked">Email</ion-label>
                            <ion-input :clear-input="true" placeholder="Enter new Email"></ion-input>
                            </ion-item>

                            <ion-item>
                            <ion-label position="stacked">Phone Number</ion-label>
                            <ion-input :clear-on-edit="true" placeholder="Enter new phone number"></ion-input>
                            </ion-item>

                            <ion-item>
                            <ion-label position="stacked">Password</ion-label>
                            <ion-input type="password" placeholder="Enter new password"></ion-input>
                            </ion-item>
                    </ion-list>

                    <ion-content class="ion-padding">
                <div class="ion-text-center">
                    <h1></h1>
                    <ion-card>
                        <ion-grid>
                            <ion-row>
                                <ion-col>
                                    <!-- <ion-button color="dark">
                                        <ion-icon :icon="add" />
                                    </ion-button> -->
                                    <!-- <p>Pay</p> -->
                                </ion-col>
                                <ion-col>
                                    <ion-button color="dark">
                                        <ion-icon :icon="wallet" />
                                    </ion-button>
                                    <p>Save</p>
                                </ion-col>
                                <ion-col>
                                    <!-- <ion-button color="dark">
                                        <ion-icon :icon="card" />
                                    </ion-button>
                                    <p>Card</p> -->
                                </ion-col>
                            </ion-row>
                        </ion-grid>
                    </ion-card>
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

