<template>
  <base-layout needToolBar="y" pageTitle="Carpark Analytics">
    <ion-grid>
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
          <h4 class="ion-text-center">Number of bookings per subscription</h4>
          <GChart
            type="ColumnChart"
            :data="ColumnChartData"
            :options="ColumnChartOptions"
          />
        </ion-col>
      </ion-row>
      

      <!-- <ion-row class="ion-align-items-center">
        <ion-col>
          <h4 class="ion-text-center">Number of bookings per subscription</h4>
          <GChart
            type="LineChart"
            :data="LineChartData"
            :options="ColumnChartOptions"
          />
        </ion-col>
      </ion-row> -->

      <div class="ion-padding-top">
        <ion-button expand="block" href="/">
        Logout
      </ion-button>
      </div>
      <admin-bottom-tab></admin-bottom-tab>
    </ion-grid>
  </base-layout>
</template>

<script>
import {
  IonGrid,
  IonRow,
  IonCol,
  IonButton
} from "@ionic/vue";
import { GChart } from "vue-google-charts";
import { defineComponent } from "vue";
import adminBottomTab from './adminBottomTab.vue';
import axios from "axios";
import adminBottomTabVue from "./adminBottomTab.vue";
export default defineComponent({
  components: {
    GChart,
    IonGrid,
    IonRow,
    IonCol,
    IonButton
  },
  data() {
    return {
      carparksArraySimu: [],
      PieChartData: [["Bookings", "Percentage of bookings"]],
      LineChartData: [["Carpark Location", "Time"]],
      ColumnChartData: [
        ["Carpark Name", "Subscription Plan", "No. of Subscribers"],
      ],
      PieChartoptions: {
        title: "Percentage of bookings per location",
        pieHole: 0.1,
        // width: 400,
        // height: 400
      },
      LineChartOptions: {
        title: "Number of bookings per location",
        legend: {
          position: "bottom",
        },
        // width: 400,
        // height: 400
      },
      ColumnChartOptions: {
        title: "Number of bookings per subscription",
        legend: {
          position: "bottom",
        },
        // width: 400,
        // height: 400
      },
    };
  },
  methods: {
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
    getLineChart() {
      let LineData = [];
      const url = "http://localhost:5001/bookings";

      axios
        .get(url)
        .then((response) => {
          LineData = response.data.data.carparks;
          for (let i = 0; i < LineData.length; i++) {
            this.LineChartData.push([
              LineData[i]["bookingLocation"],
              LineData[i]["bookingAmt"],
            ]);
          }
          return LineData;
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
    getSimulator() {
      this.carparksArraySimu = [];

      let url = "http://127.0.0.1:5004/getCarpark/1";
      axios
        .post(url, {
          requesttype: 1000,
          carparkid: 1,
        })
        .then((response) => {
          this.carparksArraySimu.push({
            data: response.data.data,
            image: "assets/images/paragon.jpg",
            availableLots:
              response.data.data.lotbalancehourly -
              response.data.data.lotusehourly,
          });

          url = "http://127.0.0.1:5004/getCarpark/2";
          axios
            .post(url, {
              requesttype: 1000,
              carparkid: 2,
            })
            .then((response) => {
              this.carparksArraySimu.push({
                data: response.data.data,
                image: "assets/images/ion.jpg",
                availableLots:
                  response.data.data.lotbalancehourly -
                  response.data.data.lotusehourly,
              });
              url = "http://127.0.0.1:5004/getCarpark/3";
              axios
                .post(url, {
                  requesttype: 1000,
                  carparkid: 3,
                })
                .then((response) => {
                  this.carparksArraySimu.push({
                    data: response.data.data,
                    image: "assets/images/takashimaya.jpeg",
                    availableLots:
                      response.data.data.lotbalancehourly -
                      response.data.data.lotusehourly,
                  });
                  url = "http://127.0.0.1:5004/getCarpark/4";
                  axios
                    .post(url, {
                      requesttype: 1000,
                      carparkid: 4,
                    })
                    .then((response) => {
                      this.carparksArraySimu.push({
                        data: response.data.data,
                        image: "assets/images/tangs.jpg",
                        availableLots:
                          response.data.data.lotbalancehourly -
                          response.data.data.lotusehourly,
                      });
                      url = "http://127.0.0.1:5004/getCarpark/5";
                      axios
                        .post(url, {
                          requesttype: 1000,
                          carparkid: 5,
                        })
                        .then((response) => {
                          this.carparksArraySimu.push({
                            data: response.data.data,
                            image: "assets/images/Wheelock.png",
                            availableLots:
                              response.data.data.lotbalancehourly -
                              response.data.data.lotusehourly,
                          });
                          url = "http://127.0.0.1:5004/getCarpark/6";
                          axios
                            .post(url, {
                              requesttype: 1000,
                              carparkid: 6,
                            })
                            .then((response) => {
                              this.carparksArraySimu.push({
                                data: response.data.data,
                                image: "assets/images/313.jpg",
                                availableLots:
                                  response.data.data.lotbalancehourly -
                                  response.data.data.lotusehourly,
                              });

                              url = "http://127.0.0.1:5004/getCarpark/7";
                              axios
                                .post(url, {
                                  requesttype: 1000,
                                  carparkid: 7,
                                })
                                .then((response) => {
                                  this.carparksArraySimu.push({
                                    data: response.data.data,
                                    image: "assets/images/scape.jpg",
                                    availableLots:
                                      response.data.data.lotbalancehourly -
                                      response.data.data.lotusehourly,
                                  });
                                  url = "http://127.0.0.1:5004/getCarpark/8";
                                  axios
                                    .post(url, {
                                      requesttype: 1000,
                                      carparkid: 8,
                                    })
                                    .then((response) => {
                                      this.carparksArraySimu.push({
                                        data: response.data.data,
                                        availableLots:
                                          response.data.data.lotbalancehourly -
                                          response.data.data.lotusehourly,
                                        image: "assets/images/wisma.jpeg",
                                      });
                                    });
                                });
                            });
                        });
                    });
                });
            });
        });
    },
  },
  // Calls function on page load
  mounted() {
    this.getSimulator();
    this.getLineChart();
    this.getPieChart();
    this.getColumnChart();
  },
});
</script>

<style scoped></style>
