<script setup>
  import { useStick } from "@/composables/useStick.js";
  import { useMovementService } from "@/services/movementService.js";
  import useInterval from "@/composables/useInterval.js";
  import { watch } from "vue";

  import JoystickBase from "@/assets/img/joystick-base.png";
  import JoystickRed from "@/assets/img/joystick-red.png";

  const { movePepperWithJoyStick } = useMovementService();

  const { position, stick, state } = useStick(40, 0);

  const { register, stop } = useInterval(
    () => {
      movePepperWithJoyStick(position.x, position.y);
    },
    50,
    false,
  );

  watch(state, (value) => (value === "PRESSED" ? register() : stop()));
</script>

<template>
  <div class="w-[80px] h-[80px] relative">
    <img :src="JoystickBase" alt="JoyStick Base" class="w-full cover" />
    <div class="w-[30px] h-[30px] absolute top-0 bottom-0 left-0 right-0 m-auto" ref="stick">
      <img :src="JoystickRed" alt="JoyStick Head" class="w-full cover" />
    </div>
  </div>
</template>
