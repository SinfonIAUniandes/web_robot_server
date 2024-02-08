import { ref } from "vue";
import { displayImageUri, displayWebUri } from "@/config/endpoints.js";

const displayRequest = (url, isReady, isWebsite = false) => {
  const uri = isWebsite ? displayWebUri : displayImageUri;

  fetch(uri(url))
    .finally(() => isReady.value = true);
}

export const useDisplayService = () => {
  const imageUrl = ref("");
  const websiteUrl = ref("");

  const imageIsReady = ref(true);
  const websiteIsReady = ref(true);

  const sendImageRequest = () => {
    if (!imageIsReady.value) return;
    imageIsReady.value = false;

    displayRequest(imageUrl.value, imageIsReady);
  }

  const sendWebsiteRequest = () => {
    if (!websiteIsReady.value) return;
    websiteIsReady.value = false;

    displayRequest(websiteUrl.value, websiteIsReady, true);
  }

  return {imageUrl, websiteUrl, imageIsReady, websiteIsReady, sendImageRequest, sendWebsiteRequest}
}