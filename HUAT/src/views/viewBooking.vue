<template>
  <base-layout
    pageTitle="My Bookings"
    needBackButton="y"
    pageToGoBack="/tabs/profile"
    needToolBar="y"
  >
    <ion-searchbar></ion-searchbar>
    <ion-card v-for="eachBooking in bookingDetails" :key="eachBooking">
      <img src="/assets/images/ion.jpg" />
      <ion-grid>
        <ion-card-header>
          <ion-row>
            <ion-col>
              <ion-card-subtitle
                >Booking Ref:<u>
                  {{ eachBooking.bookingRef }}
                </u></ion-card-subtitle
              >
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col>
              <ion-card-subtitle
                >Start Date: {{ eachBooking.startDate }}</ion-card-subtitle
              >
              <br />
     
              <ion-card-subtitle>End Date: {{ eachBooking.endDate }}</ion-card-subtitle>
            </ion-col>
            <ion-col>
              <ion-card-subtitle
                >Start Time: {{ eachBooking.startTime }}</ion-card-subtitle
              >
              <br />
              <ion-card-subtitle>End Time:{{ eachBooking.endTime }}</ion-card-subtitle>
            </ion-col>
            <ion-col>
              <ion-item lines="none">
                <ion-badge color="success" slot="end">{{
                  eachBooking.status
                }}</ion-badge>
              </ion-item>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col>
              <ion-card-title>{{ eachBooking.bookingLocation }}</ion-card-title>
              <ion-card-subtitle>{{
                eachBooking.locationName
              }}</ion-card-subtitle>
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
  </base-layout>
</template>

<script>
import {
  IonCard,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonSearchbar,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { arrowBack, home, star } from "ionicons/icons";
import axios from "axios";

export default defineComponent({
  components: {
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonSearchbar,
  },
  data() {
    return {
      bookingDetails: [],
      // passwordErrors: Array<string>(),
    };
  },
  methods: {
    getAllBookings() {
      const url = "http://127.0.0.1:5001/bookings"; // hardcoded
      axios
        .get(url)
        .then((response) => {
          const data = response.data.data.bookings;
          for (const eachBooking of data) {
            const startDateTime = new Date(eachBooking.startTime);
            const startDateOnly =
              startDateTime.getDate() +
              "/" +
              startDateTime.getMonth() +
              1 +
              "/" +
              startDateTime.getFullYear();
            const startTimeOnly =
              startDateTime.getHours() + ":" + startDateTime.getMinutes();

            const endDateTime = new Date(eachBooking.endTime);
            const endDateOnly =
              endDateTime.getDate() +
              "/" +
              endDateTime.getMonth() +
              1 +
              "/" +
              endDateTime.getFullYear();

            const endTimeOnly =
              endDateTime.getHours() + ":" + endDateTime.getMinutes();

            this.bookingDetails.push({
              bookingDate: eachBooking.bookingDate,
              bookingID: eachBooking.bookingID,
              bookingLocation: eachBooking.bookingLocation,
              locationName: eachBooking.locationName,
              startDate: startDateOnly,
              startTime: startTimeOnly,
              endDate: endDateOnly,
              endTime: endTimeOnly,
              status: eachBooking.status,
              bookingRef: eachBooking.bookingRef,
              image: eachBooking.image,
              maxCapacity: eachBooking.maxCapacity,
              currentCapacity: eachBooking.currentCapacity,
              // image: eachBooking.image,
              userID: eachBooking.userID,
            });
          }
          // console.log(this.bookingDetails);
          // for (let i = 0; i < data.length; i++) {
          //   console.log(data[i])
          //   this.bookingDetails[i] =
          // }
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },

  mounted() {
    this.getAllBookings();
  },
});
</script>

<style scoped>
/* iOS places the subtitle above the title */

ion-card-header {
  display: flex;
  flex-flow: column-reverse;
}

ion-img::part(image) {
  width: 100%;
  /* or whatever value */
  /* you can set the height value too */
}
</style>
