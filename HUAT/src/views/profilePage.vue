<template>
  <base-layout pageTitle="My Profile" needToolBar="y">
    <div class="profile-picture big-profile-picture">
      <img src="../../public/assets/images/woman.png" />
    </div>
    <ion-list class="ion-margin">
      <ion-item button>
        <ion-label @click="routeUser('viewProfile')">Edit Profile</ion-label>
      </ion-item>
      <!-- <ion-item button detail="true">
                <ion-label @click='routeUser("viewBooking")'>View Bookings</ion-label>
            </ion-item> -->

      <!-- <ion-item button detail="true">
                <ion-label>Setting</ion-label>
            </ion-item>
            <ion-item button detail="true">
                <ion-label>Language</ion-label>
            </ion-item>
            <ion-item button detail="true">
                <ion-label>Feedback</ion-label>
            </ion-item>
            <ion-item button detail="true">
                <ion-label>Help Centre</ion-label>
            </ion-item> -->
      <ion-item button href="/">
        <ion-label>Log Out</ion-label>
      </ion-item>
    </ion-list>
  </base-layout>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { IonLabel, IonItem, IonList } from "@ionic/vue";

export default defineComponent({
  components: {
    IonLabel,
    IonItem,
    IonList
  },
  data() {
    return {
      userData: {},
    };
  },
  methods: {
    loadUserData() {
      this.userData = JSON.parse(localStorage.getItem("userData") || "{}");
    },

    routeUser(route: string) {
      this.$router.push({
        path: "/" + route,
      });
    },
  },
  // Calls function on page load
  mounted() {
    this.loadUserData();
  },
});
</script>

<style scoped>
.profile-picture {
  border: 1px solid rgba(0, 0, 0, 0.25);
  padding: 3px;
  border-radius: 100%;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  margin: 0 auto;
  width: 128px;
  height: 128px;
  overflow: hidden;
}

.profile-picture img {
  width: 128px;
  border-radius: 100%;
}
</style>
