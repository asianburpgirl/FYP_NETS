<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/tabs/bookings"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Nearby Me</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-searchbar></ion-searchbar>

      <ion-list class="ion-padding-top">
        <ion-radio-group v-model="pageTab" @ionChange="resetState()">
          <ion-item>
            <ion-label>All</ion-label>
            <ion-radio slot="end" value="all"></ion-radio>
          </ion-item>

          <ion-item>
            <ion-label>Nearest</ion-label>
            <ion-radio slot="end" value="nearest"></ion-radio>
          </ion-item>

          <ion-item>
            <ion-label>Cheapest</ion-label>
            <ion-radio slot="end" value="cheapest"></ion-radio>
          </ion-item>
        </ion-radio-group>
      </ion-list>

      <ion-list v-if="pageTab == 'nearest'">
        <ion-item>
          <ion-select
            placeholder="I am at:"
            @ionChange="
              pushLog($event.detail.value);
              this.getCarparks();
            "
          >
            <IonSelectOption value="orchard">Orchard</IonSelectOption>
            <IonSelectOption value="somerset">Somerset</IonSelectOption>
            <IonSelectOption value="yishun">Yishun</IonSelectOption>
          </ion-select>
        </ion-item>
      </ion-list>

      <div v-if="this.pageTab == 'nearest' && this.selectedLocation == ''">
        <h1>Select a location to view the nearest carparks to it!</h1>
      </div>

      <ion-grid
        class="ion-padding-top"
        v-if="
          (this.pageTab == 'nearest' && this.selectedLocation != '') ||
          this.pageTab == 'all' || (this.pageTab =='cheapest' && this.startTime != '' &&
          this.endTime !='' && this.bookingDate != '' )
        "
      >
        <ion-card v-for="carpark in carparksArray" :key="carpark">
          <ion-img :src="carpark.imagePath"></ion-img>

          <ion-card-header>
            <ion-card-title>{{ carpark.carparkName }}</ion-card-title>
            <ion-card-subtitle></ion-card-subtitle>
            <ion-card-subtitle>{{ carpark.caparkLocation }}</ion-card-subtitle>
            <h3>
              <b> {{ carpark.availableLots }}</b> lots available
            </h3>
            <h3  v-if="pageTab == 'cheapest'">
              <b> Total: ${{ carpark.totalFee }}</b>
            </h3>
            <h4 v-if="this.userOrigin != ''">
              <u>{{ carpark.distance_km }},</u>
              <u>{{ carpark.duration_mins }} </u>
              away from you
            </h4>
          </ion-card-header>
        </ion-card>
      </ion-grid>
      <ion-row class="ion-justify-content-center ion-padding"  v-if="pageTab == 'cheapest'">
        <ion-button shape="round" expand="block" @click="setDateTimeOpen(true)"
          >Select Date and Time</ion-button
        >
      </ion-row>

      <ion-modal :is-open="dateTimeModal" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title class="ion-text-center"> Date and Time</ion-title>

            <ion-buttons slot="start">
              <ion-button @click="setDateTimeOpen(false)">
                <ion-icon :icon="arrowBackOutline"></ion-icon>
              </ion-button>
            </ion-buttons>
          </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
          <ion-label position="stacked"> Booking Date:</ion-label>
          <ion-datetime
            presentation="date"
            v-model="bookingDate"
          ></ion-datetime>

          <ion-label position="stacked"> Start Time:</ion-label>
          <ion-datetime presentation="time" v-model="startTime"></ion-datetime>

          <ion-label position="stacked"> End Time:</ion-label>
          <ion-datetime presentation="time" v-model="endTime"></ion-datetime>

          <ion-row
            class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom"
          >
            <ion-button shape="round" @click="confirmDateTime()"
              >Confirm</ion-button
            >
          </ion-row>
        </ion-content>
      </ion-modal>
    </ion-content>
  </ion-page>
</template>
<ion-content class="ion-padding"></ion-content>

<script>
import { arrowBackOutline } from "ionicons/icons";
import {
  IonPage,
  IonHeader,
  IonTitle,
  IonContent,
  IonToolbar,
  IonButtons,
  IonButton,
  IonBackButton,
  IonCard,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonSearchbar,
  IonList,
  IonItem,
  IonSelect,
  IonSelectOption,
  IonImg,
  IonGrid,
  IonLabel,
  IonRadio,
  IonRadioGroup,
  IonModal,
  IonDatetime,
  IonIcon,
  IonRow,
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
// import { Geolocation } from "@capacitor/geolocation";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
    IonButtons,
    IonButton,
    IonBackButton,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonSearchbar,
    IonList,
    IonItem,
    IonSelect,
    IonSelectOption,
    IonImg,
    IonGrid,
    IonLabel,
    IonRadio,
    IonRadioGroup,
    IonModal,
    IonDatetime,
    IonIcon,
    IonRow,
  },
  setup() {
    return { arrowBackOutline };
  },
  data() {
    return {
      selectedLocation: "",
      carparksArray: [],
      cheapestCarparks: [],
      pageTab: "all",
      dateTimeModal: false,

      //setting peak hours. can make it such that admin can change this value. value in 24 hours.
      startPeak: "09:00:00",
      endPeak: "17:00:00",

      userOrigin: "",
      combinedLatLang: "",
      googleMapDistanceUrl: "",

      // for cheapest carparks
      startTime: "",
      endTime: "",
      bookingDate: "",
    };
  },
  methods: {
    confirmDateTime() {
      this.setDateTimeOpen(false);
      // const startTimeFormatted = this.startTime.substring(11, 19)
      // const endTimeFormatted = this.endTime.substring(11, 19)
      const bookingDateFormatted = this.bookingDate.substring(0, 10);
      // const startDateTime = new Date(bookingDateFormatted + " " + this.startTime.substring(11, 19)).getDay()
      const startDateTime = new Date(
        bookingDateFormatted + " " + this.startTime.substring(11, 19)
      );
      const endDateTime = new Date(
        bookingDateFormatted + " " + this.endTime.substring(11, 19)
      );

      // getting the hours
      const url = "http://127.0.0.1:5003/carparks";
      axios
        .get(url)
        .then((response) => {
          this.carparksArray = response.data.data.carparks;
          let fee = 0
          for (const eachCarpark of response.data.data.carparks) {
          // add carpark lots vacacy
            eachCarpark["availableLots"] =
              eachCarpark.maxCapacity - eachCarpark.currentCapacity;

          // weekend
            if (startDateTime == 6 || startDateTime == 0) {
              console.log("weekend");
              // for (const eachCarpark of response.data.data.carparks) {
                // if booking start and end in peak
                if (
                  endDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime >
                    new Date(bookingDateFormatted + " " + this.startPeak)
                ) {
                  const duration =
                    Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                  fee = duration * eachCarpark.hourlyweekendpeak;
                }

                // if booking start in non peak and end in peak
                else if (
                  endDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime <
                    new Date(bookingDateFormatted + " " + this.startPeak)
                ) {
                  const peakFee =
                    (Math.floor(
                      (new Date(bookingDateFormatted + " " + this.startPeak) -
                        startDateTime) /
                        3600000
                    ) +
                      1) *
                    eachCarpark.hourlyweekendpeak;
                  const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * eachCarpark.hourlyweekendnonpeak;
                  fee = peakFee + nonPeakFee;
                }

                // if booking start in peak and end in non peak
                else if (
                  endDateTime >
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak)
                ) {
                  const peakFee =
                    (Math.floor(
                      (new Date(bookingDateFormatted + " " + this.endPeak) -
                        startDateTime) /
                        3600000
                    ) +
                      1) *
                    eachCarpark.hourlyweekendpeak;
                  const nonPeakFee =
                    (Math.floor(
                      (endDateTime -
                        new Date(bookingDateFormatted + " " + this.endPeak)) /
                        3600000
                    ) +
                      1) *
                    eachCarpark.hourlyweekendnonpeak;
                  fee = peakFee + nonPeakFee;
                }

                // if booking start and end in non peak
                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                else {
                  const duration =
                    Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                  fee = duration * eachCarpark.hourlyweekendnonpeak;
                }
                eachCarpark["totalFee"] = fee
                console.log(eachCarpark)
              
            }

          // weekday
            else {
              console.log("weekday");
              // for (const eachCarpark of response.data.data.carparks) {
                // if booking start and end in peak
                if (
                  endDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime >
                    new Date(bookingDateFormatted + " " + this.startPeak)
                ) {
                  const duration =
                    Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                  fee = duration * eachCarpark.hourlyweekdaypeak;
                }

                // if booking start in non peak and end in peak
                else if (
                  endDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime <
                    new Date(bookingDateFormatted + " " + this.startPeak)
                ) {
                  const peakFee =
                    (Math.floor(
                      (new Date(bookingDateFormatted + " " + this.startPeak) -
                        startDateTime) /
                        3600000
                    ) +
                      1) *
                    eachCarpark.hourlyweekdaypeak;
                  const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * eachCarpark.hourlyweekdaynonpeak;
                  fee = peakFee + nonPeakFee;
                }

                // if booking start in peak and end in non peak
                else if (
                  endDateTime >
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak)
                ) {
                  const peakFee =
                    (Math.floor(
                      (new Date(bookingDateFormatted + " " + this.endPeak) -
                        startDateTime) /
                        3600000
                    ) +
                      1) *
                    eachCarpark.hourlyweekdaypeak;
                  const nonPeakFee =
                    (Math.floor(
                      (endDateTime -
                        new Date(bookingDateFormatted + " " + this.endPeak)) /
                        3600000
                    ) +
                      1) *
                    eachCarpark.hourlyweekdaynonpeak;
                  fee = peakFee + nonPeakFee;
                }

                // if booking start and end in non peak
                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                else {
                  const duration =
                    Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                  fee = duration * eachCarpark.hourlyweekdaynonpeak;
                }

              
            }
            eachCarpark["totalFee"] = fee
          }
          console.log(this.carparksArray)
         
          this.carparksArray.sort(function (a, b) {
            const keyA = a.totalFee;
            const keyB = b.totalFee;
            if (keyA < keyB) return -1;
            if (keyA > keyB) return 1;
            return 0;
          });

          this.carparksArray = this.carparksArray.slice(0, 4);
        })
        .catch((error) => {
          console.log(error.message);
        });

      // this.bookingDate.getDay()
    },
    setDateTimeOpen(isOpen) {
      this.dateTimeModal = isOpen;
    },
    resetState() {
      if (this.pageTab == "all") {
        this.userOrigin = "";
        this.selectedLocation = "";
        this.getCarparks();
      }
    },
    pushLog(msg) {
      this.selectedLocation = msg;
    },
    getCarparks() {
      this.googleMapDistanceUrl =
        "https://maps.googleapis.com/maps/api/distancematrix/json?origins=";
      this.combinedLatLang = "";

      const url = "http://127.0.0.1:5003/carparks";
      axios
        .get(url)
        .then((response) => {
          this.carparksArray = response.data.data.carparks;
          for (const eachCarpark of response.data.data.carparks) {
            eachCarpark["availableLots"] =
              eachCarpark.maxCapacity - eachCarpark.currentCapacity;
            this.combinedLatLang +=
              eachCarpark.latitude + "," + eachCarpark.longitude + "|";
          }

          if (this.selectedLocation == "") {
            console.log("no location selected");
          } else {
            if (this.selectedLocation == "orchard") {
              this.userOrigin = "1.3064433533620563,103.83276247871694";
            } else if (this.selectedLocation == "yishun") {
              this.userOrigin = "1.4304060903894582, 103.83515323243753";
            } else if (this.selectedLocation == "somerset") {
              this.userOrigin = "1.3016313961551784, 103.83849995957749";
            }

            this.googleMapDistanceUrl +=
              this.userOrigin +
              "&destinations=" +
              this.combinedLatLang.slice(0, -1) +
              "&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI";
            this.calculateDistance();
          }
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    calculateDistance() {
      axios
        .get(this.googleMapDistanceUrl)
        .then((response) => {
          const destinations = response.data.rows[0].elements;

          for (let i = 0; i < this.carparksArray.length; i++) {
            // this.carparksArray[i]["distance_km"] = (destinations[i].distance.value / 1000).toPrecision(2)
            // this.carparksArray[i]["duration_mins"] = (destinations[i].duration_in_traffic.value / 60).toPrecision(2)
            this.carparksArray[i]["distance_km"] =
              destinations[i].distance.text;
            this.carparksArray[i]["distance_km_value"] =
              destinations[i].distance.value;
            this.carparksArray[i]["duration_mins"] =
              destinations[i].duration_in_traffic.text;
          }

          this.carparksArray.sort(function (a, b) {
            const keyA = a.distance_km_value;
            const keyB = b.distance_km_value;
            if (keyA < keyB) return -1;
            if (keyA > keyB) return 1;
            return 0;
          });

          this.carparksArray = this.carparksArray.slice(0, 4);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },

  mounted() {
    this.getCarparks();
    // this.confirmDateTime();
  },
});
</script>

<style scoped>
.addPaddingBottom {
  padding-bottom: 300px;
}
/* iOS places the subtitle above the title */
/* ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
}
ion-img::part(image) {
  width: 100%; /* or whatever value */
/* you can set the height value too */
/* } */
</style>
