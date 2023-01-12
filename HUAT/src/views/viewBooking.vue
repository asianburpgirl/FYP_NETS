<template>
    <ion-page>
      <ion-content>
        <ion-header>
          <ion-toolbar>
            <ion-title size="large" class="ion-text-center">My Bookings</ion-title>
          </ion-toolbar>
        </ion-header>
        <ion-searchbar></ion-searchbar>
        <ion-card>
            <ion-img src="assets/images/ion.jpg"></ion-img>
            <ion-grid>
                <ion-card-header>
                    <ion-row>
                        <ion-col>
                            <ion-card-subtitle>Start Date: 12/02/2023</ion-card-subtitle>  
                            <br>
                            <ion-card-subtitle>Start Time: 13:00</ion-card-subtitle>  
                            
                        </ion-col>
                        <ion-col>
                            <ion-card-subtitle>End Date: 12/02/2023</ion-card-subtitle>  
                            <br>
                            <ion-card-subtitle>End Time: 15:00</ion-card-subtitle>  
                        </ion-col>
                    </ion-row>
                    <ion-row>
                        <ion-col>
                            <ion-card-title>Ion Orchard</ion-card-title>
                            <ion-card-subtitle>Carpark 4A 478</ion-card-subtitle>                       
                        </ion-col>
                        <ion-item lines="none">
                                <ion-button fill="outline" slot="end">View</ion-button>
                        </ion-item>
                    </ion-row>
                </ion-card-header>
            </ion-grid>
        </ion-card>
        <ion-card>
            <ion-img src="assets/images/wisma.jpeg"></ion-img>
            <ion-grid>
                <ion-card-header>
                    <ion-row>
                        <ion-col>
                            <ion-card-subtitle>Start Date: 12/02/2023</ion-card-subtitle>  
                            <br>
                            <ion-card-subtitle>Start Time: 13:00</ion-card-subtitle>  
                            
                        </ion-col>
                        <ion-col>
                            <ion-card-subtitle>End Date: 12/02/2023</ion-card-subtitle>  
                            <br>
                            <ion-card-subtitle>End Time: 15:00</ion-card-subtitle>  
                        </ion-col>
                    </ion-row>
                    <ion-row>
                        <ion-col>
                            <ion-card-title>Wisma Atria</ion-card-title>
                            <ion-card-subtitle>Carpark 4A 478</ion-card-subtitle>                       
                        </ion-col>
                        <ion-item lines="none">
                                <ion-button fill="outline" slot="end">View</ion-button>
                        </ion-item>
                    </ion-row>
                </ion-card-header>
            </ion-grid>
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