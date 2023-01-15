<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Home</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true">
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-title size="large">Welcome, John Tan</ion-title>
                </ion-toolbar>
            </ion-header>
            <!-- <ExploreContainer name="Tab 1 page" />  -->
            <ion-grid>
                <ion-row>
                    <ion-col>
                        <ion-button expand="block">Subscription Plans</ion-button>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <ion-button expand="block">Find me a carpark</ion-button>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <ion-button expand="block" href="/tabs/viewBooking">My Bookings</ion-button>
                    </ion-col>
                </ion-row>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>

<style scoped>

</style>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import { person } from 'ionicons/icons';
// import ExploreContainer from '@components/ExploreContainer.vue';
</script>

