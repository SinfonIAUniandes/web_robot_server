const SERVER_URL =
  import.meta.env.VITE_BACKEND_BASE_PATH ?? "http://localhost:8000/remoteController/api";

export const getVolumeUri = `${SERVER_URL}/get/volume`;
export const setVolumeUri = `${SERVER_URL}/set/volume`;
export const getBatteryUri = `${SERVER_URL}/get/battery`;

export const moveJoystickUri = (x, y) => `${SERVER_URL}/joystick?vertical_axis=${y}&horizontal_axis=${x}`;
