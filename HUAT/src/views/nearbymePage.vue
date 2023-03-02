<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button defaultHref="/tabs/bookings"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Nearby Me!</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-searchbar></ion-searchbar>

      <ion-row class="ion-justify-content-center ion-padding">
        <ion-button shape="round" expand="block" @click="setDateTimeOpen(true)"
          >Change Booking Date and Time</ion-button
        >
      </ion-row>

      <!-- <ion-list class="ion-padding-top" v-if="endTime != '' && startTime!= '' &&bookingDate!= ''"> -->
        <ion-list class="ion-padding-top">
        <ion-radio-group v-model="pageTab" @ionChange="resetState()">
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

      <ion-list v-if="pageTab == 'nearest'">
        <ion-item>
          <ion-select
            placeholder="I am at:"
            @ionChange="
              pushLog($event.detail.value);
              this.getSimulator();
            "
          >
            <IonSelectOption value="orchard">Orchard</IonSelectOption>
            <IonSelectOption value="somerset">Somerset</IonSelectOption>
            <IonSelectOption value="yishun">Yishun</IonSelectOption>
          </ion-select>
        </ion-item>
      </ion-list>

      <div v-if="this.pageTab == 'nearest' && this.selectedLocation == ''">
        <h1>Select a location to view the nearest carparks to it!</h1>
      </div>
              
      <ion-grid
        class="ion-padding-top"
        v-if="
          (this.pageTab == 'nearest' && this.selectedLocation != '') ||
          this.pageTab == 'all' || (this.pageTab =='cheapest' && this.startTime != '' &&
          this.endTime !='' && this.bookingDate != '' ) || this.pageTab=='lotsAvail'
        "
      >
      <!-- v-if="endTime != '' && startTime!= '' &&bookingDate!= ''" -->
        <ion-card v-for="carpark in carparksArraySimu" :key="carpark">
          <ion-img :src="carpark.image"></ion-img>

          <ion-card-header>
            <ion-card-title>{{ carpark.data.carparklocation }}</ion-card-title>
            <ion-card-subtitle></ion-card-subtitle>
            <ion-card-subtitle>{{ carpark.data.carparkaddress }}</ion-card-subtitle>
            <h3>
              <b> {{ carpark.data.lotbalancehourly }}</b> lots available
            </h3>
            <h3  v-if="this.startTime != '' &&
          this.endTime !='' && this.bookingDate != '' ">
              <b> Total: ${{ carpark.data.totalFee }}</b>
            </h3>
            <h4 v-if="this.userOrigin != ''">
              <u>{{ carpark.distance_km }},</u>
              <u>{{ carpark.duration_mins }} </u>
              away from you
            </h4>
            <ion-row
            class="ion-padding-top ion-justify-content-center ion-padding-bottom">
            <!-- confirmationAlert(eachBooking.amount) -->
            <ion-button shape="round" @click="confirmationAlert(carpark,this.bookingDate,this.startTime,this.endTime,this.userData )">
              Book
              </ion-button>
            </ion-row>
          </ion-card-header>
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
          <ion-label position="stacked"> Booking Date:</ion-label>
          <ion-datetime
            presentation="date"
            v-model="bookingDate"
          ></ion-datetime>

          <ion-label position="stacked"> Start Time:</ion-label>
          <ion-datetime presentation="time" v-model="startTime"></ion-datetime>

          <ion-label position="stacked"> End Time:</ion-label>
          <ion-datetime presentation="time" v-model="endTime"></ion-datetime>

          <ion-row class="ion-padding-top">
            <ion-text color="danger" class="ion-padding-top">
              <li v-for="error in errorMessage" :key="error">
                {{ error }}
              </li>
            </ion-text>
          </ion-row>
          
          <ion-row
            class="ion-padding-top ion-justify-content-center ion-padding-bottom addPaddingBottom"
          >
            <ion-button shape="round" @click="confirmDateTime()"
              >Confirm</ion-button
            >
          </ion-row>
        </ion-content>
      </ion-modal>
    </ion-content>
  </ion-page>
</template>
<ion-content class="ion-padding"></ion-content>

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
  IonSearchbar,
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
import { defineComponent,ref } from "vue";
import axios from "axios";
// import { Geolocation } from "@capacitor/geolocation";

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
    IonSearchbar,
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
  // setup() {
  //   return { arrowBackOutline };
  // },
  data() {
    return {
      selectedLocation: "",
      // carparksArray: [],
      carparksArraySimu: [],
      pageTab: "all",
      dateTimeModal: true,

      //setting peak hours. can make it such that admin can change this value. value in 24 hours.
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

      errorMessage: ""
    };
  },
  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (carpark, bookingDate,startTime,endTime,userData ) => {
      
      const alert = await alertController.create({
        header: "Confirm your booking? ",
        subHeader: "$" + carpark.data.totalFee + " will be deducted from your account",
        buttons: [
          {
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
              console.log(carpark)
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
                console.log(response)
                  // deduct money
                  url = "http://127.0.0.1:5001/updateBalance/" + response.data.data.bookingID;
                  const bookingAmount = response.data.data.bookingAmt
                  axios
                    .put(url, {
                      bookingID: response.data.data.bookingID,
                    })
                    .then((response) => {
                      const balance = response.data.data
                      console.log(response)
                      const carparkID = carpark.data.carparkid
                      const url ="http://127.0.0.1:5004/lotAdj/"  + carparkID + "/2/1" 
                      axios
                        .get(url)
                        .then((response)=> {
                          console.log(response)
                          sucessMsg(bookingAmount, balance);

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

    const sucessMsg = async (amount,balance) => {
      const alert = await alertController.create({
        header: "Success!",
        subHeader: "$"+ amount + " deducted. Balance is " + "$" +balance.toFixed(2),
        buttons: [
          {
            text: "Okay",
            handler: () => {
              location.reload();
            },
          },
        ],
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
    deductLot(carparkid,parkingtype, lotadjustment ){
      const url ="http://127.0.0.1:5004/lotAdj/"  + carparkid + "/" + parkingtype+ "/" + lotadjustment
      axios
        .get(url)
        .then((response)=> {
          console.log(response)
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
   
    confirmDateTime() {

      // error validation
       this.errorMessage = []
      if (this.startTime >= this.endTime && this.startTime !="" && this.endTime !="" ){
        this.errorMessage.push("End Time must be later than Start Time!")
      }
      if(this.bookingDate ==""){
        this.errorMessage.push("You need to indicate booking Date!")
      }
      if(this.startTime ==""){
        this.errorMessage.push("You need to indicate start time !")
      }
      if(this.endTime ==""){
        this.errorMessage.push("You need to indicate end time !")
      }

      if (this.errorMessage.length == 0){
        this.setDateTimeOpen(false); // close popup
        this.getSimulator();
      }    
      
      // this.bookingDate.getDay()
    },
    setDateTimeOpen(isOpen) {
      this.dateTimeModal = isOpen;
    },
    resetState() {
      
      if (this.pageTab == "all") {
        this.userOrigin = "";
        this.selectedLocation = "";
        this.getSimulator();
      }
      if (this.pageTab == "lotsAvail") {
        // this.userOrigin = "";
        this.selectedLocation = "";
        // this.startTime= "",
        // this.endTime= "",
        // this.bookingDate=  "",
        this.carparksArraySimu.sort(function (a, b) {
            const keyA = a.data.lotbalancehourly;
            const keyB = b.data.lotbalancehourly;
            if (keyA < keyB) return 1;
            if (keyA > keyB) return -1;
            return 0;
          });
        this.carparksArraySimu = this.carparksArraySimu.slice(0, 4);
      }
      if (this.pageTab== "cheapest"){
        this.getCarparkPrices()
      }
      
    },
    pushLog(msg) {
      this.selectedLocation = msg;
    },
    getCarparkPrices(){
      // for (let i = 0; i < this.carparksArraySimu.length ; i++) {
      const bookingDateFormatted = this.bookingDate.substring(0, 10);
      const startDateTime = new Date(bookingDateFormatted + " " + this.startTime.substring(11, 19));
      const endDateTime = new Date(
      bookingDateFormatted + " " + this.endTime.substring(11, 19));     
  
      const url ="http://127.0.0.1:5004/getCarparkPrice/1" 
      axios
        .get(url)
        .then((response)=> {

          let fee = 0
           // weekend
           if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
              console.log("weekend");
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
                  const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
              console.log("weekday");
              // for (const eachCarpark of response.data.data.carparks) {
                // if booking start and end in peak
                if (
                  endDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime >
                    new Date(bookingDateFormatted + " " + this.startPeak)
                ) {
                  console.log("// if booking start and end in peak")
                  const duration =
                    Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                  fee = duration * response.data.data.weekdaypeakhourly;
                }

                // if booking start in non peak and end in peak
                else if (
                  new Date(bookingDateFormatted + " " + this.startPeak)<
                  endDateTime && endDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime <
                    new Date(bookingDateFormatted + " " + this.startPeak)
                ) {
                  console.log("//  if booking start in non peak and end in peak")
                  const peakFee =
                    (Math.floor(
                      (new Date(bookingDateFormatted + " " + this.startPeak) -
                        startDateTime) /
                        3600000
                    ) +
                      1) *
                    response.data.data.weekdaypeakhourly;
                  const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                  fee = peakFee + nonPeakFee;
                }

                // if booking start in peak and end in non peak
                else if (
                  endDateTime >
                    new Date(bookingDateFormatted + " " + this.endPeak) &&
                  startDateTime <
                    new Date(bookingDateFormatted + " " + this.endPeak)
                ) {
                  console.log("//  if booking start in peak and end in non peak")
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
                  console.log("else")
                  const duration =
                    Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                  fee = duration * response.data.data.weekdaynonpeakhourly;
                }
              
            }
          this.carparksArraySimu[0].data["totalFee"] = this.formatMoney(fee/100)
          
          /////////// 2
          const url ="http://127.0.0.1:5004/getCarparkPrice/2" 
          axios
            .get(url)
            .then((response)=> {

              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[1].data["totalFee"] = this.formatMoney(fee/100)
              

              ///////////////3
          const url ="http://127.0.0.1:5004/getCarparkPrice/3" 
          axios
            .get(url)
            .then((response)=> {
              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[2].data["totalFee"] = this.formatMoney(fee/100)
              

              /////////// 4
          const url ="http://127.0.0.1:5004/getCarparkPrice/4" 
          axios
            .get(url)
            .then((response)=> {
              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[3].data["totalFee"] = this.formatMoney(fee/100)
              

              /////////// 5
          const url ="http://127.0.0.1:5004/getCarparkPrice/5" 
          axios
            .get(url)
            .then((response)=> {
              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[4].data["totalFee"] = this.formatMoney(fee/100)
              

              ///////////////6
          const url ="http://127.0.0.1:5004/getCarparkPrice/6" 
          axios
            .get(url)
            .then((response)=> {
              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[5].data["totalFee"] = this.formatMoney(fee/100)
              

              ///////////////7
          const url ="http://127.0.0.1:5004/getCarparkPrice/7" 
          axios
            .get(url)
            .then((response)=> {
              console.log(response.data.data)
              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[6].data["totalFee"] = this.formatMoney(fee/100)
              

              ///////////////8
          const url ="http://127.0.0.1:5004/getCarparkPrice/8" 
          axios
            .get(url)
            .then((response)=> {
              let fee = 0
              // weekend
              if (startDateTime.getDay() == 6 || startDateTime.getDay() == 0) {
                  console.log("weekend");
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
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekendnonpeakhourly;
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
                  console.log("weekday");
                  // for (const eachCarpark of response.data.data.carparks) {
                    // if booking start and end in peak
                    if (
                      endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime >
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("// if booking start and end in peak")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaypeakhourly;
                    }

                    // if booking start in non peak and end in peak
                    else if (
                      new Date(bookingDateFormatted + " " + this.startPeak)<
                      endDateTime && endDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.startPeak)
                    ) {
                      console.log("//  if booking start in non peak and end in peak")
                      const peakFee =
                        (Math.floor(
                          (new Date(bookingDateFormatted + " " + this.startPeak) -
                            startDateTime) /
                            3600000
                        ) +
                          1) *
                        response.data.data.weekdaypeakhourly;
                      const nonPeakFee =(Math.floor((endDateTime -new Date(bookingDateFormatted + " " + this.startPeak)) /3600000) +1) * response.data.data.weekdaynonpeakhourly;
                      fee = peakFee + nonPeakFee;
                    }

                    // if booking start in peak and end in non peak
                    else if (
                      endDateTime >
                        new Date(bookingDateFormatted + " " + this.endPeak) &&
                      startDateTime <
                        new Date(bookingDateFormatted + " " + this.endPeak)
                    ) {
                      console.log("//  if booking start in peak and end in non peak")
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
                      console.log("else")
                      const duration =
                        Math.floor((endDateTime - startDateTime) / 3600000) + 1;
                      fee = duration * response.data.data.weekdaynonpeakhourly;
                    }
                  
                }
              this.carparksArraySimu[7].data["totalFee"] = this.formatMoney(fee/100)
              console.log("Fee", this.carparksArraySimu)

              if (this.pageTab == 'cheapest'){
                this.carparksArraySimu.sort(function (a, b) {
                const keyA = a.data.totalFee;
                const keyB = b.data.totalFee;
                if (keyA < keyB) return -1;
                if (keyA > keyB) return 1;
                return 0;
              });
              this.carparksArraySimu = this.carparksArraySimu.slice(0, 4);
              }
               
            })
              

            })

            })
              

            })
              

            })

              

            })


            })
          

        })
        .catch((error)=> {
          console.log(error)
        })
      // }
    },

    formatMoney(myFloat){ // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
      myFloat = myFloat.toFixed(2)
      myFloat = myFloat.toString()
      const dotExists = myFloat.includes('.')
      let newFloat= myFloat
      if (dotExists){
        newFloat = myFloat.split(".")
        if ((newFloat[1]).length ==1){
          newFloat[1] += "0"
        }
        else if ((newFloat[1]).length ==0){
          newFloat[1] += "00"
        }
        newFloat = newFloat.join(".")
      }
      else{
        newFloat += ".00"
      }
      
      return newFloat
    },
    calculateDistance() {
      const url = "http://127.0.0.1:5009/getCoords"
      axios
        .get(url)
        .then((response) => {
          const destinations = response.data.rows[0].elements;

          for (let i = 0; i < this.carparksArraySimu.length; i++) {
            // this.carparksArray[i]["distance_km"] = (destinations[i].distance.value / 1000).toPrecision(2)
            // this.carparksArray[i]["duration_mins"] = (destinations[i].duration_in_traffic.value / 60).toPrecision(2)
            this.carparksArraySimu[i]["distance_km"] =
              destinations[i].distance.text;
            this.carparksArraySimu[i]["distance_km_value"] =
              destinations[i].distance.value;
            this.carparksArraySimu[i]["duration_mins"] =
              destinations[i].duration_in_traffic.text;
          }

          this.carparksArraySimu.sort(function (a, b) {
            const keyA = a.distance_km_value;
            const keyB = b.distance_km_value;
            if (keyA < keyB) return -1;
            if (keyA > keyB) return 1;
            return 0;
          });

          this.carparksArraySimu = this.carparksArraySimu.slice(0, 4);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    getSimulator() {
      this.carparksArraySimu = []
      this.googleMapDistanceUrl ="https://maps.googleapis.com/maps/api/distancematrix/json?origins=";
      this.combinedLatLang = "";
      
      let url = "http://127.0.0.1:5004/getCarpark/1";
      axios
        .post(url,{
          "requesttype": 1000,
          "carparkid": 1
        })
        .then((response) => {
          this.carparksArraySimu.push({
            data :response.data.data,
            image: "assets/images/paragon.jpg",
            availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
            // lat: 1.3040258775031617,
            // long: 103.83608284915861
          })
          this.combinedLatLang +="1.3040258775031617" + "," + "103.83608284915861" + "|";
          url = "http://127.0.0.1:5004/getCarpark/2";
          axios
            .post(url,{
              "requesttype": 1000,
              "carparkid": 2
            })
            .then((response) => {
              this.carparksArraySimu.push({
                  data :response.data.data,
                  image: "assets/images/ion.jpg",
                  availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
                  // lat: 1.3040258775031617,
                  // long: 103.83608284915861
          })
          this.combinedLatLang +="1.3040258775031617" + "," + "103.83608284915861" + "|";
              url = "http://127.0.0.1:5004/getCarpark/3";
              axios
                .post(url,{
                  "requesttype": 1000,
                  "carparkid": 3
                })
                .then((response) => {
                  this.carparksArraySimu.push({
                    data :response.data.data,
                    image: "assets/images/takashimaya.jpeg",
                    availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
            //         lat: 1.3033454254185042,
            // long: 103.83455711763565
          })
            this.combinedLatLang +="1.3033454254185042" + "," + "103.83455711763565" + "|";
                  url = "http://127.0.0.1:5004/getCarpark/4";
                  axios
                    .post(url,{
                      "requesttype": 1000,
                      "carparkid": 4
                    })
                    .then((response) => {
                      this.carparksArraySimu.push({
                        data :response.data.data,
                        image: "assets/images/tangs.jpg",
                        availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
            //             lat: 1.3040258775031617,
            // long: 103.83608284915861
          })
            this.combinedLatLang +="1.3040258775031617" + "," + "103.83608284915861" + "|";
                      url = "http://127.0.0.1:5004/getCarpark/5";
                      axios
                        .post(url,{
                          "requesttype": 1000,
                          "carparkid": 5
                        })
                        .then((response) => {
                          this.carparksArraySimu.push({
                          data :response.data.data,
                          image: "assets/images/Wheelock.png",
                          availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
            //               lat: 1.3050314731714412,
            // long: 103.83297614415605
          })
            this.combinedLatLang +="1.3050314731714412" + "," + "103.83297614415605" + "|";
                          url = "http://127.0.0.1:5004/getCarpark/6";
                          axios
                            .post(url,{
                              "requesttype": 1000,
                              "carparkid": 6
                            })
                            .then((response) => {
                              this.carparksArraySimu.push({
                              data :response.data.data,
                              image: "assets/images/313.jpg",
                              availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
            //                   lat: 1.301171207812743,
            // long: 103.8386220085623
          })
            this.combinedLatLang +="1.301171207812743" + "," + "103.8386220085623" + "|";
                              url = "http://127.0.0.1:5004/getCarpark/7";
                              axios
                                .post(url,{
                                  "requesttype": 1000,
                                  "carparkid": 7
                                })
                                .then((response) => {
                                  this.carparksArraySimu.push({
                                data :response.data.data,
                                image: "assets/images/scape.jpg",
                                availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
            //                     lat: 1.3010677408660067,
            // long: 103.83576204980196
          })
            this.combinedLatLang +="1.3010677408660067" + "," + "103.83576204980196" + "|";
                                  url = "http://127.0.0.1:5004/getCarpark/8";
                                  axios
                                    .post(url,{
                                      "requesttype": 1000,
                                      "carparkid": 8
                                    })
                                    .then((response) => {
                                      this.getCarparkPrices()
                                      this.carparksArraySimu.push({
                                      data :response.data.data,
                                      availableLots: response.data.data.lotbalancehourly -  response.data.data.lotusehourly,
                                      image: "assets/images/wisma.jpeg",
                                      // lat: 1.303842974291844,
                                      // long: 103.8333226716273
                                    })
                                      this.combinedLatLang +="1.303842974291844" + "," + "103.8333226716273" + "|";
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

                                      
                                      // this.userOrigin = "1.3064433533620563,103.83276247871694"
                                      const url = "http://127.0.0.1:5009/getCoords";
                                      axios
                                        .post(url,{
                                          "origin": this.userOrigin
                                        })
                                        .then((response) => {
                                          

                                          const destinations = response.data.rows[0].elements
                                          for (let i = 0; i < this.carparksArraySimu.length; i++) {
                                            this.carparksArraySimu[i]["distance_km"] = destinations[i].distance.text;
                                            this.carparksArraySimu[i]["distance_km_value"] = destinations[i].distance.text;
                                            this.carparksArraySimu[i]["duration_mins"] =destinations[i].duration_in_traffic.text;
                                          }
                                          if (this.userOrigin != ""){
                                             this.carparksArraySimu.sort(function (a, b) {
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

    },
   
  },

  mounted() {
    this.userData = JSON.parse(localStorage.getItem("userData"));
            
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
