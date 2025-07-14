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
    <div class="aiPage">
      <!-- aibanner -->
      <div class="aibannerBox">
        <img
          src="@/assets/solution-banner01.jpeg"
          alt="aibanner"
          style="width: 100vw; height: 40rem"
        />
        <div class="aibannerAbsolute">
          <div class="aibannerContent">
            <div class="aibannerTitle">AI赋能建筑业 开启智能建造新时代</div>
            <div class="aibannerSubtitle">
              人工智能驱动工程设计、施工与运维创新，为建筑业注入全新动能
            </div>
            <div class="frsc">
              <button class="aibannerJgkbtn">搜索AI应用</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 介绍区域  -->
      <div class="introaiOut">
        <div class="introaiBox" :style="windowWidth <= 600 ? 'padding: 1rem;' : ''">
          <p class="introaiText">
            新型城市基础设施建设（简称"新城建"随着新一轮科技革命和产业变革深入发展，人工智能技术突飞猛进，已成为提升产业能级的重要引擎。目前，以DeepSeeK为代表的国产大模型正在快速发展与商业应用，人工智能将逐步渗透到各个行业。
          </p>
          <p class="introaiText">
            新城建通过对城市基础设施进行建筑业探索应用也将是必由之路，以数据、算法和算力为核心要素，驱动工程设计、工程施工和运营维护多维度创新应用，可实现优化资源配置、提升生产效率和创新组织管理新范式，为产业转型发展注入新动能。数字化、网络化和智能化的手段改造，推动城市高质量发展，提升城市治理水平。
          </p>
          <div class="introaiBtns">
            <button class="introaiBtn"><i class="fa fa-database"></i>数据驱动</button>
            <button class="introaiBtn"><i class="fa fa-cogs"></i>算法优化</button>
            <button class="introaiBtn"><i class="fa fa-microchip"></i>算力支撑</button>
            <button class="introaiBtn"><i class="fa fa-wifi"></i>智能决策</button>
          </div>
        </div>
      </div>
      <!-- 人工智能应用 -->
      <div class="applicationOut">
        <div class="applicationBox">
          <div class="applicationTitle">工程管理AI应用组价</div>
          <div class="applicationHeng"></div>
          <div class="applicationInfo">
            人工智能深度融入工程管理全流程，提升效率、降低成本、优化决策
          </div>
          <div class="applicationClassbox">
            <div
              v-for="index in 9"
              :key="index"
              class="applicationClassitem"
              :style="
                windowWidth > 1000
                  ? 'width: calc(33.3% - 1.5rem)'
                  : windowWidth > 600
                    ? 'width: calc(50% - 1.5rem)'
                    : 'width: 100%'
              "
            >
              <div class="applicationClassitemfa frcc">
                <i class="fa fa-pencil"></i>
              </div>
              <div class="applicationClassitemtext">智能化设计</div>
              <div class="applicationClassiteminfo">
                基于BIM模型实现工程量精准计算与动态成本管控
              </div>
              <button>提交需求</button>
            </div>
          </div>
        </div>
        <div class="applicationBox">
          <div class="applicationTitle">工程造价AI应用服务</div>
          <div class="applicationHeng"></div>
          <div class="applicationInfo">
            人工智能赋能造价管理全流程，提高精度、减少误差、优化决策
          </div>
          <div class="applicationClassbox">
            <div
              v-for="index in 4"
              :key="index"
              class="applicationClassitem"
              :style="
                windowWidth > 1000
                  ? 'width: calc(33.3% - 1.5rem)'
                  : windowWidth > 600
                    ? 'width: calc(50% - 1.5rem)'
                    : 'width: 100%'
              "
            >
              <div class="applicationClassitemfa frcc">
                <i class="fa fa-pencil"></i>
              </div>
              <div class="applicationClassitemtext">智能复核文本</div>
              <div class="applicationClassiteminfo">AI自动复核工程文本，减少人为错误</div>
              <button>立即体验</button>
            </div>
          </div>
        </div>
      </div>
      <!-- AI应用成功案例  -->
      <div class="caseBox">
        <div class="caseTitle">AI应用成功案例</div>
        <div class="caseHeng"></div>
        <div class="caseInfo">探索建筑业AI应用的实际效果与价值</div>
        <div class="caseClassbox">
          <div
            v-for="index in 3"
            :key="index"
            class="caseClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(33.3% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(50% - 1.5rem);'
                  : 'width: 100%'
            "
          >
            <img src="https://picsum.photos/100/100?random=401" alt="" class="caseClassitemfa" />
            <div class="caseClassitembox">
              <div class="caseClassitemFrsc">
                <div class="caseClassitemZnsj">智能设计</div>
                <div class="caseClassitemSpan">2024年5月</div>
              </div>
              <div class="caseClassitemtext">杭州某商业综合体AI优化设计</div>
              <div class="caseClassiteminfo">
                应用AI辅助设计工具，优化建筑结构，节省材料成本12%，缩短设计周期30%
              </div>
              <div class="frsc">
                <button class="caseClassitembtn">查看详情<i class="fa fa-arrow-right"></i></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.aiPage {
  background-color: #f9fafb;

  .aibannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .aibannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .aibannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1720px;

        .aibannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .aibannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }

        .aibannerJgkbtn {
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgb(22 93 255);
          border-radius: 9999px;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        }
      }
    }
  }

  .introaiOut {
    margin-top: 6rem;
    padding: 0 1rem;
    width: 100%;

    .introaiBox {
      position: relative;
      margin: 0 auto;
      padding: 2rem;
      width: 100%;
      max-width: 1720px;
      background-color: #fff;
      box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
      border-radius: 1rem;

      .introaiText {
        margin-bottom: 1rem;
        font-size: 1.125rem;
        line-height: 1.75rem;
        color: rgb(75 85 99);
      }

      .introaiBtns {
        margin-top: 2rem;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;

        .introaiBtn {
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

  .applicationOut {
    margin-top: 6rem;
    width: 100%;
    background-color: #f0f7ff;

    .applicationBox {
      position: relative;
      margin: 0 auto;
      padding: 4rem 1rem;
      width: 100%;
      max-width: 1720px;

      .applicationTitle {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 700;
        text-align: center;
        color: rgb(1 32 96);
      }

      .applicationHeng {
        margin: 1rem auto 0;
        width: 5rem;
        height: 0.25rem;
        border-radius: 9999px;
        background-color: rgb(22 93 255);
      }

      .applicationInfo {
        margin: 1rem auto 4rem;
        text-align: center;
        max-width: 42rem;
        color: rgb(75 85 99);
      }

      .applicationClassbox {
        width: calc(100% + 1.5rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;

        .applicationClassitem {
          margin: 0 1.5rem 1.5rem 0;
          padding: 1.5rem 1.25rem;
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: #fff;
          // background-color: rgb(249 250 251);
          border-radius: 0.75rem;

          .applicationClassitemfa {
            margin-bottom: 1rem;
            width: 4rem;
            height: 4rem;
            font-size: 1.5rem;
            line-height: 2rem;
            border-radius: 0.75rem;
            color: #fff;
            background-image: linear-gradient(to bottom right, #60a5fa, #4f46e5);
          }

          .applicationClassitemtext {
            margin-bottom: 0.5rem;
            font-size: 1.25rem;
            line-height: 1.75rem;
            font-weight: 700;
            color: rgb(1 32 96);
          }

          .applicationClassiteminfo {
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

        .applicationClassitem:hover {
          cursor: pointer;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }
    }
  }

  .caseBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 1rem 4rem;
    width: 100%;
    max-width: 1720px;

    .caseTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .caseHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .caseInfo {
      margin: 1rem auto 4rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .caseClassbox {
      width: calc(100% + 1.5rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .caseClassitem {
        overflow: hidden;
        margin: 0 1.5rem 1.5rem 0;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        // background-color: rgb(249 250 251);
        border-radius: 0.75rem;

        .caseClassitemfa {
          width: 100%;
          height: 12rem;
        }

        .caseClassitembox {
          width: 100%;
          padding: 1.5rem;

          .caseClassitemFrsc {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            margin-bottom: 1rem;

            .caseClassitemZnsj {
              padding: 0.25rem 0.75rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              font-weight: 500;
              color: rgb(22 93 255);
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 9999px;
            }

            .caseClassitemSpan {
              margin-left: 1rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: rgb(107 114 128);
            }
          }

          .caseClassitemtext {
            margin-bottom: 0.75rem;
            font-size: 1.25rem;
            line-height: 1.75rem;
            font-weight: 700;
            color: rgb(1 32 96);
          }

          .caseClassiteminfo {
            margin-bottom: 1rem;
            line-height: 1.5rem;
            color: rgb(75 85 99);
          }

          .caseClassitembtn {
            font-weight: 500;
            line-height: 1.5rem;
            color: rgb(22 93 255);

            i {
              margin-left: 0.5rem;
            }
          }
        }
      }

      .caseClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }
}
</style>
