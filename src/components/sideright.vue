<script setup lang="ts">
import { ref } from 'vue'

// 返回顶部
const emit = defineEmits(['goTopCallback'])

function goTop() {
  emit('goTopCallback')
}

// 折叠 or 展开
const foldState: any = ref(true)
const mouseState: any = ref('')

function iconMouseenter(code: string) {
  mouseState.value = code
}

function iconMouseleave() {
  mouseState.value = ''
}
</script>

<template>
  <div class="sideright">
    <div class="relativeBox" @mouseenter="iconMouseenter('ai')" @mouseleave="iconMouseleave">
      <div class="aiBtn" @click="foldState = !foldState">
        {{ foldState ? '关闭' : 'AI' }}
      </div>
      <span v-if="mouseState === 'ai'" class="flexSpan">智能助手</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('zxzx')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-headphones"></i>
      </div>
      <span v-if="mouseState === 'zxzx'" class="flexSpan">在线咨询</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('lxwm')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-phone"></i>
      </div>
      <span v-if="mouseState === 'lxwm'" class="flexSpan">联系我们</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('gzwm')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-weixin"></i>
      </div>
      <span v-if="mouseState === 'gzwm'" class="flexSpan">关注我们</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('zxly')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-pencil"></i>
      </div>
      <span v-if="mouseState === 'zxly'" class="flexSpan">在线留言</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('top')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn" @click="goTop">
        <i class="fa fa-chevron-up"></i>
      </div>
      <span v-if="mouseState === 'top'" class="flexSpan">回顶部</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.sideright {
  position: fixed;
  right: 20px;
  bottom: 20vh;
  z-index: 9999;

  .relativeBox {
    position: relative;

    .aiBtn {
      cursor: pointer;
      height: 3.5rem;
      width: 3.5rem;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #fff;
      font-size: 1.25rem;
      font-weight: 700;
      background-image: linear-gradient(to right, #3b82f6, #0ea5e9);
      border-radius: 9999px;
    }

    .aiBtn:hover {
      transform: scale(1.05);
    }

    .flexSpan {
      position: absolute;
      top: 1.125rem;
      right: 3.8rem;
      padding: 0.25rem 0;
      width: 4rem;
      font-size: 0.75rem;
      line-height: 1rem;
      text-align: center;
      transition-duration: 300ms;
      color: #fff;
      background-color: #012060;
      border-radius: 0.25rem;
    }
  }

  .float-btn {
    cursor: pointer;
    margin-top: 0.75rem;
    cursor: pointer;
    height: 3.5rem;
    width: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 9999px;
    color: rgb(1 32 96);
    background: rgba(255, 255, 255, 0.3);
    box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

    i {
      font-size: 1rem;
    }

    span {
      font-size: 0.75rem;
      line-height: 1rem;
    }
  }

  .float-btn:hover {
    color: #fff;
    background-color: #165dff;
    transform: scale(1.05);

    i {
      color: #fff !important;
    }
  }
}
</style>
