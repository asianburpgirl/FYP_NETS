<template>
  <div>
    <h2>Percentage of bookings according to locations</h2>
    <GChart
      type="PieChart"
      :options="options"
      :data="collectionData"
    />  
    <!-- <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" @click="getBookings()">Create Charts</ion-button>
    </ion-row> -->
  </div>
</template>
 
<script>
import { GChart } from "vue-google-charts";
import { defineComponent } from "vue";
import {
    IonRow,
} from "@ionic/vue";
import axios from 'axios';

export default defineComponent({
  name: "GoogleCharts",
  components: {
    GChart
  },
  data() {
    return {
      collectionData: [
        ['Bookings', 'Percentage of bookings']
      ],
      options: {
        chart: {
          title: "Percentage of bookings according to locations",
          pieHole: 0.4,
        },
        width: 1000,
        height: 400
      }
    };
  },
    mounted(){
      this.getBookings()
    },
  methods: {
    getBookings() {
      let bookingData = [];

      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5001/bookings";
      axios.get(url)
      .then(response => {
        bookingData = response.data.data.bookings;
        // console.log(bookingData)
        for (let i = 0; i < bookingData.length; i ++) {
          this.collectionData.push([bookingData[i]['bookingLocation'],bookingData[i]['bookingID']])
        }
        return bookingData
        // console.log(response.data.data.bookings)
        })
      .catch(error => {
        console.log(error.message)
        })
    }
  }
});
</script>