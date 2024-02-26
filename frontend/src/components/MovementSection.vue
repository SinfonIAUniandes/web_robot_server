<script setup>
  import JoyStick from "@/components/movement/JoyStick.vue";
  import DPad from "@/components/movement/DPad.vue";
</script>

<template>
  <div class="mt-5 flex flex-col lg:flex-row container mx-auto">
    <div>
      <h1 class="text-gray-100 font-bold my-1">Move Pepper:</h1>
      <div>
        <JoyStick />
        <DPad />
      </div>
    </div>
  </div>
</template>
