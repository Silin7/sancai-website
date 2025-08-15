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

const state = ref('gsjs')
</script>

<template>
  <div class="sdPage">
    <div class="sdHbox">
      <div class="sdHcontent">
        <div class="sdNavigation">
          <span>首页</span>
          <span class="sdNavigationXg">/</span>
          <span>供应商列表</span>
          <span class="sdNavigationXg">/</span>
          <span class="sdNavigationSp">杭州筑智信息技术有限公司</span>
        </div>

        <div class="sdhGys">
          <img src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
            alt="" />
          <div class="sdhgCenter">
            <div class="sdhgcTop">
              <div class="sdhgctTitle">杭州筑智信息技术有限公司</div>
              <div class="sdhgctInfo">
                <i class="fa fa-star"></i>
                <span>4.8</span>
                <span>|</span>
                <span>优质供应商</span>
              </div>
            </div>
            <div class="sdhgcCbox">
              <div class="sdhgcCitem">
                <i class="fa fa-tags"></i>
                <span>主营：BIM技术服务、工程数字化咨询、智能设计方案</span>
              </div>
              <div class="sdhgcCitem">
                <i class="fa fa-map-marker"></i>
                <span>浙江省 杭州市滨江区</span>
              </div>
              <div class="sdhgcCitem">
                <i class="fa fa-building-o"></i>
                <span>成立于2015年</span>
              </div>
              <div class="sdhgcCitem">
                <i class="fa fa-users"></i>
                <span>企业规模：200-500人</span>
              </div>
            </div>
            <div class="sdhgcTags">
              <div class="sdhgcTag">甲级BIM咨询资质</div>
              <div class="sdhgcTag">施工模拟</div>
              <div class="sdhgcTag">数字孪生建模</div>
              <div class="sdhgcTag">工程数字化</div>
              <div class="sdhgcTag">智慧工地</div>
            </div>
          </div>
          <div class="sdhgRight">
            <button class="sdhgcLxgys">
              <i class="fa fa-phone"></i>
              <span>联系供应商</span>
            </button>
            <button class="sdhgcJrgwc">
              <i class="fa fa-star-o"></i>
              <span>收藏</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="sdCbox">
      <div class="sdcIContent">
        <div class="sdclFl">
          <button :class="state === 'gsjs' ? 'sdclflAc' : ''" @click="state = 'gsjs'">
            公司简介
          </button>
          <button :class="state === 'hzal' ? 'sdclflAc' : ''" @click="state = 'hzal'">
            合作案例
          </button>
          <button :class="state === 'cplb' ? 'sdclflAc' : ''" @click="state = 'cplb'">
            产品列表
          </button>
          <button :class="state === 'lxfs' ? 'sdclflAc' : ''" @click="state = 'lxfs'">
            联系方式
          </button>
        </div>
        <div v-if="state === 'gsjs'" class="sdclGsjj">
          <div class="sdclxTitle">公司简介</div>
          <div class="sdclxSub">
            BIM+杭州筑智信息技术有限公司成立于2015年，是国内领先的建筑行业数字化解决方案提供商。公司专注于为建筑行业客户提供BIM技术应用、工程数字化咨询、智能设计方案及数字孪生建模等全方位服务。
          </div>
          <div class="sdclxSub">
            公司拥有一支由BIM工程师、建筑设计师、软件开发工程师组成的专业团队，核心成员均具有10年以上建筑行业经验。凭借深厚的行业积累和技术实力，公司已获得甲级BIM咨询资质、ISO9001质量管理体系认证等多项资质认证。
          </div>
          <div class="sdclxSub">
            自成立以来，筑智信息始终坚持"以技术驱动建筑创新"的理念，先后为300+大型项目提供数字化服务，涵盖市政工程、商业综合体、轨道交通、医疗建筑等多个领域，服务客户包括中建、中铁、万科等知名企业。
          </div>
          <div class="sdclxItem">
            <div class="sdclxiTitle">核心优势</div>
            <div class="sdclxiIbox">
              <div class="sdclxiInfo">
                <div class="sdclxiFa">
                  <i class="fa fa-lightbulb-o"></i>
                </div>
                <div class="sdclxiTt">技术领先</div>
                <div class="sdclxiSt">
                  拥有自主研发的BIM协同平台，掌握数字孪生核心技术，技术实力行业领先
                </div>
              </div>
              <div class="sdclxiInfo">
                <div class="sdclxiFa">
                  <i class="fa fa-lightbulb-o"></i>
                </div>
                <div class="sdclxiTt">专业团队</div>
                <div class="sdclxiSt">
                  100+专业技术人员，核心成员均有10年以上行业经验，服务经验丰富
                </div>
              </div>
              <div class="sdclxiInfo">
                <div class="sdclxiFa">
                  <i class="fa fa-lightbulb-o"></i>
                </div>
                <div class="sdclxiTt">品质保障</div>
                <div class="sdclxiSt">
                  严格的质量管理体系，标准化服务流程，确保项目交付质量与效率
                </div>
              </div>
            </div>
          </div>
          <div class="sdclxItem">
            <div class="sdclxiTitle">资质证书</div>
            <div class="sdclxiCgBox">
              <div class="sdclxiCgItem">
                <img
                  src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                  alt="" />
                <div class="sdclxicIp">甲级BIM咨询资质</div>
              </div>
              <div class="sdclxiCgItem">
                <img
                  src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                  alt="" />
                <div class="sdclxicIp">ISO9001质量管理体系认证</div>
              </div>
              <div class="sdclxiCgItem">
                <img
                  src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                  alt="" />
                <div class="sdclxicIp">高新技术企业认证</div>
              </div>
              <div class="sdclxiCgItem">
                <img
                  src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                  alt="" />
                <div class="sdclxicIp">软件企业认定证书</div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="state === 'hzal'" class="sdclHzal">
          <div class="sdclHzalRow">
            <button class="sdclHzalColActive">全部案例</button>
            <button class="sdclHzalCol">商业综合体</button>
            <button class="sdclHzalCol">市政工程</button>
            <button class="sdclHzalCol">轨道交通</button>
            <button class="sdclHzalCol">医疗建筑</button>
          </div>
          <div class="sdclHzalBox">
            <div class="sdclHzalItem" v-for="index in 4" :key="index">
              <div class="sdclHzalImgBox">
                <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" class="sdclHzalImg" />
                <div class="sdclHzalImgTag">商业综合体</div>
              </div>
              <div class="sdclHzalBox">
                <div class="sdclHzalTitle">住建部发布《建筑业数字化转型发展指南》推动行业升级</div>
                <div class="sdclHzalInfo">
                  近日，住房和城乡建设部正式发布《建筑业数字化转型发展指南》，提出到2025年，建筑业数字化转型取得明显进展，打造一批建筑产业互联网平台，培育一批行业级、企业级数字建造解决方案。指南明确了数字化转型的重点任务和保障措施，为行业发展指明方向。
                </div>

                <div class="sdclHzalClass">
                  <div class="sdclHzalCitrm">
                    <span class="sdclHzalClassSpan">BIM建模</span>
                  </div>
                  <div class="sdclHzalCitrm">
                    <span class="sdclHzalClassSpan">施工模拟</span>
                  </div>
                  <div class="sdclHzalCitrm">
                    <span class="sdclHzalClassSpan">管线优化</span>
                  </div>
                </div>
                <div class="sdclHzalCright">
                  <button>查看详情</button>
                  <i class="fa fa-angle-right"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="state === 'cplb'" class="sdclHzal">
          <div class="sdclHzalRow">
            <button class="sdclHzalColActive">全部产品</button>
            <button class="sdclHzalCol">BIM软件</button>
            <button class="sdclHzalCol">数字化平台</button>
            <button class="sdclHzalCol">咨询服务</button>
            <button class="sdclHzalCol">培训课程</button>
          </div>
          <div class="sdclCplbBox">
            <div class="sdclCplbItem" v-for="index in 6" :key="index">
              <div class="sdclCplbImgBox">
                <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" class="sdclCplbImg" />
                <div class="sdclCplbImgTag">BIM软件</div>
              </div>
              <div class="sdclCplbBox">
                <div class="sdclCplbTitle">筑智BIM协同管理平台</div>
                <div class="sdclCplbInfo">
                  集成化BIM协同管理平台，支持多专业协同设计、模型审查、碰撞检查及施工模拟。
                </div>
                <div class="sdclCplbCbtm">
                  <div class="sdclCplbCprice">¥ 28,000/套起</div>
                  <div class="sdclCplbCright">
                    <button>详情</button>
                    <i class="fa fa-arrow-right"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="state === 'lxfs'" class="sdclGsjj">
          <div class="sdclxTitle">联系方式</div>
          <div class="sdLxfsBox">
            <div class="sdLxfsItem">
              <div class="frsc">
                <div class="sdLxfsIbox frcc">
                  <i class="fa fa-map-marker"></i>
                </div>
                <div class="sdLxfsGsdz">
                  <p>公司地址</p>
                  <p>浙江省杭州市滨江区江南大道1000号智慧大厦15层</p>
                </div>
              </div>
              <img src="https://picsum.photos/600/300?random=701" alt="公司位置地图" class="sdLxfsFsdz" />
            </div>
            <div class="sdLxfsItem">
              <div class="sdLxfsRi">
                <div class="sdLxfsRiFa frcc">
                  <i class="fa fa-map-marker"></i>
                </div>
                <div class="sdLxfsRiCt">
                  <p>联系电话</p>
                  <p>400-888-9001（业务咨询）</p>
                  <p>0571-8888-7777（公司总机）</p>
                </div>
              </div>
              <div class="sdLxfsRi">
                <div class="sdLxfsRiFa frcc">
                  <i class="fa fa-map-marker"></i>
                </div>
                <div class="sdLxfsRiCt">
                  <p>电子邮箱</p>
                  <p>info@zhuzhi.com（ general inquiries）</p>
                  <p>service@zhuzhi.com（技术支持）</p>
                </div>
              </div>
              <div class="sdLxfsRi">
                <div class="sdLxfsRiFa frcc">
                  <i class="fa fa-map-marker"></i>
                </div>
                <div class="sdLxfsRiCt">
                  <p>官方平台</p>
                  <a>www.zhuzhi.com（公司官网）</a>
                  <p>微信公众号：筑智信息服务平台</p>
                </div>
              </div>
              <div class="sdLxfsRi">
                <img src="https://picsum.photos/600/300?random=701" alt="二维码" class="sdLxfsEwm" />
                <div class="sdLxfsEbox">
                  <p>扫码关注</p>
                  <p>获取最新产品及服务信息</p>
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
.sdPage {
  background-color: #f9fafb;
  overflow-x: hidden;

  .sdHbox {
    background-color: #f0f7ff;
    border-bottom: 1px solid #e0e7ff;

    .sdHcontent {
      margin: 0 auto;
      padding: 6rem 2rem 2rem;
      width: 100%;
      max-width: 1536px;
      color: rgb(1 32 96);

      @media (max-width: 992px) {
        padding: 5rem 1rem 1rem;
      }

      .sdNavigation {
        margin: 0 auto 1.5rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;

        span {
          font-size: 0.875rem;
          line-height: 1.25rem;
          color: rgb(107 114 128);
        }

        span:hover {
          cursor: pointer;
          color: rgb(22 93 255);
        }

        .sdNavigationXg {
          margin: 0 0.5rem;
        }

        .sdNavigationSp {
          color: rgb(22 93 255);
        }
      }

      .sdhGys {
        padding: 1rem;
        background-color: rgb(255 255 255);
        border-radius: 0.75rem;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (min-width: 992px) {
          padding: 1.5rem;
          display: flex;
          justify-content: space-between;
        }

        img {
          padding: 0.25rem;
          width: calc(100% - 0.5rem);
          height: 8rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

          @media (min-width: 992px) {
            width: 8rem;
          }
        }

        .sdhgCenter {
          margin-top: 1rem;
          width: 100%;

          @media (min-width: 992px) {
            margin-top: 0;
            width: calc(100% - 20rem);
          }

          .sdhgcTop {
            display: flex;
            flex-wrap: wrap;
            align-items: center;

            .sdhgctTitle {
              font-weight: 700;
              font-size: clamp(1.5rem, 3vw, 2.5rem);
              color: rgb(1 32 96);
            }

            .sdhgctInfo {
              margin-top: 1rem;
              font-weight: 500;
              font-size: 0.875rem;
              line-height: 1.25rem;
              padding: 0.25rem 0.75rem;
              color: rgb(255 255 255);
              background-color: rgb(131 203 172);
              border-radius: 9999px;

              span {
                margin-left: 0.25rem;
              }
            }

            @media (min-width: 992px) {
              .sdhgctInfo {
                margin-top: 0;
                margin-left: 1rem;
              }
            }
          }

          .sdhgcCbox {
            margin-top: 1rem;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;

            .sdhgcCitem {
              width: 100%;
              height: 3rem;
              display: flex;
              align-items: center;

              i {
                flex-shrink: 0;
                font-size: 1rem;
                width: 1rem;
                color: rgb(22 93 255);
                margin-right: 0.5rem;
              }

              span {
                color: rgb(75 85 99);
              }
            }

            @media (min-width: 992px) {
              .sdhgcCitem {
                width: calc(50% - 0.5rem);
              }
            }
          }

          .sdhgcTags {
            display: flex;
            flex-wrap: wrap;

            .sdhgcTag {
              flex-shrink: 0;
              margin-right: 0.5rem;
              margin-bottom: 0.25rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              padding: 0.25rem 0.75rem;
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 9999px;
              color: rgb(22 93 255);
            }
          }
        }

        .sdhgRight {
          margin-top: 1rem;
          width: 100%;

          @media (min-width: 992px) {
            margin-top: 0;
            width: 10rem;
          }

          .sdhgcLxgys {
            padding: 0.75rem 1rem;
            width: 100%;
            text-align: center;
            font-weight: 500;
            line-height: 1.5rem;
            color: #fff;
            background-color: rgb(22 93 255 / 0.9);
            border-radius: 0.5rem;

            i {
              margin-right: 0.5rem;
            }
          }

          .sdhgcJrgwc {
            margin-top: 1rem;
            padding: 0.75rem 1rem;
            width: 100%;
            text-align: center;
            font-weight: 500;
            line-height: 1.5rem;
            color: rgb(55 65 81);
            border: 1px solid rgb(209 213 219);
            border-radius: 0.5rem;

            i {
              margin-right: 0.5rem;
            }
          }
        }
      }
    }
  }

  .sdCbox {
    position: relative;
    margin: 0 auto;
    padding: 2rem 1rem;
    width: 100%;
    max-width: 1536px;
    color: rgb(1 32 96);

    @media (max-width: 768px) {
      padding: 1rem;
    }

    .sdcIContent {
      width: 100%;

      .sdclFl {
        overflow-x: auto;
        display: flex;
        flex-wrap: nowrap;
        margin-bottom: 2rem;
        background-color: rgb(255 255 255);
        border-radius: 0.75rem;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 768px) {
          margin-bottom: 1rem;
        }

        button {
          flex-shrink: 0;
          font-size: 1.125rem;
          line-height: 1.75rem;
          padding: 1rem 1.5rem;
          color: rgb(55 65 81);
        }

        .sdclflAc {
          color: rgb(22 93 255);
          border-bottom: 2px solid rgb(22 93 255);
        }
      }

      .sdclGsjj {
        padding: 1rem;
        background-color: rgb(255 255 255);
        border-radius: 0.75rem;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (min-width: 992px) {
          padding: 1.5rem;
        }

        .sdclxTitle {
          margin-bottom: 1.5rem;
          padding-bottom: 0.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;
          border-bottom: 1px solid rgb(243 244 246);
        }

        .sdclxSub {
          margin-bottom: 1rem;
          line-height: 1.625;
          font-size: 1.125rem;
          color: rgb(55 65 81);
        }

        .sdclxItem {
          margin-top: 1.5rem;

          .sdclxiTitle {
            margin-bottom: 0.75rem;
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
          }

          .sdclxiIbox {
            @media (min-width: 992px) {
              display: flex;
              justify-content: space-between;
            }
          }

          .sdclxiInfo {
            margin-bottom: 1rem;
            padding: 1rem;
            line-height: 1.5rem;
            background-color: rgb(240 247 255);
            border-radius: 0.75rem;

            @media (min-width: 992px) {
              padding: 1.5rem;
              width: calc(33.3% - 0.5rem);
            }

            .sdclxiFa {
              margin-bottom: 1rem;
              display: flex;
              justify-content: center;
              align-items: center;
              width: 3rem;
              height: 3rem;
              color: rgb(22 93 255);
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 0.5rem;
            }

            .sdclxiTt {
              font-weight: 700;
              font-size: 1.125rem;
              line-height: 1.75rem;
              margin-bottom: 0.5rem;
            }

            .sdclxiSt {
              color: rgb(75 85 99);
            }
          }

          .sdclxiCgBox {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;

            .sdclxiCgItem {
              cursor: pointer;
              overflow: hidden;
              margin-bottom: 1rem;
              width: 100%;
              background-color: rgb(255 255 255);
              border-radius: 0.5rem;
              box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
              border: 1px solid rgb(229 231 235);

              @media (min-width: 992px) {
                margin-bottom: 0;
                width: calc(25% - 0.5rem);
              }

              img {
                width: 100%;
                height: 10rem;
              }

              .sdclxicIp {
                font-size: 0.875rem;
                line-height: 1.25rem;
                text-align: center;
                padding: 0.75rem;
              }
            }

            .sdclxiCgItem:last-child {
              margin-bottom: 0;
            }
          }
        }

        .sdLxfsBox {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;

          .sdLxfsItem {
            margin-bottom: 1rem;
            width: calc(100%);
            padding: 1rem;
            background-color: rgb(240 247 255);
            border-radius: 0.75rem;

            @media (min-width: 992px) {
              padding: 1.5rem;
            }

            .sdLxfsIbox {
              flex-shrink: 0;
              width: 3rem;
              height: 3rem;
              color: rgb(22 93 255);
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 0.5rem;
            }

            .sdLxfsGsdz {
              margin-left: 1rem;

              p:first-child {
                font-weight: 700;
                font-size: 1.125rem;
                line-height: 1.75rem;
                margin: 0 0 0.5rem;
              }

              p:last-child {
                color: rgb(55 65 81);
                margin: 0;
              }
            }

            .sdLxfsFsdz {
              box-sizing: border-box;
              margin-top: 1rem;
              width: 100%;
              height: 12rem;
              border-width: 1px;
              border-radius: 0.5rem;

              @media (min-width: 992px) {
                margin: 1rem 0 0 4rem;
                width: calc(100% - 8rem);
              }
            }

            .sdLxfsRi {
              display: flex;
              margin-bottom: 1.5rem;

              .sdLxfsRiFa {
                flex-shrink: 0;
                width: 2.5rem;
                height: 2.5rem;
                color: rgb(22 93 255);
                background-color: rgb(22 93 255 / 0.1);
                border-radius: 9999px;
              }

              .sdLxfsRiCt {
                margin-left: 1rem;

                p {
                  margin-bottom: 0.25rem;
                  font-weight: 500;
                  line-height: 1.5rem;
                  color: rgb(55 65 81);
                }

                p:first-child {
                  color: rgb(1 32 96);
                }

                a {
                  display: inline-block;
                  margin-bottom: 0.25rem;
                  font-weight: 500;
                  line-height: 1.5rem;
                  color: rgb(22 93 255);
                }
              }

              .sdLxfsEwm {
                box-sizing: border-box;
                padding: 0.25rem;
                width: 7rem;
                height: 7rem;
                border-radius: 0.5rem;
                background-color: #fff;
                box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
              }

              .sdLxfsEbox {
                margin-left: 1rem;
                height: 7rem;
                display: flex;
                flex-flow: column;
                justify-content: center;

                p:first-child {
                  line-height: 1.5rem;
                  font-weight: 500;
                  margin-bottom: 0.25rem;
                  color: rgb(1 32 96);
                }

                p:last-child {
                  font-size: 0.875rem;
                  line-height: 1.25rem;
                  color: rgb(75 85 99 / var(--tw-text-opacity, 1));
                }
              }
            }

            .sdLxfsRi:last-child {
              margin-bottom: 0;
            }
          }

          .sdLxfsItem:last-child {
            margin-bottom: 0;

            @media (min-width: 992px) {
              width: calc(50% - 1rem);
            }
          }
        }
      }

      .sdclHzal {
        padding: 1rem;
        background-color: rgb(255 255 255);
        border-radius: 0.75rem;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (min-width: 992px) {
          padding: 1.5rem;
        }

        .sdclHzalRow {
          margin-bottom: 1rem;
          display: flex;
          flex-wrap: wrap;
          align-items: center;

          .sdclHzalCol {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
            border: 1px solid rgb(243 244 246);
            border-radius: 999px;

            @media (max-width: 768px) {
              margin: 0 0.5rem 0.5rem 0;
              padding: 0.5rem 1rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
            }
          }

          .sdclHzalCol:hover {
            @media (min-width: 768px) {
              background-color: rgb(243 244 246);
            }
          }

          .sdclHzalColActive {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border: 1px solid rgb(243 244 246);
            border-radius: 999px;

            @media (max-width: 768px) {
              margin: 0 0.5rem 0.5rem 0;
              padding: 0.5rem 1rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
            }
          }
        }

        .sdclHzalBox {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;

          .sdclHzalItem {
            overflow: hidden;
            cursor: pointer;
            margin-bottom: 1.5rem;
            border-radius: 0.75rem;
            border: 1px solid rgb(229 231 235);

            @media (min-width: 992px) {
              width: calc(50% - 0.75rem);
            }

            .sdclHzalImgBox {
              position: relative;
              width: 100%;

              .sdclHzalImg {
                width: 100%;
                height: 14rem;
              }

              .sdclHzalImgTag {
                position: absolute;
                top: 1rem;
                left: 1rem;
                z-index: 10;
                border-radius: 0.25rem;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
                padding-top: 0.25rem;
                padding-bottom: 0.25rem;
                font-size: 0.75rem;
                line-height: 1rem;
                font-weight: 700;
                color: #fff;
                background-color: rgb(22 93 255);
              }
            }

            .sdclHzalBox {
              width: 100%;
              padding: 1rem;

              @media (min-width: 992px) {
                padding: 1.5rem;
              }

              .sdclHzalTitle {
                margin-bottom: 1rem;
                font-size: 1.125rem;
                line-height: 1.75rem;
                font-weight: 700;
                color: rgb(1 32 96);
              }

              .sdclHzalInfo {
                margin-bottom: 1rem;
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: rgb(75 85 99);
              }

              .sdclHzalClass {
                margin-bottom: 1rem;
                width: 100%;
                display: flex;
                flex-wrap: wrap;

                .sdclHzalCitrm {
                  margin-right: 0.5rem;
                  padding: 0.25rem 0.5rem;
                  font-size: 0.75rem;
                  line-height: 1rem;
                  color: rgb(75 85 99);
                  background-color: rgb(243 244 246);
                  border-radius: 0.25rem;
                }

                .sdclHzalCitrm:last-child {
                  margin-right: 0;
                }
              }

              .sdclHzalCright {
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

          .sdclHzalItem:last-child {
            @media (max-width: 992px) {
              margin-bottom: 0;
            }
          }
        }

        .sdclCplbBox {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;

          .sdclCplbItem {
            overflow: hidden;
            cursor: pointer;
            margin-bottom: 1.5rem;
            border-radius: 0.75rem;
            border: 1px solid rgb(229 231 235);

            @media (min-width: 992px) {
              width: calc(33.3% - 0.75rem);
            }

            .sdclCplbImgBox {
              position: relative;
              width: 100%;

              .sdclCplbImg {
                width: 100%;
                height: 12rem;
              }

              .sdclCplbImgTag {
                position: absolute;
                top: 1rem;
                left: 1rem;
                z-index: 10;
                border-radius: 0.25rem;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
                padding-top: 0.25rem;
                padding-bottom: 0.25rem;
                font-size: 0.75rem;
                line-height: 1rem;
                font-weight: 700;
                color: #fff;
                background-color: rgb(22 93 255);
              }
            }

            .sdclCplbBox {
              width: 100%;
              padding: 1rem;

              @media (min-width: 992px) {
                padding: 1.5rem;
              }

              .sdclCplbTitle {
                margin-bottom: 1rem;
                font-size: 1.125rem;
                line-height: 1.75rem;
                font-weight: 700;
                color: rgb(1 32 96);
              }

              .sdclCplbInfo {
                margin-bottom: 1rem;
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: rgb(75 85 99);
              }

              .sdclCplbCbtm {
                width: 100%;
                display: flex;
                justify-content: space-between;
                align-items: center;

                .sdclCplbCprice {
                  font-weight: 700;
                  color: rgb(22 93 255);
                }

                .sdclCplbCright {
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

          .sdclCplbItem:last-child {
            @media (max-width: 992px) {
              margin-bottom: 0;
            }
          }

          .sdclCplbItem:hover {
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

            .sdclCplbImg {
              transform: scale(1.05);
            }

            .sdclCplbTitle {
              color: rgb(22 93 255);
            }
          }
        }
      }
    }
  }
}
</style>

<style>
/* 评分 style */
.el-rate {
  padding-bottom: 0.25rem !important;
}

.sdcrTop .el-rate__icon {
  margin-right: 0 !important;
}
</style>
