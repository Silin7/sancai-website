<script setup lang="ts">
import { useRoute } from 'vue-router';
import headmenu from '@/components/headmenu.vue'
import sidemenu from '@/components/sidemenu.vue'

const routeInfo = useRoute()
</script>

<template>
  <div v-if="!routeInfo.meta.fullScreen">
    <component :is="headmenu" ref="headmenuRef" />
    <div class="container-content">
      <div class="container-side">
        <component :is="sidemenu" ref="sidemenuRef" />
      </div>
      <div class="container-main">
        <RouterView />
      </div>
    </div>
  </div>
  <div v-else>
    <RouterView />
  </div>
</template>
