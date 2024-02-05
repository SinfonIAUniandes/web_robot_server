import { onMounted, onUnmounted } from "vue";

const useInterval = (handler, timeout, register_on_init = true) => {
  let interval;

  if (register_on_init) {
    onMounted(() => register());
  }

  const register = () => {
    interval = setInterval(handler, timeout);
  };

  const stop = () => {
    clearInterval(interval);
  };

  onUnmounted(stop);

  return { register, stop };
};

export default useInterval;
