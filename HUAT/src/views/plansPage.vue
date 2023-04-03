<template>
  <base-layout
    pageTitle="Subscription Plans"
    pageToGoBack="/tabs/"
    needToolBar="y"
  >
    <h3><b>Subscription Plans</b></h3>
    <ion-card color="primary" v-if="userHasPlan2 == false">
      <!-- <ion-grid> -->
      <ion-card-header>
        <ion-card-title>Just For You</ion-card-title>
        <ion-card-subtitle>
          10% discount on your favorite carparks🚘</ion-card-subtitle
        >
        <!-- <ul v-for="eachCarpark in commonThreeCarpark" :key="eachCarpark">
          <li>{{ eachCarpark }}</li>
        </ul> -->
        <!-- You are paying: ${{ userSpending }} a month
        <br />
        You save: ${{ userSave }} per month -->
        Price: ${{ subsAmtPlan1 }} per month
        <ion-row class="ion-padding-top">
          <ion-col>
            <ion-button
              v-if="userHasPlan1 == false && userHasPlan2 == false"
              fill="outline"
              color="dark"
              expand="block"
              @click="routeUser('buySubscription/mostVisited')"
            >
              Click for more Info</ion-button
            >
            <ion-button
              v-if="userHasPlan1 == true || userHasPlan2 == true"
              fill="outline"
              color="dark"
              expand="block"
              disabled="true"
            >
              Subscribed</ion-button
            >
          </ion-col>
          <ion-col>
            <ion-button
              v-if="userHasPlan1 == true || userHasPlan2 == true"
              fill="outline"
              color="light"
              expand="block"
              @click="confirmationAlert(this.userData)"
            >
              Cancel</ion-button
            >
          </ion-col>
        </ion-row>
      </ion-card-header>
    </ion-card>

    <ion-card color="primary" v-if="userHasPlan1 == false">
      <ion-grid>
        <ion-card-header>
          <ion-card-title>Monthly Plan</ion-card-title>
          <ion-card-subtitle>
            Monthly subscription for 4 carparks💵</ion-card-subtitle
          >
          <!-- <ul v-for="eachCarpark in subscriptionFourCarpark" :key="eachCarpark">
            <li>{{ eachCarpark.carparkName }}</li>
          </ul> -->
          Price: ${{ subsAmtPlan2 }} per month
          <ion-row class="ion-padding-top">
            <ion-col>
              <ion-button
                v-if="userHasPlan2 == false && userHasPlan1 == false"
                fill="outline"
                color="dark"
                expand="block"
                @click="routeUser('buySubscription/monthlyPlan')"
                :disabled="userHasPlan2"
              >
                Click for more Info</ion-button
              >
              <ion-button
                v-if="userHasPlan2 == true || userHasPlan1 == true"
                fill="outline"
                color="dark"
                expand="block"
                disabled="true"
              >
                Subscribed</ion-button
              >
            </ion-col>
            <ion-col>
              <ion-button
                v-if="userHasPlan1 == true || userHasPlan2 == true"
                fill="outline"
                color="light"
                expand="block"
                @click="confirmationAlert(this.userData)"
              >
                Cancel</ion-button
              >
            </ion-col>
          </ion-row>
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
  IonGrid,
  IonCard,
  IonCardHeader,
  alertController,
  IonRow,
  IonCol,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  components: {
    IonCardSubtitle,
    IonButton,
    IonCardTitle,
    IonGrid,
    IonCard,
    IonCardHeader,
    IonRow,
    IonCol,
  },
  data() {
    return {
      userData: {},
      commonThreeCarpark: [],
      subscriptionFourCarpark: [],
      userSave: 0,
      userSpending: 0,
      subsAmtPlan1: 0,
      subsAmtPlan2: 20,
      userHasPlan1: false,
      userHasPlan2: false,
      subUserHas: 0,
    };
  },

  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (userData) => {
      const alert = await alertController.create({
        header: "Delete your subscription? ",
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
              //get sub ID of user subscription
              const url =
                "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/subs/" + parseInt(userData.userID);
              axios
                .get(url)
                .then((response) => {
                  const subToDeleteID =
                    response.data.data.subscriptions[0].subsID;
                  //delete id = sub id
                  const url = "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/subs/" + subToDeleteID;
                  axios
                    .delete(url)
                    .then((response) => {
                      sucessMsg();
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
        ],
      });
      await alert.present();
    };

    const sucessMsg = async () => {
      const alert = await alertController.create({
        header: "Success!",
        subHeader: "The subscription plan has been deleted",
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
    return { confirmationAlert, sucessMsg };
  },
  methods: {
    formatMoney(myFloat) {
      // money in DB store in 1 dp (eg. 12.1), to change to 2 dp (12.10)
      myFloat = myFloat.toFixed(2);
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
    getCarparksMonthlySubs() {
      const url = "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5003/chosenCarparks";
      axios
        .get(url)
        .then((response) => {
          this.subscriptionFourCarpark = response.data.data.carparks;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    checkUserHasPlan() {
      let url =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/subs/" +
        parseInt(this.userData.userID) +
        "&" +
        1;
      axios
        .get(url)
        .then((response) => {
          this.userHasPlan1 = response.data.data.subscriptionsExists;
        })
        .catch((error) => {
          console.log(error);
        });
      url =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/subs/" +
        parseInt(this.userData.userID) +
        "&" +
        2;
      axios
        .get(url)
        .then((response) => {
          this.userHasPlan2 = response.data.data.subscriptionsExists;
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
    getCommonBookings() {
      const url =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5001/commonCarparks/" +
        parseInt(this.userData.userID);
      axios
        .get(url)
        .then((response) => {
          this.commonThreeCarpark = response.data.data.carparks;
        })
        .catch((error) => {
          console.log(error);
        });
      const url2 =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5001/commonBookingsAll/" +
        parseInt(this.userData.userID);
      axios
        .post(url2, { discount: 0.1 })
        .then((response) => {
          this.userSave = response.data.data.discount;
          this.userSpending = this.formatMoney(response.data.data.totalPrice);
          this.subsAmtPlan1 = this.formatMoney(
            Math.max((this.userSpending * 3 * 0.95).toFixed(2), 10)
          );
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getCarparksMonthlySubs();
    this.loadUserData();
    this.getCommonBookings();
    this.checkUserHasPlan();
  },
});
</script>

<style scoped>
ion-card-content {
  line-height: 1;
}
</style>
