<template>
    <base-layout needToolBar="y" pageTitle="Users">
      <ion-grid>
        <h4 class="ion-text-start">List of Users</h4>
      </ion-grid>
    </base-layout>
  </template>
  
  <script>
  import {
    IonGrid,
  } from "@ionic/vue";
  import { defineComponent } from "vue";
  import axios from "axios";
  export default defineComponent({
    components: {
      IonGrid,
    },
    data() {
      return {};
    },
    methods: {},
  });
  </script>
  
  <style scoped></style>
  