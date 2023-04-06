<template>
  <base-layout needToolBar="y" pageTitle="Carpark Analytics">
    <ion-grid>
      <h6>Price Forecasting Analysis</h6>
      <div class="chart-container">
        <canvas id="myChart"></canvas>
      </div>
      
      <div class="ion-align-items-center">
        <h6>8 Carparks</h6>
          <GChart
            type="PieChart"
            :data="PieChartData"
            :options="PieChartoptions"
          />
      </div>

      <div class="ion-align-items-center">
        <h6>Subscription Plans</h6>
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

      <ion-row class="ion-align-items-center">
        <ion-col>
          <h3>No. of bookings per location</h3>
          <GChart
            type="Map"
            :data="MapChartData"
            :options="MapChartOptions"
            :settings="settings"
          />
        </ion-col>
      </ion-row>

      <!-- <div class="ion-padding-top">
        <ion-button expand="block" href="/"> Logout </ion-button>
      </div> -->
    </ion-grid>
  </base-layout>
</template>

<script>
import { IonGrid } from "@ionic/vue";
import Chart from 'chart.js/auto';
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
      ColumnChartData: [["Subscription Plan", "No. of Subscribers", { role: 'style' }]],
      LineChartData: [["Time", "Number of bookings"]],
      BarChartData: [['Month','Revenue']],
      // MapChartData: [['Lat','Long', 'No. of Bookings']],
      MapChartData: [['Places', 'No. of Bookings', 'Marker']],
      PieChartoptions: {
        // title: "% of bookings per location",
        pieHole: 0.1,
        // width: 400,
        // height: 400
      },
      ColumnChartOptions: {
        // title: "No. of bookings per subscription",
        legend: { position: "bottom" },
        colors: ['green']
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
      MapChartOptions: {
        // region: 'SG',
        // displayMode: 'markers',
        // datalessRegionColor: 'lightblue',
        // colorAxis: {colors: ['green','gray', 'red']},
        // enableRegionInteractivity: true,
        mapType: 'terrain',
        zoomLevel: 16,
        showTooltip: true,
        showInfoWindow: true,
        useMapTypeControl: true,
        icons: {
          blue: {
            normal:   '../assets/icon/Icons-Land-Vista-Map-Markers-Map-Marker-Ball-Azure.48.png',
            selected: '../assets/icon/Icons-Land-Vista-Map-Markers-Map-Marker-Ball-Right-Azure.48.png'
          },
          green: {
            normal:   '../assets/icon/Icons-Land-Vista-Map-Markers-Map-Marker-Ball-Chartreuse.48.png',
            selected: '../assets/icon/Icons-Land-Vista-Map-Markers-Map-Marker-Ball-Right-Chartreuse.48.png'
          },
          pink: {
            normal:   '../assets/icon/Icons-Land-Vista-Map-Markers-Map-Marker-Ball-Pink.48.png',
            selected: '../assets/icon/Icons-Land-Vista-Map-Markers-Map-Marker-Ball-Right-Pink.48.png'
          }
        }
      },
      settings: {
        // packages: ['geochart']
        packages: ['map'],
        mapsApiKey: 'AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI'
      }
    };
  },
  methods: {
    getPieChart() {
      const locations = [];
      const count = {};
      let pieData = [];
      const url = "http://13.55.33.68:5001/bookings";
      
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
      const plans = {'1': 0, '2': 0}
      let columnData = [];
      const url = "http://13.55.33.68:5005/subs";

      axios
        .get(url)
        .then((response) => {
          columnData = response.data.data.subscriptions;
          console.log(columnData)
          for (let i = 0; i < columnData.length; i++) {
            for (const plan in plans) {
              if (plan == columnData[i]['subsTypeID']) {
                plans[plan] += 1;
              }
            }
          }

          for (const plan in plans){
            if (plan == '1'){
              this.ColumnChartData.push(["Just for you", plans[plan], 'color: lightgreen'])
            } else {
              this.ColumnChartData.push(["Monthly Plan", plans[plan], 'color: orange'])
            }
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
      const url = "http://13.55.33.68:5001/bookings";

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
      const url = "http://13.55.33.68:5006/transaction";

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
      // const finals = {};
      let MapData = [];
      // let carparkData = [];
      const url = "http://13.55.33.68:5001/bookings";
      // const url2 = "http://13.55.33.68:5003/carparks"
      
      axios
        .get(url)
        .then((response) => {
          MapData = response.data.data.bookings;
          // console.log(pieData)
          // Store the locations into a list first (without duplicates)
          for (let i = 0; i < MapData.length; i++){
            if (!locations.includes(MapData[i]["bookingLocation"])) {
              locations.push(MapData[i]["bookingLocation"])
            }
          }
          // console.log(locations)
          // Next, store them into a dict with value 0
          for (let i = 0; i < locations.length; i++){
            count[locations[i]] = 0;
          }
          console.log(count)
          // count the number of bookings per location 
          for (let i = 0; i < MapData.length; i++){
            for (const cnt in count){
              if (cnt == MapData[i]["bookingLocation"]){
                count[cnt] += 1;
              }
            }
          }

          // console.log(count)
          // Add it in to the chart
          for (const cnnt in count){
            if (cnnt == "*SCAPE") {
              if (count[cnnt] > 20) {
                this.MapChartData.push([cnnt + " shopping mall", "No. of bookings: " + count[cnnt], 'pink'])
              } else if (count[cnnt] >= 10 && count[cnnt] <= 20) {
                this.MapChartData.push([cnnt + " shopping mall", "No. of bookings: " + count[cnnt], 'blue'])
              } else {
                this.MapChartData.push([cnnt + " shopping mall", "No. of bookings: " + count[cnnt], 'green'])
              }
            } else {
              if (count[cnnt] > 20) {
                this.MapChartData.push([cnnt, "No. of bookings: " + count[cnnt], 'pink'])
              } else if (count[cnnt] >= 10 && count[cnnt] <= 20) {
                this.MapChartData.push([cnnt, "No. of bookings: " + count[cnnt], 'blue'])
              } else {
                this.MapChartData.push([cnnt, "No. of bookings: " + count[cnnt], 'green'])
              }
            }
            
          }

          // axios
          // .get(url2)
          // .then((response) => {
          //   carparkData = response.data.data.carparks
          //   console.log(carparkData)

          //   for (let i = 0; i < carparkData.length; i++){
          //     for (const cnt in count){
          //       if (cnt == carparkData[i]['carparkName']){
          //         finals[carparkData[i]['carparkName']] = [carparkData[i]['latitude'],carparkData[i]['longitude'],count[cnt]];
          //       }
          //     }
          //   }
          //   console.log(finals)

          //   // Add it in to the chart
          //   for (const final in finals){
          //     this.MapChartData.push([finals[final][0],finals[final][1],"No. of bookings: " + finals[final][2]])
          //   }

          //   return this.MapChartData;
          // })
          // .catch((error) => {
          //   console.log(error.message);
          // })
        })
        .catch((error) => {
          console.log(error.message);
        }); 
    },
    async getRevenueData() {
      try {
        const response = await axios.get('http://13.55.33.68:5001/forecastbooking');
        const revenueData = response.data;
        // console.log(revenueData)

        const today = new Date();
        const pastData = revenueData.past.filter(d => new Date(d.month) < today).slice(-3);
        const futureData = revenueData.future.filter(d => new Date(d.month) >= today).slice(0, 3);
        // console.log(pastData)
        // console.log(futureData)

        // const data = {
        //   labels: pastData.concat(futureData).map(d => d.month),
        //   datasets: [{
        //     label: 'Revenue',
        //     data: pastData.concat(futureData).map(d => d.revenue),
        //     borderColor: 'rgb(54, 162, 235)',
        //     fill: false,
        //     borderDash: pastData.concat(futureData).map((d, i) => i >= pastData.length ? [5, 5] : []),
        //   }]
        // };
        const data = {
          labels: pastData.concat(futureData).map(d => d.month),
          datasets: [
            {
              label: 'Actual',
              data: pastData.map(d => d.revenue),
              borderColor: 'rgb(54, 162, 235)',
              fill: false,
              // borderDash: pastData.map((d, i) => i >= pastData.length ? [5, 5] : []),
            },
            {
              label: 'Predicted',
              // lineDashType: "dash",
              data: pastData.concat(futureData).map(d => d.revenue),
              borderColor: 'red',
              fill: false,
              borderDash: [5, 5],
            }
          ]
        };

        const config = {
          type: 'line',
          data: data,
          options: {
            responsive: true,
            plugins: {
              legend: {
                display: true,
                position: 'bottom'
              },
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
          },
        };

        new Chart(document.getElementById('myChart'),config);

      } catch (error) {
        console.error(error);
      }
    },
    // getSimulator() {
    //   this.carparksArraySimu = [];

    //   let url = "http://13.55.33.68:5004/getCarpark/1";
    //   axios
    //     .post(url, {
    //       requesttype: 1000,
    //       carparkid: 1,
    //     })
    //     .then((response) => {
    //       this.carparksArraySimu.push({
    //         data: response.data.data,
    //         image: "assets/images/paragon.jpg",
    //         availableLots:
    //           response.data.data.lotbalancehourly -
    //           response.data.data.lotusehourly,
    //       });

    //       url = "http://13.55.33.68:5004/getCarpark/2";
    //       axios
    //         .post(url, {
    //           requesttype: 1000,
    //           carparkid: 2,
    //         })
    //         .then((response) => {
    //           this.carparksArraySimu.push({
    //             data: response.data.data,
    //             image: "assets/images/ion.jpg",
    //             availableLots:
    //               response.data.data.lotbalancehourly -
    //               response.data.data.lotusehourly,
    //           });
    //           url = "http://13.55.33.68:5004/getCarpark/3";
    //           axios
    //             .post(url, {
    //               requesttype: 1000,
    //               carparkid: 3,
    //             })
    //             .then((response) => {
    //               this.carparksArraySimu.push({
    //                 data: response.data.data,
    //                 image: "assets/images/takashimaya.jpeg",
    //                 availableLots:
    //                   response.data.data.lotbalancehourly -
    //                   response.data.data.lotusehourly,
    //               });
    //               url = "http://13.55.33.68:5004/getCarpark/4";
    //               axios
    //                 .post(url, {
    //                   requesttype: 1000,
    //                   carparkid: 4,
    //                 })
    //                 .then((response) => {
    //                   this.carparksArraySimu.push({
    //                     data: response.data.data,
    //                     image: "assets/images/tangs.jpg",
    //                     availableLots:
    //                       response.data.data.lotbalancehourly -
    //                       response.data.data.lotusehourly,
    //                   });
    //                   url = "http://13.55.33.68:5004/getCarpark/5";
    //                   axios
    //                     .post(url, {
    //                       requesttype: 1000,
    //                       carparkid: 5,
    //                     })
    //                     .then((response) => {
    //                       this.carparksArraySimu.push({
    //                         data: response.data.data,
    //                         image: "assets/images/Wheelock.png",
    //                         availableLots:
    //                           response.data.data.lotbalancehourly -
    //                           response.data.data.lotusehourly,
    //                       });
    //                       url = "http://13.55.33.68:5004/getCarpark/6";
    //                       axios
    //                         .post(url, {
    //                           requesttype: 1000,
    //                           carparkid: 6,
    //                         })
    //                         .then((response) => {
    //                           this.carparksArraySimu.push({
    //                             data: response.data.data,
    //                             image: "assets/images/313.jpg",
    //                             availableLots:
    //                               response.data.data.lotbalancehourly -
    //                               response.data.data.lotusehourly,
    //                           });

    //                           url = "http://13.55.33.68:5004/getCarpark/7";
    //                           axios
    //                             .post(url, {
    //                               requesttype: 1000,
    //                               carparkid: 7,
    //                             })
    //                             .then((response) => {
    //                               this.carparksArraySimu.push({
    //                                 data: response.data.data,
    //                                 image: "assets/images/scape.jpg",
    //                                 availableLots:
    //                                   response.data.data.lotbalancehourly -
    //                                   response.data.data.lotusehourly,
    //                               });
    //                               url = "http://13.55.33.68:5004/getCarpark/8";
    //                               axios
    //                                 .post(url, {
    //                                   requesttype: 1000,
    //                                   carparkid: 8,
    //                                 })
    //                                 .then((response) => {
    //                                   this.carparksArraySimu.push({
    //                                     data: response.data.data,
    //                                     availableLots:
    //                                       response.data.data.lotbalancehourly -
    //                                       response.data.data.lotusehourly,
    //                                     image: "assets/images/wisma.jpeg",
    //                                   });
    //                                 });
    //                             });
    //                         });
    //                     });
    //                 });
    //             });
    //         });
    //     });
    // },
  },
  // Calls function on page load
  mounted() {
    // this.getSimulator();
    this.getPieChart();
    this.getColumnChart();
    this.getLineChart();
    this.getBarChart();
    this.getGeoChart();
    this.getRevenueData();
  },
});
</script>

<style scoped>
.chart-container {
  display: flex;
  justify-content: center;
  margin: auto;
  /* height: 50vh;
  width: 80vw; */
}
</style>
