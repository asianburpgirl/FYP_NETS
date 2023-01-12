  <template>
    <ion-page>
      <ion-content>
        <ion-header>
          <ion-toolbar>
            <ion-title size="large" class="ion-text-center">Nearby Me</ion-title>
          </ion-toolbar>
        </ion-header>
        <ion-searchbar></ion-searchbar>
        <ion-card>
          <ion-img src="assets/images/ion.jpg"></ion-img>
            <ion-card-header>
              <ion-card-title>Ion Orchard</ion-card-title>
              <ion-card-subtitle>400 lots Left</ion-card-subtitle>
            </ion-card-header>
        </ion-card>
        <ion-card>
          <ion-img src="assets/images/wisma.jpeg"></ion-img>
            <ion-card-header>
              <ion-card-title>Wisma atria</ion-card-title>
              <ion-card-subtitle>230 lots Left</ion-card-subtitle>
            </ion-card-header>
        </ion-card>
      </ion-content>
    </ion-page>
  </template>
  <ion-content class="ion-padding"></ion-content>
  
  <script lang="ts">
    import { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle, IonSearchbar} from '@ionic/vue';
    import { defineComponent } from 'vue';
  
    export default defineComponent({
      components: { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle, IonSearchbar },
    });
  </script>
  
  <style scoped>
    /* iOS places the subtitle above the title */
    ion-card-header.ios {
      display: flex;
      flex-flow: column-reverse;
    }
    ion-img::part(image) {
      width: 100%; /* or whatever value */
      /* you can set the height value too */
    }
  </style>