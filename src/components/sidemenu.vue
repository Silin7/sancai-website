<script lang="ts" setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Fold, Expand } from '@element-plus/icons-vue'
import eventBus from '@/utils/eventBus'
import useHeaderStore from '@/store/modules/header'

const router = useRouter()
const headerStore = useHeaderStore()

const selectedTab = computed(() => {
  return headerStore.selectedTab
})

function setRouterStore(name: string) {
  headerStore.setSelectedTab(name)
  router.push({
    name,
  })
}

// 退出
function signOut() {
  ElMessageBox.confirm('确定要退出当前账号吗？ ', '退出确认', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(() => {
      ElMessage({
        type: 'success',
        message: '退出成功',
      })
    })
    .catch(() => {
      console.log('--------> 取消退出')
    })
}

// 折叠 or 展开
const isCollapse: any = ref(false)

function isCollapseClick() {
  isCollapse.value = !isCollapse.value
}

onMounted(() => {
  eventBus.on('set-router-store', setRouterStore)
})
</script>

<template>
  <div class="custom-menu">
    <el-menu :collapse="isCollapse" :default-active="selectedTab">
      <el-menu-item index="user-index" @click="setRouterStore('user-index')">
        <i class="fa fa-home"></i>
        <span>首页</span>
      </el-menu-item>
      <el-menu-item index="user-profile" @click="setRouterStore('user-profile')">
        <i class="fa fa-file-text"></i>
        <span>用户资料</span>
      </el-menu-item>
      <el-menu-item index="user-renlist" @click="setRouterStore('user-renlist')">
        <i class="fa fa-users"></i>
        <span>数字技工/方案论证</span>
      </el-menu-item>
      <el-menu-item index="user-cailist" @click="setRouterStore('user-cailist')">
        <i class="fa fa-dropbox"></i>
        <span>材料/设备</span>
      </el-menu-item>
      <el-menu-item index="user-machinelist" @click="setRouterStore('user-machinelist')">
        <i class="fa fa-wrench"></i>
        <span>智能建造装备</span>
      </el-menu-item>
      <el-menu-item index="user-itlist" @click="setRouterStore('user-itlist')">
        <i class="fa fa-info-circle"></i>
        <span>信息化产品/服务</span>
      </el-menu-item>
      <el-menu-item index="user-inquirylist" @click="setRouterStore('user-inquirylist')">
        <i class="fa fa-file-powerpoint-o"></i>
        <span>报价单</span>
      </el-menu-item>
      <el-menu-item index="user-editpwd" @click="setRouterStore('user-editpwd')">
        <i class="fa fa-key"></i>
        <span>改密码</span>
      </el-menu-item>
      <el-menu-item @click="signOut">
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
