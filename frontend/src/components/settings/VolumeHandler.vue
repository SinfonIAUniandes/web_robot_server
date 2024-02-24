<script setup>
  import { useConfig } from "@/stores/configStore";
  import { storeToRefs } from "pinia";
  import { VOLUME_RANGE } from "@/services/volumeService.js";

  const configuration = useConfig();

  const { volume } = storeToRefs(configuration);
  const { setVolume } = configuration;
</script>

<template>
  <div class="flex items-center gap-1 text-gray-100 text-sm">
    <span class="font-medium">Volume:</span>
    <input class="mx-1" type="range" :min="VOLUME_RANGE[0]" :max="VOLUME_RANGE[1]" v-model="volume" @change="setVolume" />
    {{ volume }}
  </div>
</template>

<style scoped></style>
