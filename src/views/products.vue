<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
})
</script>

<template>
  <div class="productsPage">
    <!-- BANNER -->
    <div class="bannerBox">
      <img
        src="@/assets/products-banner01.jpeg"
        alt="banner"
        mode="aspectFill"
        :style="['width: 100vw;', windowWidth < 600 ? 'height: 60rem;' : 'height: 48rem;']"
      />
      <div class="bannerAbsolute">
        <div class="bannerContent">
          <div class="bannerTitle">聚焦新型城市基础设施建设再起航</div>
          <div class="bannerSubtitle">绿色化 数字化 智能化</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.productsPage {
  background-color: #f9fafb;

  .bannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .bannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .bannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1720px;

        .bannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .bannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }
      }
    }
  }
}
</style>
