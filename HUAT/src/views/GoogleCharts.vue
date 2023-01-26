<template>
  <div>
    <h2>Percentage of bookings according to locations</h2>
    <GChart
      type="PieChart"
      :options="options"
      :data="collectionData"
    />  
    <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" @click="getBooking()">Create Charts</ion-button>
    </ion-row>
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
      collectionData: [],
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
  methods: {
    getBooking() {
        let config = {}
        let bookingData = this.collectionData;

        config = {
          method: 'get',
          url: 'http://localhost:5001/bookings',
        }

        const response =  axios(config)
            .then(function (response) {
                bookingData = JSON.stringify(response.data.data.bookings);
                // console.log(bookingData);
                return bookingData
            })
            .catch(function (error) {
                console.log(error);
            });

        return response;
    }
  }
});
</script>