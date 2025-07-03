<script setup lang="ts">
import sideright from '@/components/sideright.vue'

function goTopCallback() {
  window.scrollTo(0, 0)
}
</script>

<template>
  <div class="page-main">
    <component :is="sideright" ref="siderightRef" @goTopCallback="goTopCallback" />
  </div>
</template>

<style lang="scss" scoped>
.page-main {
  height: 1000px;
  background-color: #f9fafb;
}
</style>
