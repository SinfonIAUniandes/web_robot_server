import { defineStore } from "pinia";
import { ref } from "vue";

export const useConfig = defineStore("useConfig", () => {
  const speed = ref(30);

  return { speed };
});
