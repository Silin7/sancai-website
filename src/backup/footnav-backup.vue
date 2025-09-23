<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import pageJump from '@/hooks/pageJump'
import useHeaderStore from '@/store/modules/header'
import { sysinfosApi } from '@/api/modules/basic'

// 可视窗口宽度
const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

// 用户端-获取所有有效系统信息（如系统名称、版权信息等，按Key排序）
const sysInfos: any = ref({})

function getSysinfosApi() {
  sysinfosApi().then((res: any) => {
    if (res && res.length > 0) {
      for (let i = 0; i < res.length; i++) {
        const item = res[i]
        sysInfos.value[item.ky] = item.val
      }
    }
  })
}

const headerStore = useHeaderStore()

const selectedTab = computed(() => {
  return headerStore.selectedTab
})

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
  getSysinfosApi()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
})
</script>

<template>
  <div class="footnav">
    <div v-if="selectedTab === 'home'" class="footTop">
      <el-row :gutter="20" class="footRow">
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" class="footCol">
          <div class="frsc">
            <div class="culbbox">
              <i class="fa fa-cube"></i>
            </div>
            <div class="titletext">{{ sysInfos.sys_name }}</div>
          </div>
          <div class="loinfo">
            {{ sysInfos.sys_description }}
          </div>
          <!-- <div class="frsc" style="margin-bottom: 1rem">
            <div class="lxfsbbox">
              <i class="fa fa-weixin" style="font-size: 1rem; color: #fff"></i>
            </div>
            <div class="lxfsbbox">
              <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            </div>
            <div class="lxfsbbox">
              <i class="fa fa-linkedin" style="font-size: 1rem; color: #fff"></i>
            </div>
          </div> -->
        </el-col>
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" class="footCol">
          <div class="frsc">
            <div class="titleshu"></div>
            <div class="titletext">快速链接</div>
          </div>
          <div class="quickbox">
            <div class="quicklink" @click="pageJump('home')">系统首页</div>
            <div class="quicklink" @click="pageJump('scheme')">人材机信价格库</div>
            <div class="quicklink" @click="pageJump('datasolution')">数据方案组价</div>
            <div class="quicklink" @click="pageJump('ai')">AI赋能应用</div>
            <div class="quicklink" @click="pageJump('video')">视频演示</div>
            <div class="quicklink" @click="pageJump('supplier')">供应商</div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" class="footCol">
          <div class="frsc">
            <div class="titleshu"></div>
            <div class="titletext">关于我们</div>
          </div>
          <div class="quickbox">
            <!-- IN DOUBT -->
            <div class="quicklink" @click="pageJump('about')">公司简介</div>
            <div class="quicklink" @click="pageJump('about')">团队介绍</div>
            <div class="quicklink" @click="pageJump('about')">合作伙伴</div>
            <div class="quicklink" @click="pageJump('about')">加入我们</div>
            <div class="quicklink" @click="pageJump('about')">联系我们</div>
            <div class="quicklink" @click="pageJump('about')">隐私政策</div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" class="footCol">
          <div class="frsc">
            <div class="titleshu"></div>
            <div class="titletext">联系我们</div>
          </div>
          <div class="quickbox">
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-map-marker"></i>
              </div>
              <div class="contacttext">{{ sysInfos.sys_address }}</div>
            </div>
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-phone"></i>
              </div>
              <div class="contacttext">{{ sysInfos.sys_tel }}</div>
            </div>
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-envelope"></i>
              </div>
              <div class="contacttext">{{ sysInfos.sys_email }}</div>
            </div>
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-clock-o"></i>
              </div>
              <div class="contacttext">{{ sysInfos.sys_worktime }}</div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="footBottom">
      <div class="footInfo">{{ sysInfos.sys_company }}</div>
      <div class="footInfo">{{ sysInfos.sys_filing }}</div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.footnav {
  padding: 2rem 2rem;
  background-color: #012060;

  .footTop {
    margin: 0 auto 2rem;
    max-width: 1536px;

    .footRow {
      padding-bottom: 2rem;
      border-bottom: 1px solid #1a3670;

      .footCol {
        margin-top: 2rem;

        .culbbox {
          margin-right: 1rem;
          width: 40px;
          height: 40px;
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: rgb(22 93 255 / 0.1);
          border-radius: 8px;

          i {
            font-size: 1rem;
            color: #165dff
          }
        }

        .titletext {
          font-size: 1.25rem;
          color: #fff;
          font-weight: 700;
        }

        .loinfo {
          margin: 24px 0;
          line-height: 24px;
          color: #9ca3af;

          @media (min-width: 768px) {
            max-width: 210px;
          }
        }

        .titleshu {
          margin-right: 12px;
          width: 4px;
          height: 1rem;
          background-color: #165dff;
        }

        .quickbox {
          margin: 24px 0 0;

          .quicklink {
            margin-bottom: 12px;
            line-height: 24px;
            color: #9ca3af;
          }

          .quicklink:hover {
            @media (min-width:768px) {
              cursor: pointer;
              color: #165dff;
            }
          }
        }

        .contactUs {
          margin-bottom: 1rem;

          .contactbox {
            margin-right: 12px;
            width: 24px;
            height: 24px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: rgb(22 93 255 / 0.1);
            border-radius: 24px;

            i {
              font-size: 0.875rem;
              color: #165dff;
            }
          }

          .contacttext {
            line-height: 24px;
            color: #9ca3af;
          }
        }
      }
    }

    // .lxfsbbox {
    //   margin-right: 1rem;
    //   width: 40px;
    //   height: 40px;
    //   display: flex;
    //   justify-content: center;
    //   align-items: center;
    //   background-color: rgb(255 255 255 / 0.1);
    //   border-radius: 40px;
    // }

    // .lxfsbbox:hover {
    //   cursor: pointer;
    //   background-color: #165dff;
    // }
  }

  .footBottom {

    .footInfo {
      text-align: center;
      font-size: 1rem;
      line-height: 24px;
      color: #9ca3af;
    }

    .footInfo:last-child {
      margin-top: 8px;
    }
  }
}
</style>
