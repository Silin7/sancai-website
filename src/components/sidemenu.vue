<script lang="ts" setup>
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'

import router from '@/router/index'
import { onMounted, ref } from 'vue'

const handleOpen = (key: string, keyPath: string[]) => {
  console.log('handleOpen', key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log('handleClose', key, keyPath)
}

onMounted(() => {
  console.log('-------->', router.options.routes)
})
const isCollapse: any = ref(false)
function isCollapseClick() {
  console.log('-------->', isCollapse.value)
  isCollapse.value = !isCollapse.value
}
</script>

<template>
  <div style="padding: 0 8px;">
    <div @click="isCollapseClick">折叠</div>
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
          <span>item one</span>
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
  </div>
</template>

<style lang="scss">
.el-menu {
  border-right: 0 !important;

  .el-menu--popup {
    border-radius: 5px !important;
    border: 1px solid rgb(235.9, 245.3, 255) !important;
  }

  .el-sub-menu {
    box-sizing: border-box;
    margin: 4px 0;

    span {
      display: inline-block;
      white-space: nowrap;
      overflow: hidden;
      max-width: 120px;
      text-overflow: ellipsis;
      font-size: 14px;
      border: 1px solid red;
    }

    .el-sub-menu__title {
      box-sizing: border-box;
      margin: 4px 0;
      border-radius: 5px;
    }

    .el-sub-menu__title:hover {
      background-color: rgb(235.9, 245.3, 255) !important;
    }
  }

  .el-menu-item {
    box-sizing: border-box;
    margin: 4px 0;
    border-radius: 5px;

    span {
      display: inline-block;
      white-space: nowrap;
      overflow: hidden;
      max-width: 120px;
      text-overflow: ellipsis;
      font-size: 14px;
      border: 1px solid green;
    }
  }

  .el-menu-item:hover {
    background-color: rgb(235.9, 245.3, 255) !important;
  }
}
</style>