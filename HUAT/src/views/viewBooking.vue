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

              <ion-card-subtitle v-if="eachBooking.status == 'Booked'"
                >Booking Amount: $
                {{ eachBooking.amount }}
              </ion-card-subtitle>
              <ion-card-subtitle v-if="eachBooking.status == 'Cancelled'"
                >Refunded Amount: $
                {{ eachBooking.amount }}
              </ion-card-subtitle>

              <ion-row class="ion-padding-top ion-justify-content-center">
                <ion-button
                  shape="round"
                  @click="editBooking()"
                  v-if="eachBooking.status == 'Booked'"
                  >Edit</ion-button
                >
              </ion-row>

              <ion-row class="ion-padding-top ion-justify-content-center">
                <ion-button
                  v-if="eachBooking.status == 'Booked'"
                  shape="round"
                  @click="
                    presentAlert(eachBooking.bookingID, eachBooking.amount)
                  "
                  color="danger"
                  >Cancel</ion-button
                >
              </ion-row>

              <ion-row class="ion-padding-top ion-justify-content-center">
                <ion-button v-if="eachBooking.status == 'Cancelled'" shape="round" @click="deleteBooking(eachBooking.bookingID)"  color="light">Delete</ion-button>
              </ion-row>

            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col>
              <ion-card-subtitle
                >Start Date: {{ eachBooking.startDate }}</ion-card-subtitle
              >
              <br />

              <ion-card-subtitle
                >End Date: {{ eachBooking.endDate }}</ion-card-subtitle
              >
            </ion-col>
            <ion-col>
              <ion-card-subtitle
                >Start Time: {{ eachBooking.startTime }}</ion-card-subtitle
              >
              <br />
              <ion-card-subtitle
                >End Time:{{ eachBooking.endTime }}</ion-card-subtitle
              >
            </ion-col>
            <ion-col>
              <ion-item lines="none">
                <ion-badge
                  v-if="eachBooking.status == 'Booked'"
                  color="success"
                  slot="end"
                  >{{ eachBooking.status }}</ion-badge
                >
                <ion-badge
                  v-if="eachBooking.status == 'Cancelled'"
                  color="medium"
                  slot="end"
                  >{{ eachBooking.status }}</ion-badge
                >
              </ion-item>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col>
              <ion-card-title>{{ eachBooking.bookingLocation }}</ion-card-title>
              <!-- <ion-card-subtitle>{{
                eachBooking.locationName
              }}</ion-card-subtitle> -->
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
  IonBadge,
  IonButton,
  alertController,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";

import axios from "axios";

export default defineComponent({
  components: {
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonSearchbar,
    IonBadge,
    IonButton,
  },

  setup() {
    const handlerMessage = ref("");
    const presentAlert = async (bookingID, amount) => {
      const alert = await alertController.create({
        header: "Are you sure you want to delete this booking? ",
        subHeader: "$" + amount + " will be refunded back to your account",
        buttons: [
          {
            text: "Cancel",
            cssClass: "alert-button-cancel",
            role: "cancel",
            handler: () => {
              handlerMessage.value = "Alert canceled";
            },
          },
          {
            text: "Yes",
            cssClass: "alert-button-confirm",
            role: "confirm",
            handler: () => {
              handlerMessage.value = "Alert confirmed";
              // remove booking from db
              // const url = "http://127.0.0.1:5001/bookings/"+bookingID;
              // axios
              //   .delete(url)
              //   .then((response) => {
              //     console.log(response);
              //     location.reload();
              //   })
              //   .catch((error) => {
              //     console.log(error.message);
              //   });

              // update booking status to "cancel"
              let url = "http://127.0.0.1:5001/bookings/" + bookingID;
              axios
                .put(url, {
                  status: "Cancelled",
                })
                .then((response) => {
                  console.log(response);
                  url = "http://127.0.0.1:5001/updateBalance/" + bookingID;
                  axios
                    .put(url, {
                      bookingID: bookingID,
                    })
                    .then((response) => {
                      console.log(response);
                      location.reload();
                    })
                    .catch((error) => {
                      console.log(error.message);
                    });
                })
                .catch((error) => {
                  console.log(error.message);
                });

              //refund money
              //http://127.0.0.1:5001/updateBalance/
            },
          },
        ],
      });

      await alert.present();
      const { role } = await alert.onDidDismiss();
    };
    return {
      presentAlert,
    };
  },

  data() {
    return {
      bookingDetails: [],
      userData: {},
    };
  },
  methods: {
    deleteBooking(bookingID) {
      const url = "http://127.0.0.1:5001/bookings/" + bookingID;
      axios
        .delete(url)
        .then((response) => {
          console.log(response);
          location.reload();
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getUserBooking() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
      const url = "http://127.0.0.1:5001/bookings/" + this.userData.userID;
      axios
        .get(url)
        .then((response) => {
          const data = response.data.data.bookings;
          for (const eachBooking of data) {
            const startDateTime = new Date(eachBooking.bookingStartDateTime);
            const startDateOnly =
              startDateTime.getDate() +
              "/" +
              startDateTime.getMonth() +
              1 +
              "/" +
              startDateTime.getFullYear();
            const startTimeOnly =
              startDateTime.getHours() -
              8 +
              ":" +
              ("0" + startDateTime.getMinutes()).slice(-2);

            const endDateTime = new Date(eachBooking.bookingEndDateTime);
            const endDateOnly =
              endDateTime.getDate() +
              "/" +
              endDateTime.getMonth() +
              1 +
              "/" +
              endDateTime.getFullYear();

            const endTimeOnly =
              ("0" + (endDateTime.getHours() - 8).toString()).slice(-2) +
              ":" +
              ("0" + endDateTime.getMinutes()).slice(-2);

            this.bookingDetails.push({
              bookingDate: eachBooking.bookingDate,
              bookingID: eachBooking.bookingID,
              bookingLocation: eachBooking.bookingLocation,
              locationName: eachBooking.locationName,
              startDate: startDateOnly,
              startTime: startTimeOnly,
              endDate: endDateOnly,
              amount: eachBooking.bookingAmt,
              endTime: endTimeOnly,
              status: eachBooking.status,
              bookingRef: eachBooking.bookingRef,
              userID: eachBooking.userID,
            });
          }
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },

  mounted() {
    this.getUserBooking();
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

button.alert-button.alert-button-confirm {
  background-color: var(--ion-color-success);
  color: var(--ion-color-success-contrast);
}

.md button.alert-button.alert-button-confirm {
  border-radius: 4px;
}

.ios button.alert-button.alert-button-confirm {
  border-bottom-right-radius: 13px;
  border-top-right-radius: 13px;
}

.ios button.alert-button.alert-button-cancel {
  border-right: 0;
  border-bottom-left-radius: 13px;
  border-top-left-radius: 13px;
}
</style>
