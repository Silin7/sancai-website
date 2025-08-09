<script lang="ts" setup>
import { computed, ref } from 'vue'
import { Fold, Expand } from '@element-plus/icons-vue'
import useHeaderStore from '@/store/modules/header'
import router from '@/router/index'

const headerStore = useHeaderStore()

const selectedTab = computed(() => {
  return headerStore.selectedTab
})

const handleOpen = (key: string) => {
  router.push({
    name: key,
  })
  headerStore.setSelectedTab(key)
}

// const menuList = [
//   { name: 'user-index', title: '首页', icon: 'HomeFilled' },
//   { name: 'user-profile', title: '资料' },
//   { name: 'user-renlist', title: '数字技工/方案论证' },
//   { name: 'user-cailist', title: '材料/设备' },
//   { name: 'user-machinelist', title: '智能建造装备' },
//   { name: 'user-itlist', title: '信息化产品/服务' },
//   { name: 'user-inquirylist', title: '报价单' },
//   { name: 'user-editpwd', title: '改密码' },
//   { name: 'user-out', title: '退出' },
// ]

// 折叠 or 展开
const isCollapse: any = ref(false)

function isCollapseClick() {
  isCollapse.value = !isCollapse.value
}
</script>

<template>
  <div class="custom-menu">
    <el-menu :collapse="isCollapse" :default-active="selectedTab" @open="handleOpen">
      <el-menu-item index="user-index">
        <i class="fa fa-home"></i>
        <span>首页</span>
      </el-menu-item>
      <el-menu-item index="user-profile">
        <i class="fa fa-file-text"></i>
        <span>用户资料</span>
      </el-menu-item>
      <el-menu-item index="user-renlist">
        <i class="fa fa-users"></i>
        <span>数字技工/方案论证</span>
      </el-menu-item>
      <el-menu-item index="user-cailist">
        <i class="fa fa-dropbox"></i>
        <span>材料/设备</span>
      </el-menu-item>
      <el-menu-item index="user-machinelist">
        <i class="fa fa-wrench"></i>
        <span>智能建造装备</span>
      </el-menu-item>
      <el-menu-item index="user-itlist">
        <i class="fa fa-info-circle"></i>
        <span>信息化产品/服务</span>
      </el-menu-item>
      <el-menu-item index="user-inquirylist">
        <i class="fa fa-file-powerpoint-o"></i>
        <span>报价单</span>
      </el-menu-item>
      <el-menu-item index="user-editpwd">
        <i class="fa fa-key"></i>
        <span>改密码</span>
      </el-menu-item>
      <el-menu-item index="user-out">
        <i class="fa fa-sign-out"></i>
        <span>退出</span>
      </el-menu-item>
    </el-menu>
    <div class="collapse-box" @click="isCollapseClick">
      <div class="collapse-icons">
        <el-icon v-if="isCollapse" color="#606266" :size="20">
          <Expand />
        </el-icon>
        <el-icon v-else color="#606266" :size="20">
          <Fold />
        </el-icon>
      </div>
    </div>
  </div>
</template>
