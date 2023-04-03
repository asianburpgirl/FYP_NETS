<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons>
          <ion-back-button defaultHref="/tabs/plans"></ion-back-button>
        </ion-buttons>
        <ion-title class="ion-text-center">Subscription Plan</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-grid>
        <ion-card
          v-if="userSufficientBalance == false && userSubscribed == false"
        >
          <ion-card-content>
            <p class="insufficient">
              Note: Insufficient credit. Please proceed to top up first.
            </p>
            <div class="ion-padding-top">
              <ion-button
                color="dark"
                size="small"
                @click="routeUser('payment')"
              >
                Top up
              </ion-button>
            </div>
          </ion-card-content>
        </ion-card>
        <ion-card v-if="subscriptionPlan == 'mostVisited'" color="primary">
          <ion-card-header>
            <ion-card-title> Your Favorite Carparks</ion-card-title>
          </ion-card-header>

          <ion-card-content>
            <div
              v-for="eachCarpark in commonThreeCarpark"
              :key="eachCarpark"
              class="ion-padding-bottom"
            >
              <li>{{ eachCarpark }}</li>
            </div>

            <p>
              You have been paying
              <b
                ><u>${{ userSpending }}</u></b
              >
              a month for the past 3 months
            </p>
            <p>
              You will be saving
              <b
                ><u>${{ userSave }}</u></b
              >
              per month
            </p>
            <!-- <p>
              Total :
              <b
                ><u>${{ subsAmt }}</u></b
              >
              per month
            </p> -->
          </ion-card-content>
        </ion-card>
        <ion-card v-if="subscriptionPlan == 'monthlyPlan'" color="primary">
          <ion-card-header>
            <ion-card-title> Monthly Plan </ion-card-title>
          </ion-card-header>
          <ion-card-content>
            <ion-card-subtitle>
              Park at 4 random carparks chosen every month for free!
            </ion-card-subtitle>
            <ul
              v-for="eachCarpark in subscriptionFourCarpark"
              :key="eachCarpark"
            >
              <li>{{ eachCarpark.carparkName }}</li>
            </ul>
          </ion-card-content>
        </ion-card>

        <ion-row class="ion-padding ion-justify-content-center">
          <ion-col v-if="userSubscribed == true">
            <ion-button expand="block" color="dark" disabled>
              Subscribed
            </ion-button>
          </ion-col>
          <ion-col v-if="userSubscribed == false">
            <ion-button
              fill="outline"
              expand="block"
              color="dark"
              :disabled="!userSufficientBalance"
              @click="confirmationAlert(subsAmt, userData, subsType)"
            >
              Subscribe
            </ion-button>
          </ion-col> </ion-row
        >
        
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonRow,
  IonCol,
  IonGrid,
  IonButton,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonCardSubtitle,
  alertController,
  IonHeader,
  IonPage,
  IonContent,
  IonBackButton,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import { useRoute } from "vue-router";
import { useRouter } from "vue-router";
import axios from "axios";

export default defineComponent({
  components: {
    IonRow,
    IonCol,
    IonGrid,
    IonButton,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonCardSubtitle,
    IonHeader,
    IonPage,
    IonContent,
    IonBackButton,
  },
  setup() {
    const handlerMessage = ref("");
    const confirmationAlert = async (subsAmt, userData, subsType) => {
      const alert = await alertController.create({
        header: "Subscription Confirmation",
        subHeader: "$" + subsAmt + " will be deducted from your account",
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
              const url = "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/subs";
              axios
                .post(url, {
                  subsTypeID: subsType,
                  subsDateTime: 1,
                  subsAmt: subsAmt,
                  status: "Subscribed",
                  userID: userData.userID,
                })
                .then((response) => {
                  // this.userSave = response.data.data.discount
                  // this.userSpending =  response.data.data.totalPrice
                  // this.subsAmt = (this.userSpending * 3 * 0.95).toFixed(2)

                  // deduct money
                  const url =
                    "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/updateBalanceSub/" +
                    response.data.data.subsID;
                  axios
                    .put(url, {
                      subsID: response.data.data.subsID,
                    })
                    .then((response) => {
                      sucessMsg(subsAmt, response.data.data);
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
        ],
      });
      await alert.present();
    };
    const router = useRouter();
    const sucessMsg = async (amount, balance) => {
      const alert = await alertController.create({
        header: "Success!",
        subHeader:
          "$" + amount + " deducted. Balance is " + "$" + balance.toFixed(2),
        buttons: [
          {
            text: "Okay",
            handler: () => {
              router.push("/tabs/plans").then(() => window.location.reload());
              // this.$router.push('/success').then(() => window.location.reload())
            },
          },
        ],
      });
      await alert.present();
    };

    const route = useRoute();
    const { subscriptionPlan } = route.params;
    return { subscriptionPlan, confirmationAlert, sucessMsg, router };

    // mostVisited or monthlyPlan
  },
  data() {
    return {
      userData: {},
      commonThreeCarpark: [],
      subscriptionFourCarpark: [],
      userSave: 0,
      userSpending: 0,
      subsAmt: 0,
      userSufficientBalance: false,
      userSubscribed: false,
      subsType: 0,
    };
  },
  methods: {
    getCarparksMonthlySubs() {
      const url = "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5003/chosenCarparks";
      axios
        .get(url)
        .then((response) => {
          this.subscriptionFourCarpark = response.data.data.carparks;
          this.subsAmt = 20;
          this.checkIfSufficientBalance(this.subsAmt);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    checkUserHasPlan() {
      const route = useRoute();
      const { subscriptionPlan } = route.params;
      let planType = 2;
      this.subsType = 2;
      if (subscriptionPlan == "mostVisited") {
        planType = 1;
        this.subsType = 1;
        this.getCommonBookings();
      } else {
        this.getCarparksMonthlySubs();
      }
      const url =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5005/subs/" +
        parseInt(this.userData.userID) +
        "&" +
        planType;
      axios
        .get(url)
        .then((response) => {
          this.userSubscribed = response.data.data.subscriptionsExists;
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
    checkIfSufficientBalance(amountToCheck) {
      const url =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5002/getBalance/" + parseInt(this.userData.userID);
      axios
        .get(url)
        .then((response) => {
          const userBalance = response.data.data.balance;
          if (userBalance > amountToCheck) {
            this.userSufficientBalance = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    loadUserData() {
      console.log("hi");
      this.userData = JSON.parse(localStorage.getItem("userData"));
      console.log(this.userSubscribed);
    },
    getCommonBookings() {
      const url =
        "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5001/commonCarparks/" +
        parseInt(this.userData.userID);
      axios
        .get(url)
        .then((response) => {
          this.commonThreeCarpark = response.data.data.carparks;
          const url2 =
            "http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5001/commonBookingsAll/" +
            parseInt(this.userData.userID);
          axios
            .post(url2, { discount: 0.1 })
            .then((response) => {
              this.userSave = response.data.data.discount;
              this.userSpending = response.data.data.totalPrice;
              this.subsAmt = (this.userSpending * 3 * 0.95).toFixed(2);
              this.checkIfSufficientBalance(this.subsAmt);
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
    this.loadUserData();
    this.checkUserHasPlan();
  },
});
</script>

<style scoped>
/* iOS places the subtitle above the title */

ion-card-header.ios {
  display: flex;
  flex-flow: column-reverse;
}

.insufficient {
  font-size: 11px;
  color: #ff5370;
}
</style>
