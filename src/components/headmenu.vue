<script setup lang="ts">
import { onMounted, ref } from 'vue'
import pageJump from '@/hooks/pageJump'

// 登陆后的用户信息
const userinfo: any = ref({})

function getUserInfo() {
  if (window.localStorage.getItem('userinfo')) {
    userinfo.value = JSON.parse(window.localStorage.getItem('userinfo') as string)
  } else {
    userinfo.value = {}
  }
}

onMounted(() => {
  getUserInfo()
})
</script>

<template>
  <div class="headmenu">
    <div class="logo-title">
      <img src="@/assets/logo2.png" @click="pageJump('user-index')" />
      <!-- <span class="title">前端框架-VUE3</span> -->
    </div>
    <div class="avatar-name">
      <i class="fa fa-user-circle mr-2"></i>
      <span>{{ userinfo.name || '未登录' }}</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.headmenu {
  padding: 0 24px;
  height: 68px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #012060;

  .logo-title {
    display: flex;
    align-items: center;

    img {
      cursor: pointer;
      width: 120px;
    }

    // .title {
    //   color: #fff;
    //   font-size: 20px;
    //   font-weight: 700;
    // }
  }

  .avatar-name {
    cursor: pointer;
    display: flex;
    align-items: center;
    color: #ffffff;
    font-size: 1.25rem;
    line-height: 1.25rem;
  }
}
</style>
