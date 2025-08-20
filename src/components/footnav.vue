<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { sysinfosApi } from '@/api/modules/basic'

const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

// 用户端-获取所有有效系统信息（如系统名称、版权信息等，按Key排序）
const sysInfos: any = ref({})

function getSysinfosApi() {
  sysinfosApi().then((res: any) => {
    if (res && res.length > 0) {
      console.log('-------->', res)
      for (let i = 0; i < res.length; i++) {
        const item = res[i]
        sysInfos.value[item.ky] = item.val
      }
      console.log('-------->', sysInfos.value)
    }
  })
}

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
    <div class="footTop">
      <el-row :gutter="20" style="padding-bottom: 32px; border-bottom: 1px solid #1a3670">
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" style="margin-top: 32px">
          <div class="frsc">
            <div class="culbbox">
              <i class="fa fa-cube" style="font-size: 16px; color: #165dff"></i>
            </div>
            <div class="titletext">新材网</div>
          </div>
          <div class="loinfo" :style="windowWidth > 428 ? 'max-width: 210px;' : ''">
            聚焦新型城市基础设施建设，提供专业的人材机信价格库与数字化解决方案，推动建筑行业绿色化、数字化、智能化发展。
          </div>
          <!-- <div class="frsc" style="margin-bottom: 16px">
            <div class="lxfsbbox">
              <i class="fa fa-weixin" style="font-size: 16px; color: #fff"></i>
            </div>
            <div class="lxfsbbox">
              <i class="fa fa-weibo" style="font-size: 16px; color: #fff"></i>
            </div>
            <div class="lxfsbbox">
              <i class="fa fa-linkedin" style="font-size: 16px; color: #fff"></i>
            </div>
          </div> -->
        </el-col>
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" style="margin-top: 32px">
          <div class="frsc">
            <div class="titleshu"></div>
            <div class="titletext">快速链接</div>
          </div>
          <div class="quickbox">
            <div class="quicklink">系统首页</div>
            <div class="quicklink">人材机信价格库</div>
            <div class="quicklink">数据方案组价</div>
            <div class="quicklink">AI赋能应用</div>
            <div class="quicklink">视频演示</div>
            <div class="quicklink">供应商</div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" style="margin-top: 32px">
          <div class="frsc">
            <div class="titleshu"></div>
            <div class="titletext">关于我们</div>
          </div>
          <div class="quickbox">
            <div class="quicklink">公司简介</div>
            <div class="quicklink">团队介绍</div>
            <div class="quicklink">合作伙伴</div>
            <div class="quicklink">加入我们</div>
            <div class="quicklink">联系我们</div>
            <div class="quicklink">隐私政策</div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6" :lg="6" :xl="6" style="margin-top: 32px">
          <div class="frsc">
            <div class="titleshu"></div>
            <div class="titletext">联系我们</div>
          </div>
          <div class="quickbox">
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-map-marker" style="font-size: 12px; color: #165dff"></i>
              </div>
              <div class="contacttext">浙江省杭州市XXXXXX</div>
            </div>
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-phone" style="font-size: 12px; color: #165dff"></i>
              </div>
              <div class="contacttext">400-123-4567</div>
            </div>
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-envelope" style="font-size: 12px; color: #165dff"></i>
              </div>
              <div class="contacttext">info@xincai.com</div>
            </div>
            <div class="contactUs frsc">
              <div class="contactbox">
                <i class="fa fa-clock-o" style="font-size: 12px; color: #165dff"></i>
              </div>
              <div class="contacttext">周一至周五 9:00-18:00</div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="footBottom">
      <div class="footInfo">© 2025 杭州三才工程信息科技有限公司. 保留所有权利.</div>
      <div class="footInfo">浙ICP备12345678号-1</div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.footnav {
  padding: 32px 32px 32px;
  background-color: #012060;

  .footTop {
    margin: 0 auto;
    max-width: 1536px;

    .culbbox {
      margin-right: 16px;
      width: 40px;
      height: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: rgb(22 93 255 / 0.1);
      border-radius: 8px;
    }

    .titletext {
      font-size: 1.25rem;
      color: #fff;
      font-weight: 700;
    }

    .loinfo {
      // max-width: 210px;
      margin: 24px 0;
      line-height: 24px;
      color: #9ca3af;
    }

    // .lxfsbbox {
    //   margin-right: 16px;
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

    .titleshu {
      margin-right: 12px;
      width: 4px;
      height: 16px;
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
      margin-bottom: 16px;

      .contactbox {
        margin-right: 12px;
        width: 24px;
        height: 24px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgb(22 93 255 / 0.1);
        border-radius: 24px;
      }

      .contacttext {
        line-height: 24px;
        color: #9ca3af;
      }
    }
  }

  .footBottom {
    padding-top: 32px;

    .footInfo {
      text-align: center;
      font-size: 16px;
      line-height: 24px;
      color: #9ca3af;
    }

    .footInfo:last-child {
      margin-top: 8px;
    }
  }
}
</style>
