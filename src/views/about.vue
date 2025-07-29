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
      <!-- intro -->
      <!-- 公司简介 -->
      <div class="introtBox">
        <div class="introtTitle">公司简介</div>
        <div class="introtHeng"></div>
        <div class="introtContent">
          <div class="introtLeft">
            <p>
              杭州三才工程管理咨询有限公司成立于2014年5月，总部位于浙江省杭州市。我们以"网络强国"和"数字中国"建设思想为指引，专注于提供工程项目数字化服务与产品，是国家高新技术企业。
            </p>
            <p>
              公司主营工程造价咨询、BIM咨询、CIM咨询、智慧管理软件开发，致力于推动建筑行业数字化转型，为新型基础设施建设提供专业支持。
            </p>
            <ul>
              <li>国家高新技术企业</li>
              <li>信用认证企业</li>
              <li>行业科学技术奖</li>
              <li>20+专业书籍参编</li>
              <li>主流媒体报道</li>
            </ul>
            <div class="">
              <i class="fa fa-bullseye"></i>
              <div class="">
                <div class="">企业愿景</div>
                <div class="">
                  成为工程项目数字化服务的引领者，推动建筑行业智能化转型，构建和谐共生的数字生态。
                </div>
              </div>
            </div>
          </div>
          <div class="introtRight">
            <div class="">发展历程</div>
            <div class="">
              <div class="">2014年</div>
              <div class="">公司成立，专注于工程造价咨询服务</div>
            </div>
            <div class="">
              <div class="">2016年</div>
              <div class="">拓展BIM咨询服务，完成首个大型BIM项目</div>
            </div>
            <div class="">
              <div class="">2018年</div>
              <div class="">参编首部BIM专业书籍，获得国家高新技术企业认证</div>
            </div>
            <div class="">
              <div class="">2020年</div>
              <div class="">开展CIM咨询业务，开发智慧管理软件平台</div>
            </div>
            <div class="">
              <div class="">2021年</div>
              <div class="">获得国家行业科学技术奖，被多家主流媒体报道</div>
            </div>
            <div class="">
              <div class="">2023年至今</div>
              <div class="">聚焦BIM、CIM技术，全面实施数字化转型</div>
            </div>
          </div>
        </div>
      </div>
      <!-- 代表成果 -->
      <div class="achievementBox">
        <div class="achievementTitle">代表成果</div>
        <div class="achievementHeng"></div>
        <div class="achievementInfo">在实践探索中，我们不断突破创新，取得了丰硕成果</div>
        <div class="achievementRidbox">
          <div v-for="index in 4" :key="index" class="achievementRiditem">
            <img
              src="https://images.unsplash.com/photo-1547658719-da2b51169166?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
              alt=""
              style="width: 100%; height: 12rem"
            />
            <div class="achievementRidimgbox">
              <div class="achievementRidimgfx">
                <div
                  v-if="index % 4 == 1"
                  class="achievementFabox"
                  style="color: rgb(37 99 235); background-color: rgb(219 234 254)"
                >
                  <i class="fa fa-building"></i>
                </div>
                <div
                  v-if="index % 4 == 2"
                  class="achievementFabox"
                  style="color: rgb(22 163 74); background-color: rgb(220 252 231)"
                >
                  <i class="fa fa-book"></i>
                </div>
                <div
                  v-if="index % 4 == 3"
                  class="achievementFabox"
                  style="color: rgb(147 51 234); background-color: rgb(243 232 255)"
                >
                  <i class="fa fa-trophy"></i>
                </div>
                <div
                  v-if="index % 4 == 0"
                  class="achievementFabox"
                  style="color: rgb(22 163 74); background-color: rgb(220 252 231)"
                >
                  <i class="fa fa-certificate"></i>
                </div>
                <div class="achievementRidtitle">城市标志性建筑数字化服务</div>
                <div class="achievementGridinfo">
                  完成省内外多个城市标志性建筑的工程数字化咨询服务，提升项目管理效率30%以上
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 核心业务 -->
      <div class="businessOut">
        <div class="businessBox">
          <div class="businessTitle">核心业务</div>
          <div class="businessHeng"></div>
          <div class="businessInfo">立足应用视角，提供切实可行的数字化解决方案</div>
          <div class="serviceCardBox">
            <el-row :gutter="16">
              <el-col v-for="index in 3" :key="index" :xs="24" :sm="24" :md="8" :lg="8" :xl="8">
                <div class="serviceCardItem">
                  <div class="frsc">
                    <div class="serviceCardItemIcon frcc">
                      <i class="fa fa-video-camera"></i>
                    </div>
                    <div class="serviceCardItemTt">视频制作</div>
                  </div>
                  <div class="serviceCardItemSub">
                    我们制作专业的工程数字化教学视频，内容涵盖BIM技术应用、工程造价管理、智能建造等前沿领域。视频内容注重实操性，解决工程实践中的具体问题。
                  </div>
                  <div class="serviceCardItemYycj">应用场景：</div>
                  <div class="serviceCardItemJsbox">
                    <div class="serviceCardItemJsitem">
                      <i class="fa fa-check-circle"></i>
                      <span>工程新技术普及教育视频</span>
                    </div>
                    <div class="serviceCardItemJsitem">
                      <i class="fa fa-check-circle"></i>
                      <span>BIM软件实操教学系列</span>
                    </div>
                    <div class="serviceCardItemJsitem">
                      <i class="fa fa-check-circle"></i>
                      <span>工程数字化案例解析视频</span>
                    </div>
                    <div class="serviceCardItemJsitem">
                      <i class="fa fa-check-circle"></i>
                      <span>行业标准解读视频课程</span>
                    </div>
                  </div>
                  <button>
                    <span>查看案例</span>
                    <i class="fa fa-arrow-right"></i>
                  </button>
                </div>
              </el-col>
            </el-row>
          </div>
        </div>
      </div>
      <!-- 未来展望 -->
      <div class="futureOut">
        <div class="futureBox">
          <div class="futureTitle">未来展望</div>
          <div class="futureHeng"></div>
          <div class="futureCardBox">
            <div class="futureCardItem">
              进入"十四五"发展新阶段，杭州三才工程管理咨询有限公司将以加快数字化发展为契机，聚焦BIM、CIM技术，实施全面数字化转型。
            </div>
            <div class="futureCardItem">
              我们将继续走智能化和智慧化发展道路，为推进和谐共生的数字生态，贡献匠心智造的力量，助力建筑行业实现高质量发展。
            </div>
          </div>
          <div class="futureRow">
            <div class="futureColBox">
              <div class="futureColNum">100+</div>
              <div class="futureColText">专业团队</div>
            </div>
            <div class="futureColBox">
              <div class="futureColNum">500+</div>
              <div class="futureColText">服务项目</div>
            </div>
            <div class="futureColBox">
              <div class="futureColNum">20+</div>
              <div class="futureColText">专业书籍</div>
            </div>
            <div class="futureColBox">
              <div class="futureColNum">9年+</div>
              <div class="futureColText">行业深耕</div>
            </div>
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
          border: 1px solid rgba(255 255 255 / 0.3);
          border-radius: 9999px;
        }

        .abbannerJjfabtn:hover {
          transform: scale(1.05);
        }
      }
    }
  }

  .introtBox {
    position: relative;
    margin: 0 auto;
    padding: 6rem 1rem 5rem;
    width: 100%;
    max-width: 1720px;

    .introtTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .introtHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }
  }

  .achievementBox {
    position: relative;
    margin: 0 auto;
    padding: 6rem 1rem 5rem;
    width: 100%;
    max-width: 1720px;

    .achievementTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .achievementHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .achievementInfo {
      margin: 1rem auto 0;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .achievementRidbox {
      overflow: hidden;
      padding-top: 4rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;

      .achievementRiditem {
        margin-bottom: 1rem;
        overflow: hidden;
        background-color: #fff;
        border-radius: 1rem;

        .achievementRidimgfx {
          padding: 1.5rem;

          .achievementFabox {
            margin-bottom: 1rem;
            width: 3rem;
            height: 3rem;
            border-radius: 999px;
            font-size: 1.25rem;
            display: flex;
            justify-content: center;
            align-items: center;
          }

          .achievementRidtitle {
            margin-bottom: 0.5rem;
            font-weight: 700;
            font-size: 1.25rem;
            line-height: 1.75rem;
            color: rgb(1 32 96);
          }

          .achievementGridinfo {
            font-size: 1rem;
            line-height: 1.5rem;
            color: rgb(75 85 99);
          }
        }
        @media (max-width: 600px) {
          .achievementRidimgfx {
            padding: 1rem 0.75rem;
          }
        }
      }

      @media (min-width: 1000px) {
        .achievementRiditem {
          width: calc(25% - 1rem);
        }
      }
      @media (max-width: 999px) and (min-width: 601px) {
        .achievementRiditem {
          width: calc(50% - 0.5rem);
        }
      }
      @media (max-width: 600px) {
        .achievementRiditem {
          width: 100%;
        }
      }

      .achievementRiditem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }

      .achievementGridshu {
        width: 1px;
        height: 5rem;
        background-image: linear-gradient(to bottom, #1627ff30);
      }
    }
  }

  .businessOut {
    padding: 6rem 0;
    width: 100vw;
    background-color: #fff;

    .businessBox {
      position: relative;
      margin: 0 auto;
      padding: 0 1rem;
      width: 100%;
      max-width: 1720px;

      .businessTitle {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 700;
        text-align: center;
        color: rgb(1 32 96);
      }

      .businessHeng {
        margin: 1rem auto 0;
        width: 5rem;
        height: 0.25rem;
        border-radius: 9999px;
        background-color: rgb(22 93 255);
      }

      .businessInfo {
        margin: 1rem auto 4rem;
        text-align: center;
        max-width: 42rem;
        color: rgb(75 85 99);
      }

      .serviceCardBox {
        display: flex;
        flex-wrap: wrap;

        .serviceCardItem {
          padding: 1.5rem;
          margin-bottom: 1rem;
          border-radius: 0.75rem;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

          .serviceCardItemIcon {
            margin-right: 1rem;
            width: 4rem;
            height: 4rem;
            font-size: 1.5rem;
            line-height: 2rem;
            color: rgb(37 99 235);
            background-color: rgb(219 234 254);
            border-radius: 0.75rem;
          }

          .serviceCardItemTt {
            font-weight: 700;
            font-size: 1.5rem;
            line-height: 2rem;
            color: rgb(1 32 96);
          }
        }

        .serviceCardItemSub {
          margin: 1.5rem 0;
          line-height: 1.5rem;
          color: rgb(75 85 99);
        }

        .serviceCardItemYycj {
          font-weight: 700;
          font-size: 1.125rem;
          line-height: 1.75rem;
          margin-bottom: 0.75rem;
          color: rgb(1 32 96);
        }

        .serviceCardItemJsbox {
          margin-bottom: 1.5rem;

          .serviceCardItemJsitem {
            line-height: 1.5rem;
            display: flex;
            align-items: center;

            i {
              color: rgb(34 197 94);
              margin-right: 0.5rem;
            }

            span {
              color: rgb(1 32 96);
            }
          }
        }

        button {
          font-weight: 500;
          color: rgb(22 93 255);

          i {
            margin-left: 0.5rem;
          }
        }
      }
    }
  }

  .futureOut {
    margin-bottom: 20rem;
    padding: 6rem 0;
    width: 100vw;
    background-image: linear-gradient(to bottom right, #165dff, #012060);

    .futureBox {
      position: relative;
      margin: 0 auto;
      padding: 0 1rem;
      width: 100%;
      max-width: 1720px;

      .futureTitle {
        margin-bottom: 1.5rem;
        font-size: 2.25rem;
        font-weight: 700;
        line-height: 2.5rem;
        text-align: center;
        color: #fff;
      }

      .futureHeng {
        margin: 0 auto 2rem;
        width: 6rem;
        height: 0.25rem;
        margin-bottom: 2rem;
        background-color: rgb(255 255 255);
      }

      .futureCardBox {
        margin: 0 auto 2.5rem;
        padding: 2rem;
        max-width: 52rem;
        border-radius: 1rem;
        background-color: rgb(255 255 255 / 0.1);

        .futureCardItem {
          color: #fff;
          text-align: center;
        }

        :first-child {
          margin-bottom: 1.5rem;
        }
      }

      .futureRow {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;

        .futureColBox {
          margin: 0 1rem 1rem;

          .futureColNum {
            margin-bottom: 0.5rem;
            font-weight: 700;
            font-size: 2.25rem;
            line-height: 2.5rem;
            text-align: center;
            color: #fff;
          }

          .futureColText {
            text-align: center;
            color: #fff;
          }
        }
      }

      @media (max-width: 600px) {
        .futureCardBox {
          padding: 0.75rem;
        }
      }
    }
  }
}
</style>
