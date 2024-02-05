<script setup>
  import BatteryComponent from "@/components/settings/BatteryComponent.vue";
  import VolumeHandler from "@/components/settings/VolumeHandler.vue";
  import { useConfig } from "@/stores/configStore.js";
  import { storeToRefs } from "pinia";
  import { ref } from "vue";

  const {speed} = storeToRefs(useConfig());
  const menuIsOpen = ref(false);
</script>

<template>
  <div v-if="menuIsOpen" class="absolute w-[250px] flex flex-col md:hidden text-white p-5 bg-gray-800 shadow-2xl h-screen" :style="{zIndex: 1000}">
    <div class="flex justify-between items-center mb-2">
      <h1 class="text-xl">Settings</h1>
      <button class="font-bold" @click="menuIsOpen = !menuIsOpen">
        <span class="text-xl mdi mdi-close" />
      </button>
    </div>
    <nav class="flex flex-col items-start w-100">
      <VolumeHandler />
      <div class="text-gray-100 flex items-center gap-1">
        Speed:
        <input type="range" min="25" max="50" v-model="speed" />
        {{speed}}
      </div>
    </nav>
  </div>
  <div class="md:hidden px-2 flex justify-between h-10 items-center border-b border-white bg-gra">
    <div class="flex text-white text-xl font-bold gap-1 items-center">
      <button @click="menuIsOpen = !menuIsOpen" class="flex items-center">
        <span class="text-3xl mdi mdi-menu" />
      </button>
      <h1>Settings</h1>
    </div>
    <BatteryComponent />
  </div>
  <div class="container hidden md:flex justify-between mx-auto w-100">
    <VolumeHandler />
    <div class="text-gray-100 flex items-center gap-1">
      Speed:
      <input type="range" min="25" max="50" v-model="speed" />
      {{speed}}
    </div>
    <BatteryComponent />
  </div>
</template>
