<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/tabs/bookings"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Map</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" class="ion-padding">
      <!--   <ion-refresher slot="fixed" @ionRefresh="handleRefresh()">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher> -->

      <capacitor-google-map id="map"></capacitor-google-map>

      <!-- first popup page to open when user click on marker. User can choose either to book or subscribe to this carpark. button will open up respective popup  -->
      <ion-modal :is-open="choiceOpen" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title class="ion-text-center">
              {{ clickedMarkerName }}</ion-title
            >

            <ion-buttons slot="start">
              <ion-button @click="setChoiceOpen(false)">
                <ion-icon :icon="arrowBackOutline"></ion-icon>
              </ion-button>
            </ion-buttons>
          </ion-toolbar>
        </ion-header>

        <ion-content class="ion-padding-top ion-padding">
          <h2>
            Address: <u> {{ clickedMarkerAddress }}</u>
          </h2>
          <h1>
            Distance from your current location:
            {{ distanceToLocation_km }} km
            <br />
            Time taken from your current location:
            {{ timeToLocation_mins }} mins
            <br />
            Booking Amount: ${{ bookingAmount }}
          </h1>

          <ion-button
            shape="round"
            @click="
              setBookingOpen(true);
              setChoiceOpen(false);
            "
            expand="block"
            size="large"
            >Book</ion-button
          >
          <ion-button
            shape="round"
            @click="
              setSubscriptionOpen(true);
              setChoiceOpen(false);
            "
            expand="block"
            size="large"
            >Subscription</ion-button
          >
        </ion-content>
      </ion-modal>

      <!-- when user select to book a carpark at the location.  -->
      <ion-modal :is-open="bookingIsOpen" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title> Booking at {{ clickedMarkerName }}</ion-title>
            <ion-buttons slot="start">
              <ion-button
                @click="
                  setBookingOpen(false);
                  setChoiceOpen(true);
                "
              >
                <ion-icon :icon="arrowBackOutline"></ion-icon>
              </ion-button>
            </ion-buttons>
          </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
          <ion-item>
            Distance from your current location:
            {{ distanceToLocation_km }} km
            <br />
            <br />
            Time taken from your current location:
            {{ timeToLocation_mins }} mins
            <br />

            <ion-label position="stacked"> Booking Date:</ion-label>
            <ion-datetime
              presentation="date"
              v-model="bookingDate"
              :min = minDate
              
            ></ion-datetime>

            <ion-label position="stacked"> Start Time:</ion-label>
            <ion-datetime
              presentation="time"
              v-model="startTime"  
            ></ion-datetime>

            <ion-label position="stacked"> End Time:</ion-label>
            <ion-datetime presentation="time" v-model="endTime"></ion-datetime>

            <!-- 
            <ion-datetime presentation="time"></ion-datetime>
            <ion-datetime presentation="date"></ion-datetime>

            <ion-label position="stacked">End Time:</ion-label>
            <ion-datetime v-model="endTime"></ion-datetime> -->
          </ion-item>

          <ion-row
            class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom"
          >
            <ion-button shape="round" @click="makeBoooking()">Book</ion-button>
          </ion-row>
        </ion-content>
      </ion-modal>

      <!-- when booking is successful, to show success popup -->
      <ion-modal :is-open="bookingSuccessIsOpen" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title>Success!</ion-title>
          </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
          <ion-row>
            Your booking at {{ clickedMarkerName }} is successful!
            <br />
            These are the details: Carpark Location:
            <ul>
              <li>Carpark Location: {{ clickedMarkerAddress }}</li>
              <li>Booking Date: {{ bookingDate }}</li>

              <li>Start Time: {{ startTime }}</li>
              <li>End Time: {{ endTime }}</li>
            </ul>
          </ion-row>

          <ion-row
            class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom"
          >
            <ion-button shape="round" @click="setBookingSuccessOpen(false)"
              >Back to Map</ion-button
            >
            <ion-button shape="round" @click="routeToMyBookings()"
              >View My Bookings</ion-button
            >
          </ion-row>
        </ion-content>
      </ion-modal>

      <!-- when user select to subscription plans at the carpark location.  -->
      <ion-modal :is-open="subscriptionIsOpen" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title>Subsciption plan </ion-title>
            <ion-buttons slot="start">
              <ion-button
                @click="
                  setSubscriptionOpen(false);
                  setChoiceOpen(true);
                "
              >
                <ion-icon :icon="arrowBackOutline"></ion-icon>
              </ion-button>
            </ion-buttons>
          </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
          <h1>{{ clickedMarkerName }}</h1>

          <h3>
            Address: <u> {{ clickedMarkerAddress }} test</u>
          </h3>

          <ion-item>
            <ion-label>Subscription Type</ion-label>
            <ion-select placeholder="Type">
              <ion-select-option value="seasonal">Seasonal</ion-select-option>
              <ion-select-option value="complimentary"
                >Complimentary</ion-select-option
              >
              <ion-select-option value="hourly">Hourly</ion-select-option>
            </ion-select>
          </ion-item>

          <ion-list>
            <ion-item> Weekday Peak: $12/month </ion-item>
            <ion-item> Weekday Non-Peak: $10/month </ion-item>
            <ion-item> Weekend Peak: $20/month </ion-item>
            <ion-item> Weekend Non-Peak: $15/month </ion-item>
          </ion-list>

          <ion-row
            class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom"
          >
            <ion-button shape="round" @click="buySubscription()"
              >Buy Subscription</ion-button
            >
          </ion-row>
        </ion-content>
      </ion-modal>
    </ion-content>
  </ion-page>
</template>


<script>
import { defineComponent, ref } from "vue";
import axios from "axios";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonModal,
  IonRow,
  IonList,
  IonButtons,
  IonBackButton,
  IonButton,
  IonDatetime,
  IonIcon,
  IonItem,
  IonLabel,
  IonSelect,
  IonSelectOption,

  //   IonRefresher,
  //   IonRefresherContent,
} from "@ionic/vue";
import { GoogleMap } from "@capacitor/google-maps";
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
    IonButtons,
    IonBackButton,
    IonButton,
    IonDatetime,
    IonIcon,
    IonItem,
    IonLabel,
    IonSelect,
    IonSelectOption,
    IonRow,
    IonList,
    // IonRefresher,
    // IonRefresherContent,
  },

  setup() {
    return { arrowBackOutline };
  },
  data() {
    return {
      bookingIsOpen: false,
      bookingSuccessIsOpen: false,
      subscriptionSuccessIsOpen: false,
      subscriptionIsOpen: false,
      choiceOpen: false,

      clickedMarkerName: "",
      clickedMarkerAddress: "",
      distanceToLocation_km: "",
      timeToLocation_mins: "",
      startTime: "",
      endTime: "",
      minDate: "",
      bookingDate: "",

      userData: {},
      userOrigin: "1.2958419970838684,103.85841587741238",
      userDestinations: "1.3007033161990564,103.84528924122294",
      bookingAmount: "5.20",
    };
  },

  mounted() {
    this.createMap();
    this.getCurrentDateTime()
  },

  methods: {
    getCurrentDateTime(){
      const currentDateTime = new Date()
      const date = ("0" +currentDateTime.getDate()).slice(-2)
      const month = ("0" +currentDateTime.getMonth()+1).slice(-2)

      this.minDate =  currentDateTime.getFullYear() +"-" + month+"-" + date +"T"+
      currentDateTime.getHours() + ":" + currentDateTime.getMinutes() + ":" + currentDateTime.getSeconds()
      console.log("TIME",this.minDate)
    },
    routeToMyBookings() {
      this.setBookingSuccessOpen(false);
      this.$router
        .push({
          path: "/viewBooking",
        })
        .then(() => {
          this.$router.go(0);
        });
      location.reload();
    },
    buySubscription() {
      console.log("here");
    },
    async getCurrentLocation() {
      const coordinates = await Geolocation.getCurrentPosition();

      return coordinates;
    },
    calculateDistance() {
      this.getCurrentLocation().then((coordinates) => {
        this.userOrigin =
          coordinates.coords.latitude.toString() +
          "," +
          coordinates.coords.longitude.toString();
        // console.log("Your location:" + this.userOrigin);
        const url =
          "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" +
          this.userOrigin +
          "&destinations=" +
          this.userDestinations +
          "&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI";

        axios
          .get(url)
          .then((response) => {
            const distance_km = (
              response.data.rows[0].elements[0].distance.value / 1000
            ).toPrecision(2);
            const duration_mins = (
              response.data.rows[0].elements[0].duration_in_traffic.value / 60
            ).toPrecision(2);
            // console.log(
            //   "distance: ",
            //   distance_km + "duration: ",
            //   duration_mins
            // );
            this.distanceToLocation_km = distance_km;
            this.timeToLocation_mins = duration_mins;
          })
          .catch((error) => {
            console.log(error.message);
          });
      });
    },
    setChoiceOpen(isOpen) {
      this.choiceOpen = isOpen;
    },
    setBookingOpen(isOpen) {
      this.bookingIsOpen = isOpen;
    },
    setBookingSuccessOpen(isOpen) {
      this.bookingSuccessIsOpen = isOpen;
    },
    setSubscriptionOpen(isOpen) {
      this.subscriptionIsOpen = isOpen;
    },
    makeBoooking() {
      const currentDateTime = new Date();
      const date = currentDateTime.getDate();
      const month = currentDateTime.getMonth() + 1;
      const year = currentDateTime.getFullYear();

      const hour = currentDateTime.getHours();
      const min = currentDateTime.getMinutes();
      const sec = currentDateTime.getSeconds();

      const currentDateTimeFormatted =
        year + "-" + month + "-" + date + " " + hour + ":" + min + ":" + sec;

      this.bookingDate = this.bookingDate.substring(0, 10);

      const startDateTimeFormatted =
        this.bookingDate.substring(0, 10) +
        " " +
        this.startTime.substring(11, 19);
      this.startTime = this.startTime.substring(11, 19);

      const endDateTimeFormatted =
        this.bookingDate.substring(0, 10) +
        " " +
        this.endTime.substring(11, 19);
      this.endTime = this.endTime.substring(11, 19);

      this.userData = JSON.parse(localStorage.getItem("userData"));
      const userID = this.userData.userID;

      const url = "http://127.0.0.1:5001/bookings";

      axios
        .post(url, {
          bookingDateTime: currentDateTimeFormatted,
          bookingLocation: this.clickedMarkerName,
          locationName: this.clickedMarkerAddress,
          bookingStartDateTime: startDateTimeFormatted,
          bookingEndDateTime: endDateTimeFormatted,
          userID: userID,
          status: "Booked",
          bookingAmt: this.bookingAmount,
        })
        .then((response) => {
          this.deductFromUser(response.data.data.bookingID)
          this.setBookingOpen(false); // close booking window
          this.setBookingSuccessOpen(true); // open booking sucess window
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    deductFromUser(bookingID){
      // updateBalance
      const url = "http://127.0.0.1:5001/updateBalance/" + bookingID
      axios
        .put(url, {
          bookingID: bookingID,
        })
        .then((response) => {
          // console.log(response)
        })
        .catch((error) => {
          console.log(error.message);
        });

    },

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
      const url = "http://127.0.0.1:5003/carparks";
      axios
        .get(url)
        .then((response) => {
          // console.log(response.data.data.carparks)
          for (const eachCarpark of response.data.data.carparks) {
            const markers =  newMap.addMarkers([
            //location 1
            {
              title: eachCarpark.carparkName,
              snippet: eachCarpark.carparkLocation,
              coordinate: {
                // lat: 1.3007033161990564,
                lat: eachCarpark.latitude,
                lng: eachCarpark.longitude,
                // lng: 103.84528924122294,
              },
            },
        
      ]);
          }
         
      // listener for user click
      const markerListener = newMap.setOnMarkerClickListener((event) => {
        this.getCurrentDateTime()
        this.clickedMarkerName = event.title;
        this.clickedMarkerAddress = event.snippet;

        this.userDestinations =
          event.latitude.toString() + "," + event.longitude.toString();

        this.setChoiceOpen(true);
        this.calculateDistance();
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
  width: 330px;
  height: 690px;
}
.addPaddingBottom {
  padding-bottom: 300px;
}

h2 {
  padding-bottom: 120px;
}
</style>
