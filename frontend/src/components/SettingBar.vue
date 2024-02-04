<script setup>
  import BatteryComponent from "@/components/settings/BatteryComponent.vue";
  import VolumeHandler from "@/components/settings/VolumeHandler.vue";
</script>

<template>
  <div class="container flex justify-between mx-auto w-100">
    <VolumeHandler />
    <BatteryComponent />
  </div>
</template>
