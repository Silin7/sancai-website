<script setup lang="ts">
import pageJump from '@/hooks/pageJump'
</script>

<template>
  <div class="headmenu">
    <div class="logo-title">
      <img src="@/assets/logo.png" @click="pageJump('user-index')" />
      <!-- <span class="title">前端框架-VUE3</span> -->
    </div>
    <div class="avatar-name">
      <div class="avatar-box frcc">
        U
        <!-- <img src="@/assets/avatar.jpg" /> -->
      </div>
      <span class="title">用户名</span>
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
    display: flex;
    align-items: center;

    .avatar-box {
      margin-right: 10px;
      width: 36px;
      height: 36px;
      font-weight: 500;
      color: #ffffff;
      background-color: rgba(255, 255, 255, 0.2);
      border-radius: 50%;
    }

    // img {
    //   margin-right: 10px;
    //   width: 36px;
    //   height: 36px;
    //   border-radius: 50%;
    // }

    .title {
      font-size: 14px;
      font-weight: 500;
      color: rgba(255, 255, 255, 0.9);
    }
  }
}
</style>
