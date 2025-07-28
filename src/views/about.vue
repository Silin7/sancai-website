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
    <div class="aboutPage">
      <!-- BANNER -->
      <div class="abbannerBox">
        <img src="@/assets/about-02.jpg" alt="abbanner" style="width: 100vw; height: 40rem" />
        <div class="abbannerAbsolute">
          <div class="abbannerContent">
            <div class="abbannerTitle">杭州三才工程管理咨询有限公司</div>
            <div class="abbannerSubtitle">工程项目数字化服务与产品的国家高新技术企业</div>
            <div class="frsc">
              <button class="abbannerJgkbtn">了解我们</button>
              <button class="abbannerJjfabtn">核心业务</button>
            </div>
          </div>
        </div>
      </div>
      <!-- 人材机信价格库 -->
      <div class="containerBox">
        <div class="containerTitle">代表成果</div>
        <div class="containerHeng"></div>
        <div class="containerInfo">在实践探索中，我们不断突破创新，取得了丰硕成果</div>
        <div class="containerRidbox">
          <div
            v-for="index in 4"
            :key="index"
            class="containerRiditem"
            :style="
              windowWidth > 1000
                ? 'width: calc(25% - 0.5rem);'
                : windowWidth > 600
                  ? 'width: calc(50% - 0.5rem);'
                  : 'width: 100%'
            "
          >
            <div class="containerRidimgbox">
              <img src="@/assets/product01.jpeg" alt="" style="width: 100%; height: 12rem" />
              <div class="containerRidimgfx frsc">
                <div class="containerFabox">
                  <i class="fa fa-user" style="font-size: 20px; color: #fff"></i>
                </div>
              </div>
            </div>
            <div class="containerGridibox">
              <div class="frsc" style="margin-bottom: 0.75rem">
                <i class="fa fa-dot-circle-o" style="font-size: 1rem; color: #165dff"></i>
                <div class="containerRidtitle">数字技术指导</div>
              </div>
              <div class="frsc" style="margin-bottom: 0.75rem">
                <i class="fa fa-dot-circle-o" style="font-size: 1rem; color: #165dff"></i>
                <div class="containerRidtitle">数字方案论证</div>
              </div>
            </div>
            <div class="containerCkqbbox">
              <div class="containerCkqbtitle">查看全部</div>
              <div class="frsc">
                <div class="containerCkqbxq">详情</div>
                <i class="fa fa-arrow-right" style="font-size: 1rem; color: #165dff"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 数字化解决方案 -->
      <div class="solutionsBox">
        <div class="solutionsTitle">数字化解决方案</div>
        <div class="solutionsHeng"></div>
        <div class="solutionsInfo">
          探索我们的数字化应用与智慧化管理方案，为您的项目提供全方位的技术支持
        </div>
        <div class="solutionsSubBox1">
          <div class="solutionsSubItem solutionsActive">BIM+工程造价</div>
          <div class="solutionsSubItem">BIM+倾斜摄影</div>
        </div>
        <div class="solutionsSubBox2">
          <div class="solutionsSubItem solutionsActive">BIM+工程造价</div>
          <div class="solutionsSubItem">BIM+倾斜摄影</div>
          <div class="solutionsSubItem">BIM+三维扫描</div>
          <div class="solutionsSubItem">BIM+VR/AR</div>
          <div class="solutionsSubItem">BIM+物联网</div>
          <div class="solutionsSubItem">BIM+数字化加工</div>
          <div class="solutionsSubItem">BIM+地理信息</div>
          <div class="solutionsSubItem">BIM+放样机器人</div>
          <div class="solutionsSubItem">BIM+空间资产</div>
        </div>
        <div class="solutionsImg">
          <img
            src="@/assets/case/bimgongcheng.jpg"
            alt="abbanner"
            style="width: 100%; height: 568px"
          />
          <div class="solutionsImgTitle">BIM+倾斜摄影</div>
          <div class="solutionsImgInfo">
            <p>
              通过BIM技术实现工程造价的精准计算与动态管理，提高成本控制能力，减少预算超支风险，为项目全生命周期成本管理提供数据支撑。
            </p>
          </div>
        </div>
      </div>
      <!-- 人工智能应用 -->
      <div class="aiBox">
        <div class="aiTitle">人工智能应用</div>
        <div class="aiHeng"></div>
        <div class="aiInfo">
          以数据、算法和算力为核心要素，驱动工程设计、工程施工和运营维护多维度创新应用，为产业转型发展注入新动能
        </div>
        <div class="aiSubbox">
          <div class="aiFabox frcc">
            <i class="fa fa-cogs" style="font-size: 20px; color: #165dff"></i>
          </div>
          <div class="aiSubtitle">工程管理AI应用组价</div>
        </div>
        <div class="aiClassbox">
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-pencil" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">智能化设计</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-wrench" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">辅助设计工具</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-android" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">建筑机器人</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-tasks" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">施工管理</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-check-square" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">辅助质量控制</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-sliders" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">智能化控制</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-bolt" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">能源管理</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-expand" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">场景拓展</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa frcc">
              <i class="fa fa-random" style="font-size: 20px; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">跨界融合</div>
          </div>
        </div>
        <div class="aiSubbox">
          <div class="aiFabox2 frcc">
            <i class="fa fa-calculator" style="font-size: 20px; color: #722ed1"></i>
          </div>
          <div class="aiSubtitle">工程管理AI应用组价</div>
        </div>
        <div class="aiClassbox">
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-pencil" style="font-size: 20px; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能复核文本</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-wrench" style="font-size: 20px; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能检测漏项</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-android" style="font-size: 20px; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能预警偏离</div>
          </div>
          <div
            class="aiClassitem"
            :style="
              windowWidth > 1000
                ? 'width: calc(20% - 1.5rem);'
                : windowWidth > 600
                  ? 'width: calc(33.3% - 1.5rem);'
                  : 'width: calc(50% - 1.5rem)'
            "
          >
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-tasks" style="font-size: 20px; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能分析指标</div>
          </div>
        </div>
      </div>
      <!-- 友情链接  -->
      <div class="pyBox">
        <div class="pyTitle">友情链接</div>
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
.aboutPage {
  background-color: #f9fafb;

  .abbannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .abbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .abbannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1720px;

        .abbannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .abbannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }

        .abbannerJgkbtn {
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgb(22 93 255);
          border-radius: 9999px;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        }

        .abbannerJgkbtn:hover {
          transform: scale(1.05);
        }

        .abbannerJjfabtn {
          margin-left: 20px;
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgba(255 255 255 / 0.2);
          border: 1px solid rgba(255 255 255 / 0.1);
          border-radius: 9999px;
        }

        .abbannerJjfabtn:hover {
          transform: scale(1.05);
          border: 1px solid rgba(255 255 255 / 0.3);
        }
      }
    }
  }

  .containerBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 1rem;
    width: 100%;
    max-width: 1720px;

    .containerTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .containerHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .containerInfo {
      margin: 1rem auto 0;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .containerRidbox {
      overflow: hidden;
      padding-top: 4rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;

      .containerRiditem {
        overflow: hidden;
        background-color: #fff;
        border-radius: 1rem;

        .containerRidimgbox {
          position: relative;

          .containerRidimgfx {
            padding: 1.5rem;

            .containerFabox {
              margin-right: 0.75rem;
              width: 2.5rem;
              height: 2.5rem;
              border-radius: 0.5rem;
              display: flex;
              justify-content: center;
              align-items: center;
              background-color: rgb(219 234 254);
            }
          }
        }

        .containerGridibox {
          padding: 1.5rem;

          .containerRidtitle {
            margin-left: 0.5rem;
            font-size: 1rem;
            line-height: 1.5rem;
            color: rgb(75 85 99);
          }

          .containerGridinfo {
            font-size: 1rem;
            line-height: 1.5rem;
            color: rgba(255 255 255 / 0.8);
          }
        }

        .containerCkqbbox {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 1.5rem;
          border-top: 1px solid #f3f4f6;

          .containerCkqbtitle {
            font-size: 0.875rem;
            line-height: 1.25rem;
            color: #6b7280;
          }

          .containerCkqbxq {
            margin-right: 0.75rem;
            line-height: 1.25rem;
            color: rgb(22 93 255 / 0.8);
          }
        }
      }

      .containerRiditem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }

      .containerGridshu {
        width: 1px;
        height: 5rem;
        background-image: linear-gradient(to bottom, #1627ff30);
      }
    }
  }

  .solutionsBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 1rem;
    width: 100%;
    max-width: 1720px;

    .solutionsTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .solutionsHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .solutionsInfo {
      margin: 1rem auto 4rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .solutionsSubBox1 {
      margin-bottom: 3rem;
      display: flex;
      justify-content: center;

      .solutionsSubItem {
        flex-shrink: 1;
        margin: 0 0.75rem;
        line-height: 2rem;
        color: rgb(1 32 96);
        padding: 0.5rem 1.25rem;
        border-radius: 9999px;
        background-color: #fff;
      }

      .solutionsSubItem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        background-color: rgb(243 244 246);
      }
    }

    .solutionsSubBox2 {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;

      .solutionsSubItem {
        flex-shrink: 1;
        margin: 0.75rem;
        line-height: 2rem;
        color: rgb(1 32 96);
        padding: 0.5rem 1.25rem;
        border-radius: 9999px;
        background-color: #fff;
      }

      .solutionsSubItem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        background-color: rgb(243 244 246);
      }
    }

    .solutionsActive {
      color: #fff !important;
      background-color: #165dff !important;
    }

    .solutionsImg {
      margin-top: 3rem;
      overflow: hidden;
      position: relative;
      width: 100%;
      height: 568px;
      border-radius: 1rem;

      .solutionsImgTitle {
        position: absolute;
        top: 20%;
        left: 0;
        z-index: 2;
        width: 100%;
        text-align: center;
        font-size: 2.25rem;
        line-height: 2.5rem;
        font-weight: 700;
        text-align: center;
        color: rgb(1 32 96);
      }

      .solutionsImgInfo {
        position: absolute;
        bottom: 0;
        left: 0;
        z-index: 2;
        width: 100%;
        padding: 2.5rem;
        background-color: rgb(1 32 96 / 0.5);

        p {
          margin: 0;
          max-width: 42rem;
          line-height: 1.5rem;
          color: rgb(255 255 255 / 0.9);
        }
      }
    }
  }

  .aiBox {
    position: relative;
    margin: 6rem auto 0;
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

    .aiSubbox {
      margin-bottom: 2rem;
      display: flex;
      align-items: center;

      .aiFabox {
        margin-right: 1rem;
        width: 3rem;
        height: 3rem;
        background-color: rgba(22 93 255 / 0.1);
        border-radius: 9999px;
      }

      .aiFabox2 {
        margin-right: 1rem;
        width: 3rem;
        height: 3rem;
        background-color: rgb(114 46 209 / 0.1);
        border-radius: 9999px;
      }

      .aiSubtitle {
        font-size: 1.5rem;
        line-height: 2rem;
        font-weight: 700;
        color: rgb(1 32 96);
      }
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
          border-radius: 9999px;
          background-color: rgb(22 93 255 / 0.1);
        }

        .aiClassitemfa2 {
          margin-bottom: 1rem;
          width: 4rem;
          height: 4rem;
          border-radius: 9999px;
          background-color: rgb(114 46 209 / 0.1);
        }

        .aiClassitemtext {
          line-height: 1.5rem;
          font-weight: 500;
          color: rgb(1 32 96);
        }
      }

      .aiClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
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
