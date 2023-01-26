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

      <capacitor-google-map id="map"></capacitor-google-map>

      <div>
        {{ userLocation }}
      </div>

      <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" @click="makeBoooking()">Book</ion-button>
      </ion-row>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
//   IonRefresher,
//   IonRefresherContent,
} from "@ionic/vue";
import { GoogleMap } from "@capacitor/google-maps";
import { Geolocation } from "@capacitor/geolocation";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    // IonRefresher,
    // IonRefresherContent,
  },
//   setup() {
//     const handleRefresh = () => {
//       setTimeout(() => {
//         // Any calls to load data go here
        
//       }, 2000);
//     };
//     return { handleRefresh };
//   },

  data() {
    return {
      userLocation: { lat: 1.3521, lng: 103.8198 },
    };
  },

  //  const createMap = async () => {
  // const mapRef = document.getElementById('map');

  // const newMap = await GoogleMap.create({
  //   id: 'my-map', // Unique identifier for this map instance
  //   element: mapRef, // reference to the capacitor-google-map element
  //   apiKey: 'YOUR_API_KEY_HERE', // Your Google Maps API Key
  //   config: {
  //     center: {
  //       // The initial position to be rendered by the map
  //       lat: 33.6,
  //       lng: -117.9,
  //     },
  //     zoom: 8, // The initial zoom level to be rendered by the map
  //   },
  // });

  mounted() {
    this.createMap();
    this.getCurrentLocation();
  },

  methods: {
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

      const url = "http://127.0.0.1:5001/bookings/7"; // hardcoded
      axios
        .post(url, {
          bookingDate: currentDateTimeFormatted,
          bookingLocation: "addresstest1234", // hardcoded
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    //get Live location
    getCurrentLocation() {
      const location = Geolocation.getCurrentPosition();
      location
        .then((result) => {
          this.userLocation = {
            lat: result.coords.latitude,
            lng: result.coords.longitude,
          };
          console.log(this.userLocation);
        })
        .catch((err) => {
          // console.log(err)
          return err;
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
          zoom: 10, // The initial zoom level to be rendered by the map
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
  width: 300px;
  height: 600px;
}
</style>
