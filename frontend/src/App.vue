<script setup>
  import HomeView from "@/views/HomeView.vue";
  import { onBeforeMount } from "vue";
  import { useRos } from "@/services/useRos.js";

  const rosService = useRos();

  const {connect} = rosService;

  onBeforeMount(async() => {
    await connect();
  });
</script>

<template>
  <HomeView />
</template>
