<template>
  <base-layout needToolBar="y">
    <div>
      <h2>Percentage of bookings according to locations</h2>
      <!-- <GChart type="PieChart" :options="PieChartOptions" :data="PieChartData" /> 
      <GChart type="ColumnChart" :data="ColumnChartData" :options="ColumnChartOptions" /> -->
    </div>
  </base-layout>
</template>

<script lang="ts">
// import { GChart } from "vue-google-charts";
import { defineComponent } from "vue";
import axios from 'axios';

export default defineComponent({
  name: "GoogleCharts",
  components: {
    // GChart
  },
  data() {
    return {
      PieChartData: [
        ['Bookings', 'Percentage of bookings']
      ],
      ColumnChartData: [
        ['Year', 'Season Parking', 'Hourly Parking'],
        ['2014', 1000, 400],
        ['2015', 1170, 460],
        ['2016', 660, 1120],
        ['2017', 1030, 540],
      ],
      PieChartoptions: {
        chart: {
          title: "Percentage of bookings according to locations",
          pieHole: 0.4,
        },
        width: 1000,
        height: 400
      },
      ColumnChartOptions: {
        chart: {
          title: "Percentage of bookings according to locations",
          pieHole: 0.4,
        },
        width: 1000,
        height: 400
      },
      userData: {}
    }
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData") || '{}');
    },
    getCharts() {
      let bookingData = [];

      const url = "http://localhost:5001/bookings";
      axios.get(url)
      .then(response => {
        bookingData = response.data.data.bookings;
        // console.log(bookingData)
        for (let i = 0; i < bookingData.length; i ++) {
          this.PieChartData.push([bookingData[i]['bookingLocation'],bookingData[i]['bookingID']])
        }
        return bookingData
        // console.log(response.data.data.bookings)
        })
      .catch(error => {
        console.log(error.message)
        })
    }
  },
  // Calls function on page load
  mounted(){
    this.loadUserData();
    this.getCharts();
  }
});
</script>
