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

    <div class="ndPage">
      <div class="ndHbox">
        <div class="ndHcontent">
          <div class="ndNavigation">
            <span>首页</span>
            <span class="ndNavigationXg">/</span>
            <span>热点资讯</span>
            <span class="ndNavigationXg">/</span>
            <span class="ndNavigationSp">BIM技术在上海中心大厦的应用</span>
          </div>
        </div>
      </div>
      <div class="ndCbox">
        <div class="ndCtitle">上海中心大厦BIM技术应用案例深度解析</div>
        <div class="ndCzuoz">
          <img src="@/assets/32.jpg" alt="" />
          <div class="zuozeInfo">
            <p>作者：李明</p>
            <p>三才工程研究院 BIM技术专家</p>
          </div>
        </div>
        <div class="ndCFuwb">富文本内容</div>
        <div class="ndCTags">
          <div class="ndcTagLabel">标签：</div>
          <div class="ndcTag">BIM技术</div>
          <div class="ndcTag">超高层建筑</div>
          <div class="ndcTag">数字化建造</div>
          <div class="ndcTag">上海中心</div>
        </div>
        <div class="ndCzuobtm">
          <img src="@/assets/32.jpg" alt="" />
          <div class="zuozeInfo">
            <p>作者：李明</p>
            <p>三才工程研究院 BIM技术专家</p>
            <p>
              李明先生是国内知名的BIM技术专家，曾参与多个国家级重点工程的BIM技术应用，包括上海中心大厦、北京大兴国际机场等项目。在BIM技术研发、标准制定和工程应用方面有丰富经验。
            </p>
          </div>
        </div>
        <div class="ndCtitle2">相关推荐</div>
        <!-- 资讯列表 -->
        <div class="newsdBox">
          <div class="newsdItem" v-for="index in 3" :key="index">
            <div class="newsPiImgBox">
              <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" class="newsPiImg" />
              <div class="newsPiImgTag">政策</div>
            </div>
            <div class="newsPiBox" :style="windowWidth > 992 ? '' : 'margin-top:1rem; width: 100%;'">
              <div class="newsPiTitle">住建部发布《建筑业数字化转型发展指南》推动行业升级</div>
              <div class="newsPiInfo">
                近日，住房和城乡建设部正式发布《建筑业数字化转型发展指南》，提出到2025年，建筑业数字化转型取得明显进展，打造一批建筑产业互联网平台，培育一批行业级、企业级数字建造解决方案。指南明确了数字化转型的重点任务和保障措施，为行业发展指明方向。
              </div>
              <div class="newsPiClass">
                <div class="newsPiCleft">
                  <div class="newsPiCitrm">
                    <i class="fa fa-calendar"></i>
                    <span class="newsPiClassSpan">2023-12-15</span>
                  </div>
                  <div class="newsPiCitrm">
                    <i class="fa fa-eye"></i>
                    <span class="newsPiClassSpan">1568次预览</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ndPage {
  background-color: #fff;
  overflow-x: hidden;

  .ndHbox {
    background-color: #f0f7ff;
    border-bottom: 1px solid #e0e7ff;

    .ndHcontent {
      margin: 0 auto;
      padding: 6rem 2rem 1rem;
      width: 100%;
      max-width: 1536px;
      color: rgb(1 32 96);

      @media (max-width: 992px) {
        padding: 5rem 1rem 1rem;
      }

      .ndNavigation {
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

        .ndNavigationXg {
          margin: 0 0.5rem;
        }

        .ndNavigationSp {
          color: rgb(22 93 255);
        }
      }
    }
  }

  .ndCbox {
    position: relative;
    margin: 0 auto;
    padding: 2.5rem 1rem;
    width: 100%;
    max-width: 1536px;
    color: rgb(1 32 96);

    @media (max-width: 768px) {
      padding: 1rem;
    }

    .ndCtitle {
      margin-bottom: 1.5rem;
      font-size: clamp(1.5rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
    }

    .ndCtitle2 {
      margin-bottom: 1.5rem;
      font-size: clamp(1.25rem, 4vw, 1.5rem);
      font-weight: 700;
    }

    .ndCzuoz {
      margin-bottom: 1rem;
      display: flex;

      img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
      }

      .zuozeInfo {
        margin-left: 1rem;

        p:first-child {
          font-weight: 500;
          font-size: 0.875rem;
          line-height: 1.25rem;
        }

        p:last-child {
          font-weight: 500;
          font-size: 0.875rem;
          line-height: 1.25rem;
          color: rgb(107 114 128);
        }
      }
    }

    .ndCFuwb {
      margin-bottom: 1rem;
      padding: 10rem 2rem;
      background-color: #f1f1f1;
      border-radius: 0.5rem;
    }

    .ndCTags {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      border-top: 1px solid rgb(229 231 235);
      padding: 1.5rem 0;

      .ndcTagLabel {
        margin-bottom: 0.5rem;
        font-size: 0.875rem;
        line-height: 1.25rem;
        color: rgb(75 85 99);
      }

      .ndcTag {
        margin: 0 0.5rem 0.5rem 0;
        font-size: 0.875rem;
        line-height: 1.25rem;
        padding: 0.25rem 0.75rem;
        background-color: rgb(243 244 246);
        border-radius: 9999px;
      }

      .ndcTag:hover {
        @media (min-width: 768px) {
          cursor: pointer;
          color: #fff;
          background-color: rgb(22 93 255);
        }
      }
    }

    .ndCzuobtm {
      margin-bottom: 3rem;
      padding: 1.5rem;
      background-color: rgb(249 250 251);
      border-radius: 0.75rem;
      display: flex;

      @media (max-width: 768px) {
        padding: 1rem;
      }

      img {
        width: 4rem;
        height: 4rem;
        border-radius: 50%;

        @media (max-width: 768px) {
          width: 3rem;
          height: 3rem;
        }
      }

      .zuozeInfo {
        margin-left: 1rem;

        p:nth-child(2) {
          margin-bottom: 0.75rem;
          font-weight: 500;
          font-size: 0.875rem;
          line-height: 1.25rem;
          color: rgb(107 114 128);
        }

        p:first-child {
          font-weight: 500;
          font-size: 0.875rem;
          line-height: 1.25rem;
        }

        p:last-child {
          font-weight: 500;
          font-size: 0.875rem;
          line-height: 1.25rem;
          color: rgb(55 65 81);
        }
      }
    }

    .newsdBox {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;

      .newsdItem {
        margin-bottom: 1.5rem;
        padding: 1rem;
        width: calc(33.3% - 1rem);
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        border-radius: 0.75rem;

        @media (max-width: 992px) {
          width: 100%;
        }

        .newsPiImgBox {
          position: relative;

          .newsPiImg {
            width: 100%;
            height: 200px;
          }

          .newsPiImgTag {
            position: absolute;
            top: 1rem;
            left: 1rem;
            z-index: 10;
            border-radius: 9999px;
            padding-left: 0.75rem;
            padding-right: 0.75rem;
            padding-top: 0.25rem;
            padding-bottom: 0.25rem;
            font-size: 0.75rem;
            line-height: 1rem;
            font-weight: 700;
            color: #fff;
            background-color: rgb(59 130 246);
          }
        }

        .newsPiBox {
          width: 100%;

          .newsPiTitle {
            font-size: 1.25rem;
            line-height: 1.75rem;
            font-weight: 700;
            margin: 0.75rem 0;
            color: rgb(1 32 96);
          }

          .newsPiInfo {
            margin-bottom: 1rem;
            line-height: 1.25rem;
            color: rgb(75 85 99);
          }

          .newsPiClass {
            display: flex;
            align-items: center;
            justify-content: space-between;

            .newsPiCleft {
              width: 100%;
              display: flex;
              align-items: center;
              justify-content: space-between;

              .newsPiCitrm {
                margin-right: 1rem;
                display: flex;
                align-items: center;
                color: rgb(107 114 128);
                font-size: 0.875rem;

                .newsPiClassSpan {
                  margin-left: 0.25rem;
                  font-size: 0.875rem;
                  line-height: 1rem;
                }
              }
            }

            .newsPiCright {
              display: flex;
              align-items: center;
              font-weight: 500;
              line-height: 1.5rem;
              font-size: 0.875rem;
              color: rgb(22 93 255);

              button {
                margin-right: 0.5rem;
                font-size: 0.875rem;
                color: rgb(22 93 255);
              }
            }
          }
        }
      }

      .newsdItem:last-child {
        @media (max-width: 768px) {
          margin-bottom: 0;
        }
      }

      .newsdItem:hover {
        @media (max-width: 768px) {
          cursor: pointer;
        }
      }

    }
  }
}
</style>