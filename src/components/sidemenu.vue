<script lang="ts" setup>
import { computed, onMounted, ref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Fold, Expand } from '@element-plus/icons-vue'
import useHeaderStore from '@/store/modules/header'
import pageJump from '@/hooks/pageJump'
import { baselogoutdApi, currentuserApi } from '@/api/modules/login'

const headerStore = useHeaderStore()

const selectedTab = computed(() => {
  return headerStore.selectedTab
})

// 折叠 or 展开
const isCollapse: any = ref(false)

function isCollapseClick() {
  isCollapse.value = !isCollapse.value
}

// 退出
function signOut() {
  ElMessageBox.confirm('确定要退出当前账号吗？ ', '退出确认', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(() => {
      baselogoutdApi({}).then((res: any) => {
        if (res) {
          ElMessage({
            type: 'success',
            message: '退出成功',
          })
          window.localStorage.removeItem('token')
          window.localStorage.removeItem('userinfo')
          window.localStorage.removeItem('permission')
          pageJump('login')
        }
      })
    })
    .catch(() => {
      console.log('取消退出')
    })
}

// 用户信息
const userType: any = ref(1)
const userRole: any = ref(1)
const userPermissions: any = ref([])

onMounted(() => {
  if (window.location.hash.includes("/user/")) {
    currentuserApi().then((res: any) => {
      if (res) {
        // user_type  1-供方/2-需方
        userType.value = res.user_type
        // role  0-主管理员/1-普通管理员
        userRole.value = res.role
        const permissions = res?.related_companies[0]?.permissions
        if (res.role !== 0 && permissions) {
          for (let key in permissions) {
            userPermissions.value.push(key)
          }
        }
      }
    })
  }
})
</script>

<template>
  <div class="custom-menu">
    <el-menu :collapse="isCollapse" :default-active="selectedTab">
      <el-menu-item index="user-index" @click="pageJump('user-index')">
        <i class="fa fa-home"></i>
        <span>首页</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0" index="user-role" @click="pageJump('user-role')">
        <i class="fa fa-home"></i>
        <span>管理员管理</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0" index="user-profile" @click="pageJump('user-profile')">
        <i class="fa fa-file-text"></i>
        <span>企业资料</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0 && userType === 1" index="user-qyzzlist" @click="pageJump('user-qyzzlist')">
        <i class="fa fa-users"></i>
        <span>企业资质</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0 && userType === 1" index="user-qyallist" @click="pageJump('user-qyallist')">
        <i class="fa fa-users"></i>
        <span>企业案例</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0 && userType === 1 && userPermissions.includes('0')" index="user-renlist"
        @click="pageJump('user-renlist')">
        <i class="fa fa-users"></i>
        <span>数字技术应用论证/数字实施方案论证</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0 && userType === 1 && userPermissions.includes('1')" index="user-cailist"
        @click="pageJump('user-cailist')">
        <i class="fa fa-dropbox"></i>
        <span>材料/设备</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0 && userType === 1 && userPermissions.includes('2')" index="user-machinelist"
        @click="pageJump('user-machinelist')">
        <i class="fa fa-wrench"></i>
        <span>智能建造装备</span>
      </el-menu-item>
      <el-menu-item v-if="userRole === 0 && userType === 1 && userPermissions.includes('3')" index="user-itlist"
        @click="pageJump('user-itlist')">
        <i class="fa fa-info-circle"></i>
        <span>信息化产品/服务</span>
      </el-menu-item>
      <!-- <el-menu-item index="user-inquirylist" @click="pageJump('user-inquirylist')">
        <i class="fa fa-file-powerpoint-o"></i>
        <span>报价单</span>
      </el-menu-item> -->
      <el-menu-item index="user-quotationlist" @click="pageJump('user-quotationlist')">
        <i class="fa fa-file-powerpoint-o"></i>
        <span>询价单</span>
      </el-menu-item>
      <el-menu-item index="user-editpwd" @click="pageJump('user-editpwd')">
        <i class="fa fa-key"></i>
        <span>改密码</span>
      </el-menu-item>
      <el-menu-item index="user-mull" @click="signOut">
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
