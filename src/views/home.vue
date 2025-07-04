<script setup lang="ts">
import sideleft from '@/components/sideleft.vue'
import sideright from '@/components/sideright.vue'

function goTopCallback() {
  window.scrollTo(0, 0)
}
</script>

<template>
  <div>
    <!-- <component :is="sideleft" ref="sideleftRef" />
    <component :is="sideright" ref="siderightRef" @goTopCallback="goTopCallback" /> -->
    <div class="homepage">
      <div class="bannerbox">
        <div class="bannerzzc" />
        <img
          src="@/assets/banner00.jpeg"
          alt="banner"
          mode="cover"
          style="width: 100vw; height: 720px"
        />
        <div class="bannerabsolute">
          <div class="bannercontent">
            <div class="bannertitle">聚焦新型城市基础设施建设再起航</div>
            <div class="bannersubtitle">绿色化 数字化 智能化</div>
            <div class="frsc">
              <button class="bannerjgkbtn">价格库</button>
              <button class="bannerjjfabtn">
                解决方案 <i class="fa fa-arrow-right" style="margin-left: 0.5rem"></i>
              </button>
            </div>
            <div class="bannercompany">杭州三才工程管理咨询有限公司</div>
            <div class="bannergridbox">
              <div class="bannergriditem">
                <div class="bannerfabox">
                  <i class="fa fa-database" style="font-size: 20px; color: #fff"></i>
                </div>
                <div class="bannergridright">
                  <div class="bannergridtitle">人材机信价格库</div>
                  <div class="bannergridinfo">精准数据，助力成本管控</div>
                </div>
              </div>
              <div class="bannergridshu" />
              <div class="bannergriditem">
                <div class="bannerfabox">
                  <i class="fa fa-calculator" style="font-size: 20px; color: #fff"></i>
                </div>
                <div class="bannergridright">
                  <div class="bannergridtitle">数据方案组价</div>
                  <div class="bannergridinfo">智能组价，优化方案设计</div>
                </div>
              </div>
              <div class="bannergridshu" />
              <div class="bannergriditem">
                <div class="bannerfabox">
                  <i class="fa fa-android" style="font-size: 20px; color: #fff"></i>
                </div>
                <div class="bannergridright">
                  <div class="bannergridtitle">人工智能应用</div>
                  <div class="bannergridinfo">AI赋能，提升运行效率</div>
                </div>
              </div>
              <div class="bannergridshu" />
              <div class="bannergriditem">
                <div class="bannerfabox">
                  <i class="fa fa-play-circle" style="font-size: 20px; color: #fff"></i>
                </div>
                <div class="bannergridright">
                  <div class="bannergridtitle">视频讲解</div>
                  <div class="bannergridinfo">直观教学，掌握核心技能</div>
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
.homepage {
  height: 1000px;
  background-color: #f9fafb;

  .bannerbox {
    position: relative;
    width: 100vw;
    height: 720px;

    .bannerzzc {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
      width: 100vw;
      height: 720px;
      background-image: linear-gradient(to right, #01206090 50%, #e5e7eb90 100%);
    }

    .bannerabsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 720px;

      .bannercontent {
        margin: 0 auto;
        padding: 6rem 30px 0;
        width: 100%;
        max-width: 1720px;
        height: 720px;
        border: 1px solid red;

        .bannertitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .bannersubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }

        .bannerjgkbtn {
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgb(22 93 255);
          border-radius: 9999px;
          box-shadow:
            0 10px 15px -3px rgb(0 0 0 / 0.1),
            0 4px 6px -4px rgb(0 0 0 / 0.1);
        }

        .bannerjjfabtn {
          margin-left: 20px;
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgba(255 255 255 / 0.1);
          border: 1px solid rgba(255 255 255 / 0.3);
          border-radius: 9999px;
        }

        .bannercompany {
          margin-top: 4rem;
          font-size: 0.875rem;
          line-height: 1.25rem;
          color: rgba(255 255 255 / 0.7);
        }

        .bannergridbox {
          overflow: hidden;
          margin-top: 3rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: rgba(11, 255, 0, 0.1);
          border-radius: 1rem;

          .bannergriditem {
            width: calc(25% - 1px);
            padding: 1.5rem;
            display: flex;

            .bannerfabox {
              width: 3rem;
              height: 3rem;
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 0.5rem;
              display: flex;
              justify-content: center;
              align-items: center;
            }

            .bannergridright {
              margin-left: 1rem;

              .bannergridtitle {
                margin-bottom: 0.5rem;
                font-size: 1.25rem;
                line-height: 1.75rem;
                font-weight: 700;
                color: #fff;
              }

              .bannergridinfo {
                font-size: 1rem;
                line-height: 1.5rem;
                color: rgba(255 255 255 / 0.8);
              }
            }
          }

          .bannergriditem:hover {
            transform: scale(1.05);
            box-shadow: 10px 10px 15px -3px rgb(0 0 0 / 0.1);
          }

          .bannergridshu {
            width: 1px;
            height: 5rem;
            background-image: linear-gradient(to bottom, #1627ff30);
          }
        }
      }
    }
  }
}
</style>
