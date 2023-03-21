<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button defaultHref="/tabs/bookings"></ion-back-button>
                </ion-buttons>
                <ion-title class="ion-text-center">View Carparks</ion-title>
            </ion-toolbar>
        </ion-header>
    
        <ion-content>
            
            <ion-row class="ion-justify-content-center ion-padding">
                <ion-button expand="block" @click="setDateTimeOpen(true)">Change Booking Date and Time</ion-button>
            </ion-row>
    
            <ion-list class="ion-padding-top">
                <ion-radio-group v-model="pageTab" @ionChange="changeTab()">
                    <ion-item>
                        <ion-label>Recommended</ion-label>
                        <ion-radio slot="end" value="recommend"></ion-radio>
                    </ion-item>

                    <ion-item>
                        <ion-label>All</ion-label>
                        <ion-radio slot="end" value="all"></ion-radio>
                    </ion-item>
    
                    <ion-item>
                        <ion-label>Nearest</ion-label>
                        <ion-radio slot="end" value="nearest"></ion-radio>
                    </ion-item>
    
                    <ion-item>
                        <ion-label>Cheapest</ion-label>
                        <ion-radio slot="end" value="cheapest"></ion-radio>
                    </ion-item>
    
                    <ion-item>
                        <ion-label>Lots Available</ion-label>
                        <ion-radio slot="end" value="lotsAvail"></ion-radio>
                    </ion-item>
                </ion-radio-group>
            </ion-list>
        
            <ion-grid class="ion-padding-top">
                <ion-card v-for="carpark in carparkArrayToShow" :key="carpark">
                    <div v-if="carpark.data.lotbalancehourly != 0">
                        <ion-img :src="carpark.image"></ion-img>
                        <ion-card-header>
                            <ion-card-title>{{ carpark.data.carparklocation }}</ion-card-title>
                            <ion-card-subtitle></ion-card-subtitle>
                            <ion-card-subtitle>{{ carpark.data.carparkaddress }}</ion-card-subtitle>
                            <h3>
                                <b> {{ carpark.availableLots }}</b> lots available
                            </h3>
                            <h3 v-if="this.startTime != '' &&
                this.endTime !='' && this.bookingDate != '' ">
                                <b> Total: ${{ carpark.data.totalFee }}</b>
                            </h3>
                            <h4>
                                <u>{{ carpark.distance_km }},</u>
                                <u>{{ carpark.duration_mins }} </u> away from you
                            </h4>
                            <ion-row class="ion-padding-top ion-justify-content-center ion-padding-bottom">
                                <ion-button shape="round" @click="confirmationAlert(carpark,this.bookingDate,this.startTime,this.endTime,this.userData )" v-if="carpark.data.totalFee <= userBalance">
                                    Book
                                </ion-button>
                                <ion-text color="danger" v-if="carpark.data.totalFee > userBalance">
                                    <b> 
                                        Insufficient credit
                                    </b>
                                </ion-text>
                            </ion-row>
                        </ion-card-header>
                    </div>
                </ion-card>
            </ion-grid>
    
            <ion-modal :is-open="dateTimeModal" class="ion-padding">
                <ion-header>
                    <ion-toolbar>
                        <ion-title class="ion-text-center"> Date and Time</ion-title>
                        <ion-buttons slot="start">
                            <ion-button @click="setDateTimeOpen(false)">
                                <ion-icon :icon="arrowBackOutline"></ion-icon>
                            </ion-button>
                        </ion-buttons>
                    </ion-toolbar>
                </ion-header>
                <ion-content class="ion-padding">
                  <ion-item>
                     <ion-label position="stacked"> Booking Location:</ion-label>
                  <ion-select placeholder="Location" v-model="selectedLocation">
                        <ion-select-option value="orchard">Orchard</ion-select-option>
                        <ion-select-option value="somerset">Somerset</ion-select-option>
                        <ion-select-option value="yishun">Yishun</ion-select-option>
                    </ion-select>

                    <ion-label position="stacked"> Booking Date:</ion-label>
                    <ion-datetime presentation="date" :min=currentDateTime v-model="bookingDate"></ion-datetime>
    
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
                    
                    <ion-row class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom">
                      <ion-col>
                        <ion-button expand="block" @click="confirmDateTime()">Confirm</ion-button>
                      </ion-col>
                    </ion-row>
                </ion-content>
            </ion-modal>
        </ion-content>
    </ion-page>
</template>


<script>
import { arrowBackOutline } from "ionicons/icons";
import {
    IonText,
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
    IonButtons,
    IonButton,
    IonBackButton,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonCol,
    IonList,
    IonItem,
    IonSelect,
    IonSelectOption,
    IonImg,
    IonGrid,
    IonLabel,
    IonRadio,
    IonRadioGroup,
    IonModal,
    IonDatetime,
    IonIcon,
    IonRow,
    alertController
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
    components: {
        IonText,
        IonPage,
        IonHeader,
        IonTitle,
        IonContent,
        IonToolbar,
        IonButtons,
        IonButton,
        IonBackButton,
        IonCard,
        IonCardHeader,
        IonCardSubtitle,
        IonCardTitle,
        IonCol,
        IonList,
        IonItem,
        IonSelect,
        IonSelectOption,
        IonImg,
        IonGrid,
        IonLabel,
        IonRadio,
        IonRadioGroup,
        IonModal,
        IonDatetime,
        IonIcon,
        IonRow,
    },
    data() {
        return {
            selectedLocation: "",
            carparkArrayToShow: [],
            carparksArraySimu: [],

            pageTab: "recommend",
            dateTimeModal: true,
            currentDateTime: "",

            startPeak: "09:00:00",
            endPeak: "17:00:00",

            userOrigin: "",
            combinedLatLang: "",
            googleMapDistanceUrl: "",

            // for cheapest carparks
            // startTime: (new Date()).getHours() + ":" + (new Date()).getMinutes() ,
            startTime: "",
            endTime: "",
            bookingDate: "",

            test: "",
            userData: "",
            userBalance: 0,

            errorMessage: ""
        };
    },
    setup() {
        const handlerMessage = ref("");
        const confirmationAlert = async (carpark, bookingDate, startTime, endTime, userData) => {

            const alert = await alertController.create({
                header: "Confirm your booking? ",
                subHeader: "$" + carpark.data.totalFee + " will be deducted from your account",
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
                            // this.deductLot(carpark.data.carparkid,1,"-1" )
                            handlerMessage.value = "Alert confirmed";
                            const currentDateTime = new Date();
                            const date = currentDateTime.getDate();
                            const month = currentDateTime.getMonth() + 1;
                            const year = currentDateTime.getFullYear();

                            const hour = currentDateTime.getHours();
                            const min = currentDateTime.getMinutes();
                            const sec = currentDateTime.getSeconds();

                            const currentDateTimeFormatted =
                                year + "-" + month + "-" + date + " " + hour + ":" + min + ":" + sec;

                            bookingDate = bookingDate.substring(0, 10);

                            const startDateTimeFormatted =
                                bookingDate.substring(0, 10) +
                                " " +
                                startTime.substring(11, 19);
                            startTime = startTime.substring(11, 19);

                            const endDateTimeFormatted =
                                bookingDate.substring(0, 10) +
                                " " +
                                endTime.substring(11, 19);
                            endTime = endTime.substring(11, 19);

                            const userID = userData.userID;


                            let url = "http://127.0.0.1:5001/bookings";
                            axios
                                .post(url, {
                                    bookingDateTime: currentDateTimeFormatted,
                                    bookingLocation: carpark.data.carparklocation,
                                    locationName: carpark.data.carparkaddress,
                                    bookingStartDateTime: startDateTimeFormatted,
                                    bookingEndDateTime: endDateTimeFormatted,
                                    userID: userID,
                                    status: "Booked",
                                    bookingAmt: carpark.data.totalFee
                                })
                                .then((response) => {
                                    // deduct money
                                    url = "http://127.0.0.1:5001/updateBalance/" + response.data.data.bookingID;
                                    let bookingAmount = response.data.data.bookingAmt
                                    bookingAmount = bookingAmount.toString();
                                    const dotExists = bookingAmount.includes(".");
                                    let newFloat = bookingAmount;
                                    if (dotExists) {
                                        newFloat = bookingAmount.split(".");
                                        if (newFloat[1].length == 1) {
                                            newFloat[1] += "0";
                                        } else if (newFloat[1].length == 0) {
                                            newFloat[1] += "00";
                                        }
                                        newFloat = newFloat.join(".");
                                    } else {
                                        newFloat += ".00";
                                    }
                                    axios
                                        .put(url, {
                                            bookingID: response.data.data.bookingID,
                                        })
                                        .then((response) => {
                                            const balance = response.data.data
                                            const carparkID = carpark.data.carparkid
                                            const url = "http://127.0.0.1:5004/lotAdj/" + carparkID + "/2/1"
                                            axios
                                                .get(url)
                                                .then((response) => { 
                                                    sucessMsg(newFloat, balance);
                                                })
                                                .catch((error) => {
                                                    console.log(error.message);
                                                });
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
                subHeader: "$" + amount + " deducted. Balance is " + "$" + balance.toFixed(2),
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
    methods: {
        formatMoney(myFloat) { // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
            myFloat = myFloat.toFixed(2)
            myFloat = myFloat.toString()
            const dotExists = myFloat.includes('.')
            let newFloat = myFloat
            if (dotExists) {
                newFloat = myFloat.split(".")
                if ((newFloat[1]).length == 1) {
                    newFloat[1] += "0"
                } else if ((newFloat[1]).length == 0) {
                    newFloat[1] += "00"
                }
                newFloat = newFloat.join(".")
            } else {
                newFloat += ".00"
            }

            return newFloat
        },
        pushLog(msg) {
            this.selectedLocation = msg;
        },
        setDateTimeOpen(isOpen) {
            this.dateTimeModal = isOpen;
        },
        loaduser(){
            this.userData = JSON.parse(localStorage.getItem("userData"));

            const url = "http://127.0.0.1:5002/getBalance/" + parseInt(this.userData.userID)
            axios.get(url)
                .then((response) => {
                    this.userBalance = response.data.data.balance
                })
                .catch((error) => {
                    console.log(error);
                });

        },
        formatDate(date){ // parsing in Date require DD-MM-YY but get Date functions output is only 1 digit
            const newDate = "00" + date
            return(newDate.slice(-2))
        },
        confirmDateTime() {
            // error validation
            this.errorMessage = []
            if (this.startTime >= this.endTime && this.startTime != "" && this.endTime != "") {
                this.errorMessage.push("End Time must be later than Start Time!")
            }
            if (this.bookingDate == "") {
                this.errorMessage.push("You need to indicate booking Date!")
            }
            if (this.startTime == "") {
                this.errorMessage.push("You need to indicate start time !")
            }
            if (this.endTime == "") {
                this.errorMessage.push("You need to indicate end time !")
            }
            if (this.selectedLocation == "") {
                this.errorMessage.push("You need to indicate a location!")
            }

             // to check if booking start time > current time
            let startDateTime = this.startTime
            const currentDate = new Date();
            startDateTime = new Date(startDateTime)

            let bookingDateTime = this.bookingDate
            bookingDateTime = new Date(bookingDateTime)

            if (currentDate.getDate() == bookingDateTime.getDate() && currentDate.getMonth() == bookingDateTime.getMonth() && currentDate.getYear() == bookingDateTime.getYear() ) {
                if (currentDate-startDateTime > 0){
                   this.errorMessage.push("Start time must be after current time.")
                }
            } 
            
            if (this.errorMessage.length == 0) {
                this.carparksArraySimu = []
                this.setDateTimeOpen(false); // close popup
                this.getSimulator();   
            }
        },
        limitBookingDate(){
             // to limit booking date to after curent date
             const currentDateTime = new Date();
            const date = this.formatDate(currentDateTime.getDate());
            const month = this.formatDate(currentDateTime.getMonth() + 1);
            const year = currentDateTime.getFullYear();
            const hour = this.formatDate(currentDateTime.getHours());
            const min = this.formatDate(currentDateTime.getMinutes());
            const sec = this.formatDate(currentDateTime.getSeconds());
            const currentDateTimeFormatted =
                year + "-" + month + "-" + date + "T" + hour + ":" + min + ":" + sec;
            this.currentDateTime = currentDateTimeFormatted
        },
        changeTab(){
            if (this.pageTab == "recommend"){
                this.recommendationTab()
            }
            if (this.pageTab == "all" ){
                // this.carparkArrayToShow =  this.carparksArraySimu 
                this.carparkArrayToShow = JSON.parse(JSON.stringify(this.carparksArraySimu));
            }
            if (this.pageTab== "nearest"){
                this.nearestTab()
            }
            if (this.pageTab== "cheapest"){
                this.cheapestTab()
            }
            if (this.pageTab== "lotsAvail"){
                this.lotsAvailTab()
            }
        },
        recommendationTab(){
            const distanceWeight = 0.01 //distance in meter --> 1026. lower distance better
            const lotsAvailWeight = 1 // lots --> 40 higher lots better
            const priceWeight = 0.5 // price in dollars --> 19.5. lower price better 
            this.carparkArrayToShow = JSON.parse(JSON.stringify(this.carparksArraySimu));
            for (const eachCarpark of this.carparkArrayToShow){
                eachCarpark["points"] = distanceWeight * eachCarpark.distance_km_value +lotsAvailWeight * eachCarpark.data.lotbalancehourly + priceWeight *  eachCarpark.data.totalFee
            }
            this.carparkArrayToShow = this.carparkArrayToShow.sort(function(a, b) {
                const keyA = a.points;
                const keyB = b.points;
                if (keyA > keyB) return -1;
                if (keyA < keyB) return 1;
                return 0;
            });
            this.carparkArrayToShow= this.carparkArrayToShow.slice(0,4)
        },
        nearestTab(){
            this.carparkArrayToShow = JSON.parse(JSON.stringify(this.carparksArraySimu));
            this.carparkArrayToShow.sort(function(a, b) {
                const keyA = a.distance_km_value;
                const keyB = b.distance_km_value;
                if (keyA < keyB) return -1;
                if (keyA > keyB) return 1;
                return 0;
            })
            this.carparkArrayToShow= this.carparkArrayToShow.slice(0,4)
        },
        cheapestTab(){
            this.carparkArrayToShow = JSON.parse(JSON.stringify(this.carparksArraySimu));
            this.carparkArrayToShow.sort(function(a, b) {
                const keyA = a.data.totalFee;
                const keyB = b.data.totalFee;
                if (keyA < keyB) return -1;
                if (keyA > keyB) return 1;
                return 0;
            });
            this.carparkArrayToShow = this.carparkArrayToShow.slice(0, 4);
        },
        lotsAvailTab(){
            this.carparkArrayToShow = JSON.parse(JSON.stringify(this.carparksArraySimu));
            this.carparkArrayToShow = this.carparkArrayToShow.sort(function(a, b) {
                const keyA = a.availableLots;
                const keyB = b.availableLots;
                if (keyA > keyB) return -1;
                if (keyA < keyB) return 1;
                return 0;
            });
            this.carparkArrayToShow = this.carparkArrayToShow.slice(0, 4);
        },
        getSimulator() { 
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
                        availableLots: response.data.data.lotbalancehourly,
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
                                availableLots: response.data.data.lotbalancehourly,
                                // lat: 1.3040258775031617,
                                // long: 103.83608284915861
                            })
                            this.combinedLatLang += "1.3040258775031617" + "," + "103.83608284915861" + "|";
                            url = "http://127.0.0.1:5004/getCarpark/3";
                            axios
                                .post(url, {
                                    "requesttype": 1000,
                                    "carparkid": 3
                                })
                                .then((response) => {
                                    this.carparksArraySimu.push({
                                        data: response.data.data,
                                        image: "assets/images/takashimaya.jpeg",
                                        availableLots: response.data.data.lotbalancehourly,
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
                                                availableLots: response.data.data.lotbalancehourly,
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
                                                        availableLots: response.data.data.lotbalancehourly,
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
                                                                availableLots: response.data.data.lotbalancehourly,
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
                                                                        availableLots: response.data.data.lotbalancehourly,
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
                                                                                availableLots: response.data.data.lotbalancehourly,
                                                                                image: "assets/images/wisma.jpeg",
                                                                                // lat: 1.303842974291844,
                                                                                // long: 103.8333226716273
                                                                            })
                                                                            console.log(this.carparksArraySimu)
                                                                            
                                                                            this.combinedLatLang += "1.303842974291844" + "," + "103.8333226716273" + "|";
                                                                            
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
                                                                                    
                                                                                // this.userOrigin = "1.3064433533620563,103.83276247871694"
                                                                                const url = "http://127.0.0.1:5009/getCoords";
                                                                                axios
                                                                                    .post(url, {
                                                                                        "origin": this.userOrigin
                                                                                    })
                                                                                    .then((response) => {
                                                                                        const destinations = response.data.rows[0].elements
                                                                                        for (let i = 0; i < this.carparksArraySimu.length; i++) {
                                                                                            this.carparksArraySimu[i]["distance_km"] = destinations[i].distance.text;
                                                                                            this.carparksArraySimu[i]["distance_km_value"] = destinations[i].distance.value;
                                                                                            this.carparksArraySimu[i]["duration_mins"] = destinations[i].duration_in_traffic.text;
                                                                                        }
                                                                                        

            // for (let i = 0; i < this.carparksArraySimu.length ; i++) {
            const bookingDateFormatted = this.bookingDate.substring(0, 10);
            const startDateTime = new Date(bookingDateFormatted + " " + this.startTime.substring(11, 19));
            const endDateTime = new Date(
                bookingDateFormatted + " " + this.endTime.substring(11, 19));

            const url = "http://127.0.0.1:5004/getCarparkPrice/1"
            axios
                .get(url)
                .then((response) => {

                    let fee = 0
                    // weekend
                    if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                        // for (const eachCarpark of response.data.data.carparks) {
                        // if booking start and end in peak
                        if (
                            endDateTime <
                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                            startDateTime >
                            new Date(bookingDateFormatted + " " + this.startPeak)
                        ) {
                            const duration =
                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                            fee = duration * response.data.data.weekendpeakhourly;
                        }

                        // if booking start in non peak and end in peak
                        else if (
                            endDateTime <
                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                            startDateTime <
                            new Date(bookingDateFormatted + " " + this.startPeak)
                        ) {
                            const peakFee =
                                (Math.floor(
                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                            startDateTime) /
                                        3600000
                                    ) +
                                    1) *
                                response.data.data.weekendpeakhourly;
                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                            fee = peakFee + nonPeakFee;
                        }

                        // if booking start in peak and end in non peak
                        else if (
                            endDateTime >
                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                            startDateTime <
                            new Date(bookingDateFormatted + " " + this.endPeak)
                        ) {
                            const peakFee =
                                (Math.floor(
                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                            startDateTime) /
                                        3600000
                                    ) +
                                    1) *
                                response.data.data.weekendpeakhourly;
                            const nonPeakFee =
                                (Math.floor(
                                        (endDateTime -
                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                        3600000
                                    ) +
                                    1) *
                                response.data.data.weekendpeaknonhourly;
                            fee = peakFee + nonPeakFee;
                        }

                        // if booking start and end in non peak
                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                        else {
                            const duration =
                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                            fee = duration * response.data.data.weekendnonpeakhourly;
                        }

                    }

                    // weekday
                    else {
                        // for (const eachCarpark of response.data.data.carparks) {
                        // if booking start and end in peak
                        if (
                            endDateTime <
                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                            startDateTime >
                            new Date(bookingDateFormatted + " " + this.startPeak)
                        ) {
                            const duration =
                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                            fee = duration * response.data.data.weekdaypeakhourly;
                        }

                        // if booking start in non peak and end in peak
                        else if (
                            new Date(bookingDateFormatted + " " + this.startPeak) <
                            endDateTime && endDateTime <
                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                            startDateTime <
                            new Date(bookingDateFormatted + " " + this.startPeak)
                        ) {
                            const peakFee =
                                (Math.floor(
                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                            startDateTime) /
                                        3600000
                                    ) +
                                    1) *
                                response.data.data.weekdaypeakhourly;
                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                            fee = peakFee + nonPeakFee;
                        }

                        // if booking start in peak and end in non peak
                        else if (
                            endDateTime >
                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                            startDateTime <
                            new Date(bookingDateFormatted + " " + this.endPeak)
                        ) {
                            const peakFee =
                                (Math.floor(
                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                            startDateTime) /
                                        3600000
                                    ) +
                                    1) *
                                response.data.data.weekdaypeakhourly
                            const nonPeakFee =
                                (Math.floor(
                                        (endDateTime -
                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                        3600000
                                    ) +
                                    1) *
                                response.data.data.weekdaynonpeakhourly;
                            fee = peakFee + nonPeakFee;
                        }

                        // if booking start and end in non peak
                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                        else {
                            const duration =
                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                            fee = duration * response.data.data.weekdaynonpeakhourly;
                        }

                    }
                    this.carparksArraySimu[0].data["totalFee"] = this.formatMoney(fee / 100)

                    /////////// 2
                    const url = "http://127.0.0.1:5004/getCarparkPrice/2"
                    axios
                        .get(url)
                        .then((response) => {

                            let fee = 0
                            // weekend
                            if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                // for (const eachCarpark of response.data.data.carparks) {
                                // if booking start and end in peak
                                if (
                                    endDateTime <
                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                    startDateTime >
                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                ) {
                                    const duration =
                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                    fee = duration * response.data.data.weekendpeakhourly;
                                }

                                // if booking start in non peak and end in peak
                                else if (
                                    endDateTime <
                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                    startDateTime <
                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                ) {
                                    const peakFee =
                                        (Math.floor(
                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                    startDateTime) /
                                                3600000
                                            ) +
                                            1) *
                                        response.data.data.weekendpeakhourly;
                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                    fee = peakFee + nonPeakFee;
                                }

                                // if booking start in peak and end in non peak
                                else if (
                                    endDateTime >
                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                    startDateTime <
                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                ) {
                                    const peakFee =
                                        (Math.floor(
                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                    startDateTime) /
                                                3600000
                                            ) +
                                            1) *
                                        response.data.data.weekendpeakhourly;
                                    const nonPeakFee =
                                        (Math.floor(
                                                (endDateTime -
                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                3600000
                                            ) +
                                            1) *
                                        response.data.data.weekendpeaknonhourly;
                                    fee = peakFee + nonPeakFee;
                                }

                                // if booking start and end in non peak
                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                else {
                                    const duration =
                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                    fee = duration * response.data.data.weekendnonpeakhourly;
                                }

                            }

                            // weekday
                            else {
                                // for (const eachCarpark of response.data.data.carparks) {
                                // if booking start and end in peak
                                if (
                                    endDateTime <
                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                    startDateTime >
                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                ) {
                                    const duration =
                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                    fee = duration * response.data.data.weekdaypeakhourly;
                                }

                                // if booking start in non peak and end in peak
                                else if (
                                    new Date(bookingDateFormatted + " " + this.startPeak) <
                                    endDateTime && endDateTime <
                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                    startDateTime <
                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                ) {
                                    const peakFee =
                                        (Math.floor(
                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                    startDateTime) /
                                                3600000
                                            ) +
                                            1) *
                                        response.data.data.weekdaypeakhourly;
                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                    fee = peakFee + nonPeakFee;
                                }

                                // if booking start in peak and end in non peak
                                else if (
                                    endDateTime >
                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                    startDateTime <
                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                ) {
                                    const peakFee =
                                        (Math.floor(
                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                    startDateTime) /
                                                3600000
                                            ) +
                                            1) *
                                        response.data.data.weekdaypeakhourly
                                    const nonPeakFee =
                                        (Math.floor(
                                                (endDateTime -
                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                3600000
                                            ) +
                                            1) *
                                        response.data.data.weekdaynonpeakhourly;
                                    fee = peakFee + nonPeakFee;
                                }

                                // if booking start and end in non peak
                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                else {
                                    const duration =
                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                    fee = duration * response.data.data.weekdaynonpeakhourly;
                                }

                            }
                            this.carparksArraySimu[1].data["totalFee"] = this.formatMoney(fee / 100)


                            ///////////////3
                            const url = "http://127.0.0.1:5004/getCarparkPrice/3"
                            axios
                                .get(url)
                                .then((response) => {
                                    let fee = 0
                                    // weekend
                                    if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                        // for (const eachCarpark of response.data.data.carparks) {
                                        // if booking start and end in peak
                                        if (
                                            endDateTime <
                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                            startDateTime >
                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                        ) {
                                            const duration =
                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                            fee = duration * response.data.data.weekendpeakhourly;
                                        }

                                        // if booking start in non peak and end in peak
                                        else if (
                                            endDateTime <
                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                            startDateTime <
                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                        ) {
                                            const peakFee =
                                                (Math.floor(
                                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                            startDateTime) /
                                                        3600000
                                                    ) +
                                                    1) *
                                                response.data.data.weekendpeakhourly;
                                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                            fee = peakFee + nonPeakFee;
                                        }

                                        // if booking start in peak and end in non peak
                                        else if (
                                            endDateTime >
                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                            startDateTime <
                                            new Date(bookingDateFormatted + " " + this.endPeak)
                                        ) {
                                            const peakFee =
                                                (Math.floor(
                                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                            startDateTime) /
                                                        3600000
                                                    ) +
                                                    1) *
                                                response.data.data.weekendpeakhourly;
                                            const nonPeakFee =
                                                (Math.floor(
                                                        (endDateTime -
                                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                        3600000
                                                    ) +
                                                    1) *
                                                response.data.data.weekendpeaknonhourly;
                                            fee = peakFee + nonPeakFee;
                                        }

                                        // if booking start and end in non peak
                                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                        else {
                                            const duration =
                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                            fee = duration * response.data.data.weekendnonpeakhourly;
                                        }

                                    }

                                    // weekday
                                    else {
                                        // for (const eachCarpark of response.data.data.carparks) {
                                        // if booking start and end in peak
                                        if (
                                            endDateTime <
                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                            startDateTime >
                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                        ) {
                                            const duration =
                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                            fee = duration * response.data.data.weekdaypeakhourly;
                                        }

                                        // if booking start in non peak and end in peak
                                        else if (
                                            new Date(bookingDateFormatted + " " + this.startPeak) <
                                            endDateTime && endDateTime <
                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                            startDateTime <
                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                        ) {
                                            const peakFee =
                                                (Math.floor(
                                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                            startDateTime) /
                                                        3600000
                                                    ) +
                                                    1) *
                                                response.data.data.weekdaypeakhourly;
                                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                            fee = peakFee + nonPeakFee;
                                        }

                                        // if booking start in peak and end in non peak
                                        else if (
                                            endDateTime >
                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                            startDateTime <
                                            new Date(bookingDateFormatted + " " + this.endPeak)
                                        ) {
                                            const peakFee =
                                                (Math.floor(
                                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                            startDateTime) /
                                                        3600000
                                                    ) +
                                                    1) *
                                                response.data.data.weekdaypeakhourly
                                            const nonPeakFee =
                                                (Math.floor(
                                                        (endDateTime -
                                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                        3600000
                                                    ) +
                                                    1) *
                                                response.data.data.weekdaynonpeakhourly;
                                            fee = peakFee + nonPeakFee;
                                        }

                                        // if booking start and end in non peak
                                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                        else {
                                            const duration =
                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                            fee = duration * response.data.data.weekdaynonpeakhourly;
                                        }

                                    }
                                    this.carparksArraySimu[2].data["totalFee"] = this.formatMoney(fee / 100)


                                    /////////// 4
                                    const url = "http://127.0.0.1:5004/getCarparkPrice/4"
                                    axios
                                        .get(url)
                                        .then((response) => {
                                            let fee = 0
                                            // weekend
                                            if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                                // for (const eachCarpark of response.data.data.carparks) {
                                                // if booking start and end in peak
                                                if (
                                                    endDateTime <
                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                    startDateTime >
                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                ) {
                                                    const duration =
                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                    fee = duration * response.data.data.weekendpeakhourly;
                                                }

                                                // if booking start in non peak and end in peak
                                                else if (
                                                    endDateTime <
                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                    startDateTime <
                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                ) {
                                                    const peakFee =
                                                        (Math.floor(
                                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                    startDateTime) /
                                                                3600000
                                                            ) +
                                                            1) *
                                                        response.data.data.weekendpeakhourly;
                                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                                    fee = peakFee + nonPeakFee;
                                                }

                                                // if booking start in peak and end in non peak
                                                else if (
                                                    endDateTime >
                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                    startDateTime <
                                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                                ) {
                                                    const peakFee =
                                                        (Math.floor(
                                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                    startDateTime) /
                                                                3600000
                                                            ) +
                                                            1) *
                                                        response.data.data.weekendpeakhourly;
                                                    const nonPeakFee =
                                                        (Math.floor(
                                                                (endDateTime -
                                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                3600000
                                                            ) +
                                                            1) *
                                                        response.data.data.weekendpeaknonhourly;
                                                    fee = peakFee + nonPeakFee;
                                                }

                                                // if booking start and end in non peak
                                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                else {
                                                    const duration =
                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                    fee = duration * response.data.data.weekendnonpeakhourly;
                                                }

                                            }

                                            // weekday
                                            else {
                                                // for (const eachCarpark of response.data.data.carparks) {
                                                // if booking start and end in peak
                                                if (
                                                    endDateTime <
                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                    startDateTime >
                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                ) {
                                                    const duration =
                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                    fee = duration * response.data.data.weekdaypeakhourly;
                                                }

                                                // if booking start in non peak and end in peak
                                                else if (
                                                    new Date(bookingDateFormatted + " " + this.startPeak) <
                                                    endDateTime && endDateTime <
                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                    startDateTime <
                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                ) {
                                                    const peakFee =
                                                        (Math.floor(
                                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                    startDateTime) /
                                                                3600000
                                                            ) +
                                                            1) *
                                                        response.data.data.weekdaypeakhourly;
                                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                                    fee = peakFee + nonPeakFee;
                                                }

                                                // if booking start in peak and end in non peak
                                                else if (
                                                    endDateTime >
                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                    startDateTime <
                                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                                ) {
                                                    const peakFee =
                                                        (Math.floor(
                                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                    startDateTime) /
                                                                3600000
                                                            ) +
                                                            1) *
                                                        response.data.data.weekdaypeakhourly
                                                    const nonPeakFee =
                                                        (Math.floor(
                                                                (endDateTime -
                                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                3600000
                                                            ) +
                                                            1) *
                                                        response.data.data.weekdaynonpeakhourly;
                                                    fee = peakFee + nonPeakFee;
                                                }

                                                // if booking start and end in non peak
                                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                else {
                                                    const duration =
                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                    fee = duration * response.data.data.weekdaynonpeakhourly;
                                                }

                                            }
                                            this.carparksArraySimu[3].data["totalFee"] = this.formatMoney(fee / 100)


                                            /////////// 5
                                            const url = "http://127.0.0.1:5004/getCarparkPrice/5"
                                            axios
                                                .get(url)
                                                .then((response) => {
                                                    let fee = 0
                                                    // weekend
                                                    if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                                        // for (const eachCarpark of response.data.data.carparks) {
                                                        // if booking start and end in peak
                                                        if (
                                                            endDateTime <
                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                            startDateTime >
                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                        ) {
                                                            const duration =
                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                            fee = duration * response.data.data.weekendpeakhourly;
                                                        }

                                                        // if booking start in non peak and end in peak
                                                        else if (
                                                            endDateTime <
                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                            startDateTime <
                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                        ) {
                                                            const peakFee =
                                                                (Math.floor(
                                                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                            startDateTime) /
                                                                        3600000
                                                                    ) +
                                                                    1) *
                                                                response.data.data.weekendpeakhourly;
                                                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                                            fee = peakFee + nonPeakFee;
                                                        }

                                                        // if booking start in peak and end in non peak
                                                        else if (
                                                            endDateTime >
                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                            startDateTime <
                                                            new Date(bookingDateFormatted + " " + this.endPeak)
                                                        ) {
                                                            const peakFee =
                                                                (Math.floor(
                                                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                            startDateTime) /
                                                                        3600000
                                                                    ) +
                                                                    1) *
                                                                response.data.data.weekendpeakhourly;
                                                            const nonPeakFee =
                                                                (Math.floor(
                                                                        (endDateTime -
                                                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                        3600000
                                                                    ) +
                                                                    1) *
                                                                response.data.data.weekendpeaknonhourly;
                                                            fee = peakFee + nonPeakFee;
                                                        }

                                                        // if booking start and end in non peak
                                                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                        else {
                                                            const duration =
                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                            fee = duration * response.data.data.weekendnonpeakhourly;
                                                        }

                                                    }

                                                    // weekday
                                                    else {
                                                        // for (const eachCarpark of response.data.data.carparks) {
                                                        // if booking start and end in peak
                                                        if (
                                                            endDateTime <
                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                            startDateTime >
                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                        ) {
                                                            const duration =
                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                            fee = duration * response.data.data.weekdaypeakhourly;
                                                        }

                                                        // if booking start in non peak and end in peak
                                                        else if (
                                                            new Date(bookingDateFormatted + " " + this.startPeak) <
                                                            endDateTime && endDateTime <
                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                            startDateTime <
                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                        ) {
                                                            const peakFee =
                                                                (Math.floor(
                                                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                            startDateTime) /
                                                                        3600000
                                                                    ) +
                                                                    1) *
                                                                response.data.data.weekdaypeakhourly;
                                                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                                            fee = peakFee + nonPeakFee;
                                                        }

                                                        // if booking start in peak and end in non peak
                                                        else if (
                                                            endDateTime >
                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                            startDateTime <
                                                            new Date(bookingDateFormatted + " " + this.endPeak)
                                                        ) {
                                                            const peakFee =
                                                                (Math.floor(
                                                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                            startDateTime) /
                                                                        3600000
                                                                    ) +
                                                                    1) *
                                                                response.data.data.weekdaypeakhourly
                                                            const nonPeakFee =
                                                                (Math.floor(
                                                                        (endDateTime -
                                                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                        3600000
                                                                    ) +
                                                                    1) *
                                                                response.data.data.weekdaynonpeakhourly;
                                                            fee = peakFee + nonPeakFee;
                                                        }

                                                        // if booking start and end in non peak
                                                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                        else {
                                                            const duration =
                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                            fee = duration * response.data.data.weekdaynonpeakhourly;
                                                        }

                                                    }
                                                    this.carparksArraySimu[4].data["totalFee"] = this.formatMoney(fee / 100)


                                                    ///////////////6
                                                    const url = "http://127.0.0.1:5004/getCarparkPrice/6"
                                                    axios
                                                        .get(url)
                                                        .then((response) => {
                                                            let fee = 0
                                                            // weekend
                                                            if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                                                // for (const eachCarpark of response.data.data.carparks) {
                                                                // if booking start and end in peak
                                                                if (
                                                                    endDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                    startDateTime >
                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                ) {
                                                                    const duration =
                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                    fee = duration * response.data.data.weekendpeakhourly;
                                                                }

                                                                // if booking start in non peak and end in peak
                                                                else if (
                                                                    endDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                    startDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                ) {
                                                                    const peakFee =
                                                                        (Math.floor(
                                                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                                    startDateTime) /
                                                                                3600000
                                                                            ) +
                                                                            1) *
                                                                        response.data.data.weekendpeakhourly;
                                                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                                                    fee = peakFee + nonPeakFee;
                                                                }

                                                                // if booking start in peak and end in non peak
                                                                else if (
                                                                    endDateTime >
                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                    startDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                                                ) {
                                                                    const peakFee =
                                                                        (Math.floor(
                                                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                                    startDateTime) /
                                                                                3600000
                                                                            ) +
                                                                            1) *
                                                                        response.data.data.weekendpeakhourly;
                                                                    const nonPeakFee =
                                                                        (Math.floor(
                                                                                (endDateTime -
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                                3600000
                                                                            ) +
                                                                            1) *
                                                                        response.data.data.weekendpeaknonhourly;
                                                                    fee = peakFee + nonPeakFee;
                                                                }

                                                                // if booking start and end in non peak
                                                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                                else {
                                                                    const duration =
                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                    fee = duration * response.data.data.weekendnonpeakhourly;
                                                                }

                                                            }

                                                            // weekday
                                                            else {
                                                                // for (const eachCarpark of response.data.data.carparks) {
                                                                // if booking start and end in peak
                                                                if (
                                                                    endDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                    startDateTime >
                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                ) {
                                                                    const duration =
                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                    fee = duration * response.data.data.weekdaypeakhourly;
                                                                }

                                                                // if booking start in non peak and end in peak
                                                                else if (
                                                                    new Date(bookingDateFormatted + " " + this.startPeak) <
                                                                    endDateTime && endDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                    startDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                ) {
                                                                    const peakFee =
                                                                        (Math.floor(
                                                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                                    startDateTime) /
                                                                                3600000
                                                                            ) +
                                                                            1) *
                                                                        response.data.data.weekdaypeakhourly;
                                                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                                                    fee = peakFee + nonPeakFee;
                                                                }

                                                                // if booking start in peak and end in non peak
                                                                else if (
                                                                    endDateTime >
                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                    startDateTime <
                                                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                                                ) {
                                                                    const peakFee =
                                                                        (Math.floor(
                                                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                                    startDateTime) /
                                                                                3600000
                                                                            ) +
                                                                            1) *
                                                                        response.data.data.weekdaypeakhourly
                                                                    const nonPeakFee =
                                                                        (Math.floor(
                                                                                (endDateTime -
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                                3600000
                                                                            ) +
                                                                            1) *
                                                                        response.data.data.weekdaynonpeakhourly;
                                                                    fee = peakFee + nonPeakFee;
                                                                }

                                                                // if booking start and end in non peak
                                                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                                else {
                                                                    const duration =
                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                    fee = duration * response.data.data.weekdaynonpeakhourly;
                                                                }

                                                            }
                                                            this.carparksArraySimu[5].data["totalFee"] = this.formatMoney(fee / 100)

                                                            ///////////////7
                                                            const url = "http://127.0.0.1:5004/getCarparkPrice/7"
                                                            axios
                                                                .get(url)
                                                                .then((response) => {
                                                                    let fee = 0
                                                                    // weekend
                                                                    if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                                                        // for (const eachCarpark of response.data.data.carparks) {
                                                                        // if booking start and end in peak
                                                                        if (
                                                                            endDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                            startDateTime >
                                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                                        ) {
                                                                            const duration =
                                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                            fee = duration * response.data.data.weekendpeakhourly;
                                                                        }

                                                                        // if booking start in non peak and end in peak
                                                                        else if (
                                                                            endDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                            startDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                                        ) {
                                                                            const peakFee =
                                                                                (Math.floor(
                                                                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                                            startDateTime) /
                                                                                        3600000
                                                                                    ) +
                                                                                    1) *
                                                                                response.data.data.weekendpeakhourly;
                                                                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                                                            fee = peakFee + nonPeakFee;
                                                                        }

                                                                        // if booking start in peak and end in non peak
                                                                        else if (
                                                                            endDateTime >
                                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                            startDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.endPeak)
                                                                        ) {
                                                                            const peakFee =
                                                                                (Math.floor(
                                                                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                                            startDateTime) /
                                                                                        3600000
                                                                                    ) +
                                                                                    1) *
                                                                                response.data.data.weekendpeakhourly;
                                                                            const nonPeakFee =
                                                                                (Math.floor(
                                                                                        (endDateTime -
                                                                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                                        3600000
                                                                                    ) +
                                                                                    1) *
                                                                                response.data.data.weekendpeaknonhourly;
                                                                            fee = peakFee + nonPeakFee;
                                                                        }

                                                                        // if booking start and end in non peak
                                                                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                                        else {
                                                                            const duration =
                                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                            fee = duration * response.data.data.weekendnonpeakhourly;
                                                                        }

                                                                    }

                                                                    // weekday
                                                                    else {
                                                                        // for (const eachCarpark of response.data.data.carparks) {
                                                                        // if booking start and end in peak
                                                                        if (
                                                                            endDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                            startDateTime >
                                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                                        ) {
                                                                            const duration =
                                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                            fee = duration * response.data.data.weekdaypeakhourly;
                                                                        }

                                                                        // if booking start in non peak and end in peak
                                                                        else if (
                                                                            new Date(bookingDateFormatted + " " + this.startPeak) <
                                                                            endDateTime && endDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                            startDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.startPeak)
                                                                        ) {
                                                                            const peakFee =
                                                                                (Math.floor(
                                                                                        (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                                            startDateTime) /
                                                                                        3600000
                                                                                    ) +
                                                                                    1) *
                                                                                response.data.data.weekdaypeakhourly;
                                                                            const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                                                            fee = peakFee + nonPeakFee;
                                                                        }

                                                                        // if booking start in peak and end in non peak
                                                                        else if (
                                                                            endDateTime >
                                                                            new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                            startDateTime <
                                                                            new Date(bookingDateFormatted + " " + this.endPeak)
                                                                        ) {
                                                                            const peakFee =
                                                                                (Math.floor(
                                                                                        (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                                            startDateTime) /
                                                                                        3600000
                                                                                    ) +
                                                                                    1) *
                                                                                response.data.data.weekdaypeakhourly
                                                                            const nonPeakFee =
                                                                                (Math.floor(
                                                                                        (endDateTime -
                                                                                            new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                                        3600000
                                                                                    ) +
                                                                                    1) *
                                                                                response.data.data.weekdaynonpeakhourly;
                                                                            fee = peakFee + nonPeakFee;
                                                                        }

                                                                        // if booking start and end in non peak
                                                                        // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                                        else {
                                                                            const duration =
                                                                                Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                            fee = duration * response.data.data.weekdaynonpeakhourly;
                                                                        }

                                                                    }
                                                                    this.carparksArraySimu[6].data["totalFee"] = this.formatMoney(fee / 100)


                                                                    ///////////////8
                                                                    const url = "http://127.0.0.1:5004/getCarparkPrice/8"
                                                                    axios
                                                                        .get(url)
                                                                        .then((response) => {
                                                                            let fee = 0
                                                                            // weekend
                                                                            if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                                                                                // for (const eachCarpark of response.data.data.carparks) {
                                                                                // if booking start and end in peak
                                                                                if (
                                                                                    endDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                                    startDateTime >
                                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                                ) {
                                                                                    const duration =
                                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                                    fee = duration * response.data.data.weekendpeakhourly;
                                                                                }

                                                                                // if booking start in non peak and end in peak
                                                                                else if (
                                                                                    endDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                                    startDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                                ) {
                                                                                    const peakFee =
                                                                                        (Math.floor(
                                                                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                                                    startDateTime) /
                                                                                                3600000
                                                                                            ) +
                                                                                            1) *
                                                                                        response.data.data.weekendpeakhourly;
                                                                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekendnonpeakhourly;
                                                                                    fee = peakFee + nonPeakFee;
                                                                                }

                                                                                // if booking start in peak and end in non peak
                                                                                else if (
                                                                                    endDateTime >
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                                    startDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                                                                ) {
                                                                                    const peakFee =
                                                                                        (Math.floor(
                                                                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                                                    startDateTime) /
                                                                                                3600000
                                                                                            ) +
                                                                                            1) *
                                                                                        response.data.data.weekendpeakhourly;
                                                                                    const nonPeakFee =
                                                                                        (Math.floor(
                                                                                                (endDateTime -
                                                                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                                                3600000
                                                                                            ) +
                                                                                            1) *
                                                                                        response.data.data.weekendpeaknonhourly;
                                                                                    fee = peakFee + nonPeakFee;
                                                                                }

                                                                                // if booking start and end in non peak
                                                                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                                                else {
                                                                                    const duration =
                                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                                    fee = duration * response.data.data.weekendnonpeakhourly;
                                                                                }

                                                                            }

                                                                            // weekday
                                                                            else {
                                                                                // for (const eachCarpark of response.data.data.carparks) {
                                                                                // if booking start and end in peak
                                                                                if (
                                                                                    endDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                                    startDateTime >
                                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                                ) {
                                                                                    const duration =
                                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                                    fee = duration * response.data.data.weekdaypeakhourly;
                                                                                }

                                                                                // if booking start in non peak and end in peak
                                                                                else if (
                                                                                    new Date(bookingDateFormatted + " " + this.startPeak) <
                                                                                    endDateTime && endDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                                    startDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.startPeak)
                                                                                ) {
                                                                                    const peakFee =
                                                                                        (Math.floor(
                                                                                                (new Date(bookingDateFormatted + " " + this.startPeak) -
                                                                                                    startDateTime) /
                                                                                                3600000
                                                                                            ) +
                                                                                            1) *
                                                                                        response.data.data.weekdaypeakhourly;
                                                                                    const nonPeakFee = (Math.floor((endDateTime - new Date(bookingDateFormatted + " " + this.startPeak)) / 3600000) + 1) * response.data.data.weekdaynonpeakhourly;
                                                                                    fee = peakFee + nonPeakFee;
                                                                                }

                                                                                // if booking start in peak and end in non peak
                                                                                else if (
                                                                                    endDateTime >
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                                                                                    startDateTime <
                                                                                    new Date(bookingDateFormatted + " " + this.endPeak)
                                                                                ) {
                                                                                    const peakFee =
                                                                                        (Math.floor(
                                                                                                (new Date(bookingDateFormatted + " " + this.endPeak) -
                                                                                                    startDateTime) /
                                                                                                3600000
                                                                                            ) +
                                                                                            1) *
                                                                                        response.data.data.weekdaypeakhourly
                                                                                    const nonPeakFee =
                                                                                        (Math.floor(
                                                                                                (endDateTime -
                                                                                                    new Date(bookingDateFormatted + " " + this.endPeak)) /
                                                                                                3600000
                                                                                            ) +
                                                                                            1) *
                                                                                        response.data.data.weekdaynonpeakhourly;
                                                                                    fee = peakFee + nonPeakFee;
                                                                                }

                                                                                // if booking start and end in non peak
                                                                                // else if ((endDateTime > (new Date(bookingDateFormatted + " " + this.endPeak))) && (startDateTime > (new Date(bookingDateFormatted + " " + this.startPeak)))) {
                                                                                else {
                                                                                    const duration =
                                                                                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                                                                                    fee = duration * response.data.data.weekdaynonpeakhourly;
                                                                                }

                                                                            }
                                                                            this.carparksArraySimu[7].data["totalFee"] = this.formatMoney(fee / 100)
                                                                            this.changeTab()

                                                    
                                                                        })

                                                                })
                                                        })

                                                })
                                        })
                                })
                        })
                })
                .catch((error) => {
                    console.log(error)
                })
        
                                                                                        
                                                                                        
                                                                                    
                                                                                    })
                                                                                    .catch((error) => {
                                                                                        console.log(error);
                                                                                    });
                                                                            

                                                                        })
                                                                })
                                                        })
                                                })
                                        })
                                })
                        })

                })

        },

    },
    mounted() {
        this.loaduser()
        this.limitBookingDate()
    },
});
</script>



<style scoped>
.addPaddingBottom {
    padding-bottom: 300px;
}

/* iOS places the subtitle above the title */

/* ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
}
ion-img::part(image) {
  width: 100%; /* or whatever value */

/* you can set the height value too */

/* } */
</style>


<!-- [
    {
        "data": {
            "carparkaddress": "290 Orchard Rd",
            "carparkid": 1,
            "carparklocation": "Paragon Shopping Centre",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238859",
            "lotallocatecomplimentary": 100,
            "lotallocatehourly": 50,
            "lotallocateseason": 50,
            "lotbalancecomplimentary": 97,
            "lotbalancehourly": 32,
            "lotbalanceseason": 48,
            "lotusecomplimentary": 3,
            "lotusehourly": 18,
            "lotuseseason": 2,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "16.00"
        },
        "image": "assets/images/paragon.jpg",
        "availableLots": 14,
        "distance_km": "2.0 km",
        "distance_km_value": "2.0 km",
        "duration_mins": "6 mins"
    },
    {
        "data": {
            "carparkaddress": "2 Orchard Turn",
            "carparkid": 2,
            "carparklocation": "ION Orchard",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238859",
            "lotallocatecomplimentary": 87,
            "lotallocatehourly": 43,
            "lotallocateseason": 50,
            "lotbalancecomplimentary": 74,
            "lotbalancehourly": 40,
            "lotbalanceseason": 50,
            "lotusecomplimentary": 13,
            "lotusehourly": 3,
            "lotuseseason": 0,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "21.60"
        },
        "image": "assets/images/ion.jpg",
        "availableLots": 37,
        "distance_km": "1.0 km",
        "distance_km_value": "1.0 km",
        "duration_mins": "2 mins"
    },
    {
        "data": {
            "carparkaddress": "391 Orchard Rd",
            "carparkid": 3,
            "carparklocation": "Takashimaya Shopping Centre",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238872",
            "lotallocatecomplimentary": 250,
            "lotallocatehourly": 89,
            "lotallocateseason": 30,
            "lotbalancecomplimentary": 250,
            "lotbalancehourly": 46,
            "lotbalanceseason": 28,
            "lotusecomplimentary": 0,
            "lotusehourly": 43,
            "lotuseseason": 2,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "12.40"
        },
        "image": "assets/images/takashimaya.jpeg",
        "availableLots": 3,
        "distance_km": "0.8 km",
        "distance_km_value": "0.8 km",
        "duration_mins": "3 mins"
    },
    {
        "data": {
            "carparkaddress": "310 Orchard Road Tang Plaza",
            "carparkid": 4,
            "carparklocation": "TANGS at Tang Plaza",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238864",
            "lotallocatecomplimentary": 40,
            "lotallocatehourly": 56,
            "lotallocateseason": 10,
            "lotbalancecomplimentary": 37,
            "lotbalancehourly": 45,
            "lotbalanceseason": 9,
            "lotusecomplimentary": 3,
            "lotusehourly": 11,
            "lotuseseason": 1,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "21.20"
        },
        "image": "assets/images/tangs.jpg",
        "availableLots": 34,
        "distance_km": "1.3 km",
        "distance_km_value": "1.3 km",
        "duration_mins": "6 mins"
    },
    {
        "data": {
            "carparkaddress": "501 Orchard Rd",
            "carparkid": 5,
            "carparklocation": "Wheelock Place",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238880",
            "lotallocatecomplimentary": 23,
            "lotallocatehourly": 40,
            "lotallocateseason": 39,
            "lotbalancecomplimentary": 20,
            "lotbalancehourly": 30,
            "lotbalanceseason": 6,
            "lotusecomplimentary": 3,
            "lotusehourly": 10,
            "lotuseseason": 33,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "16.00"
        },
        "image": "assets/images/Wheelock.png",
        "availableLots": 20,
        "distance_km": "0.5 km",
        "distance_km_value": "0.5 km",
        "duration_mins": "1 min"
    },
    {
        "data": {
            "carparkaddress": "313 Orchard Rd",
            "carparkid": 6,
            "carparklocation": "313@Somerset",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238895",
            "lotallocatecomplimentary": 30,
            "lotallocatehourly": 72,
            "lotallocateseason": 32,
            "lotbalancecomplimentary": 26,
            "lotbalancehourly": 66,
            "lotbalanceseason": 27,
            "lotusecomplimentary": 4,
            "lotusehourly": 6,
            "lotuseseason": 5,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "24.00"
        },
        "image": "assets/images/313.jpg",
        "availableLots": 60,
        "distance_km": "0.5 km",
        "distance_km_value": "0.5 km",
        "duration_mins": "2 mins"
    },
    {
        "data": {
            "carparkaddress": "2 Orchard Link",
            "carparkid": 7,
            "carparklocation": "*SCAPE",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "237978",
            "lotallocatecomplimentary": 33,
            "lotallocatehourly": 90,
            "lotallocateseason": 24,
            "lotbalancecomplimentary": 3,
            "lotbalancehourly": 56,
            "lotbalanceseason": 4,
            "lotusecomplimentary": 30,
            "lotusehourly": 34,
            "lotuseseason": 20,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "18.00"
        },
        "image": "assets/images/scape.jpg",
        "availableLots": 22,
        "distance_km": "0.8 km",
        "distance_km_value": "0.8 km",
        "duration_mins": "3 mins"
    },
    {
        "data": {
            "carparkaddress": "435 Orchard Rd",
            "carparkid": 8,
            "carparklocation": "Wisma Atria",
            "carparkoperatordescription": "",
            "carparkoperatorid": 0,
            "carparkpostalcode": "238877",
            "lotallocatecomplimentary": 43,
            "lotallocatehourly": 50,
            "lotallocateseason": 40,
            "lotbalancecomplimentary": 5,
            "lotbalancehourly": 17,
            "lotbalanceseason": 38,
            "lotusecomplimentary": 38,
            "lotusehourly": 33,
            "lotuseseason": 2,
            "requeststatus": 0,
            "requesttype": 1000,
            "totalFee": "14.00"
        },
        "availableLots": -16,
        "image": "assets/images/wisma.jpeg",
        "distance_km": "0.4 km",
        "distance_km_value": "0.4 km",
        "duration_mins": "1 min"
    }
] -->