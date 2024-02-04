import { ref } from "vue";
import { setVolumeUri } from "@/config/endpoints.js";

const changeVolume = async (target) => {
  await fetch(`${setVolumeUri}?volume=${target}`);
};

export const useVolume = () => {
  const volume = ref(50);

  const setVolume = async () => {
    await changeVolume(volume.value);
  };

  return { volume, setVolume };
};
