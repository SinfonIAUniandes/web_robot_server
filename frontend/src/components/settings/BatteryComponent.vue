<script setup>
  import { computed } from "vue";
  import { useBattery } from "@/services/batteryService.js";

  const { batteryLevel, loading } = useBattery();

  const color = computed(() =>
    loading.value
      ? "bg-gray-100"
      : batteryLevel.value < 60
        ? batteryLevel.value < 30
          ? "bg-red-400"
          : "bg-yellow-500"
        : "bg-green-700",
  );
</script>

<template>
  <div class="w-[100px] flex items-center">
    <div class="shadow w-1/2 rounded border-2 border-gray-400 my-1 relative">
      <div class="text-gray-100 text-center font-bold text-xs">
        {{ loading ? "Loading..." : batteryLevel + "%" }}
      </div>
      <div
        class="top-0 absolute h-[100%]"
        :class="color"
        :style="{ width: batteryLevel + '%', zIndex: -1 }"
      ></div>
    </div>
    <div class="border-r-4 h-2 ml-[2px] rounded-r border-gray-400"></div>
  </div>
</template>
