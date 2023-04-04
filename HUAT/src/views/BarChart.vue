<template>
    <div>
      <h2>Business Analytics - Number of bookings per location</h2>
      <!-- <GChart
        type="ColumnChart"
        :options="options"
        :data="data"
      /> -->
      
    </div>
  </template>
   
  <script>
  // import { GChart } from "vue-google-charts";
  import { defineComponent } from "vue";
  import {IonRow,} from "@ionic/vue";
  import axios from 'axios';
  
  export default {
    name: "BarChart",
    components: {
      // GChart
    },
    data() {
      return {
        data: [
           ['Carpark Name', 'No. of Bookings']
          //  ['ION Orchard', 25],
          //  ['Plaza Singapura', 30],
        ],
        options: {
          width: 1000,
          height: 500
        }
      };
    },
    mounted(){
      this.getBookings()
    },
    methods: {
      getBookings() {
        let bookingData = [];
        const url = "http://13.55.33.68:5001/bookings";

        axios.get(url).then(response => {
          bookingData = response.data.data.bookings;
          console.log(bookingData)
          for(let i = 0; i < bookingData.length; i++) {
            console.log(bookingData[i]['bookingLocation'])
            this.data.push([bookingData[i]['bookingLocation'],bookingData[i]['currentCapacity']])
          }
          return bookingData
        })
      .catch(error => {
        console.log(error.message)
        })
      }
    }
  };
  </script>