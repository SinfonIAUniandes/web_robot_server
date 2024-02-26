<script setup>
  import MIcon from "@/components/common/MIcon.vue";
</script>

<template>
  <div class="dpad">
    <button type="button" class="dpad-button dpad-up">
      <MIcon icon="arrow-up-thick" />
    </button>
    <button type="button" class="dpad-button dpad-right">
      <MIcon icon="arrow-right-thick" />
    </button>
    <button type="button" class="dpad-button dpad-down">
      <MIcon icon="arrow-down-thick" />
    </button>
    <button type="button" class="dpad-button dpad-left">
      <MIcon icon="arrow-left-thick" />
    </button>
  </div>
</template>

<style scoped>
  .dpad {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: #ccc;
  }

  .dpad-button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    font-size: 24px;
  }

  .dpad-up {
    margin-bottom: 10px;
  }

  .dpad-right {
    margin-left: 10px;
  }

  .dpad-down {
    margin-top: 10px;
  }

  .dpad-left {
    margin-right: 10px;
  }
</style>
