import { ref } from "vue";
import { getBatteryUri } from "@/config/endpoints.js";
import useInterval from "@/composables/useInterval.js";
import { useRos } from "@/services/useRos.js";
import { BATTERY_MSG, BATTERY_SERVICE } from "@/config/rosServices.js";

const getBattery = (batteryRef, loading, service) => {
  const {callService} = useRos();
  loading.value = true;
  callService(service)
    .then((result) => {
      batteryRef.value = parseInt(result.porcentage);
      loading.value = false;
    });
};

export const useBattery = () => {
  const batteryLevel = ref(100);
  const loading = ref(true);
  const ready = ref(false);
  const started = ref(false);
  let batteryService;

  const init = async () => {
    batteryService = await useRos().getService(BATTERY_SERVICE, BATTERY_MSG);
    ready.value = true;
  }

  const start = () => {
    if (!ready.value || started.value) return;
    getBattery(batteryLevel, loading, batteryService);
    useInterval(() => getBattery(batteryLevel, loading, batteryService), 60000);
    started.value = true;
  }

  return { batteryLevel, loading, ready, init, start};
};
