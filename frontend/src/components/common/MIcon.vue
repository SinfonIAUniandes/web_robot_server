<script setup>
  defineProps({
    icon: { type: String, required: true },
  });
</script>

<template>
  <span :class="'mdi mdi-' + icon"></span>
</template>
