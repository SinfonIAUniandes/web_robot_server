<script setup>
  import MIcon from "@/components/common/MIcon.vue";
  import { computed } from "vue";

  const isOpen = defineModel();

  const props = defineProps({
    width: {
      type: [Number, String],
      default: 600,
    },
  });

  const usedWidth = computed(() =>
    typeof props.width === typeof 1 ? `${props.width}px` : props.width,
  );

  const close = () => {
    isOpen.value = false;
  };
</script>

<template>
  <div
    v-if="isOpen"
    class="fixed flex justify-center items-center w-full h-screen top-0 left-0 bg-[#00000080]"
    tabindex="0"
    @keyup.esc="close"
    :style="{ zIndex: 1000 }"
  >
    <div class="bg-white rounded-2xl relative p-3" :style="{ width: usedWidth, maxWidth: '90vw' }">
      <button @click="close" class="absolute right-0 top-0 p-2">
        <MIcon icon="close" class="font-bold text-3xl" />
      </button>
      <slot />
    </div>
  </div>
</template>
