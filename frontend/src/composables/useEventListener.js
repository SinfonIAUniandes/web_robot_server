import { onBeforeUnmount, onMounted, onUnmounted, toValue } from "vue";

const useEventListener = (target, event, handler, options = {}) => {
  onMounted(() => {
    if (typeof event === typeof []) {
      event.forEach((e) => toValue(target).addEventListener(e, handler, options));
    } else {
      toValue(target).addEventListener(event, handler, options);
    }
  });

  onBeforeUnmount(() => {
    if (typeof event === typeof []) {
      event.forEach((e) => toValue(target).removeEventListener(e, handler, options));
    } else {
      toValue(target).addEventListener(event, handler, options);
    }
  });
};

export default useEventListener;
