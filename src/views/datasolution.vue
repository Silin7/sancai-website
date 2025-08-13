<script setup lang="ts">
import backToTop from '@/hooks/backToTop'
import router from '@/router'
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

function pageJump() {
  backToTop()
  router.push({
    name: 'requirements',
  })
}
</script>

<template>
  <div>
    <div class="datasolutionPage">
      <!-- BANNER -->
      <div class="dsbannerBox">
        <img src="@/assets/solution-banner01.jpeg" alt="dsbanner" />
        <div class="dsbannerAbsolute">
          <div class="dsbannerContent">
            <div class="dsbannerTitle">为新城建提供绿色化 数字化 智能化综合解决方案</div>
            <!-- <div class="dsbannerSubtitle">
              信息技术深度赋能城市建设 有效应对并满足建设管理过程中多维度、多场景需求
            </div> -->
            <div class="frsc">
              <button class="dsbannerJgkbtn" @click="pageJump">提交需求</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 介绍区域  -->
      <div class="introdsOut">
        <div class="introdsBox">
          <p class="introdsText">
            新型城市基础设施建设（简称“新城建”），以人工智能（AI）、建筑信息模型（BIM）和物联网（IoT）等新一代信息技术深度融合城市建设应用，构建智能高效的新型城市基础设施体系。新城建通过对城市基础设施进行数字化、网络化和智能化的手段改造，推动城市高质量发展，提升城市治理水平。
          </p>
          <p class="introdsText">
            建设管理过程中的多维度、多场景基本需求，由需方提供《设计方案》或填写《询价需求表》（点击适用模块即可呈现），供方依此分析造价构成要素及组价（例如，软硬件使用费或购置费、数据建设费、系统开发及维护费、管理性费用和税赋等），并出具报价单。
          </p>
          <!-- <div class="introdsBtns">
            <button class="introdsBtn"><i class="fa fa-chdigitizen"></i>AI技术</button>
            <button class="introdsBtn"><i class="fa fa-header"></i>BIM建模</button>
            <button class="introdsBtn"><i class="fa fa-wifi"></i>IoT物联网</button>
          </div> -->
        </div>
      </div>
      <!-- 人工智能应用 -->
      <div class="digitizeOut">
        <div class="digitizeBox">
          <div class="digitizeSubBoxOut">
            <div class="digitizeSubBox">
              <div class="digitizeSubItem digitizeActive">数字化应用方案</div>
              <div class="digitizeSubItem">智慧化管理方案</div>
            </div>
          </div>
          <div class="digitizeClassbox">
            <div v-for="index in 9" :key="index" class="digitizeClassitem">
              <div class="digitizeClassitemfa frcc">
                <i class="fa fa-pencil"></i>
              </div>
              <div class="digitizeClassitemtext">智能化设计</div>
              <div class="digitizeClassiteminfo">基于BIM模型实现工程量精准计算与动态成本管控</div>
              <button @click="pageJump">提交需求</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 友情链接  -->
      <div class="gysBox">
        <div class="gysTitle">友情链接</div>
        <div class="gysHeng"></div>
        <div class="gysInfo">与行业领先企业及机构建立合作，共同推动建筑行业数字化转型</div>
        <div class="gysClassbox">
          <div class="gysClassitem">
            <img src="https://picsum.photos/100/100?random=402" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">建筑科技有限公司</div>
            <div class="gysClassiteminfo">专注建筑科技创新</div>
          </div>
          <div class="gysClassitem">
            <img src="https://picsum.photos/100/100?random=403" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">智能建造研究院</div>
            <div class="gysClassiteminfo">建筑智能化研究</div>
          </div>
          <div class="gysClassitem">
            <img src="https://picsum.photos/100/100?random=404" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">绿色建材协会</div>
            <div class="gysClassiteminfo">推广绿色建筑材料</div>
          </div>
          <div class="gysClassitem">
            <img src="https://picsum.photos/100/100?random=405" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">数字工程设计院</div>
            <div class="gysClassiteminfo">数字化工程设计</div>
          </div>
          <div class="gysClassitem">
            <img src="https://picsum.photos/100/100?random=406" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">智慧城市科技</div>
            <div class="gysClassiteminfo">智慧城市解决方案</div>
          </div>
          <div class="gysClassitem">
            <img src="https://picsum.photos/100/100?random=407" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">建筑信息研究院</div>
            <div class="gysClassiteminfo">建筑信息研究应用</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.datasolutionPage {
  background-color: #f9fafb;
  overflow-x: hidden;

  .dsbannerBox {
    position: relative;
    width: 100vw;
    height: 40rem;

    @media (max-width: 600px) {
      height: 30rem;
    }

    img {
      width: 100vw;
      height: 100%;
    }

    .dsbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;

      .dsbannerContent {
        margin: 0 auto;
        padding: 10rem 2rem 0;
        width: 100%;
        max-width: 1536px;

        @media (max-width: 600px) {
          padding: 6rem 1rem 0;
        }

        .dsbannerTitle {
          margin-bottom: 1.5rem;
          font-size: clamp(2rem, 4vw, 3rem);
          font-weight: 700;
          color: #fff;
        }

        .dsbannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }

        .dsbannerJgkbtn {
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgb(22 93 255);
          border-radius: 9999px;
          box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
        }

        .dsbannerJgkbtn:hover {
          transform: scale(1.05);
          box-shadow: 2px 2px 10px 0 rgb(22 93 255);
        }
      }
    }
  }

  .introdsOut {
    padding: 6rem 1rem;
    width: 100%;

    @media (max-width: 600px) {
      padding: 2rem 1rem;
    }

    .introdsBox {
      position: relative;
      margin: 0 auto;
      padding: 1rem;
      width: 100%;
      max-width: 1536px;
      background-color: #fff;
      box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
      border-radius: 1rem;

      .introdsText {
        font-size: clamp(1rem, 4vw, 1.25rem);
        line-height: 1.75rem;
        color: rgb(75 85 99);
      }

      // .introdsBtns {
      //   margin-top: 1rem;
      //   display: flex;
      //   flex-wrap: wrap;

      //   .introdsBtn {
      //     flex-shrink: 1;
      //     margin: 0 1rem 1rem 0;
      //     padding: 2.5rem;
      //     // padding: 0.5rem 1rem;
      //     line-height: 1.5rem;
      //     color: rgb(22 93 255);
      //     background-color: rgb(22 93 255 / 0.1);
      //     border-radius: 9999px;

      //     i {
      //       margin-right: 0.5rem;
      //     }
      //   }
      // }
    }
  }

  .digitizeOut {
    padding: 2.5rem 0 4rem;
    width: 100%;
    background-color: #f0f7ff;

    .digitizeBox {
      position: relative;
      margin: 0 auto;
      padding: 0 1rem;
      width: 100%;
      max-width: 1536px;

      .digitizeSubBoxOut {
        padding-bottom: 2rem;
        display: flex;
        justify-content: center;

        .digitizeSubBox {
          padding-bottom: 1rem;
          overflow-x: auto;
          display: flex;
          flex-wrap: nowrap;

          .digitizeSubItem {
            flex-shrink: 0;
            margin: 0 0.5rem;
            padding: 0.5rem 1rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            background-color: #fff;
            border-radius: 999px;

            @media (max-width: 600px) {
              margin: 0 0.25rem;
            }
          }

          .digitizeSubItem:first-child {
            margin-left: 0;
          }

          .digitizeSubItem:last-child {
            margin-right: 0;
          }

          .digitizeSubItem:hover {
            cursor: pointer;
            box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
            background-color: rgb(243 244 246);
          }
        }

        .digitizeActive {
          color: #fff !important;
          background-color: #165dff !important;
        }
      }

      .digitizeClassbox {
        // margin-bottom: 2.5rem;
        width: calc(100% + 1rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;

        @media (max-width: 600px) {
          width: 100%;
        }

        .digitizeClassitem {
          margin: 0 1rem 1rem 0;
          padding: 1.25rem;
          width: calc(33.3% - 1rem);
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: #fff;
          border-radius: 0.75rem;
          box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);

          @media (max-width: 600px) {
            width: 100%;
            margin: 0 0 1rem 0;
          }

          .digitizeClassitemfa {
            margin-bottom: 1rem;
            width: 4rem;
            height: 4rem;
            font-size: 1.5rem;
            line-height: 2rem;
            border-radius: 9999px;
            color: rgb(22 93 255);
            background-color: rgb(22 93 255 / 0.1);
          }

          .digitizeClassitemtext {
            margin-bottom: 0.5rem;
            font-size: 1.25rem;
            line-height: 1.75rem;
            font-weight: 700;
            color: rgb(1 32 96);
          }

          .digitizeClassiteminfo {
            text-align: center;
            margin-bottom: 1rem;
            line-height: 1.5rem;
            color: rgb(75 85 99);
          }

          button {
            padding: 0.5rem 1.5rem;
            line-height: 1.5rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border-radius: 0.5rem;
          }
        }

        .digitizeClassitem:hover {
          cursor: pointer;
          box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }
    }
  }

  .gysBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 2rem 4rem;
    width: 100%;
    max-width: 1536px;

    @media (max-width: 600px) {
      margin: 4rem auto 0;
      padding: 0 1rem 4rem;
    }

    .gysTitle {
      font-size: clamp(1.5rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .gysHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .gysInfo {
      margin: 1rem auto 2.5rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .gysClassbox {
      width: calc(100% + 1rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .gysClassitem {
        margin: 0 1rem 1rem 0;
        padding: 1.25rem 1rem;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        border-radius: 0.75rem;

        @media (min-width: 1140px) {
          width: calc(16.6% - 1rem);
        }

        @media (max-width: 1140px) and (min-width: 600px) {
          width: calc(33.3% - 1rem);
        }

        @media (max-width: 600px) {
          padding: 1rem 0.5rem;
          width: calc(50% - 1rem);
        }

        .gysClassitemfa1 {
          margin-bottom: 1rem;
          padding: 0.25rem;
          width: 5rem;
          height: 5rem;
          border-radius: 9999px;
          border: 2px solid rgb(22 93 255 / 0.2);
        }

        .gysClassitemfa {
          margin-bottom: 1rem;
          width: 5rem;
          height: 5rem;
          border-radius: 9999px;
          background-color: rgb(114 46 209 / 0.1);
        }

        .gysClassitemtext {
          line-height: 1.5rem;
          font-weight: 500;
          text-align: center;
          color: rgb(1 32 96);
        }

        .gysClassiteminfo {
          margin-top: 0.5rem;
          font-size: 0.875rem;
          line-height: 1.25rem;
          text-align: center;
          color: #6b7280;
        }
      }

      .gysClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }
}
</style>
