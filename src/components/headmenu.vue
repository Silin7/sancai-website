<script setup lang="ts"></script>

<template>
  <div class="headmenu">
    <div class="logo-title">
      <img src="@/assets/logo.svg" />
      <span class="title">前端框架-VUE3</span>
    </div>
    <div class="avatar-name">
      <img src="@/assets/avatar.jpg" />
      <span class="title">adminmaster</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.headmenu {
  box-sizing: border-box;
  padding: 0 20px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .logo-title {
    display: flex;
    align-items: center;

    img {
      margin-right: 10px;
      width: 30px;
      height: 30px;
    }

    .title {
      color: #333;
      font-size: 20px;
      font-weight: 700;
    }
  }

  .avatar-name {
    display: flex;
    align-items: center;

    img {
      margin-right: 10px;
      width: 30px;
      height: 30px;
      border-radius: 50%;
    }

    .name {
      color: #999;
      font-size: 20px;
      font-weight: 700;
    }
  }
}
</style>
