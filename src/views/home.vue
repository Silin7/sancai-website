<script setup lang="ts">
import sideleft from '@/components/sideleft.vue'
import sideright from '@/components/sideright.vue'

function goTopCallback() {
  window.scrollTo(0, 0)
}
</script>

<template>
  <div class="page-main">
    <component :is="sideleft" ref="sideleftRef" />
    <!-- <component :is="sideright" ref="siderightRef" @goTopCallback="goTopCallback" /> -->
  </div>
</template>

<style lang="scss" scoped>
.page-main {
  height: 1000px;
  background-color: #f9fafb;
}
</style>
