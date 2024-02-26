<script setup>
  import { useDropZone } from "@vueuse/core";
  import { ref, onMounted } from "vue";
  import { useDisplayService } from "@/services/displayService.js";
  import MIcon from "@/components/common/MIcon.vue";

  const {imageUrl, websiteUrl, imageFile, sendImageRequest, sendWebsiteRequest, sendSaveRequest, sendLedsRequest} = useDisplayService();

  const imageDropZone = ref();
  
  const previewImage = ref();

  const colorPicker = ref(null);

  const selectedColor = ref('#ffffff');

  const textColorClass = ref('');

  const openColorPicker = () => {
    colorPicker.value.click();
  };

  const displayOnlineImage = () =>{
    const imgElement = previewImage.value;
    imgElement.src = imageUrl.value;
    sendImageRequest();
  }

  const handleColorChange = () => {
    textColorClass.value = `text-[${selectedColor.value}]`;
    console.log('Color seleccionado:', selectedColor.value);
  };

  onMounted(() => {
    textColorClass.value = `text-[${selectedColor.value}]`;
  });

  const handleFileChange = (event) => {
    const fileInput = event.target;
    const file = fileInput.files[0];

    if (file) {
      const reader = new FileReader();

      reader.onload = () => {
        const imgElement = previewImage.value;

        imgElement.src = reader.result;

        var formData = new FormData();
        formData.append("image",file);
        imageFile.value = formData;
        sendSaveRequest();
      };

      reader.readAsDataURL(file);
  }};

  const onDrop = (files) => {
    let file = files[0];
    let reader  = new FileReader();
    reader.onload = function(e)  {
        let image = previewImage.value;
        image.src = e.target.result;
        var formData = new FormData();
        formData.append("image",file);
        imageFile.value = formData;
        sendSaveRequest();
    }
    reader.readAsDataURL(file);
  }

  const {isOverDropZone} = useDropZone(imageDropZone, {
    onDrop,
    dataTypes: ["image/jpeg", "image/png"]
  });
</script>

<template>
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <h1 class="text-lg text-gray-100">Display an image in pepper's tablet!:</h1>
  </div> 
  <br>
  <div ref="imageDropZone" class="flex items-center justify-center w-1/2 mx-auto" >
    <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
            <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
            </svg>
            <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop an image</p>
            <p class="text-xs text-gray-500 dark:text-gray-400">PNG or JPG </p>
        </div>
        <input @change="handleFileChange" id="dropzone-file" type="file" class="hidden" />
    </label>
  </div> 
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <h1 class="text-lg text-gray-100">Display an online image:</h1>
  </div> 
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <textarea class="rounded-md border border-gray-300 p-2 resize-none h-12 w-full" v-model="imageUrl" @keydown.enter.prevent="displayOnlineImage" placeholder="Copy here the link to the image you want to show :-)"></textarea>
  </div>
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md" @click="displayOnlineImage">
      Display
    </button>
  </div> 
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <img ref="previewImage">
  </div>
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <h1 class="text-lg text-gray-100">Display a webpage:</h1>
  </div> 
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <textarea class="rounded-md border border-gray-300 p-2 resize-none h-12 w-full" v-model="websiteUrl" @keydown.enter.prevent="sendWebsiteRequest" placeholder="Copy here the link to the webpage you want to show :-)"></textarea>
  </div>
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md" @click="sendWebsiteRequest">
      Display
    </button>
  </div> 
  <br>
  <div class="flex items-center justify-center w-1/2 mx-auto" >
    <button @click="openColorPicker">
      <MIcon icon="eye-outline" :class="textColorClass"/>
      <input ref="colorPicker" v-model="selectedColor" @input="handleColorChange" type="color" style="display: none"/>
    </button>
  </div> 
  <br>
</template>