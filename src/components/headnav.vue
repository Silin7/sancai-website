<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, computed, watch, unref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import useHeaderStore from '@/store/modules/header'
import { baselogoutdApi } from '@/api/modules/login'

const windowWidth = ref(window.innerWidth)
const windowScrollY = ref(window.scrollY)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

function handleScroll() {
  windowScrollY.value = window.scrollY
}

const headerStore = useHeaderStore()

const selectedTab = computed(() => {
  getUserInfo()
  return headerStore.selectedTab
})

function tabRouterPush(item: any) {
  if (item.children && item.children.length > 0) {
    item.expanded = !item.expanded
    return
  }
  pageJump(item.name, item.query || {})
  drawerVisible.value = false
}

const menuList: any = ref([
  { id: '1', title: '系统首页', path: '/', name: 'home', children: [] },
  {
    title: '人材机信价格库',
    expanded: false,
    children: [
      { id: '21', title: '数字技术应用论证', path: '/requirements2', name: 'requirements2', query: { id: '1' } },
      { id: '22', title: '数字实施方案论证', path: '/requirements', name: 'requirements', query: { id: '22' } },
      // { id: '2', title: '数字技术应用论证/数字实施方案论证', path: '/scheme', name: 'scheme' },
      { id: '3', title: '材料/设备', path: '/materials', name: 'materials' },
      { id: '4', title: '智能建造装备', path: '/sale', name: 'sale' },
      { id: '5', title: '信息化产品/服务', path: '/products', name: 'products' },
    ],
  },
  { id: '6', title: '数据方案组价', path: '/data-solution', name: 'datasolution', children: [] },
  { id: '7', title: 'AI赋能应用', path: '/ai', name: 'ai', children: [] },
  { id: '8', title: '视频演示', path: '/video', name: 'video', children: [] },
  { id: '9', title: '供应商', path: '/supplier', name: 'supplier', children: [] },
  { id: '10', title: '关于三才', path: '/about', name: 'about', children: [] },
  { id: '11', title: '热点资讯', path: '/news', name: 'news', children: [] },
  { id: '12', title: '工程造价+AI', path: '/engineeringai', name: 'engineeringai', children: [] },
])

// menuChild show Mouseenter Mouseleave
const menuChildShow: any = ref(false)

function menuMouseenter(item: any) {
  if (item.children.length > 0) {
    menuChildShow.value = true
  }
}

function menuMouseleave() {
  menuChildShow.value = false
}

// 登陆后的用户信息
const userinfo: any = ref({})

function getUserInfo() {
  if (window.localStorage.getItem('userinfo')) {
    userinfo.value = JSON.parse(window.localStorage.getItem('userinfo') as string)
  } else {
    userinfo.value = {}
  }
}

// 退出登录
function logoutFunction() {
  ElMessageBox.confirm('确定要退出登录吗？ ', '退出登录', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(() => {
      baselogoutdApi({}).then((res: any) => {
        if (res) {
          ElMessage({
            type: 'success',
            message: '退出成功',
          })
          menuChildShow.value = false
          window.localStorage.removeItem('token')
          window.localStorage.removeItem('userinfo')
          window.localStorage.removeItem('permission')
          pageJump('login')
        }
      })
    })
    .catch(() => {
      console.log('取消退出')
    })
}

// 移动端
const drawerVisible = ref(false)

watch(
  () => drawerVisible.value,
  (val: boolean) => {
    if (val) {
      console.log('-------->', selectedTab.value)
    } else {
      menuList.value.forEach((element: any) => {
        element.expanded = false
      })
    }
  },
  {
    immediate: true,
  },
)

const buttonRef = ref()
const popoverRef = ref()
function onClickOutside() {
  unref(popoverRef).popperRef?.delayHide?.()
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
  window.addEventListener('scroll', handleScroll)
  getUserInfo()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <div>
    <div class="headPositon">
      <div class="headflex">
        <div class="headnav">
          <img src="@/assets/logo.png" class="headlogo" @click="pageJump('home')" />
          <div v-if="windowWidth > 1290" class="menubox">
            <div v-for="(item, index) in menuList" :key="index" class="menuitem" @mouseenter="menuMouseenter(item)"
              @mouseleave="menuMouseleave" @click="tabRouterPush(item)">
              <div class="menuheng1"></div>
              <div class="menutitle frcc">
                <span>{{ item.title }}</span>
                <i v-if="item.children.length > 0" class="fa fa-chevron-down"></i>
              </div>
              <div v-if="selectedTab === item.name" class="menuheng2"></div>
              <div v-else class="menuheng3"></div>
              <div v-if="menuChildShow && item.children.length > 0" class="menuChildAbsolute">
                <div class="menuChildBox">
                  <div v-for="(item2, index2) in item.children" :key="index2" class="menuChildItem">
                    <div class="menuChildTitle" @click="tabRouterPush(item2)">
                      {{ item2.title }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="drawerIcon" @click="drawerVisible = true">
            <i class="fa fa-bars"></i>
          </div>
        </div>
        <!-- userinfo.name -->
        <div v-if="windowWidth > 1290">
          <div v-if="userinfo.name" ref="buttonRef" v-click-outside="onClickOutside" class="username">
            <i class="fa fa-user-circle mr-2"></i>
            <span class="nameStyle">{{ userinfo.name }}</span>
            <el-popover placement="bottom" :virtual-ref="buttonRef" virtual-triggering :width="160" trigger="click">
              <div class="userPopover">
                <div class="popoverItem" @click="pageJump('user-index')">
                  用户中心
                </div>
                <div class="popoverItem" @click="logoutFunction">
                  退出登录
                </div>
              </div>
            </el-popover>
          </div>
          <div v-else class="headbtns">
            <div class="headLogin">
              <div class="btnHeng1"></div>
              <button @click="pageJump('login')">登录</button>
              <div class="btnHeng2"></div>
            </div>
            <button class="registerbtn" @click="pageJump('register')">注册</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 移动端 抽屉 -->
    <el-drawer v-model="drawerVisible" :with-header="false" direction="rtl" size="80%" class="mobiledrawer">
      <div class="drawerhead">
        <div class="drawerleft">
          <div class="culbbox">
            <i class="fa fa-cube"></i>
          </div>
          <p>新材网</p>
        </div>
        <i class="fa fa-times drawerclose" @click="drawerVisible = false"></i>
      </div>
      <div class="mobilecollapse">
        <div v-for="(item, index) in menuList" :key="index"
          :class="['collapseItem', selectedTab === item.name ? 'collapseActive' : '']" @click="tabRouterPush(item)">
          <div class="frbc">
            <span>{{ item.title }}</span>
            <i v-if="item.children.length > 0 && item.expanded" class="fa fa-chevron-up"></i>
            <i v-if="item.children.length > 0 && !item.expanded" class="fa fa-chevron-down"></i>
          </div>
          <div v-if="item.children.length > 0 && item.expanded" class="collapseChildren">
            <div v-for="(item2, index2) in item.children" :key="index2"
              :class="['collapseCitem', selectedTab === item2.name ? 'collapseActive' : '']"
              @click="tabRouterPush(item2)">
              {{ item2.title }}
            </div>
          </div>
        </div>
      </div>
      <div v-if="userinfo.name" class="mobileBtns">
        <div class="frcc">
          <i class="fa fa-user-circle mr-2"></i>
          <span class="nameStyle">{{ userinfo.name }}</span>
        </div>
        <!-- <span class="logoutStyle" @click="logoutFunction">退出</span> -->
      </div>
      <div v-if="userinfo.name" class="mobileBtns">
        <div class="frcc">
          <i class="fa fa-sign-out mr-2"></i>
          <span @click="logoutFunction">退出登录</span>
        </div>
      </div>
      <div v-else class="mobileBtns">
        <button class="mobileDlbtn" @click="tabRouterPush({ name: 'login' })">登录</button>
        <button class="mobileZcbtn" @click="tabRouterPush({ name: 'register' })">注册</button>
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
  background-color: rgb(1 32 96);

  .headflex {
    margin: 0 auto;
    padding: 0 1rem;
    max-width: 1536px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: space-between;

    @media (max-width: 1290px) {
      height: 64px;
    }

    .headnav {
      width: calc(100% - 150px);
      max-width: 1280px;
      display: flex;
      align-items: center;
      justify-content: flex-start;

      @media (max-width: 1290px) {
        width: 100%;
        justify-content: space-between;
      }

      .headlogo {
        cursor: pointer;
        width: 150px;

        @media (max-width: 1289px) {
          width: 120px;
        }
      }

      .menubox {
        display: flex;
        justify-content: space-around;
        align-items: flex-end;

        .menuitem {
          position: relative;
          display: flex;
          flex-flow: column;

          @media (min-width: 1551px) {
            margin-left: 1.75rem;
          }

          @media (max-width: 1550px) and (min-width: 1351px) {
            margin-left: 1.25rem;
          }

          @media (max-width: 1350px) and (min-width: 1290px) {
            margin-left: 0.625rem;
          }

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

          .menuChildAbsolute {
            position: absolute;
            top: 2rem;
            left: 0;
            z-index: 50;
            padding-top: 1rem;

            .menuChildBox {
              min-width: 14rem;
              padding: 0.375rem 0;
              border-radius: 0.5rem;
              background-color: rgb(10 36 99 / 0.95);

              .menuChildItem {
                margin-top: 0.375rem;
                padding: 0.5rem 0;
                color: #fff;

                .menuChildTitle {
                  padding: 0.375rem 1rem;
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
            background-color: #fff;
          }
        }

        @keyframes hengChange {
          0% {
            width: 0%;
          }

          100% {
            width: 100%;
          }
        }
      }

      .drawerIcon {
        font-size: 1.25rem;
        color: #fff;
      }
    }

    .username {
      color: #fff;
      display: flex;
      align-items: center;
      // font-size: 1.25rem;

      .nameStyle {
        display: inline-block;
        max-width: 210px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }

    .username:hover {
      @media (min-width: 1291px) {
        cursor: pointer;
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
        margin-left: 1rem;
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
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgb(255 255 255);

    .drawerleft {
      display: flex;
      align-items: center;

      .culbbox {
        width: 2.5rem;
        height: 2.5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgb(22 93 255 / 0.1);
        border-radius: 0.5rem;

        i {
          font-size: 1rem;
          color: #165dff;
        }
      }

      p {
        margin: 0 0 0 0.5rem;
        font-size: 1.25rem;
        font-weight: 700;
        color: #fff;
      }
    }

    .drawerclose {
      font-size: 1.25rem;
      color: #fff;
    }
  }

  .mobilecollapse {
    padding: 0.5rem;

    .collapseItem {
      margin-bottom: 0.5rem;
      padding: 0.75rem 0.5rem;
      font-size: 1rem;
      line-height: 1rem;
      color: #fff;
      border-radius: 0.5rem;

      i {
        font-size: 0.75rem;
      }
    }

    .collapseItem:last-child {
      margin-bottom: 0;
    }

    .collapseChildren {
      margin: 0.5rem 0 0 0.5rem;

      .collapseCitem {
        margin-bottom: 0.5rem;
        padding: 0.75rem 0.5rem;
        font-size: 1rem;
        line-height: 1rem;
        color: #fff;
        border-radius: 0.5rem;
      }

      .collapseCitem:last-child {
        margin-bottom: 0;
      }
    }

    .collapseActive {
      background-color: rgb(22 93 255 / 0.2);
    }
  }

  .mobileBtns {
    margin-top: 1rem;
    padding: 0 0.5rem;
    display: flex;
    justify-content: space-between;
    color: rgb(22 93 255);

    .nameStyle {
      display: inline-block;
      max-width: 8rem;
      white-space: nowrap;
      /* 防止文本换行 */
      overflow: hidden;
      /* 隐藏溢出的文本 */
      text-overflow: ellipsis;
      /* 显示省略号 */
    }

    .logoutStyle {
      margin-left: 0.5rem;
    }

    .logoutStyle:hover {
      cursor: pointer;
      color: #165dff;
    }

    button {
      margin-bottom: 0.5rem;
      width: calc(50% - 0.25rem);
      line-height: 1.5rem;
      padding: 0.5rem 0;
      border-radius: 9999px;
    }

    .mobileDlbtn {
      color: rgb(22 93 255);
      border: 1px solid rgb(22 93 255);
    }

    .mobileZcbtn {
      color: #fff;
      background-color: rgb(22 93 255 / 0.9);
    }
  }
}

@media (min-width: 1290px) {
  .headlogo:hover {
    transform: scale(1.05);
  }
}

.popoverItem {
  line-height: 44px;
  color: #262626;
  text-align: center;
  cursor: pointer;
}

.popoverItem:hover {
  color: #165dff;
  background-color: #eee;
}
</style>

<style lang="scss">
.mobiledrawer {
  .el-drawer__body {
    padding: 0 !important;
    background-color: rgb(1 32 96);
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
