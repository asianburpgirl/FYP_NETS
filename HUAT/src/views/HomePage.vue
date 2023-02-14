<template>
  <base-layout needToolBar="y">
    <div>
      <ion-grid>
        <ion-row>
          <ion-col>
            <h2>Percentage of bookings per location</h2>
            <GChart type="PieChart" :options="PieChartoptions" :data="PieChartData" />
          </ion-col>
          <ion-col>
            <h2>Number of bookings per location</h2>
            <GChart type="BarChart" :data="BarChartData" :options="BarChartOptions" />
          </ion-col>
          <ion-col>
            <h2>Number of bookings per subscription</h2> 
            <GChart type="ColumnChart" :data="ColumnChartData" :options="ColumnChartOptions" />
          </ion-col>
        </ion-row>
      </ion-grid>
    </div>
  </base-layout>
</template>

<script lang="ts">
import { GChart } from 'vue-google-charts';
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
      BarChartData: [
        ['Booking Location', 'No. of Bookings']
      ],
      ColumnChartData: [
        ['Carpark Name', 'Subscription Plan', 'No. of Subscribers']
      ],
      PieChartoptions: {
        chart: {
          title: "Percentage of bookings per location",
          pieHole: 0.4,
        },
        // width: 400,
        // height: 400
      },
      BarChartOptions: {
        chart: {
          title: "Number of bookings per location",
          pieHole: 0.4,
        },
        // width: 400,
        // height: 400
      },
      ColumnChartOptions: {
        chart: {
          title: "Number of bookings per subscription",
          pieHole: 0.4,
        },
        // width: 400,
        // height: 400
      },
      userData: {}
    }
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData") || '{}');
    },
    getPieChart() {
      let pieData = [];

      const url = "http://localhost:5001/bookings";
      axios.get(url)
      .then(response => {
        pieData = response.data.data.bookings;
        for (let i = 0; i < pieData.length; i ++) {
          this.PieChartData.push([pieData[i]['bookingLocation'],pieData[i]['bookingID']])
        }
        return pieData
        // console.log(response.data.data.bookings)
      })
      .catch(error => {
        console.log(error.message)
      })
    },
    getBarChart() {
      let barData = [];
      const url = "http://localhost:5003/carparks";

      axios.get(url)
      .then(response => {
        barData = response.data.data.carparks;
        for(let i = 0; i < barData.length; i++) {
          this.BarChartData.push([barData[i]['carparkName'],barData[i]['currentCapacity']])
        }
        return barData
      })
      .catch(error => {
        console.log(error.message)
      })
    },
    getColumnChart() {
      let columnData = [];
      const url = "http://localhost:5003/carparks";
      
      axios.get(url)
      .then(response => {
        columnData = response.data.data.carparks;
        console.log(columnData)
        // console.log(columnData)
        for (let i=0; i < columnData.length; i++) {
          this.ColumnChartData.push([columnData[i]['carparkName'],parseInt(columnData[i]['hourlyweekdaypeak']),
          parseInt(columnData[i]['hourlyweekdaynonpeak'])])
        }
        return columnData
      })
      .catch(error => {
        console.log(error.message)
      })
    },
  },
  // Calls function on page load
  mounted(){
    this.loadUserData();
    this.getBarChart();
    this.getPieChart();
    this.getColumnChart();
  }
});
</script>
