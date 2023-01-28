<template>
    <div>
      <h2>Business Analytics - Number of bookings per location</h2>
      <GChart
        type="ColumnChart"
        :options="options"
        :data="data"
      />    
    </div>
  </template>
   
  <script>
  import { GChart } from "vue-google-charts";
  import { defineComponent } from "vue";
  import {IonRow,} from "@ionic/vue";
  import axios from 'axios';

  export default {
    name: "BarChart",
    components: {
      GChart
    },
    data() {
      return {
        data: [
           ['Carpark Name', 'No. of Bookings', { role: 'style' }],
           ['Funan', 10, '#6B58E2'],
           ['ION Orchard', 25, '#00B28F'],
           ['Plaza Singapura', 30, '#F8D12F'],
        ],
        options: {
          width: 1000,
          height: 500
        }
      };
    }
  };
  </script>