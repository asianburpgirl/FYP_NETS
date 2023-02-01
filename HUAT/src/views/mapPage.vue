<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-title>Map</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <!--   <ion-refresher slot="fixed" @ionRefresh="handleRefresh()">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher> -->
      Distance from your current location:
            {{ distanceToLocation_km }} 
            <br>
            Time taken from your current location:
            {{ timeToLocation_mins }}

      <capacitor-google-map id="map"></capacitor-google-map>

      <ion-modal :is-open="isOpen" class="ion-padding">
        <ion-header>
          <ion-toolbar>
            <ion-title>{{ clickedMarkerName }}</ion-title>
            <ion-buttons slot="end">
              <ion-button @click="setOpen(false)">Close</ion-button>
              <!-- <ion-button @click="setOpen(false)">Close</ion-button> need to reload map cause its not showing after -->
            </ion-buttons>
          </ion-toolbar>
        </ion-header>
        <ion-content class="ion-padding">
          <ion-item>
            Distance from your current location:
            {{ distanceToLocation_km }} km
            <br>
            <br>
            Time taken from your current location:
            {{ timeToLocation_mins }} mins
            <br>
            
          <ion-label position="stacked">Start Time:</ion-label>
          <ion-datetime  v-model="startTime"></ion-datetime>

           <ion-label position="stacked">End Time:</ion-label>
          <ion-datetime  v-model="endTime"></ion-datetime>
        </ion-item>
          
        <ion-row class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom" >
        <ion-button shape="round" @click="makeBoooking()" >Book</ion-button>
      </ion-row>
        </ion-content>
      </ion-modal>
      
    </ion-content>
  </ion-page>
</template>

<script lang="ts">

import { defineComponent, ref } from "vue";
import axios from "axios";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonModal,
  IonButtons,
  IonButton,
  IonDatetime
  //   IonRefresher,
  //   IonRefresherContent,
} from "@ionic/vue";
import { GoogleMap } from "@capacitor/google-maps";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonModal,
    IonButtons,
    IonButton,
    IonDatetime
    // IonRefresher,
    // IonRefresherContent,
  },
  data() {
    return {
      isOpen: false,
      clickedMarkerName: "",
      clickedMarkerAddress: "",
      distanceToLocation_km: "",
      timeToLocation_mins: "",
      startTime: "",
      endTime: "",
    };
  },

  mounted() {
    this.createMap();
    this.calculateDistance();
  },

  methods: {
    calculateDistance() {
      const url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=1.2958419970838684,103.85841587741238&destinations=1.3007033161990564,103.84528924122294&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI"; // hardcoded
      axios
        .get(url)
        .then((response) => {
          console.log(response.data);
          const distance_km = (response.data.rows[0].elements[0].distance.value / 1000).toPrecision(2);
          const duration_mins = (response.data.rows[0].elements[0].duration_in_traffic.value / 60).toPrecision(2);
          console.log("distance: ",distance_km)

          console.log( "duration: ", duration_mins)
          this.distanceToLocation_km = distance_km
          this.timeToLocation_mins = duration_mins
          
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    setOpen(isOpen: boolean) {
      this.isOpen = isOpen;
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

      const startDateTimeFormatted= this.startTime.substring(0,10) + " " + this.startTime.substring(11,19)
      const endDateTimeFormatted= this.endTime.substring(0,10) + " " + this.endTime.substring(11,19)

      const url = "http://127.0.0.1:5001/bookings"; // hardcoded
      axios
        .post(url, {
          bookingDate: currentDateTimeFormatted,
          bookingLocation:this.clickedMarkerName,
          locationName: this.clickedMarkerAddress, 
          startTime: startDateTimeFormatted,
          endTime:endDateTimeFormatted,
          userID: 1,
          status: "Booked"
        })
        .then((response) => {
          console.log(response.data);
          this.setOpen(false);
          this.$router.push({
        path: '/viewBooking',
          })
            .then(()=> {this.$router.go(0)});
      location.reload()
          
        })
        .catch((error) => {
          console.log(error.message);
        });
    },

    async createMap() {
      const mapRef = document.getElementById("map");
      const newMap = await GoogleMap.create({
        id: "my-map", // Unique identifier for this map instance
        element: mapRef!, // reference to the capacitor-google-map element
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
      const markers = await newMap.addMarkers([
        //location 1
        {
          title: "Plaza Sing",
          snippet: "68 Orchard Rd, Singapore 238839",
          coordinate: {
            lat: 1.3007033161990564,
            lng: 103.84528924122294,
          },
        },
        // location 2
        {
          title: "Suntec City",
          snippet: "3 Temasek Blvd, #1, #327-328, 038983",
          coordinate: {
            lat: 1.2958419970838684,
            lng: 103.85841587741238,
          },
        },
      ]);
      // listener for user click
      const markerListener = newMap.setOnMarkerClickListener((event) => {
        console.log(event);
        // console.log(event.latitude);
        // console.log(event.longitude);
        console.log(event.title);
        console.log(event.snippet)
        this.clickedMarkerName = event.title;
        this.clickedMarkerAddress = event.snippet;

        this.setOpen(true);
      });
      //add traffic data
      const trafficDataEnable = newMap.enableTrafficLayer(true);

      // enable current location
      const currentLocationEnable = newMap.enableCurrentLocation(true);
      return newMap;
    },
  },
});
</script>

<style>
capacitor-google-map {
  display: inline-block;
  width: 330px;
  height: 690px;
}
.addPaddingBottom{
  padding-bottom: 300px;
}
</style>
