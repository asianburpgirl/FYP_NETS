<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <!-- <ion-buttons slot="start">
                    <ion-back-button defaultHref="/tabs/bookings"></ion-back-button>
                </ion-buttons> -->
        <ion-title class="ion-text-center">Map</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <!--   <ion-refresher slot="fixed" @ionRefresh="handleRefresh()">
            <ion-refresher-content></ion-refresher-content>
          </ion-refresher> -->

      <capacitor-google-map id="map"></capacitor-google-map>

      <!-- first popup page to open when user click on marker. User can choose either to book or subscribe to this carpark. button will open up respective popup  -->
      <ion-modal :is-open="choiceOpen" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title> {{ clickedMarkerName }}</ion-title>
            <ion-buttons slot="start">
              <ion-button @click="setChoiceOpen(false)">
                <ion-icon :icon="arrowBackOutline"></ion-icon>
              </ion-button>
            </ion-buttons>
          </ion-toolbar>
        </ion-header>

        <ion-content class="ion-padding ion-justify-content-center">
          <ion-card>
            <ion-card-header>
              <ion-card-title> Details </ion-card-title>
              <ion-card-subtitle>
                <p>
                  <b>${{ bookingAmount }} </b> per hour now
                </p>

                <p>
                  <b> {{ chosenCarpark.availableLots }} </b> lots available!
                </p>
                <p>Weekday Peak: ${{ weekdaypeakhourly }} per hour</p>
                <p>Weekday Non-Peak: ${{ weekdaynonpeakhourly }} per hour</p>
                <p>Weekend Peak: ${{ weekendpeakhourly }} per hour</p>
                <p>Weekend Non-Peak: ${{ weekendnonpeakhourly }} per hour</p>
              </ion-card-subtitle>
            </ion-card-header>
          </ion-card>
          <ion-list>
            <ion-item>
              <!-- Distance from your current location:
                            {{ distanceToLocation_km }} km
                            <br />
                            <br />
                            Time taken from your current location:
                            {{ timeToLocation_mins }} mins
                            <br /> -->

              <!-- <ion-label position="stacked"> Booking Date:</ion-label>
                        <ion-datetime presentation="date" v-model="bookingDate" :min="minDate"></ion-datetime> -->

              <!-- <ion-label position="stacked"> Start Time:</ion-label>
                        <ion-datetime presentation="time" v-model="currentTime"></ion-datetime> -->

              <ion-label position="stacked"><b>End Time</b></ion-label>
              <ion-datetime
                presentation="time"
                v-model="endTime"
              ></ion-datetime>
            </ion-item>
          </ion-list>

          <ion-text color="danger" class="ion-padding">
            <li v-for="error in errorMessage" :key="error">
              {{ error }}
            </li>
          </ion-text>
          <ion-row
            class="ion-padding-top ion-justify-content-end ion-padding-bottom addPaddingBottom"
          >
            <ion-col>
              <ion-button fill="outline" expand="block" @click="makeBooking()"
                >Book</ion-button
              >
            </ion-col>
          </ion-row>
        </ion-content>
      </ion-modal>
    </ion-content>
  </ion-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { GoogleMap } from "@capacitor/google-maps";
import axios from "axios";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonModal,
  IonRow,
  // IonList,
  // IonButtons,
  // IonBackButton,
  IonButton,
  IonDatetime,
  IonIcon,
  IonItem,
  IonLabel,
  // IonSelect,
  // IonSelectOption,
  IonCol,
  IonText,
  // IonImg,
  alertController,
} from "@ionic/vue";

import { arrowBackOutline } from "ionicons/icons";
import { Geolocation } from "@capacitor/geolocation";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonModal,
    // IonButtons,
    // IonBackButton,
    IonButton,
    IonDatetime,
    IonIcon,
    IonItem,
    IonLabel,
    // IonSelect,
    // IonSelectOption,
    IonRow,
    // IonList,
    IonCol,
    IonText,
    // IonImg
  },

  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (
      carpark,
      bookingAmount,
      userBalance,
      bookingStartTime,
      endTime,
      userData
    ) => {
      const alert = await alertController.create({
        header: "Confirm your booking? ",
        subHeader: "$" + bookingAmount + " will be deducted from your account",
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
              let currentTime = new Date();

              const year = currentTime.getFullYear();
              const month = currentTime.getMonth() + 1;
              const date = currentTime.getDate();

              currentTime =
                year +
                "-" +
                month +
                "-" +
                date +
                " " +
                currentTime.getHours() +
                ":" +
                currentTime.getMinutes() +
                ":00";

              const userID = userData.userID;

              bookingStartTime =
                year + "-" + month + "-" + date + " " + bookingStartTime;

              endTime =
                year +
                "-" +
                month +
                "-" +
                date +
                " " +
                endTime.getHours() +
                ":" +
                endTime.getMinutes() +
                ":00";

              let url = "http://127.0.0.1:5001/bookings";
              axios
                .post(url, {
                  bookingDateTime: currentTime,
                  bookingLocation: carpark.data.carparklocation,
                  locationName: carpark.data.carparkaddress,
                  bookingStartDateTime: bookingStartTime,
                  bookingEndDateTime: endTime,
                  userID: userID,
                  status: "Booked",
                  bookingAmt: bookingAmount,
                })
                .then((response) => {
                  url =
                    "http://127.0.0.1:5001/updateBalance/" +
                    response.data.data.bookingID;
                  let bookingAmount = response.data.data.bookingAmt;
                  bookingAmount = bookingAmount.toString();
                  const dotExists = bookingAmount.includes(".");
                  let newFloat = bookingAmount;
                  if (dotExists) {
                    newFloat = bookingAmount.split(".");
                    if (newFloat[1].length == 1) {
                      newFloat[1] += "0";
                    } else if (newFloat[1].length == 0) {
                      newFloat[1] += "00";
                    }
                    newFloat = newFloat.join(".");
                  } else {
                    newFloat += ".00";
                  }
                  axios
                    .put(url, {
                      bookingID: response.data.data.bookingID,
                    })
                    .then((response) => {
                      const balance = response.data.data;
                      const carparkID = carpark.data.carparkid;
                      url =
                        "http://127.0.0.1:5004/lotAdj/" + carparkID + "/2/1";
                      axios
                        .get(url)
                        .then((response) => {
                          url = "http://127.0.0.1:5006/deduct";
                          axios
                            .post(url, {
                              amount: bookingAmount,
                              userID: userID,
                            })
                            .then((response) => {
                              sucessMsg(bookingAmount, balance);
                            });
                        })
                        .catch((error) => {
                          console.log(error.message);
                        });
                    })
                    .catch((error) => {
                      console.log(error.message);
                    });
                })
                .catch((error) => {
                  console.log(error);
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
        subHeader:
          "$" +
          parseFloat(amount).toFixed(2) +
          " deducted. Balance is " +
          "$" +
          balance.toFixed(2),
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

    return { arrowBackOutline, confirmationAlert, sucessMsg };
  },
  data() {
    //my data bookmark
    return {
      bookingIsOpen: false,
      subscriptionSuccessIsOpen: false,
      subscriptionIsOpen: false,
      choiceOpen: false,

      userBalance: 0,

      //setting peak hours. can make it such that admin can change this value. value in 24 hours.
      startPeak: "09:00:00",
      endPeak: "17:00:00",

      carparkPrices: [],
      clickedMarkerName: "",
      clickedMarkerAddress: "",
      clickedCarpark: "",
      distanceToLocation_km: "",
      timeToLocation_mins: "",
      currentTime: "",
      endTime: "",
      // minDate: "",
      bookingDate: "",
      carparksArraySimu: [],
      chosenCarpark: {},
      userOrigin: "1.2958419970838684,103.85841587741238",
      userDestinations: "1.3007033161990564,103.84528924122294",
      bookingAmount: "",

      errorMessage: [],

      weekdaypeakhourly: 0,
      weekdaynonpeakhourly: 0,
      weekendnonpeakhourly: 0,
      weekendpeakhourly: 0,

      // bookingDetails: [],
      // userData: {},
      // editBookingOpen: false,

      // //for editing booking
      // bookingInfo: {},
      // newDate: "",
      // newStartTime: "",
      // newEndTime: "",

      // //to open editing windows
      // editDate: false,
      // editStartTime: false,
      // editEndTime: false,
    };
  },

  mounted() {
    this.createMap();
    this.loaduser();
    this.getCurrentDateTime();
  },

  methods: {
    loaduser() {
      const userData = JSON.parse(localStorage.getItem("userData"));

      const url =
        "http://127.0.0.1:5002/getBalance/" + parseInt(userData.userID);
      axios
        .get(url)
        .then((response) => {
          this.userBalance = response.data.data.balance;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    formatMoney(myFloat) {
      // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
      myFloat = parseFloat(myFloat);
      myFloat = myFloat.toFixed(2);
      myFloat = myFloat.toString();
      const dotExists = myFloat.includes(".");
      let newFloat = myFloat;
      if (dotExists) {
        newFloat = myFloat.split(".");
        if (newFloat[1].length == 1) {
          newFloat[1] += "0";
        } else if (newFloat[1].length == 0) {
          newFloat[1] += "00";
        }
        newFloat = newFloat.join(".");
      } else {
        newFloat += ".00";
      }

      return newFloat;
    },
    getCurrentDateTime() {
      const currentDateTime = new Date();
      const date = ("0" + currentDateTime.getDate()).slice(-2);
      const month = (
        "0" +
        (parseInt(currentDateTime.getMonth()) + parseInt(1))
      ).slice(-2);

      this.bookingDate =
        currentDateTime.getFullYear() +
        "-" +
        month +
        "-" +
        date +
        "T" +
        "15:30:00";

      const currentTime =
        ("0" + currentDateTime.getHours()).slice(-2) +
        ":" +
        ("0" + (currentDateTime.getMinutes() + 1)).slice(-2) +
        ":00";
      this.currentTime = currentTime;
    },
    routeToMyBookings() {
      this.$router
        .push({
          path: "/viewBooking",
        })
        .then(() => {
          this.$router.go(0);
        });
      location.reload();
    },
    async getCurrentLocation() {
      const coordinates = await Geolocation.getCurrentPosition();

      return coordinates;
    },
    setChoiceOpen(isOpen) {
      this.choiceOpen = isOpen;
    },
    setBookingOpen(isOpen) {
      this.bookingIsOpen = isOpen;
    },

    setSubscriptionOpen(isOpen) {
      this.subscriptionIsOpen = isOpen;
    },
    calculateTotalPrice(startTime, endTime, dateFormmated, rates) {
        
        startTime = new Date(dateFormmated +" " +startTime.toString().slice(15,25))
        endTime = new Date(dateFormmated +" " +endTime.toString().slice(15,25))

        console.log(startTime, endTime, dateFormmated, rates)
      // use startTime, EndTime,date, calculate price based on weekend/weekday + peak/nonpeak
      // Tue Mar 28 2023 07:54:00 GMT+0800 (Singapore Standard Time) | Tue Mar 28 2023 15:54:00 GMT+0800 (Singapore Standard Time)| '2023-03-28' | object of rates
      let fee = 0;
      // weekend
      if (startTime.getDay() == 6 || startTime.getDay() == 0) {
        // if booking start and end in peak
        if (
          endTime < new Date(dateFormmated + " " + this.endPeak) &&
          startTime > new Date(dateFormmated + " " + this.startPeak)
        ) {
          const duration = Math.floor((endTime - startTime) / 3600000) + 1;
          fee = duration * rates.weekendpeakhourly;
        }

        // if booking start in non peak and end in peak
        else if (
          endTime < new Date(dateFormmated + " " + this.endPeak) &&
          startTime < new Date(dateFormmated + " " + this.startPeak)
        ) {
          const peakFee =
            (Math.floor(
              (new Date(dateFormmated + " " + this.startPeak) - startTime) /
                3600000
            ) +
              1) *
            rates.weekendpeakhourly;
          const nonPeakFee =
            (Math.floor(
              (endTime - new Date(dateFormmated + " " + this.startPeak)) /
                3600000
            ) +
              1) *
            rates.weekendnonpeakhourly;
          fee = peakFee + nonPeakFee;
        }

        // if booking start in peak and end in non peak
        else if (
          endTime > new Date(dateFormmated + " " + this.endPeak) &&
          startTime < new Date(dateFormmated + " " + this.endPeak)
        ) {
          const peakFee =
            (Math.floor(
              (new Date(dateFormmated + " " + this.endPeak) - startTime) /
                3600000
            ) +
              1) *
            rates.weekendpeakhourly;
          const nonPeakFee =
            (Math.floor(
              (endTime - new Date(dateFormmated + " " + this.endPeak)) / 3600000
            ) +
              1) *
            rates.weekendpeaknonhourly;
          fee = peakFee + nonPeakFee;
        }

        // if booking start and end in non peak
        // else if ((endTime > (new Date(dateFormmated + " " + this.endPeak))) && (startTime > (new Date(dateFormmated + " " + this.startPeak)))) {
        else {
          const duration = Math.floor((endTime - startTime) / 3600000) + 1;
          fee = duration * rates.weekendnonpeakhourly;
        }
      }
      // weekday
      else {
        // if booking start and end in peak
        if (
          endTime < new Date(dateFormmated + " " + this.endPeak) &&
          startTime > new Date(dateFormmated + " " + this.startPeak)
        ) {
          const duration = Math.floor((endTime - startTime) / 3600000) + 1;
          fee = duration * rates.weekdaypeakhourly;
        }

        // if booking start in non peak and end in peak
        else if (
          new Date(dateFormmated + " " + this.startPeak) < endTime &&
          endTime < new Date(dateFormmated + " " + this.endPeak) &&
          startTime < new Date(dateFormmated + " " + this.startPeak)
        ) {
          const peakFee =
            (Math.floor(
              (new Date(dateFormmated + " " + this.startPeak) - startTime) /
                3600000
            ) +
              1) *
            rates.weekdaypeakhourly;
          const nonPeakFee =
            (Math.floor(
              (endTime - new Date(dateFormmated + " " + this.startPeak)) /
                3600000
            ) +
              1) *
            rates.weekdaynonpeakhourly;
          fee = peakFee + nonPeakFee;
        }

        // if booking start in peak and end in non peak
        else if (
          endTime > new Date(dateFormmated + " " + this.endPeak) &&
          startTime < new Date(dateFormmated + " " + this.endPeak)
        ) {
          const peakFee =
            (Math.floor(
              (new Date(dateFormmated + " " + this.endPeak) - startTime) /
                3600000
            ) +
              1) *
            rates.weekdaypeakhourly;
          const nonPeakFee =
            (Math.floor(
              (endTime - new Date(dateFormmated + " " + this.endPeak)) / 3600000
            ) +
              1) *
            rates.weekdaynonpeakhourly;
          fee = peakFee + nonPeakFee;
        }

        // if booking start and end in non peak
        // else if ((endTime > (new Date(dateFormmated + " " + this.endPeak))) && (startTime > (new Date(dateFormmated + " " + this.startPeak)))) {
        else {
          const duration = Math.floor((endTime - startTime) / 3600000) + 1;
          fee = duration * rates.weekdaynonpeakhourly;
        }
      }
      return fee;
    },
    makeBooking() {
      this.errorMessage = [];
      const hour = this.endTime.slice(11, 13);
      const mins = this.endTime.slice(14, 16);
      const currentTime = new Date("2023-03-25 " + this.currentTime);
      const endTime = new Date("2023-03-25 " + hour + ":" + mins + ":00");

      for (const eachCarpark of this.carparksArraySimu) {
        if (eachCarpark.data.carparklocation == this.clickedMarkerName) {
          this.clickedCarpark = eachCarpark;
          break;
        }
      }
      const rates = {
        weekdaynonpeakhourly: this.clickedCarpark.weekdaynonpeakhourly,
        weekdaypeakhourly: this.clickedCarpark.weekdaypeakhourly,
        weekendnonpeakhourly: this.clickedCarpark.weekendnonpeakhourly,
        weekendpeakhourly: this.clickedCarpark.weekendpeakhourly,
      };

      const formattedBookingDate = this.bookingDate.slice(0, 10);
      const totalPrice = this.formatMoney(
        this.calculateTotalPrice(
          currentTime,
          endTime,
          formattedBookingDate,
          rates
        )
      );
      console.log(this.userBalance,totalPrice)
      if (this.chosenCarpark.availableLots == 0) {
        this.errorMessage.push("This carpark does not have anymore slots!");
      }
      if (
        endTime < currentTime &&
        this.currentTime != "" &&
        this.endTime != ""
      ) {
        this.errorMessage.push("End Time must be later than current time!");
      }
      if (this.endTime == "") {
        this.errorMessage.push("You need to indicate end time !");
      }
      if (this.userBalance < totalPrice) {
        this.errorMessage.push("Insufficient credit. Top up your wallet !");
      }

      if (this.errorMessage.length == 0) {
        this.userData = JSON.parse(localStorage.getItem("userData"));
        // const userID = this.userData.userID;
        const userData = JSON.parse(localStorage.getItem("userData"));
        this.confirmationAlert(
          this.clickedCarpark,
          totalPrice,
          this.userBalance,
          this.currentTime,
          endTime,
          userData
        );
      }
    },
    // deductFromUser(bookingID) {
    //     // updateBalance
    //     const url = "http://127.0.0.1:5001/updateBalance/" + bookingID;
    //     axios
    //         .put(url, {
    //             bookingID: bookingID,
    //         })
    //         .then((response) => {
    //             // console.log(response)
    //         })
    //         .catch((error) => {
    //             console.log(error.message);
    //         });
    // },

    async createMap() {
      const mapRef = document.getElementById("map");
      const newMap = await GoogleMap.create({
        id: "my-map", // Unique identifier for this map instance
        element: mapRef, // reference to the capacitor-google-map element
        apiKey: "AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI", // Your Google Maps API Key
        config: {
          center: {
            // The initial position to be rendered by the map
            lat: 1.2962823,
            lng: 103.8500894, // smu
          },
          zoom: 13, // The initial zoom level to be rendered by the map
        },
      });

      //add markers
      let url = "http://127.0.0.1:5004/getCarpark/1";
      axios
        .post(url, {
          requesttype: 1000,
          carparkid: 1,
        })
        .then((response) => {
          this.carparksArraySimu.push({
            data: response.data.data,
            image: "assets/images/paragon.jpg",
            availableLots: response.data.data.lotbalancehourly,
            lat: 1.3040258884,
            long: 103.8360824585,
          });
          url = "http://127.0.0.1:5004/getCarpark/2";
          axios
            .post(url, {
              requesttype: 1000,
              carparkid: 2,
            })
            .then((response) => {
              this.carparksArraySimu.push({
                data: response.data.data,
                image: "assets/images/ion.jpg",
                availableLots: response.data.data.lotbalancehourly,
                lat: 1.3041540384,
                long: 103.8319625854,
              });
              url = "http://127.0.0.1:5004/getCarpark/3";
              axios
                .post(url, {
                  requesttype: 1000,
                  carparkid: 3,
                })
                .then((response) => {
                  this.carparksArraySimu.push({
                    data: response.data.data,
                    image: "assets/images/takashimaya.jpeg",
                    availableLots: response.data.data.lotbalancehourly,
                    lat: 1.3033454418,
                    long: 103.8345565796,
                  });
                  url = "http://127.0.0.1:5004/getCarpark/4";
                  axios
                    .post(url, {
                      requesttype: 1000,
                      carparkid: 4,
                    })
                    .then((response) => {
                      this.carparksArraySimu.push({
                        data: response.data.data,
                        image: "assets/images/tangs.jpg",
                        availableLots: response.data.data.lotbalancehourly,
                        lat: 1.3050314188,
                        long: 103.8329772949,
                      });
                      url = "http://127.0.0.1:5004/getCarpark/5";
                      axios
                        .post(url, {
                          requesttype: 1000,
                          carparkid: 5,
                        })
                        .then((response) => {
                          this.carparksArraySimu.push({
                            data: response.data.data,
                            image: "assets/images/Wheelock.png",
                            availableLots: response.data.data.lotbalancehourly,
                            lat: 1.3048859835,
                            long: 103.8304824829,
                          });

                          url = "http://127.0.0.1:5004/getCarpark/6";
                          axios
                            .post(url, {
                              requesttype: 1000,
                              carparkid: 6,
                            })
                            .then((response) => {
                              this.carparksArraySimu.push({
                                data: response.data.data,
                                image: "assets/images/313.jpg",
                                availableLots:
                                  response.data.data.lotbalancehourly,
                                lat: 1.3011711836,
                                long: 103.8386230469,
                              });

                              url = "http://127.0.0.1:5004/getCarpark/7";
                              axios
                                .post(url, {
                                  requesttype: 1000,
                                  carparkid: 7,
                                })
                                .then((response) => {
                                  this.carparksArraySimu.push({
                                    data: response.data.data,
                                    image: "assets/images/scape.jpg",
                                    availableLots:
                                      response.data.data.lotbalancehourly,
                                    lat: 1.3010677099,
                                    long: 103.8357620239,
                                  });
                                  url = "http://127.0.0.1:5004/getCarpark/8";
                                  axios
                                    .post(url, {
                                      requesttype: 1000,
                                      carparkid: 8,
                                    })
                                    .then((response) => {
                                      this.carparksArraySimu.push({
                                        data: response.data.data,
                                        image: "assets/images/tangs.jpg",
                                        availableLots:
                                          response.data.data.lotbalancehourly,
                                        lat: 1.3038430214,
                                        long: 103.8333206177,
                                      });
                                      let url =
                                        "http://127.0.0.1:5004/getCarparkPrice/1";
                                      axios.get(url).then((response) => {
                                        this.carparksArraySimu[0][
                                          "weekdaypeakhourly"
                                        ] = this.formatMoney(
                                          response.data.data.weekdaypeakhourly /
                                            100
                                        );
                                        this.carparksArraySimu[0][
                                          "weekdaynonpeakhourly"
                                        ] = this.formatMoney(
                                          response.data.data
                                            .weekdaynonpeakhourly / 100
                                        );
                                        this.carparksArraySimu[0][
                                          "weekendnonpeakhourly"
                                        ] = this.formatMoney(
                                          response.data.data
                                            .weekendnonpeakhourly / 100
                                        );
                                        this.carparksArraySimu[0][
                                          "weekendpeakhourly"
                                        ] = this.formatMoney(
                                          response.data.data.weekendpeakhourly /
                                            100
                                        );

                                        url =
                                          "http://127.0.0.1:5004/getCarparkPrice/2";
                                        axios.get(url).then((response) => {
                                          this.carparksArraySimu[1][
                                            "weekdaypeakhourly"
                                          ] = this.formatMoney(
                                            response.data.data
                                              .weekdaypeakhourly / 100
                                          );
                                          this.carparksArraySimu[1][
                                            "weekdaynonpeakhourly"
                                          ] = this.formatMoney(
                                            response.data.data
                                              .weekdaynonpeakhourly / 100
                                          );
                                          this.carparksArraySimu[1][
                                            "weekendnonpeakhourly"
                                          ] = this.formatMoney(
                                            response.data.data
                                              .weekendnonpeakhourly / 100
                                          );
                                          this.carparksArraySimu[1][
                                            "weekendpeakhourly"
                                          ] = this.formatMoney(
                                            response.data.data
                                              .weekendpeakhourly / 100
                                          );

                                          url =
                                            "http://127.0.0.1:5004/getCarparkPrice/3";
                                          axios.get(url).then((response) => {
                                            this.carparksArraySimu[2][
                                              "weekdaypeakhourly"
                                            ] = this.formatMoney(
                                              response.data.data
                                                .weekdaypeakhourly / 100
                                            );
                                            this.carparksArraySimu[2][
                                              "weekdaynonpeakhourly"
                                            ] = this.formatMoney(
                                              response.data.data
                                                .weekdaynonpeakhourly / 100
                                            );
                                            this.carparksArraySimu[2][
                                              "weekendnonpeakhourly"
                                            ] = this.formatMoney(
                                              response.data.data
                                                .weekendnonpeakhourly / 100
                                            );
                                            this.carparksArraySimu[2][
                                              "weekendpeakhourly"
                                            ] = this.formatMoney(
                                              response.data.data
                                                .weekendpeakhourly / 100
                                            );

                                            url =
                                              "http://127.0.0.1:5004/getCarparkPrice/4";
                                            axios.get(url).then((response) => {
                                              this.carparksArraySimu[3][
                                                "weekdaypeakhourly"
                                              ] = this.formatMoney(
                                                response.data.data
                                                  .weekdaypeakhourly / 100
                                              );
                                              this.carparksArraySimu[3][
                                                "weekdaynonpeakhourly"
                                              ] = this.formatMoney(
                                                response.data.data
                                                  .weekdaynonpeakhourly / 100
                                              );
                                              this.carparksArraySimu[3][
                                                "weekendnonpeakhourly"
                                              ] = this.formatMoney(
                                                response.data.data
                                                  .weekendnonpeakhourly / 100
                                              );
                                              this.carparksArraySimu[3][
                                                "weekendpeakhourly"
                                              ] = this.formatMoney(
                                                response.data.data
                                                  .weekendpeakhourly / 100
                                              );

                                              url =
                                                "http://127.0.0.1:5004/getCarparkPrice/5";
                                              axios
                                                .get(url)
                                                .then((response) => {
                                                  this.carparksArraySimu[4][
                                                    "weekdaypeakhourly"
                                                  ] = this.formatMoney(
                                                    response.data.data
                                                      .weekdaypeakhourly / 100
                                                  );
                                                  this.carparksArraySimu[4][
                                                    "weekdaynonpeakhourly"
                                                  ] = this.formatMoney(
                                                    response.data.data
                                                      .weekdaynonpeakhourly /
                                                      100
                                                  );
                                                  this.carparksArraySimu[4][
                                                    "weekendnonpeakhourly"
                                                  ] = this.formatMoney(
                                                    response.data.data
                                                      .weekendnonpeakhourly /
                                                      100
                                                  );
                                                  this.carparksArraySimu[4][
                                                    "weekendpeakhourly"
                                                  ] = this.formatMoney(
                                                    response.data.data
                                                      .weekendpeakhourly / 100
                                                  );

                                                  url =
                                                    "http://127.0.0.1:5004/getCarparkPrice/6";
                                                  axios
                                                    .get(url)
                                                    .then((response) => {
                                                      this.carparksArraySimu[5][
                                                        "weekdaypeakhourly"
                                                      ] = this.formatMoney(
                                                        response.data.data
                                                          .weekdaypeakhourly /
                                                          100
                                                      );
                                                      this.carparksArraySimu[5][
                                                        "weekdaynonpeakhourly"
                                                      ] = this.formatMoney(
                                                        response.data.data
                                                          .weekdaynonpeakhourly /
                                                          100
                                                      );
                                                      this.carparksArraySimu[5][
                                                        "weekendnonpeakhourly"
                                                      ] = this.formatMoney(
                                                        response.data.data
                                                          .weekendnonpeakhourly /
                                                          100
                                                      );
                                                      this.carparksArraySimu[5][
                                                        "weekendpeakhourly"
                                                      ] = this.formatMoney(
                                                        response.data.data
                                                          .weekendpeakhourly /
                                                          100
                                                      );
                                                      url =
                                                        "http://127.0.0.1:5004/getCarparkPrice/7";
                                                      axios
                                                        .get(url)
                                                        .then((response) => {
                                                          this.carparksArraySimu[6][
                                                            "weekdaypeakhourly"
                                                          ] = this.formatMoney(
                                                            response.data.data
                                                              .weekdaypeakhourly /
                                                              100
                                                          );
                                                          this.carparksArraySimu[6][
                                                            "weekdaynonpeakhourly"
                                                          ] = this.formatMoney(
                                                            response.data.data
                                                              .weekdaynonpeakhourly /
                                                              100
                                                          );
                                                          this.carparksArraySimu[6][
                                                            "weekendnonpeakhourly"
                                                          ] = this.formatMoney(
                                                            response.data.data
                                                              .weekendnonpeakhourly /
                                                              100
                                                          );
                                                          this.carparksArraySimu[6][
                                                            "weekendpeakhourly"
                                                          ] = this.formatMoney(
                                                            response.data.data
                                                              .weekendpeakhourly /
                                                              100
                                                          );

                                                          url =
                                                            "http://127.0.0.1:5004/getCarparkPrice/8";
                                                          axios
                                                            .get(url)
                                                            .then(
                                                              (response) => {
                                                                this.carparksArraySimu[7][
                                                                  "weekdaypeakhourly"
                                                                ] =
                                                                  this.formatMoney(
                                                                    response
                                                                      .data.data
                                                                      .weekdaypeakhourly /
                                                                      100
                                                                  );
                                                                this.carparksArraySimu[7][
                                                                  "weekdaynonpeakhourly"
                                                                ] =
                                                                  this.formatMoney(
                                                                    response
                                                                      .data.data
                                                                      .weekdaynonpeakhourly /
                                                                      100
                                                                  );
                                                                this.carparksArraySimu[7][
                                                                  "weekendnonpeakhourly"
                                                                ] =
                                                                  this.formatMoney(
                                                                    response
                                                                      .data.data
                                                                      .weekendnonpeakhourly /
                                                                      100
                                                                  );
                                                                this.carparksArraySimu[7][
                                                                  "weekendpeakhourly"
                                                                ] =
                                                                  this.formatMoney(
                                                                    response
                                                                      .data.data
                                                                      .weekendpeakhourly /
                                                                      100
                                                                  );
                                                                console.log(
                                                                  this
                                                                    .carparksArraySimu
                                                                );
                                                              }
                                                            );
                                                        });
                                                    });
                                                });
                                            });
                                          });
                                        });
                                      });

                                      // const currentDate = new Date()
                                      // const currentDateFormatted = currentDate.toString().substring(0,10)
                                      for (const eachCarpark of this
                                        .carparksArraySimu) {
                                        const markers = newMap.addMarkers([
                                          {
                                            title:
                                              eachCarpark.data.carparklocation,
                                            snippet:
                                              eachCarpark.data.carparkaddress,
                                            coordinate: {
                                              lat: eachCarpark.lat,
                                              lng: eachCarpark.long,
                                            },
                                          },
                                        ]);
                                      }

                                      // const url = "http://127.0.0.1:5004/getCarparkPrice/1"
                                      // axios
                                      //     .get(url)
                                      //     .then((response) => {
                                    });
                                });
                            });
                        });
                    });
                });
            });

          // listener for user click
          const markerListener = newMap.setOnMarkerClickListener((event) => {
            this.getCurrentDateTime();
            this.clickedMarkerName = event.title;
            // this.clickedMarkerAddress = event.snippet;

            for (const eachcarpark of this.carparksArraySimu) {
              if (eachcarpark.data.carparklocation == this.clickedMarkerName) {
                this.chosenCarpark = eachcarpark;
                const currentDayOfWeek = new Date();
                this.weekdaypeakhourly = eachcarpark.weekdaypeakhourly;
                this.weekdaynonpeakhourly = eachcarpark.weekdaynonpeakhourly;
                this.weekendnonpeakhourly = eachcarpark.weekendnonpeakhourly;
                this.weekendpeakhourly = eachcarpark.weekendpeakhourly;
                // weekend
                if (
                  currentDayOfWeek.getDay() == 6 ||
                  currentDayOfWeek.getDay() == 0
                ) {
                  // peak
                  if (
                    this.startPeak.split(":")[0] <
                    currentDayOfWeek.getHours() <
                    this.endPeak.split(":")[0]
                  ) {
                    this.bookingAmount = this.formatMoney(
                      eachcarpark.weekendpeakhourly
                    );
                  }
                  //non peak
                  else {
                    this.bookingAmount = this.formatMoney(
                      eachcarpark.weekendnonpeakhourly
                    );
                  }
                }
                // weekdays
                else {
                  // peak
                  if (
                    this.startPeak.split(":")[0] <
                    currentDayOfWeek.getHours() <
                    this.endPeak.split(":")[0]
                  ) {
                    this.bookingAmount = this.formatMoney(
                      eachcarpark.weekdaypeakhourly
                    );
                  }
                  //non peak
                  else {
                    this.bookingAmount = this.formatMoney(
                      eachcarpark.weekdaynonpeakhourly
                    );
                  }
                }

                break;
              }
            }

            this.setChoiceOpen(true);
          });
          //add traffic data
          const trafficDataEnable = newMap.enableTrafficLayer(true);

          // enable current location
          const currentLocationEnable = newMap.enableCurrentLocation(true);
          return newMap;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
});
</script>

<style scoped>
capacitor-google-map {
  display: inline-block;
  width: 100%;
  height: 100%;
}

.addPaddingBottom {
  padding-bottom: 50px;
}

h2 {
  padding-bottom: 120px;
}

ion-label {
  padding-bottom: 10px;
}
</style>
