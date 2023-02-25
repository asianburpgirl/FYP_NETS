<template>
    <base-layout>
        <ion-page>
            <ion-header>
                <ion-toolbar>
                    <ion-title class="ion-text-center">Edit Profile</ion-title>
                </ion-toolbar>
            </ion-header>
            <ion-content class="ion-padding">
                <ion-list lines="none">
                    <ion-item>
                        <ion-label position="stacked">Email</ion-label>
                        <ion-input :clear-input="true" placeholder="Enter new email"></ion-input>
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
                    <div class="ion-text-center ion-padding-top">
                        <ion-button shape="round" expand="block">
                            Save
                        </ion-button>
                    </div>
                </ion-content>
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

<style scoped>
h1 {
    font-size: 50px;
}
</style>

