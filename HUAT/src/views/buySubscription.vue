<template>
    <ion-page>
        <ion-content>
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-buttons slot="start">
                        <ion-back-button default-href="/tabs/home"></ion-back-button>
                    </ion-buttons>
                    <ion-title>Buy Subscription</ion-title>
                </ion-toolbar>
            </ion-header>
            <ion-card>
                <ion-grid>
                    <ion-card-header>
                        <ion-card-title>Premium Plan</ion-card-title>
                        <ion-card-subtitle>Free 2 hour parking</ion-card-subtitle>
                        <ion-card-subtitle>Free parking once a month</ion-card-subtitle>
                        <ion-card-subtitle>Pay parking fees at the end of the month</ion-card-subtitle>

                        <br>
                        <ion-card-subtitle color="danger">*No refund after buying</ion-card-subtitle>
                        <br>
                        <ion-item lines="none">
                            <ion-button slot="end" color="success" size="large" expand="block" href="/buySubscription">Buy</ion-button>
                        </ion-item>
                    </ion-card-header>
                </ion-grid>
            </ion-card>
        </ion-content>
    </ion-page>
</template>
  <!-- <ion-content class="ion-padding"></ion-content> -->
  
<script lang="ts">
import { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle, IonButton, IonButtons, IonIcon, IonBackButton } from '@ionic/vue';
import { defineComponent } from 'vue';
// import { arrowBack, home, star } from 'ionicons/icons';

export default defineComponent({
    components: { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle, IonButton, IonButtons, IonBackButton },
});
</script>
  
<style scoped>
/* iOS places the subtitle above the title */

ion-card-header.ios {
    display: flex;
    flex-flow: column-reverse;
}
</style>
