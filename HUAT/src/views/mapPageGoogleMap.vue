<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-title>Mappppp</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <capacitor-google-map id="map"></capacitor-google-map>

      <div>
        {{ userLocation }}
      </div>
      
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
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
  },
  data() {
    return {
      userLocation: { lat: 1.3521, lng: 103.8198 },
    };
  },

  mounted() {
    this.getCurrentLocation()
  },

  methods: {
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
            this.createMap(this.userLocation)

            
        })
        .catch((err) => {
          console.log(err)
        });
    },

     async createMap(location: any) {
      const mapRef = document.getElementById("map");
      const newMap =  GoogleMap.create({
        id: "my-map", // Unique identifier for this map instance
        element: mapRef!, // reference to the capacitor-google-map element
        apiKey: "AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI", // Your Google Maps API Key
        config: {
          center: {
            // The initial position to be rendered by the map
            lat: 1.2962823,
            lng: 103.8500894 // smu
          },
          zoom: 10, // The initial zoom level to be rendered by the map
        },
      });
      
      const markers = await (await newMap).addMarkers([
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
          title: "Plaza Sing",
          snippet: "68 Orchard Rd, Singapore 238839",
          coordinate: {
            lat: 1.2958419970838684,
            lng: 103.85841587741238,
          },
          },
        //user location
        {
          title: "User Location",
          snippet: "You",
        coordinate: location
        },
      ]); 

       const markerListener = (await newMap).setOnMarkerClickListener((event) => {
        console.log(event);
       });
       const myLocationListener = (await newMap).setOnMyLocationButtonClickListener((event) => {
           console.log(event);
        console.log("mylocation")
       });
  
         const myLocationLienableTrafficstener = (await newMap).enableTrafficLayer(true);
         const enableCurrentLocation = (await newMap).enableCurrentLocation(true);
         
      return newMap;
      },

       //add user location marker
      userMarker(newMap: any) {
        newMap.addMarker(
        //location 1
        {
          title: "User Location",
          snippet: "You",
              coordinate: {
            lat: 1.2962823,
            lng: 103.8500894
              }, 
        },
      );

      } 
  },
});
</script>

<style>
capacitor-google-map {
  display: inline-block;
  width: 350px;
  height: 600px;
}
</style>

