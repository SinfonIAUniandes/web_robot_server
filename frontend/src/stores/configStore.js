import { useVolume } from "@/services/volumeService";
import { defineStore } from "pinia";
import { ref, watch } from "vue";

export const SPEED_RANGE = [0, 100];
export const ROBOT_MAXIMUM_SPEED = 0.5;

export const useConfig = defineStore("useConfig", () => {
  const speed = ref(30);
  const {volume, setVolume} = useVolume();

  watch(speed, (newSpeed) => {
    const speedInRange = newSpeed >= SPEED_RANGE[0] && newSpeed <= SPEED_RANGE[1];

    if (speedInRange) return;

    speed.value = Math.max(SPEED_RANGE[0], Math.min(SPEED_RANGE[1], newSpeed));
  });

  return { speed, volume, setVolume };
});
