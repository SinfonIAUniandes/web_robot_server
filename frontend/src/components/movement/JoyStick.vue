<script setup>
  import JoyStickBase from "@/assets/joystick-base.png";
  import JoyStickHead from "@/assets/joystick-red.png";
  import { useStick } from "@/composables/useStick.js";
  import { watch } from "vue";

  const {position, stick} = useStick(40, 0);

  watch(position, (value) => {
    //TODO("Use joystick service")
  }, {deep: true});
</script>

<template>
  <div class="w-[80px] h-[80px] relative">
    <img :src="JoyStickBase" alt="JoyStick Base" class="w-100 cover">
    <div class="w-[30px] h-[30px] absolute top-0 bottom-0 left-0 right-0 m-auto" ref="stick">
      <img :src="JoyStickHead" alt="JoyStick Head" class="w-100 cover">
    </div>
  </div>
</template>
