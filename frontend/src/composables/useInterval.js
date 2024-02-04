import { onMounted, onUnmounted } from "vue";

const useInterval = (handler, timeout) => {
  let interval;

  onMounted(() => interval = setInterval(handler, timeout));
  onUnmounted(() => clearInterval(interval));
}

export default useInterval;