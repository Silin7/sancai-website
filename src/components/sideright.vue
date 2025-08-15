<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const windowWidth = ref(window.innerWidth)
const windowScrollY = ref(window.scrollY)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

function handleScroll() {
  windowScrollY.value = window.scrollY
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
  window.addEventListener('scroll', handleScroll)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
  window.removeEventListener('scroll', handleScroll)
})

// 返回顶部
const emit = defineEmits(['goTopCallback'])

function goTop() {
  emit('goTopCallback')
}

// 折叠 or 展开
const foldState: any = ref(false)
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
      <span v-if="windowWidth > 600 && mouseState === 'ai'" class="flexSpan">智能助手</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('zxzx')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-headphones"></i>
      </div>
      <span v-if="windowWidth > 600 && mouseState === 'zxzx'" class="flexSpan">在线咨询</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('lxwm')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-phone"></i>
      </div>
      <span v-if="windowWidth > 600 && mouseState === 'lxwm'" class="flexSpan">联系我们</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('gzwm')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-weixin"></i>
      </div>
      <span v-if="windowWidth > 600 && mouseState === 'gzwm'" class="flexSpan">关注我们</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('zxly')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn">
        <i class="fa fa-pencil"></i>
      </div>
      <span v-if="windowWidth > 600 && mouseState === 'zxly'" class="flexSpan">在线留言</span>
    </div>

    <div class="relativeBox" @mouseenter="iconMouseenter('top')" @mouseleave="iconMouseleave">
      <div v-if="foldState" class="float-btn" @click="goTop">
        <i class="fa fa-chevron-up"></i>
      </div>
      <span v-if="windowWidth > 600 && mouseState === 'top'" class="flexSpan">回顶部</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.sideright {
  position: fixed;
  right: 20px;
  bottom: 26vh;
  z-index: 9999;

  .relativeBox {
    position: relative;

    .aiBtn {
      height: 3.5rem;
      width: 3.5rem;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #fff;
      font-size: 1rem;
      font-weight: 700;
      background: linear-gradient(135deg, #165dff 0%, #36cfc9 100%);
      border-radius: 999px;
    }

    .aiBtn:hover {
      @media (max-width: 768px) {
        cursor: pointer;
        transform: scale(1.05);
      }
    }

    .float-btn {
      margin-top: 0.75rem;
      height: 3.5rem;
      width: 3.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 999px;
      color: rgb(1 32 96);
      background: rgba(255, 255, 255);
      box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

      i {
        font-size: 1rem;
      }
    }

    .float-btn:hover {
      @media (max-width: 768px) {
        cursor: pointer;
        color: #fff;
        background-color: #165dff;
        transform: scale(1.05);

        i {
          color: #fff !important;
        }
      }
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
}
</style>
