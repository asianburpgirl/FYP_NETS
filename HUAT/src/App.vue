<template>
  <ion-page>
    <ion-app>
      <ion-router-outlet></ion-router-outlet>
    </ion-app>
  </ion-page>
</template>

<script lang="ts">
import { IonApp, IonPage, IonRouterOutlet } from '@ionic/vue';

import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonApp, IonPage, IonRouterOutlet
  },

});
</script>
