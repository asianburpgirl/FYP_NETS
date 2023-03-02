<template>
  <base-layout pageTitle="Bookings" needToolBar="y">
    <ion-row>
      <ion-col>
        <ion-button expand="block" size="large" @click="routeUser('nearbyMe')"
          >View Carparks</ion-button
        >
      </ion-col>
      <ion-col>
        <ion-button expand="block" size="large" @click="routeUser('map')"
          >Book by Map</ion-button
        >
      </ion-col>
    </ion-row>

    <ion-modal :is-open="editBookingOpen">
      <ion-header>
        <ion-toolbar>
          <ion-title class="ion-text-center"> Edit Booking</ion-title>

          <ion-buttons slot="start">
            <ion-button @click="setEditBookingOpen(false)">
              <ion-icon :icon="arrowBackOutline"></ion-icon>
            </ion-button>
          </ion-buttons>
        </ion-toolbar>
      </ion-header>

      <ion-content class="ion-padding-top">
        <ion-item>
          <ion-label position="stacked">
            Booking Date: {{ bookingInfo.startDate }}</ion-label
          >
          <ion-datetime
            presentation="date"
            v-model="newDate"
            v-if="editDate == true"
          ></ion-datetime>
          <ion-button
            shape="round"
            @click="editDate = true"
            v-if="editDate == false"
            >Edit Booking Date</ion-button
          >
          <ion-button
            shape="round"
            @click="editDate = true"
            v-if="editDate == true"
            color="danger"
            >Cancel</ion-button
          >

          <ion-label position="stacked">
            Start Time: {{ bookingInfo.startTime }}</ion-label
          >
          <ion-datetime
            presentation="time"
            v-model="newStartTime"
            v-if="editStartTime == true"
          ></ion-datetime>
          <ion-button
            shape="round"
            @click="editStartTime = true"
            v-if="editStartTime == false"
            >Edit Start Time</ion-button
          >
          <ion-button
            shape="round"
            @click="editDate = true"
            v-if="editStartTime == true"
            color="danger"
            >Cancel</ion-button
          >

          <ion-label position="stacked">
            End Time: {{ bookingInfo.endTime }}</ion-label
          >
          <ion-datetime
            presentation="time"
            v-model="newEndTime"
            v-if="editEndTime == true"
          ></ion-datetime>
          <ion-button
            shape="round"
            @click="editEndTime = true"
            v-if="editEndTime == false"
            >Edit End Time</ion-button
          >
          <ion-button
            shape="round"
            @click="editDate = true"
            v-if="editEndTime == true"
            color="danger"
            >Cancel</ion-button
          >
        </ion-item>

        <ion-row
          class="ion-padding-top ion-justify-content-center addPaddingBottom"
        >
          <ion-button @click="saveEditBooking()"> Save </ion-button>
        </ion-row>
      </ion-content>
    </ion-modal>
    <ion-card v-for="eachBooking in bookingDetails" :key="eachBooking">
      <ion-img :src="eachBooking.imagePath"></ion-img>
      <ion-card-header>
        <ion-list lines="none">
          <ion-item>
            <ion-badge
              v-if="eachBooking.status == 'Booked'"
              color="success"
              slot="end"
              >Booked</ion-badge
            >
            <ion-badge
              v-if="eachBooking.status == 'Cancelled'"
              color="success"
              slot="end"
              >Cancelled</ion-badge
            >
            <ion-card-title>{{ eachBooking.bookingLocation }}</ion-card-title>
          </ion-item>
        </ion-list>
      </ion-card-header>

      <ion-card-content>
        <div class="ion-padding">
          <!-- <ion-list lines="full">
            <ion-item>
              <ion-badge
                v-if="eachBooking.status == 'Booked'"
                color="success"
                slot="end"
                >Booked</ion-badge
              >
              <ion-badge
                v-if="eachBooking.status == 'Cancelled'"
                color="success"
                slot="end"
                >Cancelled</ion-badge
              >
              <ion-button size="small" fill="outline" slot="start"
                >Directions</ion-button
              >
            </ion-item>
          </ion-list> -->
          <ion-button size="small" fill="outline" slot="start"
            >Directions</ion-button
          >
          <div class="ion-padding-top"> 
            <ion-card-subtitle
            >Booking Ref: <u>{{ eachBooking.bookingRef }}</u></ion-card-subtitle
          >
          <ion-card-subtitle v-if="eachBooking.status == 'Booked'"
            >Booking Amount: ${{ eachBooking.amount }}</ion-card-subtitle
          >
          <ion-card-subtitle v-if="eachBooking.status == 'Cancelled'"
            >Refunded Amount: $ {{ eachBooking.amount }}</ion-card-subtitle
          >
          <ion-card-subtitle
            ><b>Start Date: {{ eachBooking.startDate }}</b></ion-card-subtitle
          >
          <ion-card-subtitle
            ><b>End Date: {{ eachBooking.endDate }}</b></ion-card-subtitle
          >
          <ion-card-subtitle
            ><b>Start Time: {{ eachBooking.startTime }}</b></ion-card-subtitle
          >
          <ion-card-subtitle
            ><b>End Time:{{ eachBooking.endTime }}</b></ion-card-subtitle
          >
          </div>
        </div>
        <div class="ion-padding">
          <ion-row>
            <ion-col md="6" v-if="eachBooking.status == 'Booked'">
              <ion-button
                expand="block"
                @click="editBooking(eachBooking)"
                >Edit</ion-button
              >
            </ion-col>
            <ion-col md="6" v-if="eachBooking.status == 'Booked'">
              <ion-button
                expand="block"
                @click="
                  confirmationAlert(eachBooking.bookingID, eachBooking.amount)
                "
                color="danger"
                >Cancel</ion-button
              >
            </ion-col>
            <ion-col md="6" v-if="eachBooking.status == 'Cancelled'">
              <ion-button
                @click="deleteBooking(eachBooking.bookingID)"
                color="light"
                >Delete</ion-button
              >
            </ion-col>
          </ion-row>
      </div>
      </ion-card-content>
    </ion-card>
  </base-layout>
</template>

<script>
import { arrowBackOutline } from "ionicons/icons";
import {
  IonHeader,
  IonContent,
  IonCard,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  // IonBadge,
  IonButton,
  alertController,
  IonModal,
  IonToolbar,
  IonTitle,
  IonIcon,
  IonButtons,
  IonLabel,
  IonDatetime,
  IonItem,
  IonRow,
  IonCol,
  IonImg,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonHeader,
    IonContent,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    // IonBadge,
    IonButton,
    IonModal,
    IonToolbar,
    IonTitle,
    IonIcon,
    IonButtons,
    IonLabel,
    IonDatetime,
    IonItem,
    IonRow,
    IonCol,
    IonImg,
  },
  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (bookingID, amount) => {
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

              // update booking status to "cancel"
              let url = "http://127.0.0.1:5001/bookings/" + bookingID;
              axios
                .put(url, {
                  status: "Cancelled",
                })
                .then((response) => {
                  //refund money
                  url = "http://127.0.0.1:5001/updateBalance/" + bookingID;
                  axios
                    .put(url, {
                      bookingID: bookingID,
                    })
                    .then((response) => {
                      sucessMsg(amount, response.data.data);
                    })
                    .catch((error) => {
                      console.log(error.message);
                    });
                })
                .catch((error) => {
                  console.log(error.message);
                });
            },
          },
        ],
      });
      await alert.present();
    };

    const sucessMsg = async (amount, balance) => {
      const alert = await alertController.create({
        header: "Success!",
        subHeader: "$" + amount + " refunded. Balance is " + "$" + balance,
        buttons: [
          {
            text: "Okay",
            handler: () => {
              location.reload();
            },
          },
        ],
      });

      await alert.present();
    };

    return {
      confirmationAlert,
      sucessMsg,
      arrowBackOutline,
    };
  },
  data() {
    return {
      bookingDetails: [],
      userData: {},
      editBookingOpen: false,

      //for editing booking
      bookingInfo: {},
      newDate: "",
      newStartTime: "",
      newEndTime: "",

      //to open editing windows
      editDate: false,
      editStartTime: false,
      editEndTime: false,
    };
  },
  methods: {
    routeUser(route) {
      this.$router.push({
        path: "/" + route,
      });
    },
    // getBalance() {
    //   this.userData = JSON.parse(localStorage.getItem("userData"));

    //   const url = "http://127.0.0.1:5002/getBalance/" + this.userData.userID;
    //   axios
    //     .get(url)
    //     .then((response) => {
    //       console.log(response);
    //       this.balance = response.data.data.balance;
    //     })
    //     .catch((error) => {
    //       console.log(error.message);
    //     });
    // },
    formatMoney(myFloat) {
      // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
      myFloat = myFloat.toString();
      let newFloat = myFloat.split(".");
      if (newFloat[1].length == 1) {
        newFloat[1] += "0";
      }
      newFloat = newFloat.join(".");
      return newFloat;
    },
    editBooking(bookingInfo) {
      this.setEditBookingOpen(true);
      this.bookingInfo = bookingInfo;
      // console.log(this.bookingInfo)
    },
    saveEditBooking() {
      // const startDateTimeFormatted = this.bookingDate.substring(0, 10) + " " + this.startTime.substring(11, 19);

      // to change user booking timing to current timing
      const currentDateTime = new Date();
      const date = currentDateTime.getDate();

      const month = currentDateTime.getMonth() + 1;
      const year = currentDateTime.getFullYear();
      const hour = currentDateTime.getHours();
      const min = currentDateTime.getMinutes();
      const sec = currentDateTime.getSeconds();

      const currentDateTimeFormatted = //here
        year + "-" + month + "-" + date + " " + hour + ":" + min + ":" + sec;

      // to change booking date
      let newStartDateFormatted = this.bookingInfo.startDate;
      if (this.newDate != "") {
        newStartDateFormatted = this.newDate.substring(0, 10);
      }

      // to change start time
      let newStartTimeFormatted = this.bookingInfo.startTime;
      if (this.newStartTime != "") {
        newStartTimeFormatted = this.newStartTime.substring(11, 19);
      }
      const newStartDateTime =
        newStartDateFormatted + " " + newStartTimeFormatted;

      // to change end time
      let newEndTimeFormatted = this.bookingInfo.endTime;
      if (this.newEndTime != "") {
        newEndTimeFormatted = this.newEndTime.substring(11, 19);
      }
      const newEndDateTime = newStartDateFormatted + " " + newEndTimeFormatted;

      const url =
        "http://127.0.0.1:5001/bookings/" + this.bookingInfo.bookingID;
      axios
        .put(url, {
          bookingDateTime: currentDateTimeFormatted,
          bookingStartDateTime: newStartDateTime,
          bookingEndDateTime: newEndDateTime,
        })
        .then((response) => {
          // console.log(response)
        })
        .catch((error) => {
          console.log(error.message);
        });
    },

    setEditBookingOpen(isOpen) {
      this.editBookingOpen = isOpen;
    },
    deleteBooking(bookingID) {
      const url = "http://127.0.0.1:5001/bookings/" + bookingID;
      axios
        .delete(url)
        .then((response) => {
          // console.log(response);
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
            let startDateTime = new Date(eachBooking.bookingStartDateTime);
            startDateTime = startDateTime.toUTCString();
            const startDateOnly = startDateTime.slice(5, 16);
            const startTimeOnly = startDateTime.slice(17, 22);

            let endDateTime = new Date(eachBooking.bookingEndDateTime);
            endDateTime = endDateTime.toUTCString();
            const endDateOnly = endDateTime.slice(5, 16);
            const endTimeOnly = endDateTime.slice(17, 22);

            let imagePath = "";

            const url = "http://127.0.0.1:5003/carparkImage";
            axios
              .post(url, {
                carparkName: eachBooking.bookingLocation,
              })
              .then((response) => {
                imagePath = response.data.data.imagePath;

                this.bookingDetails.push({
                  bookingDate: eachBooking.bookingDateTime,
                  bookingID: eachBooking.bookingID,
                  bookingLocation: eachBooking.bookingLocation,
                  locationName: eachBooking.locationName,
                  startDate: startDateOnly,
                  startTime: startTimeOnly,
                  endDate: endDateOnly,
                  amount: this.formatMoney(eachBooking.bookingAmt),
                  endTime: endTimeOnly,
                  status: eachBooking.status,
                  bookingRef: eachBooking.bookingRef,
                  userID: eachBooking.userID,
                  imagePath: imagePath,
                });
                console.log(this.bookingDetails);
              })
              .catch((error) => {
                console.log(error.message);
              });
          }
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  mounted() {
    // this.getBalance();
    this.getUserBooking();
  },
});
</script>

<style scoped>
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

.addPaddingBottom {
  padding-bottom: 300px;
}
</style>
