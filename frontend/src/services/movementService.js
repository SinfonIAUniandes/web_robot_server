import { useConfig, SPEED_RANGE, ROBOT_MAXIMUM_SPEED } from "@/stores/configStore.js";
import { storeToRefs } from "pinia";
import { moveHeadUri, moveJoystickUri, moveUri } from "@/config/endpoints.js";
import { ref } from "vue";

const calculateMovement = (target, speed) => {
  const metersPerSecond = speed * (ROBOT_MAXIMUM_SPEED / (SPEED_RANGE[1] - SPEED_RANGE[0]));

  return {
    xAxis: target.x * metersPerSecond,
    yAxis: target.y * metersPerSecond,
  };
};

const doJoystickRequest = (x, y, done) => {
  fetch(moveJoystickUri(x, y)).finally(() => (done.value = true));
};

const doHeadRequest = (x, y, done) =>{
  fetch(moveHeadUri(x, y)).finally(() => (done.value = true));
}

const doMoveRequest = (direction, speed, done) =>{
  fetch(moveUri(direction, speed)).finally(() => (done.value = true));
}

export const useMovementService = () => {
  const { speed } = storeToRefs(useConfig());
  const done = ref(true);

  const movePepperWithJoyStick = (x, y) => {
    if (!done.value) return;
    done.value = false;
    const { xAxis, yAxis } = calculateMovement({ x, y }, speed.value);
    doJoystickRequest(xAxis, yAxis, done);
  };

  const movePepper = (direction) => {
    if (done.value) return;
    done.value = false;
    doMoveRequest(direction, speed.value, done)
  };

  const moveHead = (angleX, angleY) => {
    if (!done.value) return;
    done.value = false;
    doHeadRequest(angleX, angleY, done);
  };

  return { movePepperWithJoyStick, movePepper, moveHead };
};
