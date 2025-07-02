<script setup lang="ts">
import { useRoute } from 'vue-router';
import headnav from '@/components/headnav.vue'
import sidemenu from '@/components/sidemenu.vue'

const routeInfo = useRoute()
</script>

<template>
  <div v-if="!routeInfo.meta.fullScreen">
    <component :is="headnav" ref="headnavRef" />
    <div class="container-content">
      <component :is="sidemenu" ref="sidemenuRef" />
      <div class="container-main">
        <RouterView />
      </div>
    </div>
  </div>
  <div v-else>
    <RouterView />
  </div>
</template>
