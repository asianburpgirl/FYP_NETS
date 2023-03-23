<template>
  <base-layout pageTitle="Subscription Plans" pageToGoBack="/tabs/" needToolBar="y">
      <ion-card v-if="userHasPlan2==false"  >
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
            <br> 
            Price: ${{ subsAmtPlan1 }} per month
            
            <br />
            <ion-item lines="none" >
              <ion-button  
              v-if="userHasPlan1==false && userHasPlan2==false "                
                slot ="end"
                color="success"
                size="large"
                @click="routeUser('buySubscription/mostVisited')">
                Subscribe</ion-button
              >
              <ion-button  
                v-if="userHasPlan1==true || userHasPlan2==true "   
                slot ="end"
                color="success"
                size="large"
                disabled = true>
                Subscribed</ion-button
              >
            </ion-item>
            <br>
              <ion-button  
              v-if="userHasPlan1==true || userHasPlan2==true "   
                color="danger"
                size="large"
                @click="confirmationAlert(this.userData)">
                Cancel</ion-button
              >
          </ion-card-header>
        </ion-grid>
      </ion-card>
      
      <ion-card v-if="userHasPlan1==false "  >
        <ion-grid>
          <ion-card-header>
            <ion-card-title>Monthly Subscription</ion-card-title>
            <ion-card-subtitle> Monthly subscription for these carparks for a fixed fee!</ion-card-subtitle> 
            <ul v-for="eachCarpark in subscriptionFourCarpark" :key="eachCarpark">
              <li>{{ eachCarpark.carparkName }}</li>
            </ul>
            <br> 
            Price: ${{ subsAmtPlan2 }} per month
            <br>
            
            <ion-item lines="none" >
              <ion-button         
              v-if="userHasPlan2==false && userHasPlan1==false"           
                slot ="end"
                color="success"
                size="large"
                @click="routeUser('buySubscription/monthlyPlan')"
                :disabled = userHasPlan2>
                Subscribe</ion-button
              >
              <ion-button          
              v-if="userHasPlan2==true || userHasPlan1==true "       
                slot ="end"
                color="success"
                size="large"
                disabled = true>
                Subscribed</ion-button
              >
            </ion-item>
            <br>
              <ion-button  
                v-if="userHasPlan1==true || userHasPlan2==true "   
                color="danger"
                size="large"
                @click="confirmationAlert(this.userData)">
                Cancel</ion-button
              >
          </ion-card-header>
        </ion-grid>
      </ion-card>
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
  alertController

} from "@ionic/vue";
import { defineComponent,ref } from "vue";
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
     
  },
  data() {
        return {
            userData: {},
            commonThreeCarpark : [],
            subscriptionFourCarpark : [],
            userSave: 0,
            userSpending: 0,
            subsAmtPlan1: 0,
            subsAmtPlan2: 20,
            userHasPlan1: false,
            userHasPlan2: false,
            subUserHas: 0,
        }
    },

  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (userData) => {
        const alert = await alertController.create({
            header: "Delete your subscription? ",
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
                            //get sub ID of user subscription
                            const url = "http://127.0.0.1:5005/subs/" + parseInt(userData.userID) 
                                axios.get(url)
                                    .then((response) => {
                                      const subToDeleteID =  response.data.data.subscriptions[0].subsID
                                      //delete id = sub id         
                                      const url = "http://127.0.0.1:5005/subs/" + subToDeleteID
                                      axios.delete(url)
                                          .then((response) => {
                                            
                                            sucessMsg()
                                          })
                                          .catch((error) => {
                                              console.log(error);
                                          });

                                      })
                                    .catch((error) => {
                                        console.log(error);
                                    });  
                        },
                    },
            ]
        });
        await alert.present();
    };
        
        const sucessMsg = async () => {
            const alert = await alertController.create({
                header: "Success!",
                subHeader: "The subscription plan has been deleted",
                buttons: [{
                    text: "Okay",
                    handler: () => {
                      location.reload()
                    },
                }, ],
            });
            await alert.present();
        };
      return {  confirmationAlert, sucessMsg };
      
    },
  methods: {
    getCarparksMonthlySubs(){
      const url = "http://127.0.0.1:5003/chosenCarparks"
      axios.get(url)
          .then((response) => {
            this.subscriptionFourCarpark = response.data.data.carparks
            })
          .catch((error) => {
              console.log(error);
          });
    },
    checkUserHasPlan(){
      let url = "http://127.0.0.1:5005/subs/" + parseInt(this.userData.userID) + "&"+ 1
      axios.get(url)
          .then((response) => {
            this.userHasPlan1 = response.data.data.subscriptionsExists
            
                })
          .catch((error) => {
              console.log(error);
          });
      url = "http://127.0.0.1:5005/subs/" + parseInt(this.userData.userID) + "&"+ 2
        axios.get(url)
            .then((response) => {
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
          this.subsAmtPlan1 = Math.max((this.userSpending * 3 * 0.95).toFixed(2),10)
        })
        .catch((error) => {
            console.log(error);
        });
    }
  },
  mounted() {
        this.getCarparksMonthlySubs()
        this.loadUserData()
        this.getCommonBookings()
        this.checkUserHasPlan()
    }
  })
</script>


<style scoped>

</style>
