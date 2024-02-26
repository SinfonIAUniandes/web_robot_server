<script setup>
  import { availableLanguages, useSpeechService } from "@/services/speechService.js";

  const { language, text, ready, sendRequest } = useSpeechService();

  const sendHello = () => {
    language.value = "English";
    text.value = "Hello";
    sendRequest();
  };

  const sendHowAreYou = () => {
    language.value = "English";
    text.value = "How are you?";
    sendRequest();
  };
</script>

<template>
  <div class="flex flex-col gap-4 bg-gray-800 p-2 rounded-lg shadow-lg m-1">
    <div class="flex items-center gap-1">
      <h1 class="text-lg text-gray-100">Select your language:</h1>
      <select class="rounded-md border border-gray-300 p-2 bg-gray-300" v-model="language">
        <option v-for="lang in availableLanguages">{{ lang }}</option>
      </select>
    </div>

    <textarea
      class="rounded-md border border-gray-300 p-2 resize-none h-24"
      v-model="text"
      @keydown.enter.prevent="sendRequest"
      placeholder="Type here what you want Pepper to say :-)"
    ></textarea>

    <div class="flex justify-between">
      <button
        class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium py-2 px-4 rounded-md disabled:opacity-50"
        @click="sendHello"
      >
        Hello
      </button>

      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        @click="sendRequest"
      >
        Speak
      </button>

      <button
        class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium py-2 px-4 rounded-md disabled:opacity-50"
        @click="sendHowAreYou"
      >
        How are you?
      </button>
    </div>
  </div>
</template>
