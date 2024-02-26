import { ref } from "vue";
import { displayImageUri, displayWebUri, saveImageUri } from "@/config/endpoints.js";

const displayRequest = (url, isWebsite = false) => {
  const uri = isWebsite ? displayWebUri : displayImageUri;
  fetch(uri(url));
};

const saveRequest = (imageFile) => {
  fetch(saveImageUri(), { method: "POST", body: imageFile });
};

export const useDisplayService = () => {
  const imageUrl = ref("");
  const imageFile = ref("");
  const websiteUrl = ref("");

  const sendSaveRequest = () => {
    saveRequest(imageFile.value);
  };

  const sendImageRequest = () => {
    displayRequest(imageUrl.value);
  };

  const sendWebsiteRequest = () => {
    displayRequest(websiteUrl.value, true);
  };

  return { imageUrl, websiteUrl, imageFile, sendImageRequest, sendWebsiteRequest, sendSaveRequest };
};
