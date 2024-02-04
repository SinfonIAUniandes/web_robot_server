import { onMounted, onUnmounted, toValue } from "vue";

const useEventLister = (target, event, handler, options = {}) => {
  onMounted(() => {
    if (typeof event === typeof []) {
      event.forEach((e) => toValue(target).addEventListener(e, handler, options));
    } else {
      toValue(target).addEventListener(event, handler, options);
    }
  });

  onUnmounted(() => {
    if (typeof event === typeof []) {
      event.forEach((e) => toValue(target).removeEventListener(e, handler, options));
    } else {
      toValue(target).addEventListener(event, handler, options);
    }
  });
};

export default useEventLister;
