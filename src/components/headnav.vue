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

// 移动端
const drawer2 = ref(false)
</script>

<template>
  <div>
    <div class="headPositon">
      <div class="headflex">
        <div
          class="headnav"
          :style="
            windowWidth > 1140 ? 'width: calc(100% - 130px);' : 'justify-content: space-between;'
          "
        >
          <img
            src="@/assets/logo.png"
            mode="widthFix"
            alt="logo"
            style="width: 120px; margin-bottom: 2px"
          />
          <div v-if="windowWidth > 1140" class="menubox">
            <div
              v-for="(item, index) in menuList"
              :key="index"
              class="menuitem"
              :style="windowWidth > 1280 ? 'margin-left: 40px;' : 'margin-left: 20px;'"
              @click="tabRouterPush(item.name)"
            >
              <div class="menutitle" :style="selectedTab === item.name ? 'font-weight: 700;' : ''">
                {{ item.tetle }}
              </div>
              <div class="menuheng"></div>
            </div>
          </div>
          <div v-else @click="drawer2 = true">
            <i class="fa fa-bars" style="font-size: 28px; color: #fff"></i>
          </div>
        </div>
        <div v-if="windowWidth > 1140" class="headbtns">
          <button class="loginbtn">登录</button>
          <button class="registerbtn">注册</button>
        </div>
      </div>
    </div>
    <el-drawer v-model="drawer2" :with-header="false" direction="rtl" size="80%">
      <div>
        <div class="culbbox">
          <i class="fa fa-cube" style="font-size: 16px; color: #165dff"></i>
        </div>
        <p style="font-size: 1.25rem; font-weight: 700; color: #012060">新材网</p>
      </div>
      <i class="fa fa-times" style="font-size: 28px; color: #6b7280"></i>
    </el-drawer>
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

    .headnav {
      width: 100%;
      display: flex;
      align-items: center;

      .menubox {
        height: 33px;
        display: flex;
        justify-content: space-around;
        align-items: flex-end;

        .menuitem {
          margin-left: 30px;
          display: flex;
          flex-flow: column;

          .menutitle {
            font-size: var(--title-size);
            color: #fff;
          }

          .menuheng {
            margin-top: 2px;
            width: 0%;
            height: 2px;
          }
        }

        .menuitem:hover {
          .menutitle {
            cursor: pointer;
            color: #165dff;
          }

          .menuheng {
            animation: hengChange 0.5s infinite alternate;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
          }
        }

        @keyframes hengChange {
          0% {
            width: 0%;
            background-color: #165dff;
          }

          100% {
            width: 100%;
            background-color: #165dff;
          }
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
