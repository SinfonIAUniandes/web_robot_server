const SERVER_URL =
  import.meta.env.VITE_BACKEND_BASE_PATH ?? "http://localhost:8000/remoteController/api";

const showUri = `${SERVER_URL}/show`;

export const getVolumeUri = `${SERVER_URL}/get/volume`;
export const setVolumeUri = `${SERVER_URL}/set/volume`;
export const getBatteryUri = `${SERVER_URL}/get/battery`;

export const moveJoystickUri = (x, y) =>
  `${SERVER_URL}/joystick?vertical_axis=${y}&horizontal_axis=${x}`;

export const moveHeadUri = (x, y) =>
  `${SERVER_URL}/move/head?angle0=${x}&angle1=${y}`;

export const moveUri = (direction, speed) =>
  `${SERVER_URL}/move?direction=${direction}&speed=${speed}`;

export const speakUri = (text, language) =>
  `${SERVER_URL}/joystick?text=${text}&language=${language}`;

export const displayImageUri = (url) => `${showUri}/image?url=${url}`;
export const displayWebUri = (url) => `${showUri}/web?url=${url}`;
