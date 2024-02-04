import { onMounted, onUnmounted, ref } from "vue";

const getBattery = (batteryRef, loading) => {
  fetch("http://192.168.0.210:8000/remoteController/getBattery/")
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
  let interval;

  onMounted(() => {
    getBattery(batteryLevel, loading);
    interval = setInterval(() => getBattery(batteryLevel, loading), 60000);
  });

  onUnmounted(() => {
    clearInterval(interval);
  });

  return { batteryLevel, loading };
};
