<script setup>
  import BatteryComponent from "@/components/settings/BatteryComponent.vue";
  import VolumeHandler from "@/components/settings/VolumeHandler.vue";
  import { useConfig } from "@/stores/configStore.js";
  import { storeToRefs } from "pinia";
  import { ref } from "vue";
  import MIcon from "@/components/common/MIcon.vue";
  import { useAudioService } from "@/services/audioService.js";

  const { speed } = storeToRefs(useConfig());

  const {connect, disconnect, isConnected} = useAudioService();

  const menuIsOpen = ref(false);
</script>

<template>
  <div
    v-if="menuIsOpen"
    class="absolute w-[250px] flex flex-col lg:hidden text-white p-5 bg-gray-800 shadow-2xl h-screen"
    :style="{ zIndex: 1000 }"
  >
    <div class="flex justify-between items-center mb-2">
      <h1 class="text-xl">Settings</h1>
      <button class="font-bold" @click="menuIsOpen = !menuIsOpen">
        <MIcon class="text-xl" icon="close" />
      </button>
    </div>
    <nav class="flex flex-col items-start w-100">
      <VolumeHandler />
      <div class="text-gray-100 flex items-center gap-1">
        Speed:
        <input type="range" min="25" max="50" v-model="speed" />
        {{ speed }}
      </div>
    </nav>
  </div>
  <div class="w-100 h-12 flex items-center bg-gray-900 shadow-md">
    <div class="container mx-auto p-1 text-gray-100 grid grid-cols-3 text-lg font-medium">
      <div class="text-lg font-medium flex items-center gap-1">
        <button @click="menuIsOpen = !menuIsOpen" class="flex items-center lg:hidden">
          <MIcon class="text-3xl" icon="menu" />
        </button>
        <div class="hidden lg:flex items-center justify-center">
          <div v-if="isConnected" class="p-1 rounded-full bg-green-500"></div>
          <div v-else class="p-1 rounded-full bg-red-500"></div>
          <button v-if="!isConnected" @click="connect"><MIcon icon="volume-high" /></button>
          <button v-else @click="disconnect"><MIcon icon="volume-variant-off" /></button>
        </div>
        <h1>Settings</h1>
        <span class="hidden lg:flex">:</span>
        <VolumeHandler class="lg:flex hidden" />
        <div class="lg:flex text-gray-100 hidden items-center gap-1 text-sm">
          Speed:
          <input type="range" min="25" max="50" v-model="speed" />
          {{ speed }}
        </div>
      </div>
      <div class="font-bold text-xl text-center">SinfonIA</div>
      <div class="flex justify-end">
        <BatteryComponent />
      </div>
    </div>
  </div>
</template>
