<template>
  <base-layout pageTitle="Subscription Plans" pageToGoBack="/tabs/" needToolBar="y">
      <ion-card>
          <ion-grid>
          <ion-card-header>
            <ion-card-title>Just for you</ion-card-title>
            <ion-card-subtitle> 10% discount on your favourite carparks!</ion-card-subtitle>
            <ul v-for="eachCarpark in commonThreeCarpark" :key="eachCarpark">
              <li>{{ eachCarpark }}</li>
            </ul>
            You are paying: ${{ userSpending }} a month 
            <br>
            You save: ${{ userSave }} per month
            
            <br />
            <ion-item lines="none" >
              <ion-button  
              v-if="userHasPlan1==false"                
                slot ="end"
                color="success"
                size="large"
                @click="routeUser('buySubscription/mostVisited')">
                Subscribe</ion-button
              >
              <ion-button  
                v-if="userHasPlan1==true"   
                slot ="end"
                color="success"
                size="large"
                disabled = true>
                Subscribed</ion-button
              >
            </ion-item>
          </ion-card-header>
        </ion-grid>
      </ion-card>
      
      <ion-card>
        <ion-grid>
          <ion-card-header>
            <ion-card-title>Monthly Subscription</ion-card-title>
            <ion-card-subtitle> Monthly subscription for a fixed fee!</ion-card-subtitle> 
            <br />
            <ion-item lines="none" >
              <ion-button         
              v-if="userHasPlan2==false"           
                slot ="end"
                color="success"
                size="large"
                @click="routeUser('buySubscription/monthlyPlan')"
                :disabled = userHasPlan2>
                Subscribe</ion-button
              >
              <ion-button          
              v-if="userHasPlan2==true"       
                slot ="end"
                color="success"
                size="large">
                Subscribed</ion-button
              >
            </ion-item>
          </ion-card-header>
        </ion-grid>
      </ion-card>

      <!-- <ion-card>
        <ion-grid>
          <ion-card-header>
            <ion-card-title>Off Peak Discount</ion-card-title>
            <ion-card-subtitle> 10% discount on all carparks for non-peak parking!</ion-card-subtitle> 
            <br />
            <ion-item lines="none" >
              <ion-button                
                slot ="end"
                color="success"
                size="large"
                @click="routeUser('buySubscription/nonPeak')">
                Buy</ion-button
              >
            </ion-item>
          </ion-card-header>
        </ion-grid>
      </ion-card> -->

  </base-layout>
</template>

<script>
import {
  IonCardSubtitle,
  IonButton,
  IonCardTitle,
  IonItem,
  IonGrid,
  IonCard,
  IonCardHeader,
  // IonRow,
  // IonCol

} from "@ionic/vue";
import { defineComponent } from "vue";
// import ExploreContainer from '@/components/ExploreContainer.vue';
import axios from "axios";

export default defineComponent({
  components: {
    IonCardSubtitle,
    IonButton,
    IonCardTitle,
    IonItem,
    IonGrid,
    IonCard,
    IonCardHeader,
    // IonRow,
    // IonCol
     
  },
  data() {
        return {
            userData: {},
            commonThreeCarpark : [],
            userSave: 0,
            userSpending: 0,
            userHasPlan1: false,
            userHasPlan2: false
        }
    },
  methods: {
    load(){
      const url = "http://127.0.0.1:5003/carparkCat"
      axios.get(url)
          .then((response) => {
            console.log(response)
            })
          .catch((error) => {
              console.log(error);
          });
    },
    checkUserHasPlan(){
      let url = "http://127.0.0.1:5005/subs/" + parseInt(this.userData.userID) + "&"+ 1
      axios.get(url)
          .then((response) => {
            console.log(response.data.data,"1")
            this.userHasPlan1 = response.data.data.subscriptionsExists
            
                })
          .catch((error) => {
              console.log(error);
          });
      url = "http://127.0.0.1:5005/subs/" + parseInt(this.userData.userID) + "&"+ 2
        axios.get(url)
            .then((response) => {
              console.log(response.data.data,"2")
              this.userHasPlan2 = response.data.data.subscriptionsExists
            })
            .catch((error) => {
                console.log(error);
            });
    
    },
    routeUser(route) {
      this.$router.push({
        path: "/" + route,
      });
    },
    loadUserData() {
            this.userData = JSON.parse(localStorage.getItem("userData"));
            
        },
    getCommonBookings(){
      const url = "http://127.0.0.1:5001/commonCarparks/" + parseInt(this.userData.userID)
    axios.get(url)
        .then((response) => {
           this.commonThreeCarpark = response.data.data.carparks
        })
        .catch((error) => {
            console.log(error);
        });
        const url2 = "http://127.0.0.1:5001/commonBookingsAll/" + parseInt(this.userData.userID)
    axios.post(url2, { discount: 0.1})
        .then((response) => {
          this.userSave = response.data.data.discount
          this.userSpending =  response.data.data.totalPrice

           
        })
        .catch((error) => {
            console.log(error);
        });

    }
    
  },
  mounted() {
        this.load()
        this.loadUserData()
        this.getCommonBookings()
        this.checkUserHasPlan()
    }


  })
</script>



<style scoped>
.item-inner {
  padding: 0;
}
</style>
