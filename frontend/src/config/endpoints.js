const IP = "192.168.0.210";
const PORT = 8000;

const SERVER_URL = `http://${IP}:${PORT}/remoteController/`;

export const getVolumeUri = `${SERVER_URL}/getVolume/`;
export const setVolumeUri = `${SERVER_URL}/setVolume/`;
export const getBatteryUri = `${SERVER_URL}/getBattery/`;
