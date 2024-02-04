import { ref } from "vue";
import axios from "axios";
import { setVolumeUri } from "@/config/endpoints.js";

const changeVolume = async (target) => {
  await axios.get(`${setVolumeUri}?volume=${target}`);
};

export const useVolume = () => {
  const volume = ref(50);

  const setVolume = async () => {
    await changeVolume(volume.value);
  };

  return { volume, setVolume };
};
