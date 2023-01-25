<template>
  <div>
    <h2>Vue Js Google line Charts Demo</h2>
    <GChart
      type="LineChart"
      :options="options"
      :data="collectionData"
    />  
    <ion-row class="ion-padding-top ion-justify-content-center">
        <ion-button shape="round" @click="getUser()">Create Charts</ion-button>
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
  name: "App",
  components: {
    GChart
  },
  data() {
    return {
      collectionData: [
        ["Day", "Guardians of the Galaxy", "The Avengers", "Transformers"],
        [1,  40.45, 90.5, 42.8],
        [2,  22.5, 68.4, 33.4],
        [3,  36.5, 47, 55.5],
        [4,  12.7, 23.8, 14.5],
        [5,  10.9, 44.5, 10.3],
        [6,   7.8, 14.5,  6.7],
        [7,   8.6, 11.2,  19.6]
      ],
      options: {
        chart: {
          title: "First 7 days movies collection",
          subtitle: "In millions of dollars (USD)"
        },
        width: 1000,
        height: 400
      }
    };
  },
  methods: {
    getUser() {
        let config = {}

        config = {
          method: 'get',
          url: 'http://localhost:5001/bookings',
        }

        const response =  axios(config)
            .then(function (response) {
                localStorage.setItem("bookingData", JSON.stringify(response.data.data));
                // console.log(response.data);
                return response.data
            })
            .catch(function (error) {
                console.log(error);
            });

        return response;
    }
  }
});
</script>