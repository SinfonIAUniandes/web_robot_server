import { ref, watch } from "vue";
import { setVolumeUri } from "@/config/endpoints.js";

export const VOLUME_RANGE = [0, 100];

const changeVolume = async (target) => {
  await fetch(`${setVolumeUri}?volume=${target}`);
};

export const useVolume = () => {
  const volume = ref(50); //TODO("Get the robot volume and set it as the default value");

  const setVolume = async () => {
    await changeVolume(volume.value);
  };

  watch(volume, (newVolume) => {
    const volumeInRange = newVolume >= VOLUME_RANGE[0] && newVolume <= VOLUME_RANGE[1];

    if (volumeInRange) return;

    volume.value = Math.max(VOLUME_RANGE[0], Math.min(VOLUME_RANGE[1], newVolume));
  });

  return { volume, setVolume };
};
