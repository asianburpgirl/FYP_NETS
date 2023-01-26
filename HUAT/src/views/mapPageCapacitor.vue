<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-title>Map</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <capacitor-google-map id="map"></capacitor-google-map>
      <div>
        <a>
          Longitude: {{ currentLocation.lng }} Latitude:
          {{ currentLocation.lat }}
        </a>
      </div>
    </ion-content>
  </ion-page>
</template>

<script>
import { GoogleMap } from "@capacitor/google-maps";
import { Geolocation } from "@capacitor/geolocation";

import { defineComponent } from "vue";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
} from "@ionic/vue";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
  },
  data() {
    return {
      currentLocation: { lat: 1.3521, lng: 103.8198 },
    };
  },

  mounted() {
    this.createMap();
    this.getCurrentLocation();
  },

  methods: {
    getCurrentLocation() {
      const location = Geolocation.getCurrentPosition();
      location
        .then((result) => {
          this.currentLocation = {
            lat: result.coords.latitude,
            lng: result.coords.longitude,
          };
        })
        .catch((err) => {
          // console.log(err)
          return err;
        });
    },

    async createMap() {
      try {
        const mapRef = document.getElementById("map");

        const newMap = await GoogleMap.create({
          id: "my-map", // Unique identifier for this map instance
          element: mapRef, // reference to the capacitor-google-map element
          apiKey: "AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI", // Your Google Maps API Key
          config: {
            center: {
              // The initial position to be rendered by the map
              lat: 1.3521,
              lng: 103.8198,
            },
            zoom: 10, // The initial zoom level to be rendered by the map
          },
        });

        const markers = await newMap.addMarkers([
          {
            title: "Plaza Sing",
            snippet: "68 Orchard Rd, Singapore 238839",
            coordinate: {
              lat: 1.3007033161990564,
              lng: 103.84528924122294,
            },
          },

          {
            coordinate: {
              lat: 1.2958419970838684,
              lng: 103.85841587741238,
            },
          },
        ]);

        const listener = await newMap.setOnMarkerClickListener()
        const currentLocation = await newMap.enableCurrentLocation()
        // enableCurrentLocation(enabled: boolean) => Promise<void>
          // setOnMapClickListener(callback?: MapListenerCallback<MapClickCallbackData> | undefined) => Promise<void>

      }
      catch (e) {
        console.log(e);
      }
    },
  
    // async addListeners() {
    addListeners() {
      // await this.newMap.setOnMarkerClickListener((event) => {
        this.newMap.setOnMarkerClickListener((event) => {
        console.log(event);
      });
    },
  },
});
</script>

<style scoped>
capacitor-google-map {
  display: inline-block;
  width: 450px;
  height: 600px;
}
</style>
