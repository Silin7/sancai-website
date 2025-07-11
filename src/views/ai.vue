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
      <div class="bannerBox">
        <img
          src="@/assets/solution-banner01.jpeg"
          alt="banner"
          style="width: 100vw; height: 40rem"
        />
        <div class="bannerAbsolute">
          <div class="bannerContent">
            <div class="bannerTitle">AI赋能建筑业 开启智能建造新时代</div>
            <div class="bannerSubtitle">
              人工智能驱动工程设计、施工与运维创新，为建筑业注入全新动能
            </div>
            <div class="frsc">
              <button class="bannerJgkbtn">搜索AI应用</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 介绍区域  -->
      <div class="introOut">
        <div class="introBox">
          <p class="introText">
            新型城市基础设施建设（简称"新城建"随着新一轮科技革命和产业变革深入发展，人工智能技术突飞猛进，已成为提升产业能级的重要引擎。目前，以DeepSeeK为代表的国产大模型正在快速发展与商业应用，人工智能将逐步渗透到各个行业。
          </p>
          <p class="introText">
            新城建通过对城市基础设施进行建筑业探索应用也将是必由之路，以数据、算法和算力为核心要素，驱动工程设计、工程施工和运营维护多维度创新应用，可实现优化资源配置、提升生产效率和创新组织管理新范式，为产业转型发展注入新动能。数字化、网络化和智能化的手段改造，推动城市高质量发展，提升城市治理水平。
          </p>
          <div class="introBtns">
            <button class="introBtn"><i class="fa fa-database"></i>数据驱动</button>
            <button class="introBtn"><i class="fa fa-cogs"></i>算法优化</button>
            <button class="introBtn"><i class="fa fa-microchip"></i>算力支撑</button>
            <button class="introBtn"><i class="fa fa-wifi"></i>智能决策</button>
          </div>
        </div>
      </div>
      <!-- 人工智能应用 -->
      <div class="aiOut">
        <div class="aiBox">
          <div class="aiTitle">工程管理AI应用组价</div>
          <div class="aiHeng"></div>
          <div class="aiInfo">人工智能深度融入工程管理全流程，提升效率、降低成本、优化决策</div>
          <div class="aiClassbox">
            <div
              v-for="index in 9"
              :key="index"
              class="aiClassitem"
              :style="
                windowWidth > 1000
                  ? 'width: calc(33.3% - 1.5rem)'
                  : windowWidth > 600
                    ? 'width: calc(50% - 1.5rem)'
                    : 'width: 100%'
              "
            >
              <div class="aiClassitemfa frcc">
                <i class="fa fa-pencil"></i>
              </div>
              <div class="aiClassitemtext">智能化设计</div>
              <div class="aiClassiteminfo">基于BIM模型实现工程量精准计算与动态成本管控</div>
              <button>提交需求</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 推荐供应商  -->
      <div class="pyBox">
        <div class="pyTitle">推荐供应商</div>
        <div class="pyHeng"></div>
        <div class="pyInfo">与行业领先企业及机构建立合作，共同推动建筑行业数字化转型</div>
        <div class="pyClassbox">
          <div
            class="pyClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=402" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">建筑科技有限公司</div>
            <div class="pyClassiteminfo">专注建筑科技创新</div>
          </div>
          <div
            class="pyClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=403" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">智能建造研究院</div>
            <div class="pyClassiteminfo">建筑智能化研究</div>
          </div>
          <div
            class="pyClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=404" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">绿色建材协会</div>
            <div class="pyClassiteminfo">推广绿色建筑材料</div>
          </div>
          <div
            class="pyClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=405" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">数字工程设计院</div>
            <div class="pyClassiteminfo">数字化工程设计</div>
          </div>
          <div
            class="pyClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=406" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">智慧城市科技</div>
            <div class="pyClassiteminfo">智慧城市解决方案</div>
          </div>
          <div
            class="pyClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(16.6% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <img src="https://picsum.photos/100/100?random=407" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">建筑信息研究院</div>
            <div class="pyClassiteminfo">建筑信息研究应用</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.datasolutionPage {
  background-color: #f9fafb;

  .bannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .bannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .bannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1720px;

        .bannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .bannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }

        .bannerJgkbtn {
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgb(22 93 255);
          border-radius: 9999px;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        }
      }
    }
  }

  .introOut {
    margin-top: 6rem;
    padding: 0 1rem;
    width: 100%;

    .introBox {
      position: relative;
      margin: 0 auto;
      padding: 2.5rem;
      width: 100%;
      max-width: 1720px;
      background-color: #fff;
      box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
      border-radius: 1rem;

      .introText {
        margin-bottom: 1rem;
        font-size: 1.125rem;
        line-height: 1.75rem;
        color: rgb(75 85 99);
      }

      .introBtns {
        margin-top: 1rem;
        display: flex;
        flex-wrap: wrap;

        .introBtn {
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

  .aiOut {
    margin-top: 6rem;
    padding: 5rem 0 4rem;
    width: 100%;
    background-color: #f0f7ff;

    .aiBox {
      position: relative;
      margin: 0 auto;
      padding: 0 1rem;
      width: 100%;
      max-width: 1720px;

      .aiTitle {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 700;
        text-align: center;
        color: rgb(1 32 96);
      }

      .aiHeng {
        margin: 1rem auto 0;
        width: 5rem;
        height: 0.25rem;
        border-radius: 9999px;
        background-color: rgb(22 93 255);
      }

      .aiInfo {
        margin: 1rem auto 4rem;
        text-align: center;
        max-width: 42rem;
        color: rgb(75 85 99);
      }

      .aiClassbox {
        margin-bottom: 2.5rem;
        width: calc(100% + 1.5rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;

        .aiClassitem {
          margin: 0 1.5rem 1.5rem 0;
          padding: 1.25rem;
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: #fff;
          // background-color: rgb(249 250 251);
          border-radius: 0.75rem;

          .aiClassitemfa {
            margin-bottom: 1rem;
            width: 4rem;
            height: 4rem;
            font-size: 1.5rem;
            line-height: 2rem;
            border-radius: 0.75rem;
            color: #fff;
            background-image: linear-gradient(to bottom right, #60a5fa, #4f46e5);
          }

          .aiClassitemtext {
            margin-bottom: 0.5rem;
            font-size: 1.25rem;
            line-height: 1.75rem;
            font-weight: 700;
            color: rgb(1 32 96);
          }

          .aiClassiteminfo {
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

        .aiClassitem:hover {
          cursor: pointer;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }
    }
  }

  .pyBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 1rem 4rem;
    width: 100%;
    max-width: 1720px;

    .pyTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .pyHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .pyInfo {
      margin: 1rem auto 4rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .pyClassbox {
      width: calc(100% + 1.5rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .pyClassitem {
        margin: 0 1.5rem 1.5rem 0;
        padding: 1.25rem;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        // background-color: rgb(249 250 251);
        border-radius: 0.75rem;

        .pyClassitemfa {
          margin-bottom: 1rem;
          width: 5rem;
          height: 5rem;
          border-radius: 9999px;
          background-color: rgb(114 46 209 / 0.1);
        }

        .pyClassitemtext {
          line-height: 1.5rem;
          font-weight: 500;
          text-align: center;
          color: rgb(1 32 96);
        }

        .pyClassiteminfo {
          margin-top: 0.5rem;
          font-size: 0.875rem;
          line-height: 1.25rem;
          text-align: center;
          color: #6b7280;
        }
      }

      .pyClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }
}
</style>
