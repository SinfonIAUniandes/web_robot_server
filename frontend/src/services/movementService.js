import { useConfig } from "@/stores/configStore.js";
import { storeToRefs } from "pinia";
import { moveJoystickUri } from "@/config/endpoints.js";
import { ref } from "vue";


const calculateMovement = (target, speed) => {
  return {
    xAxis: target.x * speed / 100,
    yAxis: target.y * speed / 100,
  }
}

const doJoystickRequest = (x, y, done) => {
  done.value = false;
  fetch(moveJoystickUri(x, y))
    .finally(() => done.value = true);
}

export const movementService = () => {
  const {speed} = storeToRefs(useConfig());
  const done = ref(true);

  const movePepperWithJoyStick = (x, y) => {
    if (!done.value) return;
    const {xAxis, yAxis} = calculateMovement({x, y}, speed.value);
    doJoystickRequest(xAxis, yAxis, done);
  }

  const movePepper = () => {

  }

  const moveHead = () => {

  }

  return {movePepperWithJoyStick, movePepper, moveHead}
}