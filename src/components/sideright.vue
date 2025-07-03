<script setup lang="ts">
const emit = defineEmits(['goTopCallback'])

function goTop() {
  emit('goTopCallback')
}
</script>

<template>
  <div class="sideright">
    <div class="siderflex">
      <div class="ai-helper-top">AI助手</div>
      <div class="float-btn">
        <i class="fa fa-headphones" style="font-size: 16px; color: #374151"></i>
        <span>在线咨询</span>
      </div>
      <div class="float-btn">
        <i class="fa fa-phone" style="font-size: 16px; color: #374151"></i>
        <span>联系我们</span>
      </div>
      <div class="float-btn">
        <i class="fa fa-weixin" style="font-size: 16px; color: #374151"></i>
        <span>关注我们</span>
      </div>
      <div class="float-btn">
        <i class="fa fa-pencil" style="font-size: 16px; color: #374151"></i>
        <span>在线留言</span>
      </div>
      <div class="float-btn" @click="goTop">
        <i class="fa fa-chevron-up" style="font-size: 16px; color: #374151"></i>
        <span>回顶部</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.sideright {
  position: fixed;
  right: 20px;
  bottom: 20vh;
  z-index: 9999;

  .siderflex {
    display: flex;
    flex-flow: column;
    align-items: center;
    border-radius: 12px;
    background-color: #e6e9ef99;
    padding: 12px;
    box-shadow: 0 10px 10px -3px rgb(0 0 0 / 0.1);

    .ai-helper-top {
      cursor: pointer;
      width: 96px;
      height: 48px;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #fff;
      font-size: var(--title-size);
      font-weight: 700;
      background-image: linear-gradient(to right, #3b82f6, #0ea5e9);
      border-radius: 24px;
    }

    .float-btn {
      cursor: pointer;
      margin-top: 12px;
      cursor: pointer;
      height: 64px;
      width: 64px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-radius: 9999px;
      color: #4b5563;
      background-color: #fff;

      span {
        margin-top: 4px;
        font-size: 12px;
        line-height: 16px;
      }
    }

    .float-btn:hover {
      color: #fff;
      background-color: #165dff;

      .fa {
        color: #fff !important;
      }
    }
  }
}
</style>
