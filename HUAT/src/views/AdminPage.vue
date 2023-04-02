<template>
  <base-layout needToolBar="y" pageTitle="Carpark Analytics">
    <ion-grid>
      <div class="chart-container">
        <h6>Price Forecasting Analysis</h6>
        <canvas id="myChart"></canvas>
      </div>
      <div class="ion-align-items-center">
        <h6>Top 8 Popular Carparks</h6>
          <GChart
            type="PieChart"
            :data="PieChartData"
            :options="PieChartoptions"
          />
      </div>

      <div class="ion-align-items-center">
        <h6>Most Popular Subscription Plans</h6>
          <GChart
            type="ColumnChart"
            :data="ColumnChartData"
            :options="ColumnChartOptions"
          />
      </div>

      <!-- <ion-row class="ion-align-items-center">
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
      </ion-row> -->

      <div class="ion-align-items-center">
          <h6>No. of bookings per location</h6>
          <GChart
            type="GeoChart"
            :data="GeoChartData"
            :options="GeoChartOptions"
            :settings="settings"
          />
      </div>

      <!-- <div class="ion-padding-top">
        <ion-button expand="block" href="/"> Logout </ion-button>
      </div> -->
    </ion-grid>
  </base-layout>
</template>

<script>
import { IonGrid } from "@ionic/vue";
import Chart from 'chart.js';
import { GChart } from "vue-google-charts";
import { defineComponent } from "vue";
import axios from "axios";
export default defineComponent({
  components: {
    GChart,
    IonGrid,
  },
  data() {
    return {
      carparksArraySimu: [],
      PieChartData: [["Bookings", "Percentage of bookings"]],
      ColumnChartData: [["Carpark Name", "Subscription Plan", "No. of Subscribers"]],
      LineChartData: [["Time", "Number of bookings"]],
      BarChartData: [['Month','Revenue']],
      GeoChartData: [['Places', 'No. of Bookings']],
      PieChartoptions: {
        title: "% of bookings per location",
        pieHole: 0.1,
        // width: 400,
        // height: 400
      },
      ColumnChartOptions: {
        title: "No. of bookings per subscription",
        legend: { position: "bottom" },
        colors: ['#ADD8E6', 'orange']
        // width: 400,
        // height: 400
      },
      LineChartOptions: {
        title: "Peak Time Analysis",
        legend: { position: "bottom" },
        colors: ['#e2431e']
        // width: 400,
        // height: 400
      },
      BarChartOptions: {
        title: "Revenue per month",
        legend: { position: "bottom" },
        colors: ['#90EE90']
        // width: 400,
        // height: 400
      },
      GeoChartOptions: {
        region: 'SG',
        displayMode: 'markers',
        datalessRegionColor: 'lightblue',
        colorAxis: {colors: ['green','gray', 'red']},
        enableRegionInteractivity: true,
        mapType: 'styledMap',
        // zoomLevel: 15,
        // showTooltip: true,
        // showInfoWindow: true,
        // useMapTypeControl: true,
      },
      settings: {
        packages: ['geochart'],
        mapsApiKey: 'AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI'
      }
    };
  },
  methods: {
    getPieChart() {
      const locations = [];
      const count = {};
      let pieData = [];
      const url = "http://localhost:5001/bookings";
      
      axios
        .get(url)
        .then((response) => {
          pieData = response.data.data.bookings;
          // console.log(pieData)
          // Store the locations into a list first (without duplicates)
          for (let i = 0; i < pieData.length; i++){
            if (!locations.includes(pieData[i]["bookingLocation"])) {
              locations.push(pieData[i]["bookingLocation"])
            }
          }
          // console.log(locations)
          // Next, store them into a dict with value 0
          for (let i = 0; i < locations.length; i++){
            count[locations[i]] = 0;
          }
          // console.log(count)
          // count the number of bookings per location 
          for (let i = 0; i < pieData.length; i++){
            for (const cnt in count){
              if (cnt == pieData[i]["bookingLocation"]){
                count[cnt] += 1;
              }
            }
          }
          // console.log(count)
          // Add it in to the chart
          for (const cnnt in count){
            this.PieChartData.push([cnnt, count[cnnt]])
          }
          return this.PieChartData;
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
          // console.log(LineData)
          for (let i = 0; i < LineData.length; i++) {
            for (const num in timeAxis){
              if (num == parseInt(LineData[i]["bookingStartDateTime"].slice(17, 20))){
                timeAxis[num] += 1;
              }
            }
          }
          // console.log(timeAxis)
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
          // console.log(BarData)
          for (let i = 0; i < BarData.length; i++) {
            for (const month in months) {
              if (month == BarData[i]["transDate"].slice(8, 11) && BarData[i]["transType"] == "topup") {
                months[month] += BarData[i]["amount"]
              }
            }
          }
          // console.log(months)
          for (const mon in months){
            this.BarChartData.push([mon, months[mon]])
          }
          return this.BarChartData;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getGeoChart() {
      const locations = [];
      const count = {};
      let GeoData = [];
      const url = "http://localhost:5001/bookings";
      
      axios
        .get(url)
        .then((response) => {
          GeoData = response.data.data.bookings;
          // console.log(pieData)
          // Store the locations into a list first (without duplicates)
          for (let i = 0; i < GeoData.length; i++){
            if (!locations.includes(GeoData[i]["bookingLocation"])) {
              locations.push(GeoData[i]["bookingLocation"])
            }
          }
          // console.log(locations)
          // Next, store them into a dict with value 0
          for (let i = 0; i < locations.length; i++){
            count[locations[i]] = 0;
          }
          // console.log(count)
          // count the number of bookings per location 
          for (let i = 0; i < GeoData.length; i++){
            for (const cnt in count){
              if (cnt == GeoData[i]["bookingLocation"]){
                count[cnt] += 1;
              }
            }
          }
          // console.log(count)
          // Add it in to the chart
          for (const cnnt in count){
            // if (cnnt == "*SCAPE") {
            //   this.GeoChartData.push([cnnt + " shopping mall", "No. of bookings: " + count[cnnt]])
            // } else {
            //   this.GeoChartData.push([cnnt, "No. of bookings: " + count[cnnt]])
            // }
            this.GeoChartData.push([cnnt, count[cnnt]])
          }
          return this.GeoChartData;
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
    async getRevenueData() {
      try {
        const response = await axios.get('http://127.0.0.1:5001/forecastbooking');
        const revenueData = response.data;

        const today = new Date();
        const pastData = revenueData.past.filter(d => new Date(d.month) < today).slice(-3);
        const futureData = revenueData.future.filter(d => new Date(d.month) >= today).slice(0, 3);

        const data = {
          labels: pastData.concat(futureData).map(d => d.month),
          datasets: [{
            label: 'Revenue',
            data: pastData.concat(futureData).map(d => d.revenue),
            borderColor: 'rgb(54, 162, 235)',
            fill: false,
          }]
        };

        const config = {
          type: 'line',
          data: data,
          options: {
            responsive: true,
            plugins: {
              legend: {
                display: false
              }
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Month'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Revenue ($)'
                }
              }
            },
            elements: {
              line: {
                borderDash: pastData.map(() => [5, 5]).concat(futureData.map(() => [])),
              },
            },
          },
        };


        const myChart = new Chart(
          document.getElementById('myChart'),
          config
        );
      } catch (error) {
        console.error(error);
      }
    }

    
    
  },
  // Calls function on page load
  mounted() {
    this.getSimulator();
    this.getPieChart();
    this.getColumnChart();
    this.getLineChart();
    this.getBarChart();
    this.getGeoChart();
    this.getRevenueData();
  },
});
</script>

<style scoped></style>
