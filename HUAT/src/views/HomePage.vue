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
                    <GChart type="PieChart" :options="PieChartoptions" :data="PieChartData" />
                </ion-col>
            </ion-row>
    
            <!-- <ion-row class="ion-align-items-center">
                                                                <ion-col>
                                                                    <h4 class="ion-text-center">Current Capacity per location</h4>
                                                                    <GChart type="BarChart" :data="BarChartData" :options="BarChartOptions" />
                                                                </ion-col>
                                                            </ion-row> -->
    
            <ion-row class="ion-align-items-center">
                <ion-col>
                    <h4 class="ion-text-center">Number of bookings per subscription</h4>
                    <GChart type="ColumnChart" :data="ColumnChartData" :options="ColumnChartOptions" />
                </ion-col>
            </ion-row>
        </ion-grid>
    
        <!-- User home -->
        <ion-grid v-if="userRole == 'User'">
            <h4 class="ion-text-start">Carparks Details</h4>
            
            
        </ion-grid>
    </base-layout>
</template>

<script>
import {
    IonButton,
    IonRow,
    IonCol,
    IonGrid,
} from "@ionic/vue";
import {
    GChart
} from "vue-google-charts";
import {
    defineComponent
} from "vue";
import axios from "axios";
export default defineComponent({
    components: {
        GChart,
        IonButton,
        IonRow,
        IonCol,
        IonGrid,
    },
    data() {
        return {
            userRole: "",
            userData: {},

            PieChartData: [
                ["Bookings", "Percentage of bookings"]
            ],
            BarChartData: [
                ["Booking Location", "No. of Bookings"]
            ],
            ColumnChartData: [
                ["Carpark Name", "Subscription Plan", "No. of Subscribers"],
            ],
            PieChartoptions: {
                title: "Percentage of bookings per location",
                pieHole: 0.1,
                // width: 400,
                // height: 400
            },
            BarChartOptions: {
                title: "Number of bookings per location",
                legend: {
                    position: 'bottom'
                }
                // width: 400,
                // height: 400
            },
            ColumnChartOptions: {
                title: "Number of bookings per subscription",
                legend: {
                    position: 'bottom'
                }
                // width: 400,
                // height: 400
            },
        };
    },
    methods: {
        changeRole(role) {
            this.userRole = role;
        },
        loadUserData() {
            this.userData = JSON.parse(localStorage.getItem("userData"));
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

<style scoped>
</style>
