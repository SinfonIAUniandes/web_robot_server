import { ref } from "vue";
import { speakUri } from "@/config/endpoints.js";

export const availableLanguages = ["English", "Spanish"];

const requestSpeech = (text, language, ready) => {
  fetch(speakUri(text, language)).finally(() => (ready.value = true));
};

export const useSpeechService = () => {
  const text = ref("");
  const language = ref("English");
  const ready = ref(true);

  const sendRequest = () => {
    if (!ready.value) return;
    ready.value = false;
    requestSpeech(text.value, language.value, ready);
    text.value = "";
  };

  return { text, language, ready, sendRequest };
};
