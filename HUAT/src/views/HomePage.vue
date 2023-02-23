<template>
  <base-layout needToolBar="y" pageTitle="Home">
  
  <!-- this is for ease of development -->
  <ion-grid> 
    <ion-row class="ion-justify-content-center"> 
      <ion-button color="dark" @click="changeRole('Admin')"> Admin </ion-button>
      <ion-button color="dark" @click="changeRole('User')"> User </ion-button>
  </ion-row>
  </ion-grid>

    <!-- admin home -->
    <ion-grid v-if="userRole == 'Admin'">

      <ion-row class="ion-align-items-center">
        <ion-col>
          <h4 class="ion-text-center">Percentage of bookings per location</h4>
          <GChart
            type="PieChart"
            :options="PieChartoptions"
            :data="PieChartData"
          />
        </ion-col>
      </ion-row>

      <ion-row class="ion-align-items-center">
        <ion-col>
          <h4 class="ion-text-center">Current Capacity per location</h4>
          <GChart
            type="BarChart"
            :data="BarChartData"
            :options="BarChartOptions"
          />
        </ion-col>
      </ion-row>

      <ion-row class="ion-align-items-center">
        <ion-col>
          <h4 class="ion-text-center">Number of bookings per subscription</h4>
          <GChart
            type="ColumnChart"
            :data="ColumnChartData"
            :options="ColumnChartOptions"
          />
        </ion-col>
      </ion-row>
    </ion-grid>

    <!-- User home -->
    <ion-grid v-if="userRole == 'User'">
      <ion-row class="ion-align-items-center">
        <ion-col>
          <h4 class="ion-text-start">Your upcoming Booking</h4>
        </ion-col>
      </ion-row>
    </ion-grid>
  </base-layout>
</template>

<script>
import { IonGrid, IonCol, IonRow, IonButton } from "@ionic/vue";
import { GChart } from "vue-google-charts";
import { defineComponent } from "vue";
import axios from "axios";
export default defineComponent({
  components: {
    GChart,
    IonGrid,
    IonCol,
    IonRow,
    IonButton
  },
  data() {
    return {
      userRole: "",

      PieChartData: [["Bookings", "Percentage of bookings"]],
      BarChartData: [["Booking Location", "No. of Bookings"]],
      ColumnChartData: [
        ["Carpark Name", "Subscription Plan", "No. of Subscribers"],
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
      userData: {},
    };
  },
  methods: {
    changeRole(role) {
      this.userRole = role;
    },
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData") || "{}");
      this.userRole = this.userData.role;
    },
    getPieChart() {
      let pieData = [];

      const url = "http://localhost:5001/bookings";
      axios
        .get(url)
        .then((response) => {
          pieData = response.data.data.bookings;
          // console.log(pieData)
          for (let i = 0; i < pieData.length; i++) {
            this.PieChartData.push([
              pieData[i]["bookingLocation"],
              pieData[i]["bookingID"],
            ]);
          }
          return pieData;
          // console.log(response.data.data.bookings)
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getBarChart() {
      let barData = [];
      const url = "http://localhost:5003/carparks";

      axios
        .get(url)
        .then((response) => {
          barData = response.data.data.carparks;
          for (let i = 0; i < barData.length; i++) {
            this.BarChartData.push([
              barData[i]["carparkName"],
              barData[i]["currentCapacity"],
            ]);
          }
          return barData;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getColumnChart() {
      let columnData = [];
      const url = "http://localhost:5003/carparks";

      axios
        .get(url)
        .then((response) => {
          columnData = response.data.data.carparks;
          // console.log(columnData)
          for (let i = 0; i < columnData.length; i++) {
            this.ColumnChartData.push([
              columnData[i]["carparkName"],
              columnData[i]["hourlyweekdaypeak"],
              columnData[i]["hourlyweekdaynonpeak"],
            ]);
          }
          return columnData;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  // Calls function on page load
  mounted() {
    this.loadUserData();
    this.getBarChart();
    this.getPieChart();
    this.getColumnChart();
  },
});
</script>
