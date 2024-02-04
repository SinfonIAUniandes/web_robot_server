import { ref } from "vue";
import { getBatteryUri } from "@/config/endpoints.js";
import useInterval from "@/composables/useInterval.js";

const getBattery = (batteryRef, loading) => {
  fetch(getBatteryUri)
    .then((res) => res.text())
    .then((res) => {
      batteryRef.value = parseInt(res);
      loading.value = false;
    })
    .catch((err) => {
      console.error("Unexpected error: " + err);
      loading.value = true;
    });
};

export const useBattery = () => {
  const batteryLevel = ref(100);
  const loading = ref(true);

  useInterval(() => getBattery(batteryLevel, loading), 60000);

  return { batteryLevel, loading };
};
