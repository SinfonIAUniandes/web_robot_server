<script setup>
  import { useStick } from "@/composables/useStick.js";
  import { watch } from "vue";

  const {position, stick} = useStick(40, 0);

  watch(position, (value) => {
    console.log(value);
  }, {deep: true});
</script>

<template>
  <div class="rounded-full bg-gray-200 w-[80px] h-[80px] flex items-center justify-center">
    <div class="rounded-full bg-red-400 w-[20px] h-[20px]" ref="stick"></div>
  </div>
</template>
