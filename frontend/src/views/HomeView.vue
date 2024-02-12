<script setup>
  import SettingBar from "@/components/SettingsBar.vue";
  import JoyStick from "@/components/movement/JoyStick.vue";
  import MovementSection from "@/components/MovementSection.vue";
  import SpeakSection from "@/components/SpeakSection.vue";
  import { useDisplay } from "@/composables/useDisplay.js";
  import DisplaySection from "@/components/DisplaySection.vue";

  const display = useDisplay();
</script>

<template>
  <SettingBar />
  <MovementSection v-if="display.isMobile" />
  <SpeakSection />
  <DisplaySection />
</template>
