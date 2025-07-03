<script setup lang="ts">
// import { onMounted, onUnmounted, ref } from 'vue'

// const emit = defineEmits(['goTopCallback'])

// function goTop() {
//   emit('goTopCallback')
// }

// const interval: any = ref(null)
// const scrollContainer: any = ref(0)

// onMounted(() => {
//   interval.value = setInterval(() => {
//     scrollContainer.value.scrollTop += 1 // 向上滚动1像素
//     if (scrollContainer.value.scrollTop >= scrollContainer.value.scrollHeight) {
//       scrollContainer.value.scrollTop = 0 // 回到顶部
//     }
//   }, 10) // 每10毫秒滚动一次
// })

// onUnmounted(() => {
//   clearInterval(interval.value)
// })
</script>

<template>
  <div class="sideleft">
    <div class="scroll-container">
      <div class="scroll-list">
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
        <div class="float-btn">
          <i class="fa fa-chevron-up" style="font-size: 16px; color: #374151"></i>
          <span>回顶部</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.sideleft {
  position: fixed;
  left: 20px;
  bottom: 30vh;
  z-index: 9999;

  .scroll-container {
    overflow: hidden;
    width: 300px; /* 或者你希望的宽度 */
    height: 50px; /* 或者你希望的高度 */
    border: 1px solid red;
  }

  .scroll-list {
    display: flex; /* 使列表项水平排列 */
    width: 100%; /* 与容器宽度相同 */
    animation: scroll 10s linear infinite; /* 动画名称、持续时间、速度曲线、重复次数 */
  }

  @keyframes scroll {
    0% {
      transform: translateY(0);
    }
    100% {
      transform: translateY(-100%);
    } /* 根据列表项数量调整 */
  }
}
</style>
