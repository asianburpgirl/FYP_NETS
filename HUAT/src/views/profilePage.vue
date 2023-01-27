<template>
  <base-layout pageTitle="My Profile" needToolBar="y">
      <ion-content>
          <ion-list line="none" class="list card">
              <ion-item class="profile-item">
                  <div class="profile-picture big-profile-picture">
                      <img src="https://ionicframework.com/docs/img/demos/avatar.svg">
                  </div>
              </ion-item>
              
          </ion-list >
          <ion-grid>
              <!-- <ion-row class="ion-padding-horizontal ion-padding-top ion-justify-content-center ion-align-items-center"> -->
              <!-- <ion-row>
                      <ion-col>
                        <ion-avatar>
                          <img
                            alt="Silhouette of a person's head"
                            src="https://ionicframework.com/docs/img/demos/avatar.svg"
                          />
                        </ion-avatar>
                      </ion-col>
                      <ion-col size="10">
                        <ion-item button detail="true">
                          <ion-label>
                            <h2>Mary Tan</h2>
                            <p>Edit Profile</p>
                          </ion-label>
                        </ion-item>
                      </ion-col>
                    </ion-row> -->
  
              <!-- <ion-row>
                          <ion-col>
                              <ion-avatar>
                                  <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
                              </ion-avatar>
                              <ion-label><h1> {{userData.name}} </h1> </ion-label>
                          </ion-col>
                      </ion-row> -->
  
              <!-- <ion-row class="ion-padding">
                      <h4>My Wallet</h4>
                    </ion-row> -->
  
              <!-- <ion-row>
                      <ion-col class="ion-margin-horizontal">
                        <ion-icon :icon="wallet" />
                        <ion-badge color="danger" style="position: absolute"
                          >$100.45</ion-badge
                        >
                      </ion-col>
                      <ion-col>
                        <ion-button shape="round" color="danger">Top Up</ion-button>
                      </ion-col>
                    </ion-row> -->
              <!-- <ion-item>
                      <ion-col class="ion-margin-horizontal"> -->
              <!-- <ion-icon :icon="wallet" /> -->
              <!-- <ion-badge color="danger" style="position: absolute"
                          >$100.45</ion-badge
                        >
                      </ion-col>
                      <ion-col>
                        <ion-button shape="round" color="danger">Top Up</ion-button>
                      </ion-col>
                    </ion-item> -->
          </ion-grid>
  
          <ion-list class="ion-margin">
              <ion-item button detail="true">
                  <ion-label>Edit Profile</ion-label>
              </ion-item>
              <ion-item button detail="true">
                  <ion-label @click='routeUser("viewBooking")'>View Bookings</ion-label>
              </ion-item>
  
              <ion-item button detail="true">
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
              </ion-item>
              <ion-item button detail="true" href="/">
                  <ion-label>Log Out</ion-label>
              </ion-item>
          </ion-list>
      </ion-content>
  
  </base-layout>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
      return {
          userData: {}
      }
  },
  methods: {
      loadUserData() {
          this.userData = JSON.parse(localStorage.getItem("userData") || '{}');
      },

      routeUser(route: string) {
          this.$router.push({
              path: '/' + route,
          });
      }
  },
  // Calls function on page load
  mounted() {
      this.loadUserData();
  }
});
</script>



<style scoped>
/* ion-icon {
  font-size: 50px;
} */

.profile-item {
text-align: center;
}

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

.profile-name {
padding-top: 20px;
font-size: x-large !important;
font-weight: bold !important;
text-transform: capitalize;
}
</style>
