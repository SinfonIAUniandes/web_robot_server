import { ref } from "vue";
import axios from "axios";

const changeVolume = async (target) => {
  await axios.get("http://192.168.0.210:8000/remoteController/setVolume/?volume=" + target);
};

export const useVolume = () => {
  const volume = ref(50);

  const setVolume = async () => {
    await changeVolume(volume.value);
  };

  return { volume, setVolume };
};
