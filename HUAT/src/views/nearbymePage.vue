<template>
  <ion-page class="ion-padding">
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Nearby Me</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-searchbar></ion-searchbar>

      <ion-list class="ion-padding-top">
        <ion-radio-group v-model="pageTab">
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
        </ion-radio-group>
      </ion-list>

      <ion-list v-if="pageTab == 'nearest'">
        <ion-item>
          <ion-select
            placeholder="I am at:"
            @ionChange="
              pushLog($event.detail.value);
              this.getCarparks();
            "
          >
            <IonSelectOption value="orchard">Orchard</IonSelectOption>
            <IonSelectOption value="somerset">Somerset</IonSelectOption>
            <IonSelectOption value="yishun">Yishun</IonSelectOption>
          </ion-select>
        </ion-item>
      </ion-list>

      <!-- <ion-grid v-if="selectedLocation == 'orchard'"> -->
      <!-- <ion-grid v-if="pageTab=='all' && selectedLocation == 'orchard'" > -->
      <ion-grid class="ion-padding-top">
        <ion-card v-for="carpark in carparksArray" :key="carpark">
          <ion-img :src="carpark.imagePath"></ion-img>

          <ion-card-header>
            <ion-card-title>{{ carpark.carparkName }}</ion-card-title>
            <ion-card-subtitle></ion-card-subtitle>
            <ion-card-subtitle>{{ carpark.caparkLocation }}</ion-card-subtitle>
            <h3>
              <b> {{ carpark.availableLots }}</b> lots available
            </h3>
            <h4 v-if="this.userOrigin != '' &&  pageTab == 'nearest' ">
              <u>{{ carpark.distance_km }},</u>
              <u>{{ carpark.duration_mins }} </u>
              away from you
            </h4>
          </ion-card-header>
        </ion-card>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>
<ion-content class="ion-padding"></ion-content>

<script>
import {
  IonPage,
  IonHeader,
  IonTitle,
  IonContent,
  IonToolbar,
  IonButtons,
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
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
import { Geolocation } from "@capacitor/geolocation";

export default defineComponent({
  components: {
    IonPage,
    IonHeader,
    IonTitle,
    IonContent,
    IonToolbar,
    IonButtons,
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
  },
  data() {
    return {
      selectedLocation: "",
      carparksArray: [],
      pageTab: "all",

      userOrigin: "",
      combinedLatLang: "",
      googleMapDistanceUrl: "",
    };
  },
  methods: {
    pushLog(msg) {
      this.selectedLocation = msg;
    },
    getCarparks() {
        this.googleMapDistanceUrl =
        "https://maps.googleapis.com/maps/api/distancematrix/json?origins=";
      this.combinedLatLang = ""

      if (this.selectedLocation == "") { 
        console.log("empty")
      }
      else {
         if (this.selectedLocation == "orchard") {
        this.userOrigin = "1.3064433533620563,103.83276247871694";
      } else if (this.selectedLocation == "yishun") {
        this.userOrigin = "1.4304060903894582, 103.83515323243753";
      } else if (this.selectedLocation == "somerset") {
        this.userOrigin = "1.3016313961551784, 103.83849995957749";
      }
    
      
      const url = "http://127.0.0.1:5003/carparks";
      axios
        .get(url)
        .then((response) => {
          this.carparksArray = response.data.data.carparks;
          for (const eachCarpark of response.data.data.carparks) {
            eachCarpark["availableLots"] =
              eachCarpark.maxCapacity - eachCarpark.currentCapacity;
            this.combinedLatLang +=
              eachCarpark.latitude + "," + eachCarpark.longitude + "|";
          }
       
          this.googleMapDistanceUrl +=
            this.userOrigin +
            "&destinations=" +
            this.combinedLatLang.slice(0, -1) +
            "&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI";
          console.log(this.googleMapDistanceUrl);
          this.calculateDistance();
        })
        .catch((error) => {
          console.log(error.message);
        });
      }
    },
    calculateDistance() {
      axios
        .get(this.googleMapDistanceUrl)
        .then((response) => {
          const destinations = response.data.rows[0].elements;

          for (let i = 0; i < this.carparksArray.length; i++) {
            // this.carparksArray[i]["distance_km"] = (destinations[i].distance.value / 1000).toPrecision(2)
            // this.carparksArray[i]["duration_mins"] = (destinations[i].duration_in_traffic.value / 60).toPrecision(2)
            this.carparksArray[i]["distance_km"] =
              destinations[i].distance.text;
            this.carparksArray[i]["distance_km_value"] =
              destinations[i].distance.value;
            this.carparksArray[i]["duration_mins"] =
              destinations[i].duration_in_traffic.text;
          }

          this.carparksArray.sort(function (a, b) {
            var keyA = a.distance_km_value;
            var keyB = b.distance_km_value;
            if (keyA < keyB) return -1;
            if (keyA > keyB) return 1;
            return 0;
          });

          this.carparksArray = this.carparksArray.slice(0, 4);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },

  mounted() {
    this.getCarparks();
  },
});
</script>

<style scoped>
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
