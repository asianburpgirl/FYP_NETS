<template>
  <base-layout pageTitle="Map" needToolBar="y">
    <GMapMap
      :center="center"
      :zoom="7"
      map-type-id="terrain"
      style="width: 400px; height: 800px"
    >
      <GMapCluster>
        <!-- <GMapMarker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        :clickable="true"
        :draggable="true"
        @click="center = m.position"
      /> -->
        <GMapMarker />
      </GMapCluster>
    </GMapMap>
  </base-layout>
</template>
<script>
export default {
  name: "MapPage",
  data() {
    return {
      center: { lat: 51.093048, lng: 6.84212 },
      markers: [
        {
          position: {
            lat: 51.093048,
            lng: 6.84212,
          },
        }, // Along list of clusters
      ],
    };
  },
};
</script>
