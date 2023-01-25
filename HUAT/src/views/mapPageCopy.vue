<template>
  <base-layout pageTitle="Map" needToolBar="y">
    <GMapMap
      :center="center"
      :zoom="10"
      map-type-id="terrain"
      style="width: 350px; height: 600px"
    >
      <GMapMarker
        :key="index"
        v-for="(marker, index) in markers"
        :position="marker.position"
        :clickable="true"
        @click="openMarker(marker.id)"
      >
        <GMapInfoWindow
          :closeclick="true"
          @closeclick="openMarker(null)"
          :opened="openedMarkerID === marker.id"
        >
          <div>
            <h1>{{ marker.name }}</h1>
            <h5>
              {{ marker.location }}
              Avaiable slots: {{ marker.carparkSlotsTotalAvailable }} / {{ marker.carparkSlotsTotal }}
            </h5>
          </div>
        </GMapInfoWindow>
      </GMapMarker>
    </GMapMap>

    <div>
      <a> Longitude: {{ center.lng }} Latitude: {{ center.lat }} </a>
    </div>
  </base-layout>
</template>

<script lang="ts">
import { Geolocation } from "@capacitor/geolocation";

import { defineComponent } from "vue";
// import axios from "axios";

export default defineComponent({
  // lat: 1.4505518,
  // lng: 103.825558, // my home

  data() {
    return {
      openedMarkerID: null,
      center: { lat: 1.3521, lng: 103.8198 },
      markers: [
        {
          id: 1,
          name: "Plaza Sing",
          location: "68 Orchard Rd, Singapore 238839",
          carparkSlotsTotal: 44,
          carparkSlotsTotalAvailable: 10,
          position: {
            lat: 1.3007033161990564,
            lng: 103.84528924122294, // plaza sing
            // 1.2958419970838684, 103.85841587741238 suntec
          },
        },
        {
          id: 2,
          name: "Suntec",
          location: "1 Raffles Blvd, Singapore 039593",
          carparkSlotsTotal: 40,
          carparkSlotsTotalAvailable: 15,
          position: {
            lat: 1.2958419970838684,
            lng: 103.85841587741238, // suntec
          },
        },
      ],
    };
  },
  mounted() {
    this.getLiveMap();
  },
  methods: {
    openMarker(id: any) {
      this.openedMarkerID = id;
    },
    getLiveMap() {
      const location = Geolocation.getCurrentPosition();
      console.log(location);
      location
        .then((result) => {
          this.center = {
            lat: result.coords.latitude,
            lng: result.coords.longitude,
          };

          // this.latitude = result.coords.latitude;
          // this.longitude = result.coords.longitude;
          // console.log(this.latitude);
          // console.log(this.longitude);
        })
        .catch((err) => {
          // console.log(err)
          return err;
        });
    },
  },

  // methods: {
  //   async getStreetAddressFrom(lat: string, long: string) {
  //     try {
  //       const { data } = await axios.get(
  //         "https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
  //           lat +
  //           "," +
  //           long +
  //           "&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI"
  //       );
  //       if (data.error_message) {
  //         console.log(data.error_message);
  //       } else {
  //         this.address = data.results[0].formatted_address;
  //       }
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   },
  //   locatorButtonPressed() {
  //     navigator.geolocation.getCurrentPosition(
  //       (position) => {
  //         this.getStreetAddressFrom(
  //           position.coords.latitude,
  //           position.coords.longitude
  //         );
  //       },
  //       (error) => {
  //         console.log(error.message);
  //       }
  //     );
  //   },
  // },
});
</script>

<style scoped></style>
