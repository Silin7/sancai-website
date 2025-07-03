<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import useHeaderStore from '@/store/modules/header'

const router = useRouter()
const store = useHeaderStore()

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

const selectedTab = computed(() => {
  return store.selectedTab
})

function tabRouterPush(name: string) {
  router.push({
    name,
  })
  store.setSelectedTab(name)
  window.localStorage.setItem('selectedTab', name)
}

const menuList: any = ref([
  { tetle: '系统首页', path: '/', name: 'home', children: [] },
  { tetle: '人材机信价格库', path: '/products', name: 'products', children: [] },
  {
    tetle: '数据方案组价',
    path: '/data-solution',
    name: 'datasolution',
    children: [
      { tetle: '数据方案组价子路由1', path: '/data-solution/child1', name: 'date-solution1' },
      { tetle: '数据方案组价子路由2', path: '/data-solution/child2', name: 'date-solution2' },
      { tetle: '数据方案组价子路由3', path: '/data-solution/child3', name: 'date-solution3' },
      { tetle: '数据方案组价子路由4', path: '/data-solution/child4', name: 'date-solution4' },
      { tetle: '数据方案组价子路由5', path: '/data-solution/child5', name: 'date-solution5' },
    ],
  },
  { tetle: 'AI赋能应用', path: '/ai', name: 'ai', children: [] },
  { tetle: '视频讲解', path: '/video', name: 'video', children: [] },
  { tetle: '关于三才', path: '/about', name: 'about', children: [] },
  { tetle: '热点资讯', path: '/news', name: 'news', children: [] },
])
</script>

<template>
  <div class="headPositon">
    <div class="headflex">
      <div class="headnav">
        <img style="width: 120px" src="@/assets/logo.png" mode="widthFix" alt="logo" />
        <div class="menubox">
          <div
            v-for="(item, index) in menuList"
            :key="index"
            class="menuitem"
            @click="tabRouterPush(item.name)"
          >
            {{ item.tetle }}
          </div>
          <div style="color: #fff">{{ selectedTab }}</div>
          <!-- <div style="color: #fff">{{ windowWidth }}\{{ windowScrollY }}</div> -->
        </div>
      </div>
      <div class="headbtns">
        <button class="loginbtn">登录</button>
        <button class="registerbtn">注册</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.headPositon {
  width: 100vw;
  position: fixed;
  top: 0;
  z-index: 999;
  background-color: #012060;

  .headflex {
    margin: 0 auto;
    padding: 0 30px;
    max-width: 1800px;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid red;

    .headnav {
      width: calc(100% - 130px);
      display: flex;
      align-items: center;

      .menubox {
        display: flex;
        justify-content: space-around;

        .menuitem {
          margin-left: 30px;
          font-size: var(--title-size);
          color: #fff;
        }
      }
    }

    .headbtns {
      display: flex;
      align-items: center;

      button {
        color: #fff;
      }

      .loginbtn:hover {
        color: #165dff;
      }

      .registerbtn {
        display: inline-block;
        margin-left: 16px;
        padding: 8px 20px;
        color: #fff;
        background-color: #165dff;
        border-radius: 9999px;
      }

      .registerbtn:hover {
        transform: scale(1.05);
      }
    }
  }
}
</style>
