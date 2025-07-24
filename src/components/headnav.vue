<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import backToTop from '@/hooks/backToTop'
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
  backToTop()
  store.setSelectedTab(name)
  window.localStorage.setItem('selectedTab', name)
  drawerVisible.value = false
}

const menuList: any = ref([
  { title: '系统首页', path: '/', name: 'home', children: [] },
  { title: '人材机信价格库', path: '/products', name: 'products', children: [] },
  {
    title: '数据方案组价',
    path: '/data-solution',
    name: 'datasolution',
    children: [
      { title: '数据方案组价子路由1', path: '/data-solution/child1', name: 'date-solution1' },
      { title: '数据方案组价子路由2', path: '/data-solution/child2', name: 'date-solution2' },
      { title: '数据方案组价子路由3', path: '/data-solution/child3', name: 'date-solution3' },
      { title: '数据方案组价子路由4', path: '/data-solution/child4', name: 'date-solution4' },
      { title: '数据方案组价子路由5', path: '/data-solution/child5', name: 'date-solution5' },
    ],
  },
  { title: 'AI赋能应用', path: '/ai', name: 'ai', children: [] },
  { title: '视频讲解', path: '/video', name: 'video', children: [] },
  { title: '关于三才', path: '/about', name: 'about', children: [] },
  { title: '热点资讯', path: '/news', name: 'news', children: [] },
])

// 移动端
const drawerVisible = ref(false)
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
          <img src="@/assets/logo.png" alt="logo" style="width: 120px; margin-bottom: 2px" />
          <div v-if="windowWidth > 1140" class="menubox">
            <div
              v-for="(item, index) in menuList"
              :key="index"
              class="menuitem"
              :style="windowWidth > 1280 ? 'margin-left: 40px;' : 'margin-left: 20px;'"
              @click="tabRouterPush(item.name)"
            >
              <div class="menutitle" :style="selectedTab === item.name ? 'font-weight: 700;' : ''">
                {{ item.title }}
              </div>
              <div class="menuheng"></div>
            </div>
          </div>
          <div v-else @click="drawerVisible = true">
            <i class="fa fa-bars" style="font-size: 28px; color: #fff"></i>
          </div>
        </div>
        <div v-if="windowWidth > 1140" class="headbtns">
          <button class="loginbtn">登录</button>
          <button class="registerbtn">注册</button>
        </div>
      </div>
    </div>
    <!-- 移动端 抽屉 -->
    <el-drawer
      v-model="drawerVisible"
      :with-header="false"
      direction="rtl"
      size="80%"
      class="mobiledrawer"
    >
      <div class="drawerhead">
        <div class="drawerleft">
          <div class="culbbox">
            <i class="fa fa-cube" style="font-size: 16px; color: #165dff"></i>
          </div>
          <p style="">新材网</p>
        </div>
        <i
          class="fa fa-times"
          style="font-size: 28px; color: #6b7280; cursor: pointer"
          @click="drawerVisible = false"
        ></i>
      </div>
      <div class="mobilecollapse">
        <el-collapse v-model="selectedTab" accordion @change="tabRouterPush">
          <el-collapse-item
            v-for="(item, index) in menuList"
            :key="index"
            :title="item.title"
            :name="item.name"
          >
          </el-collapse-item>
        </el-collapse>
      </div>
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
    max-width: 1536px;
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
            font-size: 1.25rem;
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

.mobiledrawer {
  .drawerhead {
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e5e7eb;

    .drawerleft {
      display: flex;
      align-items: center;

      .culbbox {
        width: 40px;
        height: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgb(22 93 255 / 0.1);
        border-radius: 8px;
      }

      p {
        margin: 0 0 0 8px;
        font-size: 1.25rem;
        font-weight: 700;
        color: #012060;
      }
    }
  }
  .mobilecollapse {
    padding: 20px;
  }
}
</style>

<style lang="scss">
.mobiledrawer {
  .el-drawer__body {
    padding: 0 !important;
  }

  .el-collapse {
    border: 0 !important;

    .el-icon {
      display: none;
    }

    .el-collapse-item__header {
      border: 0 !important;
    }

    .el-collapse-item__header:hover {
      color: #165dff !important;
    }

    .el-collapse-item__title {
      font-size: 1.25rem !important;
    }

    .el-collapse-item__wrap {
      border: 0 !important;
    }

    .el-collapse-item__content {
      display: none;
    }

    .is-active {
      color: #165dff !important;
    }
  }
}
</style>
