<script setup lang="ts">
import dayjs from 'dayjs'
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import pageJump from '@/hooks/pageJump'
import { fileURL } from '@/api/baseConfig'
import { aialdetailsApi } from '@/api/modules/ai'
import { sysinfosApi } from '@/api/modules/basic'

// 路由信息
const route = useRoute()

// 可视窗口宽度
const windowWidth = ref(window.innerWidth)

function uaipdateWindowWidth() {
  windowWidth.value = window.innerWidth
}

// 案例详情
const aixqid: any = ref('')
const aialdetail: any = ref({})

function getAialdetail() {
  aialdetailsApi(aixqid.value).then((res: any) => {
    aialdetail.value = res
    if (aialdetail.value.tags) {
      aialdetail.value.tags = aialdetail.value.tags.split(',')
    } else {
      aialdetail.value.tags = []
    }
  })
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

// // 用户端-获取最新6条推荐案例（公开接口）
// const aialRecommended: any = ref([])

// function getAialrecommended() {
//   aialrecommendedApi().then((res: any) => {
//     if (res) {
//       aialRecommended.value = res
//     }
//   })
// }

onMounted(() => {
  window.addEventListener('resize', uaipdateWindowWidth)
  aixqid.value = route.query.aixqid
  getAialdetail()
  getSysinfosApi()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', uaipdateWindowWidth)
})
</script>

<template>
  <div class="aidPage">
    <div class="aidHbox">
      <div class="aidHcontent">
        <div class="aidNavigation">
          <span @click="pageJump('home')">首页</span>
          <span class="aidNavigationXg">/</span>
          <span @click="pageJump('ai')">AI赋能应用</span>
          <span class="aidNavigationXg">/</span>
          <!-- <span class="aidNavigationSp">{{ aialdetail.title }}</span> -->
          <span class="aidNavigationSp">AI辅助设计工具</span>
        </div>
      </div>
    </div>
    <div class="aidCbox">
      <div class="adicTopOut">
        <div class="adicTop">
          <div class="adictTitle">AI辅助设计工具</div>
          <!-- <div class="adictTitle">{{ aialdetail.title }}</div> -->
          <div class="adictTags">
            <!-- <span v-for="(item, index) in aialdetail.tags" :key="index" class="adictTag adictTag1">{{ item }}</span>
          <span class="adictTag adictTag2">
            {{ dayjs(aialdetail.created_at).format('YYYY年MM月') }}
          </span> -->
            <span class="adictTag adictTag1">AI设计</span>
            <span class="adictTag adictTag2">智能建模</span>
            <span class="adictTag adictTag3">效率提升</span>
          </div>
        </div>
        <button>联系我们</button>
      </div>
      <div class="adicCpjj">
        <div class="adicCpjjLeft">
          <div class="adicCpjjLeftTitle">产品简介</div>
          <div class="adicCpjjLeftInfo">
            AI辅助设计工具是基于深度学习和计算机视觉技术开发的智能化设计辅助系统，专为建筑、土木工程等领域打造。
            <br>
            <br>
            该工具整合了海量建筑设计数据和工程规范，能够自动识别设计需求、生成初步方案、优化设计细节，帮助设计师大幅提升工作效率，降低设计误差，实现设计过程的智能化升级。
          </div>
        </div>
        <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" alt="" class="caseClassitemfa" />
      </div>
      <div class="adicHxgn">
        <div class="adicHxgnTitle">核心功能</div>
        <div class="adicHxgnItem">
          <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
          <div class="">
            <div class="">智能方案生成</div>
            <div class="">根据用户输入的设计需求和约束条件，自动生成多个优化设计方案供选择。</div>
          </div>
        </div>
        <div class="adicHxgnItem">
          <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
          <div class="">
            <div class="">参数化建模</div>
            <div class="">实时对照最新行业规范和标准，自动识别设计违规点并给出优化建议。</div>
          </div>
        </div>
        <div class="adicHxgnItem">
          <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
          <div class="">
            <div class="">设计规范检查</div>
            <div class="">实时对照最新行业规范和标准，自动识别设计违规点并给出优化建议。</div>
          </div>
        </div>
        <div class="adicHxgnItem">
          <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
          <div class="">
            <div class="">性能优化分析</div>
            <div class="">自动进行结构性能、能耗、采光等多维度分析，提供优化方向和解决方案。</div>
          </div>
        </div>
        <div class="adicHxgnItem">
          <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
          <div class="">
            <div class="">多格式导出</div>
            <div class="">支持导出CAD、BIM、PDF等多种格式文件，无缝对接后续设计和施工流程。</div>
          </div>
        </div>
        <div class="adicHxgnItem">
          <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
          <div class="">
            <div class="">自然语言交互</div>
            <div class="">支持通过自然语言描述设计需求，AI自动理解并转化为设计参数和方案。</div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="">适用场景</div>
        <div class="">
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">建筑方案设计</div>
            <div class="">住宅、商业、办公等各类建筑的概念设计和方案设计阶段。</div>
          </div>
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">市政工程设计</div>
            <div class="">道路、桥梁、管网等市政基础设施的设计和优化。</div>
          </div>
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">室内装修设计</div>
            <div class="">住宅、商业空间等室内装修方案设计和施工图生成。</div>
          </div>
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">城市规划设计</div>
            <div class="">片区规划、控制性详细规划等城市规划设计工作。</div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="">技术优势</div>
        <div class="">
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">深度学习算法</div>
            <div class="">基于海量设计数据训练的深度学习模型，具备强大的设计理解和生成能力。</div>
          </div>
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">海量数据支撑</div>
            <div class="">整合了10万+优质设计案例和最新行业规范，确保设计方案的专业性和合规性。</div>
          </div>
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">无缝集成能力</div>
            <div class="">可与主流设计软件无缝集成，不改变现有工作流程，降低学习和使用成本。</div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="">联系我们</div>
        <div class="">如需了解更多AI辅助设计工具的详细信息，或预约产品演示，欢迎通过以下方式联系我们，专业顾问将为您提供一对一服务。</div>
        <div class="">
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">咨询热线</div>
            <div class="">400-123-4567</div>
            <div class="">周一至周五 9:00-18:00</div>
          </div>
          <div class="">
            <i class="fa fa-weibo" style="font-size: 1rem; color: #fff"></i>
            <div class="">咨询邮箱</div>
            <div class="">ai_design@xincai.com</div>
            <div class="">24小时内回复邮件咨询</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.aidPage {
  overflow-x: hidden;
  min-height: calc(100vh - 120px);
  background-color: #f9fafb;

  .aidHbox {
    .aidHcontent {
      margin: 0 auto;
      padding: 6rem 2rem 1rem;
      width: 100%;
      max-width: 1536px;
      color: rgb(1 32 96);

      @media (max-width: 992px) {
        padding: 5rem 1rem 1rem;
      }

      .aidNavigation {
        margin: 0 auto;

        span {
          font-size: 0.875rem;
          line-height: 1.25rem;
          color: rgb(107 114 128);
        }

        span:hover {
          @media (min-width: 768px) {
            cursor: pointer;
            color: rgb(22 93 255);
          }
        }

        .aidNavigationXg {
          margin: 0 0.5rem;
        }

        .aidNavigationSp {
          color: rgb(22 93 255);
        }
      }
    }
  }

  .aidCbox {
    position: relative;
    margin: 0 auto;
    padding: 1rem 2rem;
    width: 100%;
    max-width: 1536px;
    color: rgb(1 32 96);

    @media (max-width: 768px) {
      padding: 0 1rem 1rem;
    }

    .adicTopOut {
      display: flex;
      justify-content: space-between;
      align-items: center;

      @media (max-width: 768px) {
        padding: 1rem 0;
      }

      .adicTop {
        width: calc(100% - 160px);

        @media (max-width: 768px) {
          width: 100%;
        }

        .adictTitle {
          margin-bottom: 1rem;
          font-size: 1.875rem;
          font-weight: 700;
          color: rgb(1 32 96);
        }

        .adictTags {
          // margin-bottom: 1rem;
          display: flex;
          flex-wrap: wrap;

          .adictTag {
            margin: 0 1rem 0.5rem 0;
            padding: 0.25rem 0.75rem;
            font-weight: 500;
            font-size: 0.875rem;
            line-height: 1.25rem;
            border-radius: 9999px;

            @media (max-width: 768px) {
              margin: 0 0.5rem 0.5rem 0;
            }
          }

          .adictTag1 {
            color: rgb(22 93 255);
            background-color: rgb(22 93 255 / 0.1);
          }

          .adictTag2 {
            color: rgb(54 207 201);
            background-color: rgb(54 207 201 / 0.1);
          }

          .adictTag3 {
            color: rgb(114 46 209);
            background-color: rgb(114 46 209 / 0.1);
          }
        }

        .adictImgs {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;

          img {
            margin-bottom: 1rem;
            width: calc(50% - 1rem);
            height: 20rem;
            border-radius: 0.75rem;

            @media (max-width: 768px) {
              width: 100%;
            }
          }

          img:last-child {
            margin-bottom: 0;
          }
        }
      }

      button {
        color: #fff;
        padding-top: 0.75rem;
        padding-bottom: 0.75rem;
        padding-left: 2rem;
        padding-right: 2rem;
        font-size: 1.125rem;
        line-height: 1.75rem;
        background-color: rgb(22 93 255 / 0.9);
        border-radius: 9999px;
      }

      button:hover {
        @media (min-width: 768px) {
          cursor: pointer;
          box-shadow: 0 10px 15px -3px rgb(22 93 255 / 0.1), 0 4px 6px -4px rgb(22 93 255 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }
    }

    .adicCpjj {
      margin-top: 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;

      .adicCpjjLeft {
        width: calc(100% - 480px);

        .adicCpjjLeftTitle {
          color: rgb(1 32 96);
          font-weight: 700;
          font-size: 1.5rem;
          line-height: 2rem;
          margin-bottom: 1.5rem;
        }

        .adicCpjjLeftInfo {
          margin-bottom: 1rem;
          font-size: 1.125rem;
          line-height: 1.725;
          color: rgb(75 85 99);
        }
      }

      img {
        width: 460px;
        height: 280px;
        border-radius: 0.75rem;
      }
    }

    .adicHxgn {
      margin-top: 2rem;
      padding: 2rem;
      border-radius: 1rem;
      -tw-bg-opacity: 1;
      background-color: rgb(240 247 255);

      @media (max-width: 768px) {
        padding: 1rem;
      }

      .adicHxgnTitle {
        text-align: center;
        color: rgb(1 32 96);
        font-weight: 700;
        font-size: 1.5rem;
        line-height: 2rem;
        margin-bottom: 1.5rem;
      }

      .adicHxgnItem {
        border: 1px solid red;
      }
    }
  }
}
</style>
