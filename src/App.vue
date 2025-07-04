<script setup lang="ts">
import { useRoute } from 'vue-router'
import headmenu from '@/components/headmenu.vue'
import sidemenu from '@/components/sidemenu.vue'
import headnav from '@/components/headnav.vue'
import footnav from '@/components/footnav.vue'

const routeInfo = useRoute()
</script>

<template>
  <div>
    <RouterView />
  </div>
  <!-- <div v-if="routeInfo.meta.website">
    <component v-if="routeInfo.meta.hashead" :is="headnav" ref="headnavRef" />
    <RouterView />
    <component v-if="routeInfo.meta.hasfoot" :is="footnav" ref="footnavRef" />
  </div>
  <div v-else>
    <component :is="headmenu" ref="headmenuRef" />
    <div class="container-content">
      <component :is="sidemenu" ref="sidemenuRef" />
      <div class="container-main">
        <RouterView />
      </div>
    </div>
  </div> -->
</template>
