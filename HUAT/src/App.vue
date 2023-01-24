<template>
  <ion-page>
    <ion-app>
      <ion-router-outlet></ion-router-outlet>
    </ion-app>
  </ion-page>
</template>

<script setup lang="ts">
import { IonApp,IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
import { albums, card, ellipse, home, map, person, square, triangle } from 'ionicons/icons';
</script>
