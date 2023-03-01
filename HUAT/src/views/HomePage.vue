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
            <h4 class="ion-text-start">Your Bookings</h4>
            <ion-modal :is-open="editBookingOpen">
                <ion-header>
                    <ion-toolbar>
                        <ion-title class="ion-text-center">
                            Edit Booking</ion-title>
    
                        <ion-buttons slot="start">
                            <ion-button @click="setEditBookingOpen(false)">
                                <ion-icon :icon="arrowBackOutline"></ion-icon>
                            </ion-button>
                        </ion-buttons>
    
                    </ion-toolbar>
                </ion-header>
    
                <ion-content class="ion-padding-top">
                    <ion-item>
    
                        <ion-label position="stacked"> Booking Date: {{ bookingInfo.startDate }}</ion-label>
                        <ion-datetime presentation="date" v-model="newDate" v-if="editDate==true"></ion-datetime>
                        <ion-button shape="round" @click="editDate=true" v-if="editDate==false">Edit Booking Date</ion-button>
                        <ion-button shape="round" @click="editDate=true" v-if="editDate==true" color="danger">Cancel</ion-button>
    
                        <ion-label position="stacked"> Start Time: {{ bookingInfo.startTime }}</ion-label>
                        <ion-datetime presentation="time" v-model="newStartTime" v-if="editStartTime==true"></ion-datetime>
                        <ion-button shape="round" @click="editStartTime=true" v-if="editStartTime==false">Edit Start Time</ion-button>
                        <ion-button shape="round" @click="editDate=true" v-if="editStartTime==true" color="danger">Cancel</ion-button>
    
                        <ion-label position="stacked"> End Time: {{ bookingInfo.endTime }}</ion-label>
                        <ion-datetime presentation="time" v-model="newEndTime" v-if="editEndTime==true"></ion-datetime>
                        <ion-button shape="round" @click="editEndTime=true" v-if="editEndTime==false">Edit End Time</ion-button>
                        <ion-button shape="round" @click="editDate=true" v-if="editEndTime==true" color="danger">Cancel</ion-button>
    
                    </ion-item>
    
                    <ion-row class="ion-padding-top ion-justify-content-center addPaddingBottom">
                        <ion-button @click="saveEditBooking()">
                            Save
                        </ion-button>
                    </ion-row>
    
                </ion-content>
            </ion-modal>
            <ion-card v-for="eachBooking in bookingDetails" :key="eachBooking">
                <ion-img :src="eachBooking.imagePath"></ion-img>
                <ion-card-header>
                    <ion-card-title>{{ eachBooking.bookingLocation }}</ion-card-title>
                </ion-card-header>
    
                <ion-card-content>
                    <ion-list>
                        <ion-item lines="none">
                            <ion-button fill="outline" slot="start">Directions</ion-button>
                            <ion-badge v-if="eachBooking.status == 'Booked'" color="success" slot="end">{{ eachBooking.status }}</ion-badge>
                            <ion-badge v-if="eachBooking.status == 'Cancelled'" color="medium" slot="end">{{ eachBooking.status }}</ion-badge>
                        </ion-item>
                    </ion-list>
                    <ion-card-subtitle>Booking Ref: <u>{{ eachBooking.bookingRef }}</u></ion-card-subtitle>
                    <ion-card-subtitle v-if="eachBooking.status == 'Booked'">Booking Amount: ${{ eachBooking.amount }}</ion-card-subtitle>
                    <ion-card-subtitle v-if="eachBooking.status == 'Cancelled'">Refunded Amount: $ {{ eachBooking.amount }}</ion-card-subtitle>
                    <ion-card-subtitle><b>Start Date: {{ eachBooking.startDate }}</b></ion-card-subtitle>
                    <ion-card-subtitle><b>End Date: {{ eachBooking.endDate }}</b></ion-card-subtitle>
                    <ion-card-subtitle><b>Start Time: {{ eachBooking.startTime }}</b></ion-card-subtitle>
                    <ion-card-subtitle><b>End Time:{{ eachBooking.endTime }}</b></ion-card-subtitle>
                </ion-card-content>
                <ion-row class="ion-padding ion-justify-content-center">
                    <ion-col  >
                        <ion-button v-if="eachBooking.status == 'Booked'" shape="round" @click="editBooking(eachBooking)" >Edit</ion-button>
                    </ion-col>
                    <ion-col >
                        <ion-button v-if="eachBooking.status == 'Booked'" shape="round" @click="confirmationAlert(eachBooking.bookingID, eachBooking.amount)" color="danger">Cancel</ion-button>
                    </ion-col>
                    <ion-col >
                        <ion-button v-if="eachBooking.status == 'Cancelled'" shape="round" @click="deleteBooking(eachBooking.bookingID)" color="light">Delete</ion-button>
                    </ion-col>
                </ion-row>
                <div>
                  <ion-button v-if="eachBooking.status == 'Booked'" @click="editBooking(eachBooking)" >Edit</ion-button>
                  <ion-button v-if="eachBooking.status == 'Booked'" @click="confirmationAlert(eachBooking.bookingID, eachBooking.amount)" color="danger">Cancel</ion-button>
                  <ion-button v-if="eachBooking.status == 'Cancelled'" @click="deleteBooking(eachBooking.bookingID)" color="light">Delete</ion-button>
                </div>
            </ion-card>
        </ion-grid>
    </base-layout>
</template>

<script>
import {
    arrowBackOutline,
} from "ionicons/icons";
import {
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    // IonSearchbar,
    IonBadge,
    IonButton,
    alertController,
    IonModal,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonIcon,
    IonButtons,
    IonLabel,
    IonDatetime,
    IonItem,
    IonRow,
    IonCol,
    IonGrid,
    IonImg
} from "@ionic/vue";
import {
    GChart
} from "vue-google-charts";
import {
    defineComponent,
    ref
} from "vue";
import axios from "axios";
export default defineComponent({
    components: {
        GChart,
        IonCard,
        IonCardHeader,
        IonCardSubtitle,
        IonCardTitle,
        // IonSearchbar,
        IonBadge,
        IonButton,
        IonModal,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonIcon,
        IonButtons,
        IonLabel,
        IonDatetime,
        IonItem,
        IonRow,
        IonCol,
        IonGrid,
        IonImg
    },
    setup() {
        const handlerMessage = ref("");
        const confirmationAlert = async (bookingID, amount) => {
            const alert = await alertController.create({
                header: "Are you sure you want to delete this booking? ",
                subHeader: "$" + amount + " will be refunded back to your account",
                buttons: [{
                        text: "Cancel",
                        cssClass: "alert-button-cancel",
                        role: "cancel",
                        handler: () => {
                            handlerMessage.value = "Alert canceled";
                        },
                    },
                    {
                        text: "Yes",
                        cssClass: "alert-button-confirm",
                        role: "confirm",
                        handler: () => {
                            handlerMessage.value = "Alert confirmed";

                            // update booking status to "cancel"
                            let url = "http://127.0.0.1:5001/bookings/" + bookingID;
                            axios
                                .put(url, {
                                    status: "Cancelled",
                                })
                                .then((response) => {
                                    //refund money
                                    url = "http://127.0.0.1:5001/updateBalance/" + bookingID;
                                    axios
                                        .put(url, {
                                            bookingID: bookingID,
                                        })
                                        .then((response) => {
                                            sucessMsg(amount, response.data.data);
                                        })
                                        .catch((error) => {
                                            console.log(error.message);
                                        });
                                })
                                .catch((error) => {
                                    console.log(error.message);
                                });
                        },
                    },
                ],
            });
            await alert.present();
        };

        const sucessMsg = async (amount, balance) => {
            const alert = await alertController.create({
                header: "Success!",
                subHeader: "$" + amount + " refunded. Balance is " + "$" + balance,
                buttons: [{
                    text: "Okay",
                    handler: () => {
                        location.reload();
                    },
                }, ],
            });

            await alert.present();
        };

        return {
            confirmationAlert,
            sucessMsg,
            arrowBackOutline
        };
    },
    data() {
        return {
            userRole: "",

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

            userData: {},
            bookingDetails: [],
            editBookingOpen: false,

            //for editing booking
            bookingInfo: {},
            newDate: "",
            newStartTime: "",
            newEndTime: "",

            //to open editing windows
            editDate: false,
            editStartTime: false,
            editEndTime: false,
        };
    },
    methods: {
        changeRole(role) {
            this.userRole = role;
        },
        loadUserData() {
            this.userData = JSON.parse(localStorage.getItem("userData") || "{}");
            this.userRole = this.userData.role;

            const url = "http://127.0.0.1:5001/bookings/" + this.userData.userID;
            axios
                .get(url)
                .then((response) => {
                    const data = response.data.data.bookings;

                    for (const eachBooking of data) {

                        let startDateTime = new Date(eachBooking.bookingStartDateTime);
                        startDateTime = startDateTime.toUTCString()
                        const startDateOnly = startDateTime.slice(5, 16)
                        const startTimeOnly = startDateTime.slice(17, 22)

                        let endDateTime = new Date(eachBooking.bookingEndDateTime);
                        endDateTime = endDateTime.toUTCString()
                        const endDateOnly = endDateTime.slice(5, 16)
                        const endTimeOnly = endDateTime.slice(17, 22)

                        let imagePath = ""

                        const url = "http://127.0.0.1:5003/carparkImage"
                        axios
                            .post(url, {
                                carparkName: eachBooking.bookingLocation
                            })
                            .then((response) => {

                                imagePath = response.data.data.imagePath

                                this.bookingDetails.push({
                                    bookingDate: eachBooking.bookingDateTime,
                                    bookingID: eachBooking.bookingID,
                                    bookingLocation: eachBooking.bookingLocation,
                                    locationName: eachBooking.locationName,
                                    startDate: startDateOnly,
                                    startTime: startTimeOnly,
                                    endDate: endDateOnly,
                                    amount: this.formatMoney(eachBooking.bookingAmt),
                                    endTime: endTimeOnly,
                                    status: eachBooking.status,
                                    bookingRef: eachBooking.bookingRef,
                                    userID: eachBooking.userID,
                                    imagePath: imagePath
                                });
                                console.log(this.bookingDetails)

                            })
                            .catch((error) => {
                                console.log(error.message);
                            });

                    }
                })
                .catch((error) => {
                    console.log(error.message);
                });
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
        formatMoney(myFloat) { // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
            myFloat = myFloat.toString()
            let newFloat = myFloat.split(".")
            if ((newFloat[1]).length == 1) {
                newFloat[1] += "0"
            }
            newFloat = newFloat.join(".")
            return newFloat
        },
        editBooking(bookingInfo) {
            this.setEditBookingOpen(true)
            this.bookingInfo = bookingInfo
            // console.log(this.bookingInfo)
        },
        saveEditBooking() {
            // const startDateTimeFormatted = this.bookingDate.substring(0, 10) + " " + this.startTime.substring(11, 19);

            // to change user booking timing to current timing
            const currentDateTime = new Date();
            const date = currentDateTime.getDate();

            const month = currentDateTime.getMonth() + 1;
            const year = currentDateTime.getFullYear();
            const hour = currentDateTime.getHours();
            const min = currentDateTime.getMinutes();
            const sec = currentDateTime.getSeconds();

            const currentDateTimeFormatted = //here
                year + "-" + month + "-" + date + " " + hour + ":" + min + ":" + sec;

            // to change booking date
            let newStartDateFormatted = this.bookingInfo.startDate
            if (this.newDate != "") {
                newStartDateFormatted = this.newDate.substring(0, 10)
            }

            // to change start time
            let newStartTimeFormatted = this.bookingInfo.startTime
            if (this.newStartTime != "") {
                newStartTimeFormatted = this.newStartTime.substring(11, 19)
            }
            const newStartDateTime = newStartDateFormatted + " " + newStartTimeFormatted

            // to change end time
            let newEndTimeFormatted = this.bookingInfo.endTime
            if (this.newEndTime != "") {
                newEndTimeFormatted = this.newEndTime.substring(11, 19)
            }
            const newEndDateTime = newStartDateFormatted + " " + newEndTimeFormatted

            const url = "http://127.0.0.1:5001/bookings/" + this.bookingInfo.bookingID;
            axios
                .put(url, {
                    bookingDateTime: currentDateTimeFormatted,
                    bookingStartDateTime: newStartDateTime,
                    bookingEndDateTime: newEndDateTime
                })
                .then((response) => {
                    // console.log(response)
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },

        setEditBookingOpen(isOpen) {
            this.editBookingOpen = isOpen
        },
        deleteBooking(bookingID) {
            const url = "http://127.0.0.1:5001/bookings/" + bookingID;
            axios
                .delete(url)
                .then((response) => {
                    // console.log(response);
                    location.reload();
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
/* iOS places the subtitle above the title */

ion-card-header {
    display: flex;
    flex-flow: column-reverse;
}

ion-img::part(image) {
    width: 100%;
    /* or whatever value */
    /* you can set the height value too */
}

button.alert-button.alert-button-confirm {
    background-color: var(--ion-color-success);
    color: var(--ion-color-success-contrast);
}

.md button.alert-button.alert-button-confirm {
    border-radius: 4px;
}

.ios button.alert-button.alert-button-confirm {
    border-bottom-right-radius: 13px;
    border-top-right-radius: 13px;
}

.ios button.alert-button.alert-button-cancel {
    border-right: 0;
    border-bottom-left-radius: 13px;
    border-top-left-radius: 13px;
}

.addPaddingBottom {
    padding-bottom: 300px;
}
</style>
