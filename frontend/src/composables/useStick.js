import { reactive, ref } from "vue";
import useEventLister from "@/composables/useEventLister.js";

export const useStick = (maxDistance = 64, deadZone = 0) => {
  const stick = ref();
  const dragStart = reactive({x: 0, y: 0});
  const touchId = ref(null);
  const active = ref(false);
  const position = reactive({x: 0, y: 0});

  const onDown = (event) => {
    active.value = true;
    stick.value.style.transition = '0s';
    event.preventDefault();
    if (event.changedTouches) {
      dragStart.x = event.changedTouches[0].clientX;
      dragStart.y = event.changedTouches[0].clientY;
      touchId.value = event.changedTouches[0].identifier;
    } else {
      dragStart.x = event.clientX;
      dragStart.y = event.clientY;
    }
  }

  const onMove = (event) => {
    if (!active.value) return;

    let found = false;

    if (event.changedTouches) {
      for (let changed of event.changedTouches) {
        if (changed.identifier !== touchId.value) continue;
        found = true;
        event.clientX = changed.clientX;
        event.clientY = changed.clientY;
        if (found) break;
      }

      if (!found) return;
    }

    const xDiff = event.clientX - dragStart.x;
    const yDiff = event.clientY - dragStart.y;
    const angle = Math.atan2(yDiff, xDiff);
    const distance = Math.min(maxDistance, Math.hypot(xDiff, yDiff));
    const xPosition = distance * Math.cos(angle);
    const yPosition = distance * Math.sin(angle);

    stick.value.style.transform = `translate3d(${Math.round(xPosition)}px, ${Math.round(yPosition)}px, 0px)`;

    const distance2 = (distance < deadZone) ? 0 : maxDistance / (maxDistance - deadZone) * (distance - deadZone);
    const xPosition2 = distance2 * Math.cos(angle);
    const yPosition2 = distance2 * Math.sin(angle);
    position.x = parseFloat((xPosition2 / maxDistance).toFixed(4));
    position.y = parseFloat((yPosition2 / maxDistance).toFixed(4));
  }

  const onUp = (event) => {
    if ( !active.value ) return;

    if (event.changedTouches && touchId.value !== event.changedTouches[0].identifier) return;

    stick.value.style.transition = '.2s';
    stick.value.style.transform = `translate3d(0px, 0px, 0px)`;

    position.x = 0;
    position.y = 0;
    touchId.value = null;
    active.value = false;
  }

  useEventLister(stick, ["mousedown", "touchstart"], onDown);
  useEventLister(document, ["mousemove", "touchmove"], onMove,{passive: false});
  useEventLister(document, ["mouseup", "touchend"], onUp);

  return {stick, position};
}