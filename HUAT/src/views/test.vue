<template>
  <ion-page class="ion-padding">
    <ion-header collapse="condense">
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/tabs/home"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">My Bookings</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-searchbar></ion-searchbar>
      <ion-card v-for="eachBooking in bookingDetails" :key="eachBooking">
        <img src="/assets/images/ion.jpg" />
        <ion-grid>
          <ion-card-header>
            <ion-row>
              <ion-col>
                <ion-card-subtitle>Booking Ref: {{ eachBooking.bookingID }}</ion-card-subtitle>
              </ion-col>
            </ion-row>
             <!-- bookingDate: eachBooking.bookingDate,
              bookingID: eachBooking.bookingID,
              bookingLocation: eachBooking.bookingLocation -->
            <ion-row>
              <ion-col>
                <ion-card-subtitle>Start Date: {{ eachBooking.bookingDate }}</ion-card-subtitle>
                <br />
                <ion-card-subtitle>End Date: 18/01/2023</ion-card-subtitle>
              </ion-col>
              <ion-col>
                <ion-card-subtitle>Start Time: 12:00</ion-card-subtitle>
                <br />
                <ion-card-subtitle>End Time: 13:00</ion-card-subtitle>
              </ion-col>
              <ion-col>
                <ion-item lines="none">
                  <ion-badge color="success" slot="end">Upcoming</ion-badge>
                </ion-item>
              </ion-col>
            </ion-row>
            <ion-row>
              <ion-col>
                <ion-card-title>Ion Orchard</ion-card-title>
                <ion-card-subtitle>{{ eachBooking.bookingLocation  }}</ion-card-subtitle>
              </ion-col>
              <ion-col>
                <ion-item lines="none">
                  <ion-button fill="outline" slot="end">Directions</ion-button>
                </ion-item>
              </ion-col>
            </ion-row>
          </ion-card-header>
        </ion-grid>
      </ion-card>
      <!-- <ion-card>
        <img src="/assets/images/wisma.jpeg" />
        <ion-grid>
          <ion-card-header>
            <ion-row>
              <ion-col>
                <ion-card-subtitle>Booking Ref: IS8RFD2984</ion-card-subtitle>
              </ion-col>
            </ion-row>
            <ion-row>
              <ion-col>
                <ion-card-subtitle>Start Date: 15/01/2023</ion-card-subtitle>
                <br />
                <ion-card-subtitle>End Date: 15/01/2023</ion-card-subtitle>
              </ion-col>
              <ion-col>
                <ion-card-subtitle>Start Time: 12:00</ion-card-subtitle>
                <br />
                <ion-card-subtitle>End Time: 15:00</ion-card-subtitle>
              </ion-col>
              <ion-col>
                <ion-item lines="none">
                  <ion-badge color="dark" slot="end">Ended</ion-badge>
                </ion-item>
              </ion-col>
            </ion-row>
            <ion-row>
              <ion-col>
                <ion-card-title>Wisma Atria</ion-card-title>
                <ion-card-subtitle>Carpark 4A 478</ion-card-subtitle>
              </ion-col>
              <ion-col>
                <ion-item lines="none">
                  <ion-button fill="outline" disabled slot="end"
                    >Directions</ion-button
                  >
                </ion-item>
              </ion-col>
            </ion-row>
          </ion-card-header>
        </ion-grid>
      </ion-card> -->
    </ion-content>
  </ion-page>
</template>
<!-- <ion-content class="ion-padding"></ion-content> -->

<script>
import {
  IonCard,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonSearchbar,
  IonButton,
  IonButtons,
  IonBackButton,
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { arrowBack, home, star } from "ionicons/icons";
import axios from 'axios';

export default defineComponent({
  components: {
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonSearchbar,
    IonButton,
    IonBackButton,
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
  },
  data() {
    return {
      bookingDetails: []
      // passwordErrors: Array<string>(),
    }
  },
  methods: {
    getAllBookings() {
      const url = "http://127.0.0.1:5001/bookings"; // hardcoded
      axios
        .get(url)
        .then((response) => {
          console.log(response.data.data.bookings)
          const data = response.data.data.bookings
          for (const eachBooking of data) {
            console.log(eachBooking)
            this.bookingDetails.push({
              bookingDate: eachBooking.bookingDate,
              bookingID: eachBooking.bookingID,
              bookingLocation: eachBooking.bookingLocation
            })
            
          }
          console.log(this.bookingDetails)
          // for (let i = 0; i < data.length; i++) {
          //   console.log(data[i])
          //   this.bookingDetails[i] = 
          // }
        })
        .catch((error) => {
          console.log(error.message);
        });
    }
  },

  mounted() {
    this.getAllBookings()
  }

});
</script>

<style scoped>
/* iOS places the subtitle above the title */

ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
}

ion-img::part(image) {
  width: 100%;
  /* or whatever value */
  /* you can set the height value too */
}
</style>
