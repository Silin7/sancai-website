<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from 'vue'

const windowWidth = ref(window.innerWidth);

const updateWindowWidth = () => {
  windowWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth);
});


const activeIndex = ref('1')
const menuList: any = ref([
  { tetle: "系统首页", path: "/", children: [] },
  { tetle: "人材机信价格库", path: "/products", children: [] },
  {
    tetle: "数据方案组价", path: "/data-solution", children: [
      { tetle: "数据方案组价子路由1", path: "/data-solution/child1" },
      { tetle: "数据方案组价子路由2", path: "/data-solution/child2" },
      { tetle: "数据方案组价子路由3", path: "/data-solution/child3" },
      { tetle: "数据方案组价子路由4", path: "/data-solution/child4" },
      { tetle: "数据方案组价子路由5", path: "/data-solution/child5" },
    ]
  },
  { tetle: "AI赋能应用", path: "/ai", children: [] },
  { tetle: "视频讲解", path: "/video", children: [] },
  { tetle: "关于三才", path: "/about", children: [] },
  { tetle: "热点资讯", path: "/news", children: [] },
])
</script>

<template>
  <div class="headnav">
    <img style="width: 120px" src="@/assets/logo.png" mode="widthFix" alt="logo" />
    <div class="menubox" style="">
      <div v-for="(item, index) in menuList" :key="index" class="menuitem">
        {{ item.tetle }}
      </div>
      {{ windowWidth - 210 }}
    </div>
    <div class="headbtns">
      <button>登录</button>
      <button>注册</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.headnav {
  padding: 0 30px;
  height: 72px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #001f5f;

  .menubox {
    max-width: 1500px;
    width: calc(100% - 210px);
    margin-left: 30px;
    display: flex;
    justify-content: space-around;
    border: 1px solid red;

    .menuitem {
      color: #fff;
      font-size: var(--title-size);
    }
  }

  .headbtns {
    border: 1px solid red;
    display: flex;
    align-items: center;

    button :first-child {
      color: #fff;
    }

    button :last-child {
      color: #fff;
      background-color: #165dff;
    }
  }
}
</style>
