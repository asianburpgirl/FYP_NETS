<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button defaultHref="/tabs/bookings"></ion-back-button>
                </ion-buttons>
                <ion-title class="ion-text-center">Map</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content>
            <!--   <ion-refresher slot="fixed" @ionRefresh="handleRefresh()">
            <ion-refresher-content></ion-refresher-content>
          </ion-refresher> -->
    
            <capacitor-google-map id="map"></capacitor-google-map>
    
            <!-- first popup page to open when user click on marker. User can choose either to book or subscribe to this carpark. button will open up respective popup  -->
            <ion-modal :is-open="choiceOpen" class="ion-padding">
                <ion-header>
                    <ion-toolbar>
                        <ion-title> {{ clickedMarkerName }}</ion-title>
                        <ion-buttons slot="start">
                            <ion-button @click="setChoiceOpen(false)">
                                <ion-icon :icon="arrowBackOutline"></ion-icon>
                            </ion-button>
                        </ion-buttons>
                    </ion-toolbar>
                </ion-header>
    
                <ion-content class="ion-padding ion-justify-content-center">
                    <div>
                        <!-- <p>
                            <b>Distance:</b> {{ distanceToLocation_km }} km
                        </p>
                        <p>
                            <b>Time Taken:</b> {{ timeToLocation_mins }} mins
                        </p> -->
                        <p><b>Booking Amount:</b> ${{ bookingAmount }} per hour</p>
                    </div>
    
                    <ion-row>
                        <ion-col md="6">
                            <ion-button @click="
                      setBookingOpen(true);
                      setChoiceOpen(false);
                    " expand="block">Book</ion-button>
                        </ion-col>
                        <ion-col md="6">
                            <ion-button @click="
                      setSubscriptionOpen(true);
                      setChoiceOpen(false);
                    " expand="block">Subscribe</ion-button>
                        </ion-col>
                    </ion-row>
                </ion-content>
            </ion-modal>
    
            <!-- when user select to book a carpark at the location.  -->
            <ion-modal :is-open="bookingIsOpen" class="ion-padding">
                <ion-header>
                    <ion-toolbar>
                        <ion-title> Booking Overview</ion-title>
                        <ion-buttons slot="start">
                            <ion-button @click="
                      setBookingOpen(false);
                      setChoiceOpen(true);
                    ">
                                <ion-icon :icon="arrowBackOutline"></ion-icon>
                            </ion-button>
                        </ion-buttons>
                    </ion-toolbar>
                </ion-header>
                <ion-content class="ion-padding">
                    <ion-item>
                        <!-- Distance from your current location:
                            {{ distanceToLocation_km }} km
                            <br />
                            <br />
                            Time taken from your current location:
                            {{ timeToLocation_mins }} mins
                            <br /> -->
  
                        <ion-label position="stacked"> Booking Date:</ion-label>
                        <ion-datetime presentation="date" v-model="bookingDate" :min="minDate"></ion-datetime>
    
                        <ion-label position="stacked"> Start Time:</ion-label>
                        <ion-datetime presentation="time" v-model="startTime"></ion-datetime>
    
                        <ion-label position="stacked"> End Time:</ion-label>
                        <ion-datetime presentation="time" v-model="endTime"></ion-datetime>
    
                        <ion-text color="danger" class="ion-padding-top">
                            <li v-for="error in errorMessage" :key="error">
                                {{ error }}
                            </li>
                        </ion-text>
                    </ion-item>
    
                    <ion-row class="ion-padding-top ion-justify-content-end ion-padding-bottom addPaddingBottom">
                      <ion-col>
                        <ion-button expand="block" @click="makeBoooking()">Book</ion-button>
                      </ion-col>  
                    </ion-row>
                </ion-content>
            </ion-modal>
    
            <!-- when booking is successful, to show success popup -->
            <ion-modal :is-open="bookingSuccessIsOpen" class="ion-padding">
                <ion-header>
                    <ion-toolbar>
                        <ion-title>Booking Details</ion-title>
                    </ion-toolbar>
                </ion-header>
                <ion-content class="ion-padding">
                    <ion-img :src="clickedMarkerImage"></ion-img>
    
    
                    <ion-row>
                        Your booking at {{ clickedMarkerName }} is successful!
                        <br /> Your booking details are as followed:
                        <ul>
                            <!-- <li><b>Carpark Location:</b> {{ clickedMarkerAddress }}</li> -->
                            <li><b>Booking Date:</b> {{ bookingDate }}</li>
    
                            <li><b>Start Time:</b> {{ startTime }}</li>
                            <li><b>End Time:</b> {{ endTime }}</li>
                        </ul>
                    </ion-row>
    
                    <ion-row class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom">
                        <ion-col md="6">
                          <ion-button expand="block" @click="setBookingSuccessOpen(false)">Back to Map</ion-button>
                            
                            
                        </ion-col>
                        <ion-col md="6">
                          <ion-button @click="routeToMyBookings()"
                  >View My Bookings</ion-button>
                        </ion-col>
                    </ion-row>

                    
                </ion-content>
            </ion-modal>
    
            <!-- when user select to subscription plans at the carpark location.  -->
            <ion-modal :is-open="subscriptionIsOpen" class="ion-padding">
                <ion-header>
                    <ion-toolbar>
                        <ion-title>Subscription plan</ion-title>
                        <ion-buttons slot="start">
                            <ion-button @click="
                      setSubscriptionOpen(false);
                      setChoiceOpen(true);
                    ">
                                <ion-icon :icon="arrowBackOutline"></ion-icon>
                            </ion-button>
                        </ion-buttons>
                    </ion-toolbar>
                </ion-header>
                <ion-content class="ion-padding">
                    <h1>{{ clickedMarkerName }}</h1>
    
                    <h3>
                        Address: <u> {{ clickedMarkerAddress }} test</u>
                    </h3>
    
                    <ion-item>
                        <ion-label>Subscription Type</ion-label>
                        <ion-select placeholder="Type">
                            <ion-select-option value="seasonal">Seasonal</ion-select-option>
                            <ion-select-option value="complimentary">Complimentary</ion-select-option>
                            <ion-select-option value="hourly">Hourly</ion-select-option>
                        </ion-select>
                    </ion-item>
    
                    <ion-list>
                        <ion-item> Weekday Peak: $12/month </ion-item>
                        <ion-item> Weekday Non-Peak: $10/month </ion-item>
                        <ion-item> Weekend Peak: $20/month </ion-item>
                        <ion-item> Weekend Non-Peak: $15/month </ion-item>
                    </ion-list>
                    <ion-row class="ion-padding-top ion-justify-content-center addPaddingBottom">
                        <ion-col>
                            <ion-button expand="block" @click="buySubscription()">Buy Subscription</ion-button>
                        </ion-col>
                    </ion-row>
    
                </ion-content>
    
            </ion-modal>
        </ion-content>
    </ion-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { GoogleMap } from "@capacitor/google-maps";
import axios from "axios";
import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonModal,
    IonRow,
    IonList,
    IonButtons,
    IonBackButton,
    IonButton,
    IonDatetime,
    IonIcon,
    IonItem,
    IonLabel,
    IonSelect,
    IonSelectOption,
    IonCol,
    IonText,
    IonImg

} from "@ionic/vue";

import { arrowBackOutline } from "ionicons/icons";
import { Geolocation } from "@capacitor/geolocation";

export default defineComponent({
    components: {
        IonPage,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonModal,
        IonButtons,
        IonBackButton,
        IonButton,
        IonDatetime,
        IonIcon,
        IonItem,
        IonLabel,
        IonSelect,
        IonSelectOption,
        IonRow,
        IonList,
        IonCol,
        IonText,
        IonImg

    },

    setup() {
        return { arrowBackOutline };
    },
    data() {
        return {
            bookingIsOpen: false,
            bookingSuccessIsOpen: false,
            subscriptionSuccessIsOpen: false,
            subscriptionIsOpen: false,
            choiceOpen: false,

            //setting peak hours. can make it such that admin can change this value. value in 24 hours.
            startPeak: "09:00:00",
            endPeak: "17:00:00",

            carparkPrices: [],
            clickedMarkerName: "",
            clickedMarkerAddress: "",
            distanceToLocation_km: "",
            timeToLocation_mins: "",
            startTime: "",
            endTime: "",
            minDate: "",
            bookingDate: "",
            carparksArraySimu: [],
            userOrigin: "1.2958419970838684,103.85841587741238",
            userDestinations: "1.3007033161990564,103.84528924122294",
            bookingAmount: "",

            errorMessage: [],

            // bookingDetails: [],
            // userData: {},
            // editBookingOpen: false,

            // //for editing booking
            // bookingInfo: {},
            // newDate: "",
            // newStartTime: "",
            // newEndTime: "",

            // //to open editing windows
            // editDate: false,
            // editStartTime: false,
            // editEndTime: false,
        };
    },

    mounted() {
        this.createMap();
        this.getCurrentDateTime();
    },

    methods: {
        formatMoney(myFloat) {
            // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
            myFloat = myFloat.toString();
            const dotExists = myFloat.includes(".");
            let newFloat = myFloat;
            if (dotExists) {
                newFloat = myFloat.split(".");
                if (newFloat[1].length == 1) {
                    newFloat[1] += "0";
                } else if (newFloat[1].length == 0) {
                    newFloat[1] += "00";
                }
                newFloat = newFloat.join(".");
            } else {
                newFloat += ".00";
            }

            return newFloat;
        },
        getCurrentDateTime() {
            const currentDateTime = new Date();
            const date = ("0" + currentDateTime.getDate()).slice(-2);
            const month = (
                "0" +
                (parseInt(currentDateTime.getMonth()) + parseInt(1))
            ).slice(-2);

            this.minDate =
                currentDateTime.getFullYear() +
                "-" +
                month +
                "-" +
                date +
                "T" +
                currentDateTime.getHours() +
                ":" +
                currentDateTime.getMinutes() +
                ":" +
                currentDateTime.getSeconds();
        },
        routeToMyBookings() {
            this.setBookingSuccessOpen(false);
            this.$router
                .push({
                    path: "/viewBooking",
                })
                .then(() => {
                    this.$router.go(0);
                });
            location.reload();
        },
        buySubscription() {
            console.log("here");
        },
        async getCurrentLocation() {
            const coordinates = await Geolocation.getCurrentPosition();

            return coordinates;
        },
        calculateDistance() {
            this.getCurrentLocation().then((coordinates) => {
                this.userOrigin =
                    coordinates.coords.latitude.toString() +
                    "," +
                    coordinates.coords.longitude.toString();
                // console.log("Your location:" + this.userOrigin);
                const url =
                    "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" +
                    this.userOrigin +
                    "&destinations=" +
                    this.userDestinations +
                    "&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI";

                axios
                    .get(url)
                    .then((response) => {
                        const distance_km = (
                            response.data.rows[0].elements[0].distance.value / 1000
                        ).toPrecision(2);
                        const duration_mins = (
                            response.data.rows[0].elements[0].duration_in_traffic.value / 60
                        ).toPrecision(2);
                        // console.log(
                        //   "distance: ",
                        //   distance_km + "duration: ",
                        //   duration_mins
                        // );
                        this.distanceToLocation_km = distance_km;
                        this.timeToLocation_mins = duration_mins;
                    })
                    .catch((error) => {
                        console.log(error.message);
                    });
            });
        },
        setChoiceOpen(isOpen) {
            this.choiceOpen = isOpen;
        },
        setBookingOpen(isOpen) {
            this.bookingIsOpen = isOpen;
        },
        setBookingSuccessOpen(isOpen) {
            this.bookingSuccessIsOpen = isOpen;
        },
        setSubscriptionOpen(isOpen) {
            this.subscriptionIsOpen = isOpen;
        },
        makeBoooking() {
            this.errorMessage = [];
            if (
                this.startTime >= this.endTime &&
                this.startTime != "" &&
                this.endTime != ""
            ) {
                this.errorMessage.push("End Time must be later than Start Time!");
            }
            if (this.bookingDate == "") {
                this.errorMessage.push("You need to indicate booking Date!");
            }
            if (this.startTime == "") {
                this.errorMessage.push("You need to indicate start time !");
            }
            if (this.endTime == "") {
                this.errorMessage.push("You need to indicate end time !");
            }

            if (this.errorMessage.length == 0) {
                console.log("time");
                const currentDateTime = new Date();
                const date = currentDateTime.getDate();
                const month = currentDateTime.getMonth() + 1;
                const year = currentDateTime.getFullYear();

                const hour = currentDateTime.getHours();
                const min = currentDateTime.getMinutes();
                const sec = currentDateTime.getSeconds();

                const currentDateTimeFormatted =
                    year + "-" + month + "-" + date + " " + hour + ":" + min + ":" + sec;

                this.bookingDate = this.bookingDate.substring(0, 10);

                const startDateTimeFormatted =
                    this.bookingDate.substring(0, 10) +
                    " " +
                    this.startTime.substring(11, 19);
                this.startTime = this.startTime.substring(11, 19);

                const endDateTimeFormatted =
                    this.bookingDate.substring(0, 10) +
                    " " +
                    this.endTime.substring(11, 19);
                this.endTime = this.endTime.substring(11, 19);

                this.userData = JSON.parse(localStorage.getItem("userData"));
                const userID = this.userData.userID;

                const url = "http://127.0.0.1:5001/bookings";

                axios
                    .post(url, {
                        bookingDateTime: currentDateTimeFormatted,
                        bookingLocation: this.clickedMarkerName,
                        locationName: this.clickedMarkerAddress,
                        bookingStartDateTime: startDateTimeFormatted,
                        bookingEndDateTime: endDateTimeFormatted,
                        userID: userID,
                        status: "Booked",
                        bookingAmt: this.bookingAmount,
                    })
                    .then((response) => {
                        this.deductFromUser(response.data.data.bookingID);
                        this.setBookingOpen(false); // close booking window
                        this.setBookingSuccessOpen(true); // open booking sucess window
                    })
                    .catch((error) => {
                        console.log(error.message);
                    });
            }
        },
        deductFromUser(bookingID) {
            // updateBalance
            const url = "http://127.0.0.1:5001/updateBalance/" + bookingID;
            axios
                .put(url, {
                    bookingID: bookingID,
                })
                .then((response) => {
                    // console.log(response)
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },

        async createMap() {
            const mapRef = document.getElementById("map");
            const newMap = await GoogleMap.create({
                id: "my-map", // Unique identifier for this map instance
                element: mapRef, // reference to the capacitor-google-map element
                apiKey: "AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI", // Your Google Maps API Key
                config: {
                    center: {
                        // The initial position to be rendered by the map
                        lat: 1.2962823,
                        lng: 103.8500894, // smu
                    },
                    zoom: 13, // The initial zoom level to be rendered by the map
                },
            });

            //add markers
            const url = "http://127.0.0.1:5003/carparks";
            axios
                .get(url)
                .then((response) => {
                    // console.log(response.data.data.carparks)
                    for (const eachCarpark of response.data.data.carparks) {
                        const markers = newMap.addMarkers([
                            //location 1
                            {
                                title: eachCarpark.carparkName,
                                snippet: eachCarpark.carparkLocation,
                                coordinate: {
                                    lat: eachCarpark.latitude,
                                    lng: eachCarpark.longitude,
                                },
                            },
                        ]);
                        this.carparkPrices.push({
                            carparkname: eachCarpark.carparkName,
                            hourlyweekdaypeak: eachCarpark.hourlyweekdaypeak,
                            hourlyweekendpeak: eachCarpark.hourlyweekendpeak,
                            hourlyweekdaynonpeak: eachCarpark.hourlyweekdaynonpeak,
                            hourlyweekendnonpeak: eachCarpark.hourlyweekendnonpeak,
                        });
                    }
                    // listener for user click
                    const markerListener = newMap.setOnMarkerClickListener((event) => {
                        this.getCurrentDateTime();
                        this.clickedMarkerName = event.title;
                        // this.clickedMarkerAddress = event.snippet;

                        for (const eachcarpark of this.carparkPrices) {
                            if (eachcarpark.carparkname == this.clickedMarkerName) {
                                const currentDayOfWeek = new Date();

                                // weekend
                                if (
                                    currentDayOfWeek.getDay() == 6 ||
                                    currentDayOfWeek.getDay() == 0
                                ) {
                                    // peak
                                    if (
                                        this.startPeak.split(":")[0] <
                                        currentDayOfWeek.getHours() <
                                        this.endPeak.split(":")[0]
                                    ) {
                                        this.bookingAmount = this.formatMoney(
                                            eachcarpark.hourlyweekendpeak
                                        );
                                    }
                                    //non peak
                                    else {
                                        this.bookingAmount = this.formatMoney(
                                            eachcarpark.hourlyweekendnonpeak
                                        );
                                    }
                                }
                                // weekdays
                                else {
                                    // peak
                                    if (
                                        this.startPeak.split(":")[0] <
                                        currentDayOfWeek.getHours() <
                                        this.endPeak.split(":")[0]
                                    ) {
                                        this.bookingAmount = this.formatMoney(
                                            eachcarpark.hourlyweekdaypeak
                                        );
                                    }
                                    //non peak
                                    else {
                                        this.bookingAmount = this.formatMoney(
                                            eachcarpark.hourlyweekdaynonpeak
                                        );
                                    }
                                }
                            }
                        }

                        this.userDestinations =
                            event.latitude.toString() + "," + event.longitude.toString();

                        this.setChoiceOpen(true);
                        this.calculateDistance();
                    });
                    //add traffic data
                    const trafficDataEnable = newMap.enableTrafficLayer(true);

                    // enable current location
                    const currentLocationEnable = newMap.enableCurrentLocation(true);
                    return newMap;
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
        getSimulator() {
            this.carparksArraySimu = []
            this.googleMapDistanceUrl = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=";
            this.combinedLatLang = "";

            let url = "http://127.0.0.1:5004/getCarpark/1";
            axios
                .post(url, {
                    "requesttype": 1000,
                    "carparkid": 1
                })
                .then((response) => {
                    this.carparksArraySimu.push({
                        data: response.data.data,
                        image: "assets/images/paragon.jpg",
                        // lat: 1.3040258775031617,
                        // long: 103.83608284915861
                    })
                    this.combinedLatLang += "1.3040258775031617" + "," + "103.83608284915861" + "|";
                    url = "http://127.0.0.1:5004/getCarpark/2";
                    axios
                        .post(url, {
                            "requesttype": 1000,
                            "carparkid": 2
                        })
                        .then((response) => {
                            this.carparksArraySimu.push({
                                data: response.data.data,
                                image: "assets/images/ion.jpg",
                                // lat: 1.3040258775031617,
                                // long: 103.83608284915861
                            })
                            this.combinedLatLang += "1.3040258775031617" + "," + "103.83608284915861" + "|";
                            url = "http://127.0.0.1:5004/getCarpark/3";
                            console.log(url)
                            axios
                                .post(url, {
                                    "requesttype": 1000,
                                    "carparkid": 3
                                })
                                .then((response) => {
                                    this.carparksArraySimu.push({
                                        data: response.data.data,
                                        image: "assets/images/takashimaya.jpeg",
                                        //         lat: 1.3033454254185042,
                                        // long: 103.83455711763565
                                    })
                                    this.combinedLatLang += "1.3033454254185042" + "," + "103.83455711763565" + "|";
                                    url = "http://127.0.0.1:5004/getCarpark/4";
                                    axios
                                        .post(url, {
                                            "requesttype": 1000,
                                            "carparkid": 4
                                        })
                                        .then((response) => {
                                            this.carparksArraySimu.push({
                                                data: response.data.data,
                                                image: "assets/images/tangs.jpg",
                                                //             lat: 1.3040258775031617,
                                                // long: 103.83608284915861
                                            })
                                            this.combinedLatLang += "1.3040258775031617" + "," + "103.83608284915861" + "|";
                                            url = "http://127.0.0.1:5004/getCarpark/5";
                                            axios
                                                .post(url, {
                                                    "requesttype": 1000,
                                                    "carparkid": 5
                                                })
                                                .then((response) => {
                                                    this.carparksArraySimu.push({
                                                        data: response.data.data,
                                                        image: "assets/images/Wheelock.png",
                                                        //               lat: 1.3050314731714412,
                                                        // long: 103.83297614415605
                                                    })
                                                    this.combinedLatLang += "1.3050314731714412" + "," + "103.83297614415605" + "|";
                                                    url = "http://127.0.0.1:5004/getCarpark/6";
                                                    axios
                                                        .post(url, {
                                                            "requesttype": 1000,
                                                            "carparkid": 6
                                                        })
                                                        .then((response) => {
                                                            this.carparksArraySimu.push({
                                                                data: response.data.data,
                                                                image: "assets/images/313.jpg",
                                                                //                   lat: 1.301171207812743,
                                                                // long: 103.8386220085623
                                                            })
                                                            this.combinedLatLang += "1.301171207812743" + "," + "103.8386220085623" + "|";
                                                            url = "http://127.0.0.1:5004/getCarpark/7";
                                                            axios
                                                                .post(url, {
                                                                    "requesttype": 1000,
                                                                    "carparkid": 7
                                                                })
                                                                .then((response) => {
                                                                    this.carparksArraySimu.push({
                                                                        data: response.data.data,
                                                                        image: "assets/images/scape.jpg",
                                                                        //                     lat: 1.3010677408660067,
                                                                        // long: 103.83576204980196
                                                                    })
                                                                    this.combinedLatLang += "1.3010677408660067" + "," + "103.83576204980196" + "|";
                                                                    url = "http://127.0.0.1:5004/getCarpark/8";
                                                                    axios
                                                                        .post(url, {
                                                                            "requesttype": 1000,
                                                                            "carparkid": 8
                                                                        })
                                                                        .then((response) => {
                                                                            this.carparksArraySimu.push({
                                                                                data: response.data.data,
                                                                                image: "assets/images/wisma.jpeg",
                                                                                // lat: 1.303842974291844,
                                                                                // long: 103.8333226716273
                                                                            })
                                                                            this.combinedLatLang += "1.303842974291844" + "," + "103.8333226716273" + "|";

                                                                            if (this.selectedLocation == "") {
                                                                                console.log("no location selected");
                                                                            } else {
                                                                                if (this.selectedLocation == "orchard") {
                                                                                    this.userOrigin = "1.3064433533620563,103.83276247871694";
                                                                                } else if (this.selectedLocation == "yishun") {
                                                                                    this.userOrigin = "1.4304060903894582, 103.83515323243753";
                                                                                } else if (this.selectedLocation == "somerset") {
                                                                                    this.userOrigin = "1.3016313961551784, 103.83849995957749";
                                                                                }


                                                                                this.googleMapDistanceUrl +=
                                                                                    this.userOrigin +
                                                                                    "&destinations=" +
                                                                                    this.combinedLatLang.slice(0, -1) +
                                                                                    "&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI";
                                                                                // this.calculateDistance();

                                                                                console.log(this.userOrigin, "HEREEEE")
                                                                                // this.userOrigin = "1.3064433533620563,103.83276247871694"
                                                                                // console.log("HERE2")
                                                                                const url = "http://127.0.0.1:5009/getCoords";
                                                                                axios
                                                                                    .post(url, {
                                                                                        "origin": this.userOrigin
                                                                                    })
                                                                                    .then((response) => {
                                                                                        console.log(response.data.rows[0].elements)
                                                                                        const destinations = response.data.rows[0].elements
                                                                                        for (let i = 0; i < this.carparksArraySimu.length; i++) {
                                                                                            this.carparksArraySimu[i]["distance_km"] = destinations[i].distance.text;
                                                                                            this.carparksArraySimu[i]["distance_km_value"] = destinations[i].distance.text;
                                                                                            this.carparksArraySimu[i]["duration_mins"] = destinations[i].duration_in_traffic.text;
                                                                                        }
                                                                                        if (this.userOrigin != "") {
                                                                                            this.carparksArraySimu.sort(function(a, b) {
                                                                                                const keyA = a.distance_km_value;
                                                                                                const keyB = b.distance_km_value;
                                                                                                if (keyA < keyB) return -1;
                                                                                                if (keyA > keyB) return 1;
                                                                                                return 0;
                                                                                            });

                                                                                            this.carparksArraySimu = this.carparksArraySimu.slice(0, 4);
                                                                                        }

                                                                                        // this.test = response 
                                                                                    })
                                                                                    .catch((error) => {
                                                                                        console.log(error);
                                                                                    });
                                                                            }

                                                                        })
                                                                })
                                                        })
                                                })
                                        })
                                })
                        })

                })

            // this.calculateDistance()

            // this.googleMapDistanceUrl =
            //   "https://maps.googleapis.com/maps/api/distancematrix/json?origins=";
            // this.combinedLatLang = "";

            // for (const eachCarpark in this.carparksArraySimu){
            //     console.log(this.carparksArraySimu[eachCarpark])
            //     this.combinedLatLang +=
            //         eachCarpark.lat + "," + eachCarpark.long + "|";
            // }

            //   if (this.selectedLocation == "") {
            //       console.log("no location selected");
            //     } else {
            //       if (this.selectedLocation == "orchard") {
            //         this.userOrigin = "1.3064433533620563,103.83276247871694";
            //       } else if (this.selectedLocation == "yishun") {
            //         this.userOrigin = "1.4304060903894582, 103.83515323243753";
            //       } else if (this.selectedLocation == "somerset") {
            //         this.userOrigin = "1.3016313961551784, 103.83849995957749";
            //       }

            //       this.googleMapDistanceUrl +=
            //         this.userOrigin +
            //         "&destinations=" +
            //         this.combinedLatLang.slice(0, -1) +
            //         "&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI";
            //       this.calculateDistance();
            //       console.log(this.googleMapDistanceUrl)
            //     }

        },
    },
});
</script>

<style scoped>
capacitor-google-map {
    display: inline-block;
    width: 100%;
    height: 100%;
}

.addPaddingBottom {
    padding-bottom: 50px;
}

h2 {
    padding-bottom: 120px;
}
</style>
