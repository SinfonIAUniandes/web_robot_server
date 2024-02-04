<script setup>
  import { useVolume } from "@/services/volumeService.js";

  const { volume, setVolume } = useVolume();
</script>

<template>
  <div class="flex items-center text-gray-100">
    <span class="font-medium">Volume:</span>
    <input class="mx-1" type="range" min="0" max="100" v-model="volume" @change="setVolume" />
    {{ volume }}
  </div>
</template>

<style scoped></style>
