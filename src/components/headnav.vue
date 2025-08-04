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
  {
    title: '人材机信价格库',
    path: '/products',
    name: 'products',
    children: [
      { title: '数字技工/方案论证', path: '/products?id=child1', name: 'products-child1' },
      { title: '材料/设备', path: '/products?id=child2', name: 'products-child2' },
      { title: '智能建造装备', path: '/products?id=child3', name: 'products-child3' },
      { title: '信息化产品/服务', path: '/products?id=child4', name: 'products-child4' },
    ],
  },
  { title: '数据方案组价', path: '/data-solution', name: 'datasolution', children: [] },
  { title: 'AI赋能应用', path: '/ai', name: 'ai', children: [] },
  { title: '视频演示', path: '/video', name: 'video', children: [] },
  { title: '供应商', path: '/supplier', name: 'supplier', children: [] },
  { title: '关于三才', path: '/about', name: 'about', children: [] },
  { title: '热点资讯', path: '/news', name: 'news', children: [] },
  { title: '工程造价+AI', path: '/engineering-ai', name: 'engineeringai', children: [] },
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
            windowWidth > 1290 ? 'width: calc(100% - 130px);' : 'justify-content: space-between;'
          "
        >
          <img src="@/assets/logo.png" alt="logo" class="headlogo" />
          <div v-if="windowWidth > 1290" class="menubox">
            <div
              v-for="(item, index) in menuList"
              :key="index"
              class="menuitem"
              @click="tabRouterPush(item.name)"
            >
              <div class="menuheng1"></div>
              <div class="menutitle frcc">
                <span>{{ item.title }}</span>
                <i v-if="item.children.length > 0" class="fa fa-chevron-down"></i>
              </div>
              <div v-if="selectedTab === item.name" class="menuheng2"></div>
              <div v-else class="menuheng3"></div>
              <div v-if="item.children.length > 0" class="menuChildBox">
                <div v-for="(item2, index2) in item.children" :key="index2" class="menuChildItem">
                  <div class="menuChildTitle" @click="tabRouterPush(item2.name)">
                    {{ item2.title }}
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-else @click="drawerVisible = true">
            <i class="fa fa-bars" style="font-size: 28px; color: #fff"></i>
          </div>
        </div>
        <div v-if="windowWidth > 1290" class="headbtns">
          <div class="headLogin">
            <div class="btnHeng1"></div>
            <button>登录</button>
            <div class="btnHeng2"></div>
          </div>
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
  background-color: rgb(1 32 96 / 0.95);

  .headflex {
    margin: 0 auto;
    padding: 0 30px;
    max-width: 1536px;
    height: 90px;
    display: flex;
    align-items: center;
    justify-content: space-between;

    .headnav {
      width: 100%;
      display: flex;
      align-items: center;

      .headlogo {
        width: 150px;
      }

      .headlogo:hover {
        cursor: pointer;
        transform: scale(1.05);
      }

      .menubox {
        display: flex;
        justify-content: space-around;
        align-items: flex-end;

        .menuitem {
          position: relative;
          display: flex;
          flex-flow: column;

          .menutitle {
            color: #fff;
            line-height: 1.25rem;

            span {
              font-size: 1.25rem;
            }

            i {
              margin-left: 0.25rem;
              font-size: 0.75rem;
              line-height: 0.75rem;
              font-weight: normal;
            }
          }

          .menuheng1 {
            margin-bottom: 0.5rem;
            width: 0%;
            height: 2px;
          }

          .menuheng2 {
            margin-top: 0.5rem;
            width: 100%;
            height: 2px;
            background-color: #fff;
          }

          .menuheng3 {
            margin-top: 0.5rem;
            width: 0%;
            height: 2px;
          }

          .menuChildBox {
            position: absolute;
            top: 3rem;
            left: 0;
            z-index: 50;
            min-width: 14rem;
            padding: 0.375rem 0;
            border-radius: 0.5rem;
            background-color: rgb(10 36 99 / 0.95);

            .menuChildItem {
              margin-top: 0.375rem;
              padding: 0.5rem 0;
              color: #fff;
              // color: rgb(1 32 96);

              .menuChildTitle {
                padding: 0.75rem 1rem;
                font-size: 1.25rem;
              }
            }

            .menuChildItem:first-child {
              margin-top: 0;
            }

            .menuChildItem:hover {
              cursor: pointer;
              background-color: #0b2f82;
            }
          }
        }

        @media (min-width: 1551px) {
          .menuitem {
            margin-left: 32px;
          }
        }

        @media (max-width: 1550px) and (min-width: 1351px) {
          .menuitem {
            margin-left: 1.25rem;
          }
        }

        @media (max-width: 1350px) and (min-width: 1290px) {
          .menuitem {
            margin-left: 10px;
          }
        }

        .menuitem:hover {
          .menutitle {
            cursor: pointer;
          }

          i {
            transform: rotate(180deg);
            transition: transform 0.5s ease;
          }

          .menuheng3 {
            animation: hengChange 0.5s infinite alternate;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
          }
        }

        @keyframes hengChange {
          0% {
            width: 0%;
            background-color: #fff;
          }

          100% {
            width: 100%;
            background-color: #fff;
          }
        }
      }
    }

    .headbtns {
      display: flex;
      align-items: center;

      .headLogin {
        .btnHeng1 {
          margin-bottom: 8px;
          width: 0%;
          height: 2px;
        }

        button {
          color: #fff;
        }

        .btnHeng2 {
          margin-top: 8px;
          width: 0%;
          height: 2px;
        }
      }

      .headLogin:hover {
        .btnHeng2 {
          animation: loginbtnHeng1 0.5s infinite alternate;
          animation-iteration-count: 1;
          animation-fill-mode: forwards;
        }
      }

      @keyframes loginbtnHeng1 {
        0% {
          width: 0%;
          background-color: #165dff;
        }

        100% {
          width: 100%;
          background-color: #165dff;
        }
      }

      .registerbtn {
        display: inline-block;
        margin-left: 16px;
        padding: 8px 1.25rem;
        color: #fff;
        background-color: #165dff;
        border-radius: 9999px;
      }

      .registerbtn:hover {
        transform: scale(1.05);
        box-shadow: 2px 2px 10px 0 rgb(22 93 255 / 0.1);
      }
    }
  }
}

.mobiledrawer {
  .drawerhead {
    padding: 1.25rem;
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
    padding: 1.25rem;
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
