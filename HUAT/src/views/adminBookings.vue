<template>
  <base-layout needToolBar="y" pageTitle="Bookings">
    <ion-grid>
      <h4 class="ion-text-start">List of Bookings</h4>
      <ion-grid>
        <ion-row>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">Booking Reference</ion-col>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">Location</ion-col>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">UserID</ion-col>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">Status</ion-col>
          <!-- <ion-col size="3" size-md="3" size-lg="3">Balance</ion-col> -->
        </ion-row>
        <ion-row v-for="booking in bookingList" :key="booking.bookingID">
          <ion-col size="3" size-md="3" size-lg="3">{{booking.bookingRef}}</ion-col>
          <ion-col size="3" size-md="3" size-lg="3">{{booking.locationName}}</ion-col>
          <ion-col size="3" size-md="3" size-lg="3">{{booking.userID}}</ion-col>
          <ion-col size="3" size-md="3" size-lg="3">{{booking.status}}</ion-col>
        </ion-row>
      </ion-grid>
    </ion-grid>
  </base-layout>
</template>

<script>
import { IonGrid, IonRow, IonCol } from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
export default defineComponent({
  components: {
    IonGrid, IonRow, IonCol
  },
  data() {
    return {
      bookingList: []
    };
  },
  methods: {
    getUsers() {
      const url = "http://13.55.33.68:5001/bookings";
      axios
        .get(url)
        .then((response) => {
          // console.log(response.data.data);
          this.bookingList = response.data.data.bookings
          console.log(this.bookingList)
          
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  mounted(){
    this.getUsers();
  }
});
</script>

<style scoped>
ion-col {
  background-color: #9cc8fa;
  border: solid 1px #fff;
  text-align: center;
  font-size: 11px;
}

.row-header {
  background-color: #4099ff;
  border: solid 1px #fff;
  font-weight: 700;
  text-align: center;
}
</style>
