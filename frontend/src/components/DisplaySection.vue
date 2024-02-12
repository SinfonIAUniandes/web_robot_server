<script setup>
  import { useDropZone } from "@vueuse/core";
  import { ref } from "vue";

  const imageDropZone = ref();

  const onDrop = (files) => {
    console.log(files)
  }

  const {isOverDropZone} = useDropZone(imageDropZone, {
    onDrop,
    dataTypes: ["image/jpeg", "image/png"]
  });
</script>

<template>
  <div ref="imageDropZone" class="p-1 border-2 border-blue-800 flex align-items justify-center">
    Drop here your images
  </div>
</template>