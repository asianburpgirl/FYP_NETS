<template>
  <base-layout needToolBar="y" pageTitle="Home">
    <ion-grid>
      <h1>Hello, {{ this.name }}</h1>
      <ion-row class="ion-justify-content-center">
        <ion-col size="9">
          <h3><b>Bookings</b></h3>
        </ion-col>
        <ion-col>
          <ion-button fill="outline" @click="routeUser('nearbyMe')"
            >+</ion-button
          >
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col>
          <ion-searchbar color="light"></ion-searchbar>
        </ion-col>
        <ion-col>
          <ion-list lines="none">
            <ion-item>
              <ion-select
                class="ion-padding-top ion-padding-bottom"
                v-model="bookingStatusToShow"
                @ionChange="changeStatus()"
              >
                <ion-select-option value="all">All</ion-select-option>
                <ion-select-option value="upcoming">Upcoming</ion-select-option>
                <ion-select-option value="past">Past</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </ion-col>
      </ion-row>

      <ion-modal :is-open="editBookingOpen">
        <ion-header>
          <ion-toolbar>
            <ion-buttons slot="start">
              <ion-back-button
                defaultHref="/tabs/home"
                @click="setEditBookingOpen(false)"
                ><ion-icon :icon="arrowBackOutline"></ion-icon
              ></ion-back-button>
            </ion-buttons>
            <ion-title class="ion-text-center">Edit Booking</ion-title>
          </ion-toolbar>
        </ion-header>
        <ion-content>
          <ion-img :src="bookingInfo.imagePath"></ion-img>
          <ion-card color="dark" class="ion-padding">
            <ion-card-header>
              <ion-card-title>Booking Details</ion-card-title>
            </ion-card-header>
            <ion-card-content>
              <p>
                Booking Reference: <b>{{ bookingInfo.bookingRef }}</b>
              </p>
              <p v-if="bookingInfo.status == 'Booked'">
                Booking Amount: <b>${{ bookingInfo.amount }}</b>
              </p>
              <p v-if="bookingInfo.status == 'Cancelled'">
                Refunded Amount: <b>${{ bookingInfo.amount }}</b>
              </p>
              <p>Lot Number: <b>123</b></p>
              <p>Level: <b>B2</b></p>
            </ion-card-content>
          </ion-card>
          <ion-card>
            <ion-card-header>
              <ion-list lines="none">
                <ion-item>
                  <ion-card-title>{{ bookingInfo.startDate }}</ion-card-title>
                  <ion-button
                    fill="clear"
                    @click="editDate = true"
                    v-if="editDate == false"
                    slot="end"
                    >Edit</ion-button
                  ><ion-button
                    fill="clear"
                    @click="editDate = true"
                    v-if="editDate == true"
                    color="danger"
                    slot="end"
                    >Cancel</ion-button
                  >
                </ion-item>
              </ion-list>
            </ion-card-header>
            <ion-card-content>
              <ion-datetime
                presentation="date"
                v-model="newDate"
                v-if="editDate == true"
              ></ion-datetime>
            </ion-card-content>
          </ion-card>
          <ion-card>
            <ion-card-header>
              <ion-list>
                <ion-item lines="none">
                  <ion-card-title
                    >Start: {{ bookingInfo.startTime }}</ion-card-title
                  >
                  <ion-button
                    fill="clear"
                    @click="editStartTime = true"
                    v-if="editStartTime == false"
                    slot="end"
                    >Edit</ion-button
                  >
                  <ion-button
                    fill="clear"
                    @click="editDate = true"
                    v-if="editStartTime == true"
                    color="danger"
                    slot="end"
                    >Cancel</ion-button
                  >
                </ion-item>
              </ion-list>
            </ion-card-header>
            <ion-card-content>
              <ion-datetime
                presentation="time"
                v-model="newStartTime"
                v-if="editStartTime == true"
              ></ion-datetime>
            </ion-card-content>
          </ion-card>
          <ion-card>
            <ion-card-header>
              <ion-list lines="none">
                <ion-item>
                  <ion-card-title
                    >End: {{ bookingInfo.endTime }}</ion-card-title
                  >
                  <ion-button
                    fill="clear"
                    @click="editEndTime = true"
                    v-if="editEndTime == false"
                    slot="end"
                    >Edit</ion-button
                  >
                  <ion-button
                    fill="clear"
                    @click="editDate = true"
                    v-if="editEndTime == true"
                    color="danger"
                    slot="end"
                    >Cancel</ion-button
                  >
                </ion-item>
              </ion-list>
            </ion-card-header>
            <ion-card-content>
              <ion-datetime
                presentation="time"
                v-model="newEndTime"
                v-if="editEndTime == true"
              ></ion-datetime>
            </ion-card-content>
          </ion-card>
          <ion-grid>
            <ion-row class="add-bottom">
              <ion-col>
                <ion-button
                  @click="saveEditBooking()"
                  fill="outline"
                  expand="block"
                >
                  Save
                </ion-button>
              </ion-col>
            </ion-row>
          </ion-grid>
        </ion-content>
      </ion-modal>

      <ion-card v-for="eachBooking in bookingsToShow" :key="eachBooking">
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
                v-if="eachBooking.status == 'Cancelled' || eachBooking.status == 'Completed'"
                color="medium"
                slot="end"
                >{{eachBooking.status}}</ion-badge
              >
              <ion-card-title>{{ eachBooking.bookingLocation }}</ion-card-title>
            </ion-item>
          </ion-list>
        </ion-card-header>

        <ion-card-content>
          <div class="ion-padding">
            <div class="ion-padding-top">
              <ion-card-subtitle v-if="eachBooking.status == 'Cancelled'"
                >Refunded Amount: $ {{ eachBooking.amount }}</ion-card-subtitle
              >
              <ion-card-subtitle><b>Level: B2</b></ion-card-subtitle>
              <ion-card-subtitle><b>Lot Number: 123</b></ion-card-subtitle>
              <ion-card-subtitle
                ><b
                  >Start Date: {{ eachBooking.startDate }}</b
                ></ion-card-subtitle
              >
              <ion-card-subtitle
                ><b>End Date: {{ eachBooking.endDate }}</b></ion-card-subtitle
              >
              <ion-card-subtitle
                ><b
                  >Start Time: {{ eachBooking.startTime }}</b
                ></ion-card-subtitle
              >
              <ion-card-subtitle
                ><b>End Time: {{ eachBooking.endTime }}</b></ion-card-subtitle
              >
            </div>
          </div>
          <div class="ion-padding">
            <ion-row>
              <ion-col md="6" v-if="eachBooking.status == 'Booked'">
                <ion-button
                  fill="outline"
                  expand="block"
                  @click="editBooking(eachBooking)"
                  >Edit</ion-button
                >
              </ion-col>
              <ion-col md="6" v-if="eachBooking.status == 'Booked'">
                <ion-button
                  expand="block"
                  fill="outline"
                  @click="
                    confirmationAlert(
                      eachBooking.bookingID,
                      eachBooking.amount,
                      eachBooking.bookingLocation
                    )
                  "
                  color="danger"
                  >Cancel</ion-button
                >
              </ion-col>
              <ion-col md="12" v-if="eachBooking.status == 'Cancelled'|| eachBooking.status == 'Completed' ">
                <ion-button
                  @click="deleteBooking(eachBooking.bookingID)"
                  color="dark"
                  fill="outline"
                  expand="block"
                  >Delete</ion-button
                >
              </ion-col>
            </ion-row>
          </div>
        </ion-card-content>
      </ion-card>
    </ion-grid>

    <!-- <ion-grid>
      <h4 class="ion-text-start">Carpark Details</h4>
      <ion-card v-for="carpark in carparksArraySimu" :key="carpark">
        <ion-img :src="carpark.image"></ion-img>
        <ion-card-header>
          <ion-card-title>{{ carpark.data.carparklocation }}</ion-card-title>
          <ion-card-subtitle>{{
            carpark.data.carparkaddress
          }}</ion-card-subtitle>
        </ion-card-header>
      </ion-card>
    </ion-grid> -->
  </base-layout>
</template>

<script>
import { arrowBackOutline } from "ionicons/icons";
import {
  IonGrid,
  IonSelectOption,
  IonSelect,
  IonHeader,
  IonCard,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonBadge,
  IonList,
  IonCardContent,
  IonButton,
  alertController,
  IonModal,
  IonToolbar,
  IonTitle,
  IonIcon,
  IonButtons,
  IonDatetime,
  IonItem,
  IonRow,
  IonCol,
  IonImg,
  IonSearchbar,
  IonContent,
  IonBackButton,
} from "@ionic/vue";
import { GChart } from "vue-google-charts";
import { defineComponent, ref } from "vue";
import axios from "axios";
export default defineComponent({
  components: {
    IonGrid,
    IonSelectOption,
    IonSelect,
    IonHeader,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonBadge,
    IonList,
    IonCardContent,
    IonButton,
    IonModal,
    IonToolbar,
    IonTitle,
    IonIcon,
    IonButtons,
    IonDatetime,
    IonItem,
    IonRow,
    IonCol,
    IonImg,
    IonSearchbar,
    IonContent,
    IonBackButton,
  },
  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (bookingID, amount, bookingLocation) => {
      let amount2 = amount;
      amount2 = amount2.toString();
      const dotExists = amount.includes(".");
      if (dotExists) {
        amount2 = amount2.split(".");
        if (amount2[1].length == 1) {
          amount2[1] += "0";
        } else if (amount[1].length == 0) {
          amount2[1] += "00";
        }
        amount = amount2.join(".");
      } else {
        amount += ".00";
      }

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
              refund(amount);
              let url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/bookings/" + bookingID;
              axios
                .put(url, {
                  status: "Cancelled",
                })
                .then((response) => {
                  //refund money
                  url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/updateBalance/" + bookingID;
                  axios
                    .put(url, {
                      bookingID: bookingID,
                    })

                    .then((response) => {
                      // update lot to plus one
                      const balance = response.data.data.toString();
                      url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5003/carparks";
                      axios.get(url).then((response) => {
                        let newFloat = balance;
                        const carparks = response.data.data.carparks;
                        for (const eachCarpark of carparks) {
                          if (eachCarpark.carparkName == bookingLocation) {
                            url =
                              "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/lotAdj/" +
                              eachCarpark.carparkID +
                              "/2/-1";
                            axios.get(url).then((response) => {
                              console.log(response);
                              const dotExists = balance.includes(".");
                              if (dotExists) {
                                newFloat = balance.split(".");
                                if (newFloat[1].length == 1) {
                                  newFloat[1] += "0";
                                } else if (newFloat[1].length == 0) {
                                  newFloat[1] += "00";
                                }
                                newFloat = newFloat.join(".");
                              } else {
                                newFloat += ".00";
                              }
                              sucessMsg(amount, newFloat);
                            });
                          }
                        }
                      });
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

    const refund = async (amount) => {
      const userData = JSON.parse(localStorage.getItem("userData"));
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5006/deduct";
      axios
        .post(url, {
          amount: amount,
          userID: userData["userID"],
        })
        .then((response) => {
          console.log(response);
        });
    };

    return {
      confirmationAlert,
      sucessMsg,
      arrowBackOutline,
    };
  },
  data() {
    return {
      bookingStatusToShow: "all",

      bookingDetails: [],
      upcomingBookings: [],
      pastBookings: [],
      bookingsToShow: [],

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
      carparksArraySimu: [],
      name: "",
      PieChartData: [["Bookings", "Percentage of bookings"]],
      BarChartData: [["Booking Location", "No. of Bookings"]],
      ColumnChartData: [
        ["Carpark Name", "Subscription Plan", "No. of Subscribers"],
      ],
      PieChartoptions: {
        title: "Percentage of bookings per location",
        pieHole: 0.1,
      },
      BarChartOptions: {
        title: "Number of bookings per location",
        legend: {
          position: "bottom",
        },
      },
      ColumnChartOptions: {
        title: "Number of bookings per subscription",
        legend: {
          position: "bottom",
        },
      },
    };
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
      this.name = this.userData.name;
    },
    getPieChart() {
      let pieData = [];

      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/bookings";
      axios
        .get(url)
        .then((response) => {
          pieData = response.data.data.bookings;
          // console.log(pieData)
          for (let i = 0; i < pieData.length; i++) {
            this.PieChartData.push([
              pieData[i]["bookingLocation"],
              pieData[i]["bookingID"],
            ]);
          }
          return pieData;
          // console.log(response.data.data.bookings)
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getBarChart() {
      let barData = [];
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5003/carparks";

      axios
        .get(url)
        .then((response) => {
          barData = response.data.data.carparks;
          for (let i = 0; i < barData.length; i++) {
            this.BarChartData.push([
              barData[i]["carparkName"],
              barData[i]["currentCapacity"],
            ]);
          }
          return barData;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getColumnChart() {
      let columnData = [];
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5003/carparks";

      axios
        .get(url)
        .then((response) => {
          columnData = response.data.data.carparks;
          // console.log(columnData)
          for (let i = 0; i < columnData.length; i++) {
            this.ColumnChartData.push([
              columnData[i]["carparkName"],
              columnData[i]["hourlyweekdaypeak"],
              columnData[i]["hourlyweekdaynonpeak"],
            ]);
          }
          return columnData;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getSimulator() {
      this.carparksArraySimu = [];

      let url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/1";
      axios
        .post(url, {
          requesttype: 1000,
          carparkid: 1,
        })
        .then((response) => {
          this.carparksArraySimu.push({
            data: response.data.data,
            image: "assets/images/paragon.jpg",
            availableLots:
              response.data.data.lotbalancehourly -
              response.data.data.lotusehourly,
          });

          url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/2";
          axios
            .post(url, {
              requesttype: 1000,
              carparkid: 2,
            })
            .then((response) => {
              this.carparksArraySimu.push({
                data: response.data.data,
                image: "assets/images/ion.jpg",
                availableLots:
                  response.data.data.lotbalancehourly -
                  response.data.data.lotusehourly,
              });
              url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/3";
              axios
                .post(url, {
                  requesttype: 1000,
                  carparkid: 3,
                })
                .then((response) => {
                  this.carparksArraySimu.push({
                    data: response.data.data,
                    image: "assets/images/takashimaya.jpeg",
                    availableLots:
                      response.data.data.lotbalancehourly -
                      response.data.data.lotusehourly,
                  });
                  url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/4";
                  axios
                    .post(url, {
                      requesttype: 1000,
                      carparkid: 4,
                    })
                    .then((response) => {
                      this.carparksArraySimu.push({
                        data: response.data.data,
                        image: "assets/images/tangs.jpg",
                        availableLots:
                          response.data.data.lotbalancehourly -
                          response.data.data.lotusehourly,
                      });
                      url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/5";
                      axios
                        .post(url, {
                          requesttype: 1000,
                          carparkid: 5,
                        })
                        .then((response) => {
                          this.carparksArraySimu.push({
                            data: response.data.data,
                            image: "assets/images/Wheelock.png",
                            availableLots:
                              response.data.data.lotbalancehourly -
                              response.data.data.lotusehourly,
                          });
                          url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/6";
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
                                  response.data.data.lotbalancehourly -
                                  response.data.data.lotusehourly,
                              });

                              url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/7";
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
                                      response.data.data.lotbalancehourly -
                                      response.data.data.lotusehourly,
                                  });
                                  url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5004/getCarpark/8";
                                  axios
                                    .post(url, {
                                      requesttype: 1000,
                                      carparkid: 8,
                                    })
                                    .then((response) => {
                                      this.carparksArraySimu.push({
                                        data: response.data.data,
                                        availableLots:
                                          response.data.data.lotbalancehourly -
                                          response.data.data.lotusehourly,
                                        image: "assets/images/wisma.jpeg",
                                      });
                                    });
                                });
                            });
                        });
                    });
                });
            });
        });
    },
    changeStatus() {
      if (this.bookingStatusToShow == "upcoming") {
        this.bookingsToShow = this.upcomingBookings;
      } else if (this.bookingStatusToShow == "past") {
        this.bookingsToShow = this.pastBookings;
      } else {
        this.bookingsToShow = this.bookingDetails;
      }
      //bookingsToShow
    },
    routeUser(route) {
      this.$router.push({
        path: "/" + route,
      });
    },
    // getBalance() {
    //   this.userData = JSON.parse(localStorage.getItem("userData"));

    //   const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5002/getBalance/" + this.userData.userID;
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
    editBooking(bookingInfo) {
      this.setEditBookingOpen(true);
      this.bookingInfo = bookingInfo;
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
        "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/bookings/" + this.bookingInfo.bookingID;
      axios
        .put(url, {
          bookingDateTime: currentDateTimeFormatted,
          bookingStartDateTime: newStartDateTime,
          bookingEndDateTime: newEndDateTime,
        })
        .then((response) => {
          location.reload();
        })
        .catch((error) => {
          console.log(error.message);
        });
    },

    setEditBookingOpen(isOpen) {
      this.editBookingOpen = isOpen;
    },
    deleteBooking(bookingID) {
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/bookings/" + bookingID;
      axios
        .delete(url)
        .then((response) => {
          location.reload();
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    // cancelRefund(amount) {
    //   this.userData = JSON.parse(localStorage.getItem("userData"));
    //   const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5006/deduct"
    //     axios
    //       .post(url, {
    //         "amount": amount,
    //         "userID": this.userData
    //       })
    //       .then((response) => {
    //         console.log(response)
    //       })
    // },
    editBookings(){
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/editStatus"
      axios
        .delete(url)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error.message);
        });
      // editStatus
    },

    getUserBooking() {
      this.userData = JSON.parse(localStorage.getItem("userData"));
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/bookings/" + this.userData.userID;
      axios
        .get(url)
        .then((response) => {
          let pastBookings = [];
          let upcomingBookings = [];
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

            const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5003/carparkImage";
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
                this.bookingDetails = this.bookingDetails.sort(function (a, b) {
                  const keyA = a.startDate;
                  const keyB = b.startDate;
                  if (keyA > keyB) return -1;
                  if (keyA < keyB) return 1;
                  return 0;
                });
                if (
                  new Date() - new Date(eachBooking.bookingStartDateTime) >
                  0
                ) {
                  pastBookings.push({
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
                  pastBookings = pastBookings.sort(function (a, b) {
                  const keyA = a.startDate;
                  const keyB = b.startDate;
                  if (keyA > keyB) return -1;
                  if (keyA < keyB) return 1;
                  return 0;
                });
                } else {
                  upcomingBookings.push({
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
                  upcomingBookings = upcomingBookings.sort(function (a, b) {
                  const keyA = a.startDate;
                  const keyB = b.startDate;
                  if (keyA > keyB) return -1;
                  if (keyA < keyB) return 1;
                  return 0;
                });
                }
                this.changeStatus();
              })
              .catch((error) => {
                console.log(error.message);
              });
          }
          this.pastBookings = pastBookings;
          this.upcomingBookings = upcomingBookings;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  // Calls function on page load
  mounted() {
    this.getSimulator();
    this.loadUserData();
    this.getBarChart();
    this.getPieChart();
    this.getColumnChart();
    this.getUserBooking();
    this.editBookings()
  },
});
</script>

<style scoped>
h1 {
  font-size: 30px;
  color: #3880ff;
  font-weight: 700;
}

ion-searchbar {
  padding-left: 0;
}

.add-bottom {
  padding-bottom: 50px;
}
</style>
