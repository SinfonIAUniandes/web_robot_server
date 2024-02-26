<script setup>
  import BatteryComponent from "@/components/settings/BatteryComponent.vue";
  import VolumeHandler from "@/components/settings/VolumeHandler.vue";
  import { ref } from "vue";
  import MIcon from "@/components/common/MIcon.vue";
  import { useAudioService } from "@/services/audioService.js";
  import SpeedHandler from "./settings/SpeedHandler.vue";
  import ModalComponent from "@/components/common/ModalComponent.vue";

  const { connect, disconnect, isConnected } = useAudioService();

  const menuIsOpen = ref(false);

  const open = ref(true);
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
    <nav class="flex flex-col items-start w-full">
      <VolumeHandler />
      <SpeedHandler />
    </nav>
  </div>
  <div class="h-12 flex items-center bg-gray-900 shadow-md px-3">
    <div class="w-full p-1 text-gray-100 grid grid-cols-3 text-lg font-medium">
      <div class="text-lg font-medium flex items-center gap-1">
        <button @click="menuIsOpen = !menuIsOpen" class="flex items-center lg:hidden">
          <MIcon class="text-3xl" icon="menu" />
        </button>
        <div class="hidden lg:flex items-center justify-center">
          <div v-if="isConnected" class="p-1 rounded-full bg-green-500"></div>
          <div v-else class="p-1 rounded-full bg-red-500"></div>
          <button v-if="!isConnected" @click="connect"><MIcon icon="microphone-off" /></button>
          <button v-else @click="disconnect"><MIcon icon="microphone" /></button>
        </div>
        <h1>Settings</h1>
        <span class="hidden lg:flex">:</span>
        <VolumeHandler class="lg:flex hidden" />
        <SpeedHandler class="lg:flex hidden" />
      </div>
      <div class="font-bold text-xl text-center">SinfonIA</div>
      <div class="flex justify-end">
        <BatteryComponent />
      </div>
    </div>
  </div>
  <ModalComponent v-model="open">
    <div>CONTENIDO AQUÍ</div>
  </ModalComponent>
</template>
