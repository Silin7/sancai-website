<script lang="ts" setup>
import {
  Fold,
  Expand,
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
import { onMounted, ref } from 'vue'
import router from '@/router/index'

const handleOpen = (key: string, keyPath: string[]) => {
  console.log('handleOpen', key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log('handleClose', key, keyPath)
}

// onMounted(() => {
//   console.log('router.options.routes ', router.options.routes)
// })

const isCollapse: any = ref(false)
function isCollapseClick() {
  isCollapse.value = !isCollapse.value
}
</script>

<template>
  <div class="custom-menu">
    <el-menu :collapse="isCollapse" @open="handleOpen" @close="handleClose">
      <el-sub-menu index="1">
        <template #title>
          <el-icon>
            <location />
          </el-icon>
          <span>Navigator One</span>
        </template>
        <el-menu-item index="1-1">
          <el-icon><icon-menu /></el-icon>
          <span>item one one one one one</span>
        </el-menu-item>
        <el-menu-item index="1-2">
          <el-icon><icon-menu /></el-icon>
          <span>item two</span>
        </el-menu-item>
        <el-menu-item index="1-3">
          <el-icon><icon-menu /></el-icon>
          <span>item three</span>
        </el-menu-item>
        <el-sub-menu index="1-4">
          <template #title>
            <el-icon><icon-menu /></el-icon>
            <span>item four</span>
          </template>
          <el-menu-item index="1-4-1">
            <el-icon><icon-menu /></el-icon>
            <span>item four - one</span>
          </el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-menu-item index="2">
        <el-icon><icon-menu /></el-icon>
        <span>人</span>
      </el-menu-item>
      <el-menu-item index="3">
        <el-icon>
          <document />
        </el-icon>
        <span>材</span>
      </el-menu-item>
      <el-menu-item index="4">
        <el-icon>
          <setting />
        </el-icon>
        <span>机</span>
      </el-menu-item>
    </el-menu>
    <div class="collapse-box" @click="isCollapseClick">
      <div class="collapse-icons">
        <el-icon v-if="isCollapse" color="#000" :size="20">
          <Expand />
        </el-icon>
        <el-icon v-else color="#000" :size="20">
          <Fold />
        </el-icon>
      </div>
    </div>
  </div>
</template>
