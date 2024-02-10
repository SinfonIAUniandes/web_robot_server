import { ref } from "vue";
import { audioStreamUri } from "@/config/endpoints.js";
import axios from "axios";

const handleAudioConnection = (data, last, target, playing) => {
  const takeLast = data.length - last.value;
  const buffer = target.createBuffer(1, takeLast, 16000);
  const channel = buffer.getChannelData(0);

  for (let i = last.value; i < data.length; i++)
    channel[i - last.value] = data[i] / 32768.0;

  last.value = data.length;

  const source = target.createBufferSource();
  source.buffer = buffer;
  if (playing.value) source.stop()
  source.connect(target.destination);
  source.start();
  playing.value = true;
}

export const useAudioService = () => {
  const isConnected = ref(false);
  const token = axios.CancelToken.source();
  const last = ref(0);
  const target = ref();
  const playing = ref(false);

  const connect = () => {
    if (isConnected.value) return;
    if (target.value == null) target.value = new window.AudioContext();

    axios.get(audioStreamUri, {
      cancelToken: token.token,
      onDownloadProgress: (e) => {
        handleAudioConnection(e.event.currentTarget.response.split(","), last, target.value, playing);
      },
    }).finally(() => console.log("Finished audio connection"));

    isConnected.value = true;
  }

  const disconnect = () => {
    if (!isConnected.value) return;
    token.cancel();
    isConnected.value = false;
  }

  return {isConnected, connect, disconnect};
}