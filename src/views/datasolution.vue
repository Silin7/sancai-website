<script setup lang="ts">
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
</script>

<template>
  <div>
    <div class="datasolutionPage">
      <!-- BANNER -->
      <div class="dsbannerBox">
        <div class="dsbannerImg">
          <img
            src="@/assets/solution-banner01.jpeg"
            alt="dsbanner"
            style="width: 100vw; height: 34rem"
          />
        </div>
        <div class="dsbannerAbsolute">
          <div class="dsbannerContent">
            <div class="dsbannerTitle">为新城建提供绿色化 数字化 智能化综合解决方案</div>
            <!-- <div class="dsbannerSubtitle">
              信息技术深度赋能城市建设 有效应对并满足建设管理过程中多维度、多场景需求
            </div> -->
            <div class="frsc">
              <button class="dsbannerJgkbtn">提交需求</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 介绍区域  -->
      <div class="introdsOut">
        <div class="introdsBox">
          <p class="introdsText">
            新型城市基础设施建设（简称"新城建"），以人工智能（AI）、建筑信息模型（BIM）和物联网（IoT）等新一代信息技术深度融合城市建设应用，构建智能高效的新型城市基础设施体系。
          </p>
          <p class="introdsText">
            新城建通过对城市基础设施进行数字化、网络化和智能化的手段改造，推动城市高质量发展，提升城市治理水平。
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
            <div
              v-for="index in 9"
              :key="index"
              class="digitizeClassitem"
              :style="
                windowWidth > 1000
                  ? 'width: calc(33.3% - 1.5rem)'
                  : windowWidth > 600
                    ? 'width: calc(50% - 1.5rem)'
                    : 'width: 100%'
              "
            >
              <div class="digitizeClassitemfa frcc">
                <i class="fa fa-pencil"></i>
              </div>
              <div class="digitizeClassitemtext">智能化设计</div>
              <div class="digitizeClassiteminfo">基于BIM模型实现工程量精准计算与动态成本管控</div>
              <button>提交需求</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 推荐供应商  -->
      <div class="gysBox">
        <div class="gysTitle">推荐供应商</div>
        <div class="gysHeng"></div>
        <div class="gysInfo">与行业领先企业及机构建立合作，共同推动建筑行业数字化转型</div>
        <div class="gysClassbox">
          <div
            class="gysClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=402" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">建筑科技有限公司</div>
            <div class="gysClassiteminfo">专注建筑科技创新</div>
          </div>
          <div
            class="gysClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=403" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">智能建造研究院</div>
            <div class="gysClassiteminfo">建筑智能化研究</div>
          </div>
          <div
            class="gysClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=404" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">绿色建材协会</div>
            <div class="gysClassiteminfo">推广绿色建筑材料</div>
          </div>
          <div
            class="gysClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=405" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">数字工程设计院</div>
            <div class="gysClassiteminfo">数字化工程设计</div>
          </div>
          <div
            class="gysClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=406" alt="" class="gysClassitemfa" />
            <div class="gysClassitemtext">智慧城市科技</div>
            <div class="gysClassiteminfo">智慧城市解决方案</div>
          </div>
          <div
            class="gysClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
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

  .dsbannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .dsbannerImg {
      width: 100vw;
      height: 34rem;
      background-color: #012060;
    }

    .dsbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .dsbannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1536px;

        .dsbannerTitle {
          margin-bottom: 1.5rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
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
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        }

        .dsbannerJgkbtn:hover {
          transform: scale(1.05);
          box-shadow: 2px 2px 10px 0 rgb(22 93 255);
        }
      }
    }
  }

  .introdsOut {
    margin-top: 2.5rem;
    padding: 0 1rem;
    width: 100%;

    .introdsBox {
      position: relative;
      margin: 0 auto;
      padding: 2.5rem;
      width: 100%;
      max-width: 1536px;
      background-color: #fff;
      box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
      border-radius: 1rem;

      .introdsText {
        margin-bottom: 1rem;
        font-size: 1.125rem;
        line-height: 1.75rem;
        color: rgb(75 85 99);
      }

      .introdsBtns {
        margin-top: 1rem;
        display: flex;
        flex-wrap: wrap;

        .introdsBtn {
          flex-shrink: 1;
          margin: 0 1rem 1rem 0;
          padding: 0.5rem 1rem;
          line-height: 1.5rem;
          color: rgb(22 93 255);
          background-color: rgb(22 93 255 / 0.1);
          border-radius: 9999px;

          i {
            margin-right: 0.5rem;
          }
        }
      }
    }
  }

  .digitizeOut {
    margin-top: 2.5rem;
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
            margin: 0 0.75rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            padding: 0.5rem 1.25rem;
            border-radius: 999px;
            background-color: #fff;
          }

          .digitizeSubItem:hover {
            cursor: pointer;
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            background-color: rgb(243 244 246);
          }
        }

        .digitizeSubBox2 {
          padding-bottom: 1rem;
          overflow-x: auto;
          display: flex;
          flex-wrap: nowrap;

          .digitizeSubItem {
            flex-shrink: 0;
            margin: 0 0.75rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            padding: 0.5rem 1.25rem;
            border-radius: 0.5rem;
            background-color: #fff;
          }

          .digitizeSubItem:hover {
            cursor: pointer;
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            background-color: rgb(243 244 246);
          }
        }

        .digitizeActive {
          color: #fff !important;
          background-color: #165dff !important;
        }
      }

      .digitizeClassbox {
        margin-bottom: 2.5rem;
        width: calc(100% + 1.5rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;

        .digitizeClassitem {
          margin: 0 1.5rem 1.5rem 0;
          padding: 1.25rem;
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: #fff;
          // background-color: rgb(249 250 251);
          border-radius: 0.75rem;

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
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }
    }
  }

  .gysBox {
    position: relative;
    margin: 4rem auto 0;
    padding: 0 1rem 4rem;
    width: 100%;
    max-width: 1536px;

    .gysTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
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
      margin: 1rem auto 4rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .gysClassbox {
      width: calc(100% + 1.5rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .gysClassitem {
        margin: 0 1.5rem 1.5rem 0;
        padding: 1.25rem;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        // background-color: rgb(249 250 251);
        border-radius: 0.75rem;

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
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }
}
</style>
