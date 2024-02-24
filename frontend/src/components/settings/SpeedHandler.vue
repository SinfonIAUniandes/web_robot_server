<script setup>
  import { useConfig, SPEED_RANGE } from "@/stores/configStore";
  import { storeToRefs } from "pinia";

  const configuration = useConfig();

  const { speed } = storeToRefs(configuration);
</script>

<template>
  <div class="flex items-center gap-1 text-gray-100 text-sm">
    <span class="font-medium">Speed:</span>
    <input class="mx-1" type="range" :min="SPEED_RANGE[0]" :max="SPEED_RANGE[1]" v-model="speed" />
    {{ speed }}%
  </div>
</template>

<style scoped></style>
