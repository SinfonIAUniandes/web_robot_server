import { readonly, reactive, onMounted, onUnmounted } from "vue";
import useEventListener from "@/composables/useEventListener.js";

export const useDisplay = () => {
  const properties = reactive({
    isDesktop: false,
    isMobile: false,
  });

  const updateDeviceTypes = () => {
    const isMobileDevice = window.innerWidth < 768;
    properties.isMobile = isMobileDevice;
    properties.isDesktop = !isMobileDevice;
  };

  updateDeviceTypes();

  useEventListener(window, "resize", updateDeviceTypes);

  return readonly(properties);
};
