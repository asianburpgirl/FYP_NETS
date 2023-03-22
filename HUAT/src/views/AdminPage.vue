<template>
  <base-layout needToolBar="y" pageTitle="Carpark Analytics">
    <ion-grid>
      <ion-row class="ion-align-items-center">
        <ion-col>
          <GChart
            type="PieChart"
            :data="PieChartData"
            :options="PieChartoptions"
          />
        </ion-col>
      </ion-row>

      <ion-row class="ion-align-items-center">
        <ion-col>
          <GChart
            type="ColumnChart"
            :data="ColumnChartData"
            :options="ColumnChartOptions"
          />
        </ion-col>
      </ion-row>

      <ion-row class="ion-align-items-center">
        <ion-col>
          <GChart
            type="LineChart"
            :data="LineChartData"
            :options="LineChartOptions"
          />
        </ion-col>
      </ion-row>

      <ion-row class="ion-align-items-center">
        <ion-col>
          <GChart
            type="ColumnChart"
            :data="BarChartData"
            :options="BarChartOptions"
          />
        </ion-col>
      </ion-row>

      <div class="ion-padding-top">
        <ion-button expand="block" href="/">
        Logout
      </ion-button>
      </div>
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
import axios from "axios";
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
      ColumnChartData: [["Carpark Name", "Subscription Plan", "No. of Subscribers"]],
      LineChartData: [["Time", "Number of bookings"]],
      BarChartData: [['Month','Revenue']],
      PieChartoptions: {
        title: "Percentage of bookings per location",
        pieHole: 0.1,
        // width: 400,
        // height: 400
      },
      ColumnChartOptions: {
        title: "Number of bookings per subscription",
        legend: { position: "bottom" },
        // width: 400,
        // height: 400
      },
      LineChartOptions: {
        title: "Peak Time Analysis",
        legend: { position: "bottom" },
        // width: 400,
        // height: 400
      },
      BarChartOptions: {
        title: "Revenue per month",
        legend: { position: "bottom" },
        // width: 400,
        // height: 400
      }
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
    getLineChart() {
      const timeAxis = { '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0,
      '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0};
      let LineData = [];
      const url = "http://localhost:5001/bookings";

      axios
        .get(url)
        .then((response) => {
          LineData = response.data.data.bookings;
          console.log(LineData)
          for (let i = 0; i < LineData.length; i++) {
            for (const num in timeAxis){
              if (num == parseInt(LineData[i]["bookingStartDateTime"].slice(17, 20))){
                timeAxis[num] += 1;
              }
            }
          }
          console.log(timeAxis)
          for (const number in timeAxis){
            this.LineChartData.push([number + ":00", timeAxis[number]])
          }
          return this.LineChartData;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getBarChart() {
      const months = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0, 'Jul': 0, 'Aug': 0, 'Sep': 0, 'Nov': 0, 'Oct': 0, 'Dec': 0}
      let BarData = [];
      const url = "http://localhost:5006/transaction";

      axios
        .get(url)
        .then((response) => {
          BarData = response.data.data.transactions;
          console.log(BarData)
          for (let i = 0; i < BarData.length; i++) {
            for (const month in months) {
              if (month == BarData[i]["transDate"].slice(8, 11) && BarData[i]["transType"] == "topup") {
                months[month] += BarData[i]["amount"]
              }
            }
          }
          console.log(months)
          for (const mon in months){
            this.BarChartData.push([mon, months[mon]])
          }
          return this.BarChartData;
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
    this.getPieChart();
    this.getColumnChart();
    this.getLineChart();
    this.getBarChart();
  },
});
</script>

<style scoped></style>
