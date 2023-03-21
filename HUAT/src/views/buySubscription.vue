<template>
  <base-layout pageTitle="Buy Subscription" pageToGoBack="/tabs/plans" needBackButton="y" needToolBar="y">
    
  <h2 v-if="subscriptionPlan=='mostVisited'">
    Your Favourite Carparks
    </h2>
    <ul v-for="eachCarpark in commonThreeCarpark" :key="eachCarpark" >
        <div v-if="subscriptionPlan=='mostVisited'">
            <li>{{ eachCarpark }}</li>
        </div>
        
    </ul>
  
  <ion-list v-if="subscriptionPlan=='mostVisited'">
    <br> 
    You are paying: <b>${{ userSpending }} </b> a month for last 3 months
            <br>
    You save: <b> ${{ userSave }}</b> per month
</ion-list>
    <br>
    <br>
    <br>
    
    <h1>Total :  ${{ subsAmt }} per month </h1> 
    
    <ion-list v-if="userSufficientBalance==false && userSubscribed==false">
        <ion-text color="danger" >
            <b>
                Insufficient credit. Please top up your balance first.
            </b>
        </ion-text>
        <ion-row class="ion-padding-top ion-justify-content-center ion-padding-bottom">
            <ion-button shape="round" @click="routeUser('payment')">
                Top up
            </ion-button>
        </ion-row>
    </ion-list>
    
    <ion-list v-if="userSubscribed==true">
        <ion-row class="ion-padding-top ion-justify-content-center ion-padding-bottom">
            <ion-button shape="round" disabled>
                Subscribed
            </ion-button>
        </ion-row>
    </ion-list>


    <ion-row class="ion-justify-content-center ion-padding-bottom" v-if="userSubscribed==false">
        <ion-button :disabled=!userSufficientBalance shape="round" @click="confirmationAlert(subsAmt)">
            Subscribe
        </ion-button>
    </ion-row>

  </base-layout>
</template>


<script>
import {  IonList, IonRow,IonButton,IonText, alertController  } from "@ionic/vue";
import { defineComponent,ref } from "vue";
import { useRoute } from 'vue-router';
import BaseLayout from "../components/baseLayout.vue";
import axios from "axios";
// import { arrowBack, home, star } from 'ionicons/icons';

export default defineComponent({
  components: {
    BaseLayout,
    IonList,
    IonRow,
    IonButton,
    IonText
  },
  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async ( subsAmt) => {
        const alert = await alertController.create({
            header: "Confirm your subscription? ",
            subHeader: "$" + subsAmt+ " will be deducted from your account",
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
                            const url="http://127.0.0.1:5005/subs" 
                            axios.post(url, { 
                                subsTypeID : "1",
                                subsDateTime: 1,
                                subsAmt: subsAmt,
                                status: "Subscribed",
                                userID: 1
                            })
                            .then((response) => {
                            // this.userSave = response.data.data.discount
                            // this.userSpending =  response.data.data.totalPrice
                            // this.subsAmt = (this.userSpending * 3 * 0.95).toFixed(2)

                            // deduct money
                            const url = "http://127.0.0.1:5005/updateBalanceSub/" + response.data.data.subsID;
                            axios
                                .put(url, {
                                    subsID: response.data.data.subsID,
                                })
                                .then((response) => {
                                    sucessMsg(subsAmt,response.data.data)
                                })
                                .catch((error) => {
                                    console.log(error.message);
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
        const sucessMsg = async (amount, balance) => {
            const alert = await alertController.create({
                header: "Success!",
                subHeader: "$" + amount + " deducted. Balance is " + "$" + balance.toFixed(2),
                buttons: [{
                    text: "Okay",
                    handler: () => {
                        
                        this.$router.push("/tabs/plans")
                    },
                }, ],
            });
            await alert.present();
        };
        
      const route = useRoute();
      const { subscriptionPlan } = route.params;
      return { subscriptionPlan, confirmationAlert, sucessMsg };
      
      // mostVisited or monthlyPlan
    },
    data() {
        return {
            userData: {},
            commonThreeCarpark : [],
            userSave: 0,
            userSpending: 0,
            subsAmt :0,
            userSufficientBalance: false,
            userSubscribed: false
        }
    },
  methods: {
    
    checkUserHasPlan(){
        const route = useRoute();
      const { subscriptionPlan } = route.params;
        let planType = 2
        if (subscriptionPlan =="mostVisited"){
            planType = 1
        }
      const url = "http://127.0.0.1:5005/subs/" + parseInt(this.userData.userID) + "&"+ planType
      axios.get(url)
          .then((response) => {
            this.userSubscribed = response.data.data.subscriptionsExists
            
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
    checkIfSufficientBalance(amountToCheck){
        const url = "http://127.0.0.1:5002/getBalance/" + parseInt(this.userData.userID)
    axios.get(url)
        .then((response) => {
           const userBalance= response.data.data.balance
           if (userBalance >amountToCheck ){
            this.userSufficientBalance = true
           }
        })
        .catch((error) => {
            console.log(error);
        });
    },
    changeCarParkChoice(){
      this.getCarparkPrices()
    },
    loadUserData() {
            this.userData = JSON.parse(localStorage.getItem("userData"));
            
        },
    getCommonBookings(){
        
      const url = "http://127.0.0.1:5001/commonCarparks/" + parseInt(this.userData.userID)
    axios.get(url)
        .then((response) => {
           this.commonThreeCarpark = response.data.data.carparks
           const url2 = "http://127.0.0.1:5001/commonBookingsAll/" + parseInt(this.userData.userID)
            axios.post(url2, { discount: 0.1})
                .then((response) => {
                this.userSave = response.data.data.discount
                this.userSpending =  response.data.data.totalPrice
                this.subsAmt = (this.userSpending * 3 * 0.95).toFixed(2)
                this.checkIfSufficientBalance(this.subsAmt)
                
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
  mounted() {
        this.loadUserData()
        this.checkUserHasPlan()
        this.getCommonBookings()
        
    }

});
</script>

<style scoped>
/* iOS places the subtitle above the title */

ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
}
</style>
