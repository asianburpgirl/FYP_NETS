<template>
  <base-layout needToolBar="y" pageTitle="Users">
    <ion-grid>
      <h4 class="ion-text-start">List of Users</h4>
      <ion-grid>
        <ion-row>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">User ID</ion-col>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">Name</ion-col>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">Email</ion-col>
          <ion-col size="3" size-md="3" size-lg="3" class="row-header">Number</ion-col>
          <!-- <ion-col size="3" size-md="3" size-lg="3">Balance</ion-col> -->
        </ion-row>
        <ion-row v-for="user in userList" :key="user.userID">
          <ion-col size="3" size-md="3" size-lg="3">{{user.userID}}</ion-col>
          <ion-col size="3" size-md="3" size-lg="3">{{user.name}}</ion-col>
          <ion-col size="3" size-md="3" size-lg="3">{{user.email}}</ion-col>
          <ion-col size="3" size-md="3" size-lg="3">{{user.phoneNum}}</ion-col>
        </ion-row>
      </ion-grid>
    </ion-grid>
  </base-layout>
</template>

<script>
import { IonGrid, IonRow, IonCol } from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
export default defineComponent({
  components: {
    IonGrid, IonRow, IonCol
  },
  data() {
    return {
      userList: [],
    };
  },
  methods: {
    getUsers() {
      const url = "http://ec2-3-26-37-251.ap-southeast-2.compute.amazonaws.com :5002/users";
      axios
        .get(url)
        .then((response) => {
          // console.log(response.data.data);
          this.userList = response.data.data.users
          console.log(this.userList)
          
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  mounted(){
    this.getUsers();
  }
});
</script>

<style scoped>
ion-col {
  background-color: #9cc8fa;
  border: solid 1px #fff;
  text-align: center;
  font-size: 11px;
}

.row-header{
  background-color: #4099ff;
  border: solid 1px #fff;
  font-weight: 700;
  text-align: center;
}
</style>
