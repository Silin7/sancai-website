<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const windowWidth = ref(window.innerWidth)

function uaipdateWindowWidth() {
  windowWidth.value = window.innerWidth
}

onMounted(() => {
  window.addEventListener('resize', uaipdateWindowWidth)
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
          <span>首页</span>
          <span class="aidNavigationXg">/</span>
          <span>AI赋能应用</span>
          <span class="aidNavigationXg">/</span>
          <span class="aidNavigationSp">AI应用成功案例</span>
        </div>
      </div>
    </div>
    <div class="aidCbox">
      <div class="adicTop">
        <div class="adictTitle">杭州某商业综合体AI优化设计</div>
        <div class="adictTags">
          <span class="adictTag adictTag1">智能设计</span>
          <span class="adictTag adictTag2"> <i class="fa fa-calendar-o mr-1"></i> 2024年5月 </span>
          <span class="adictTag adictTag2"> <i class="fa fa-map-marker mr-1"></i> 杭州市 </span>
          <span class="adictTag adictTag2"> <i class="fa fa-building-o mr-1"></i> 商业综合体 </span>
        </div>
        <div class="adictImgs">
          <img src="@/assets/ai-banner-source.jpg" alt="" />
          <img src="@/assets/ai-banner-source.jpg" alt="" />
        </div>
      </div>

      <div class="aipdCbox">
        <div class="aipdcLeft">
          <div class="aipdclJbcs">
            <img src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
              alt="" />
            <div class="aipdcljCenter">
              <div class="aipdcljcTop">
                <div class="aipdcljctItem">
                  <span>除税价：</span>
                  <span class="aipdcljctiSp1">¥4,500.00</span>
                </div>
                <div class="aipdcljctItem">
                  <span>含税价：</span>
                  <span class="aipdcljctiSp2">¥5,000.00</span>
                </div>
                <div class="aipdcljctItem">
                  <span>税率：</span>
                  <span class="aipdcljctiSp1">13%</span>
                </div>
              </div>
              <button class="aipdcljcLxgys">
                <i class="fa fa-phone"></i>
                <span>联系供应商</span>
              </button>
              <button class="aipdcljcJrgwc">
                <i class="fa fa-shopping-cart"></i>
                <span>加入购物车</span>
              </button>
            </div>
            <div class="aipdcljRight">
              <div class="aipdcljrTitle">基本参数</div>
              <div class="aipdcljrItem">
                <span>格型号：</span>
                <span>全专业模型整合V2.0</span>
              </div>
              <div class="aipdcljrItem">
                <span>品牌名称：</span>
                <span>筑智科技</span>
              </div>
              <div class="aipdcljrItem">
                <span>服务周期：</span>
                <span>5-7个工作日</span>
              </div>
              <div class="aipdcljrItem">
                <span>服务方式：</span>
                <span>线上+线下结合</span>
              </div>
              <div class="aipdcljrItem">
                <span>交付成果：</span>
                <span>碰撞检查报告+优化建议</span>
              </div>
              <div class="aipdcljrItem">
                <span>报价时间：</span>
                <span>2025-06-15</span>
              </div>
            </div>
          </div>
          <div class="aipdclXq">
            <div class="aipdclxTitle">
              <i class="fa fa-info-circle"></i>
              项目背景
            </div>
            <div class="aipdclxSub">
              BIM+杭州某商业综合体项目总建筑面积约12万平方米，包含商业购物中心、办公塔楼及配套设施。项目初期面临三大核心挑战：
            </div>
            <div><span></span>传统设计流程周期长，各专业协同效率低，易出现设计冲突</div>
            <div><span></span>建筑能耗模拟不准确，难以满足绿色建筑标准要求</div>
            <div><span></span>空间布局不合理，影响后期商业运营效率和用户体验</div>
            <div class="aipdclxSub">
              为解决上述问题，项目团队引入AI辅助设计工具，通过智能算法优化设计方案，实现设计效率与建筑性能的双重提升。
            </div>
          </div>
          <div class="aipdclXq">
            <div class="aipdclxTitle">
              <i class="fa fa-lightbulb-o"></i>
              AI应用方案
            </div>
            <div class="frbc">
              <div class="">
                <div class="">智能协同设计</div>
                <div class="">基于AI的多专业模型整合与冲突检测</div>
              </div>
              <div class="">
                <div class="">
                  应用AI协同设计平台，实现建筑、结构、机电各专业模型的实时整合与碰撞检测。AI系统可自动识别85%以上的设计冲突，并提供优化建议，减少人工排查时间。
                </div>
                <div class="">
                  通过自然语言处理技术，将设计规范转化为算法规则，在设计过程中实时校验，确保方案符合国家及地方规范要求。
                </div>
              </div>
            </div>
            <div class="frbc">
              <div class="">
                <div class="">
                  利用AI能耗模拟工具，结合杭州气候数据与建筑形态参数，构建能耗预测模型。与传统模拟方法相比，AI模型的预测精度提升40%，计算时间缩短70%。
                </div>
                <div class="">
                  通过遗传算法优化建筑朝向、窗墙比及围护结构参数，最终实现建筑综合能耗降低12%，达到绿色建筑二星级标准。
                </div>
              </div>
              <div class="">
                <div class="">能耗智能优化</div>
                <div class="">AI驱动的建筑能耗模拟与优化</div>
              </div>
            </div>
            <div class="frbc">
              <div class="">
                <div class="">空间智能规划</div>
                <div class="">基于用户行为分析的空间布局优化</div>
              </div>
              <div class="">
                <div class="">
                  引入AI空间规划算法，结合同类商业项目运营数据，模拟不同布局下的人流分布与商业价值。AI系统提供3套优化方案，并量化各方案的预期运营效益。
                </div>
                <div class="">
                  最终采用的优化方案使商业区域有效租赁面积增加8%，预计年客流量提升15%，商铺坪效提高10%。
                </div>
              </div>
            </div>
          </div>
          <div class="aipdclXq">
            <div class="aipdclxTitle">
              <i class="fa fa-tasks"></i>
              实施过程
            </div>

            <div class="aipdclxItem">
              <div class="">
                <div class="aipdclxiInfo fwlcBorder">
                  <div class="aipdclxiNbox frcc">1</div>
                  <div class="aipdclxiPbox">
                    <p>数据准备与模型训练（2周）</p>
                    <p>
                      收集同类商业建筑设计数据、杭州气候数据及商业运营数据，构建训练数据集；基于项目需求定制AI算法模型，完成参数调优。
                    </p>
                  </div>
                </div>
                <div class="aipdclxiInfo fwlcBorder">
                  <div class="aipdclxiNbox frcc">2</div>
                  <div class="aipdclxiPbox">
                    <p>AI辅助方案设计（4周）</p>
                    <p>
                      各专业团队基于AI设计平台开展协同设计，系统实时检测设计冲突并提供优化建议；每周生成设计优化报告，跟踪关键指标改善情况。
                    </p>
                  </div>
                </div>
                <div class="aipdclxiInfo fwlcBorder">
                  <div class="aipdclxiNbox frcc">3</div>
                  <div class="aipdclxiPbox">
                    <p>方案验证与迭代（2周）</p>
                    <p>
                      通过BIM技术与物理模拟验证AI优化方案的可行性；组织设计、施工、运营多方评审，基于反馈进行方案迭代优化。
                    </p>
                  </div>
                </div>
                <div class="aipdclxiInfo fwlcBorder">
                  <div class="aipdclxiNbox frcc">4</div>
                  <div class="aipdclxiPbox">
                    <p>成果交付与应用（1周）</p>
                    <p>
                      输出最终优化设计方案及技术说明；对设计与施工团队进行AI工具应用培训，确保方案落地实施。
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="aipdclXq">
            <div class="aipdclxTitle">
              <i class="fa fa-chart"></i>
              实施成果
            </div>
            <div class="aipdclxItem">
              <div class="aipdclxiCgBox">
                <div class="aipdclxiCgItem">
                  <div class="">
                    <i class="fa fa-clock-o"></i>效率提升
                  </div>
                  <div class="">
                    <div class="">设计周期</div>
                    <div class="">缩短30%（从12周至8.4周）</div>
                  </div>
                  <div class="">
                    <div class="">碰撞检测效率</div>
                    <div class="">提升80%（从5天至1天）</div>
                  </div>
                  <div class="">
                    <div class="">方案迭代速度</div>
                    <div class="">提升60%（平均迭代周期从7天至2.8天）</div>
                  </div>
                </div>
                <div class="aipdclxiCgItem">
                  <div class="">
                    <i class="fa fa-line-chart"></i>效益提升
                  </div>
                  <div class="">
                    <div class="">建筑能耗</div>
                    <div class="">降低12%（年节约能耗约8.5万度）</div>
                  </div>
                  <div class="">
                    <div class="">有效商业面积</div>
                    <div class="">增加8%（约650平方米）</div>
                  </div>
                  <div class="">
                    <div class="">预计运营收益</div>
                    <div class="">提升15%（年增加收益约280万元）</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="aipdcRight">
          <div class="aipdcrTitle">供应商信息</div>
          <div class="aipdcrTop frss">
            <img src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
              alt="" />
            <div>
              <div class="aipdcrtTitle">杭州筑智信息技术有限公司</div>
              <div class="aipdcrtRate">
                <span> 4.8</span>
              </div>
              <div class="aipdcrtTag">
                <span>优质供应商</span>
                <span class="aipdcrtagShu">|</span>
                <span>BIM技术服务</span>
              </div>
            </div>
          </div>
          <div class="aipdcrItem">
            <div class="aipdcrIbox frcc">
              <i class="fa fa-check"></i>
            </div>
            <div class="aipdcrPbox">
              <p>公司地址</p>
              <p>浙江省杭州市滨江区江南大道1000号智慧大厦15层</p>
            </div>
          </div>
          <div class="aipdcrItem">
            <div class="aipdcrIbox frcc">
              <i class="fa fa-check"></i>
            </div>
            <div class="aipdcrPbox">
              <p>联系电话</p>
              <p>400-888-9001</p>
            </div>
          </div>
          <div class="aipdcrItem">
            <div class="aipdcrIbox frcc">
              <i class="fa fa-check"></i>
            </div>
            <div class="aipdcrPbox">
              <p>电子邮箱</p>
              <p>service@zhuzhi.com</p>
            </div>
          </div>
          <div class="aipdcrItem">
            <div class="aipdcrIbox frcc">
              <i class="fa fa-check"></i>
            </div>
            <div class="aipdcrPbox">
              <p>成立时间</p>
              <p>2025年</p>
            </div>
          </div>
          <button class="aipdcrGysxq">
            <span>查看供应商详情</span>
          </button>
          <button class="aipdcrZxzx">
            <i class="fa fa-comment"></i>
            <span>在线咨询</span>
          </button>
        </div>
      </div>

      <div class="aipdcCptj">
        <div class="aipdccTitle">相关案例推荐</div>
        <div class="aipdccCgBox">
          <div class="aipdccCgItem">
            <img src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
              alt="" />
            <div class="aipdccgiContent">
              <span class="aipdccgicTag">智能施工</span>
              <div class="aipdccgicTitle">宁波地铁项目AI施工管理</div>
              <div class="aipdccgicSub">应用AI施工管理系统，减少人工误差，提升施工效率25%，降低安全风险 </div>
              <button>查看详情<i class="fa fa-angle-right"></i></button>
            </div>
          </div>
          <div class="aipdccCgItem">
            <img src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
              alt="" />
            <div class="aipdccgiContent">
              <span class="aipdccgicTag">智能造价</span>
              <div class="aipdccgicTitle">施工进度模拟论证服务</div>
              <div class="aipdccgicSub">4D进度模拟与关键节点可行性分析</div>
              <button>查看详情<i class="fa fa-angle-right"></i></button>
            </div>
          </div>
          <div class="aipdccCgItem">
            <img src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
              alt="" />
            <div class="aipdccgiContent">
              <span class="aipdccgicTag">智能运维</span>
              <div class="aipdccgicTitle">施工进度模拟论证服务</div>
              <div class="aipdccgicSub">4D进度模拟与关键节点可行性分析</div>
              <button>查看详情<i class="fa fa-angle-right"></i></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.aidPage {
  background-color: #f9fafb;
  overflow-x: hidden;

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

    .adicTop {
      padding: 2rem;
      box-shadow:
        0 10px 15px -3px rgb(0 0 0 / 0.1),
        0 4px 6px -4px rgb(0 0 0 / 0.1);
      border-radius: 1rem;
      background-color: #fff;

      @media (max-width: 768px) {
        padding: 1rem;
      }

      .adictTitle {
        margin-bottom: 1rem;
        font-size: 1.875rem;
        font-weight: 700;
        color: #1f2937;
      }

      .adictTags {
        margin-bottom: 1rem;
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
          color: rgb(55 65 81);
          background-color: rgb(243 244 246);
        }
      }

      .adictImgs {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;

        img {
          width: calc(50% - 1rem);
          height: 20rem;
          border-radius: 0.75rem;

          @media (max-width: 768px) {
            margin-bottom: 1rem;
            width: 100%;
          }
        }

        img:last-child {
          margin-bottom: 0;
        }
      }
    }
  }

  .aipdCbox {
    position: relative;
    margin: 0 auto;
    padding: 1rem;
    width: 100%;
    max-width: 1536px;
    color: rgb(1 32 96);

    @media (min-width: 992px) {
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
    }

    .aipdcLeft {
      margin-bottom: 2rem;
      width: 100%;

      @media (min-width: 992px) {
        margin-bottom: 0;
        width: calc(66.7% - 1rem);
      }

      .aipdclJbcs {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (min-width: 992px) {
          display: flex;
          justify-content: space-between;
        }

        img {
          width: 100%;
          height: 16rem;
          border-radius: 0.5rem;

          @media (min-width: 992px) {
            width: calc(33.4% - 2rem);
            height: 16rem;
            border-radius: 0.5rem;
          }
        }

        .aipdcljCenter {
          margin-top: 1rem;
          width: 100%;

          @media (min-width: 992px) {
            margin-top: 0;
            width: calc(33.3%);
          }

          .aipdcljcTop {
            padding: 1rem;
            background-color: rgb(249 250 251);
            border-radius: 0.5rem;

            .aipdcljctItem {
              margin-bottom: 0.25rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: rgb(107 114 128);

              .aipdcljctiSp1 {
                font-weight: 500;
                font-size: 1.125rem;
                line-height: 1.75rem;
                color: rgb(1 32 96);
              }

              .aipdcljctiSp2 {
                font-weight: 700;
                font-size: 1.25rem;
                line-height: 1.75rem;
                color: rgb(22 93 255);
              }
            }
          }

          .aipdcljcLxgys {
            margin-top: 1rem;
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

          .aipdcljcJrgwc {
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

        .aipdcljRight {
          margin-top: 1rem;
          width: 100%;

          @media (min-width: 992px) {
            margin-top: 0;
            width: calc(33.3%);
          }

          .aipdcljrTitle {
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
            margin-bottom: 1rem;
          }

          .aipdcljrItem {
            margin-top: 0.75rem;
            display: flex;
            align-items: center;

            span:first-child {
              width: 6rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: rgb(107 114 128);
            }

            span:last-child {
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: rgb(1 32 96);
            }
          }
        }
      }

      .aipdclXq {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        .aipdclxTitle {
          margin-bottom: 1.5rem;
          padding-bottom: 0.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;
          border-bottom: 1px solid rgb(243 244 246);
        }

        .aipdclxSub {
          line-height: 1.5rem;
        }

        .aipdclxItem {
          margin-top: 1.5rem;

          .aipdclxiTitle {
            margin-bottom: 0.75rem;
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
          }

          .aipdclxiInfo {
            position: relative;
            display: flex;
            line-height: 1.5rem;
            padding-bottom: 1rem;

            .aipdclxiDian {
              flex-shrink: 0;
              margin-right: 10px;
              margin-top: 0.6rem;
              width: 6px;
              height: 6px;
              border-radius: 9999px;
              background-color: rgb(1 32 96);
            }

            .aipdclxiIbox {
              flex-shrink: 0;
              margin-right: 0.75rem;
              width: 2rem;
              height: 2rem;
              color: rgb(22 93 255);
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 9999px;
            }

            .aipdclxiNbox {
              position: absolute;
              top: 0;
              left: -1rem;
              width: 2rem;
              height: 2rem;
              color: #fff;
              background-color: rgb(22 93 255);
              border-radius: 9999px;
            }

            .aipdclxiPbox {
              p:first-child {
                font-weight: 500;
                line-height: 1.5rem;
              }

              p:last-child {
                font-weight: 500;
                font-size: 0.875rem;
                line-height: 1.5rem;
                color: rgb(75 85 99);
              }
            }
          }

          .fwlcBorder {
            margin-left: 1rem;
            padding-left: 2rem;
            border-left: 2px solid #e5e7eb;
          }

          .alignCenter {
            align-items: center;
          }

          .aipdclxiCgBox {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;

            .aipdclxiCgItem {
              overflow: hidden;
              margin-bottom: 1rem;
              width: 100%;
              background-color: rgb(255 255 255);
              border-radius: 0.5rem;
              box-shadow:
                0 10px 15px -3px rgb(0 0 0 / 0.1),
                0 4px 6px -4px rgb(0 0 0 / 0.1);
              border: 1px solid rgb(229 231 235);

              @media (min-width: 992px) {
                margin-bottom: 0;
                width: calc(50% - 0.5rem);
              }

              img {
                width: 100%;
                height: 10rem;
              }

              .aipdclxicIp {
                font-size: 0.875rem;
                line-height: 1.25rem;
                text-align: center;
                padding: 0.75rem;
              }
            }

            .aipdclxiCgItem:last-child {
              margin-bottom: 0;
            }

            .aipdclxiCgItem:hover {
              @media (min-width: 768px) {
                cursor: pointer;
              }
            }
          }
        }
      }
    }

    .aipdcRight {
      padding: 1.5rem;
      width: 100%;
      height: 100%;
      background-color: rgb(255 255 255);
      border-radius: 1rem;
      box-shadow:
        0 10px 15px -3px rgb(0 0 0 / 0.1),
        0 4px 6px -4px rgb(0 0 0 / 0.1);

      @media (min-width: 992px) {
        width: calc(33.3% - 1rem);
      }

      .aipdcrTitle {
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        font-weight: 700;
        font-size: 1.25rem;
        line-height: 1.75rem;
      }

      .aipdcrTop {
        margin-bottom: 1.5rem;

        img {
          margin-right: 1rem;
          width: 4rem;
          height: 4rem;
          border-radius: 0.75rem;
        }

        .aipdcrtTitle {
          font-weight: 700;
          font-size: 1.125rem;
          line-height: 1.75rem;
        }

        .aipdcrtRate {
          display: flex;
          align-items: center;

          span {
            margin-left: 0.25rem;
            font-size: 0.875rem;
            line-height: 1.25rem;
            color: rgb(75 85 99);
          }
        }

        .aipdcrtTag {
          color: rgb(107 114 128);
          font-size: 0.875rem;
          line-height: 1.25rem;

          .aipdcrtagShu {
            margin: 0.25rem;
          }
        }
      }

      .aipdcrItem {
        position: relative;
        display: flex;
        line-height: 1.5rem;
        padding-bottom: 1rem;

        .aipdcrIbox {
          flex-shrink: 0;
          margin-right: 0.75rem;
          width: 2rem;
          height: 2rem;
          color: rgb(22 93 255);
          background-color: rgb(22 93 255 / 0.1);
          border-radius: 9999px;
        }

        .aipdcrPbox {
          p:first-child {
            font-weight: 500;
            font-size: 0.875rem;
            line-height: 1.5rem;
            color: rgb(75 85 99);
          }

          p:last-child {
            font-weight: 500;
            line-height: 1.5rem;
          }
        }
      }

      .aipdcrGysxq {
        margin-top: 1rem;
        padding: 0.75rem 1rem;
        width: 100%;
        text-align: center;
        font-weight: 500;
        line-height: 1.5rem;
        color: rgb(22 93 255);
        border: 1px solid rgb(22 93 255);
        border-radius: 0.5rem;

        i {
          margin-right: 0.5rem;
        }
      }

      .aipdcrZxzx {
        margin-top: 1rem;
        padding: 0.75rem 1rem;
        width: 100%;
        text-align: center;
        font-weight: 500;
        line-height: 1.5rem;
        color: rgb(22 93 255);
        background-color: rgb(22 93 255 / 0.2);
        border-radius: 0.5rem;

        i {
          margin-right: 0.5rem;
        }
      }
    }
  }

  .aipdcCptj {
    padding: 1.5rem;
    background-color: rgb(255 255 255);
    border-radius: 1rem;
    box-shadow:
      0 10px 15px -3px rgb(0 0 0 / 0.1),
      0 4px 6px -4px rgb(0 0 0 / 0.1);

    .aipdccTitle {
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      font-weight: 700;
      font-size: 1.25rem;
      line-height: 1.75rem;
    }

    .aipdccCgBox {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;

      .aipdccCgItem {
        overflow: hidden;
        margin-bottom: 1rem;
        width: 100%;
        background-color: rgb(255 255 255);
        border-radius: 0.5rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);
        border: 1px solid rgb(229 231 235);

        @media (min-width: 992px) {
          margin-bottom: 0;
          width: calc(33.3% - 0.5rem);
        }

        img {
          width: 100%;
          height: 10rem;
        }

        .aipdccgiContent {
          padding: 1rem;

          .aipdccgicTag {
            display: inline-block;
            margin-bottom: 0.5rem;
            padding: 0.25rem 1rem;
            font-size: 0.75rem;
            line-height: 1rem;
            color: rgb(22 93 255);
            background-color: rgb(22 93 255 / 0.1);
            border-radius: 9999px;
          }

          .aipdccgicTitle {
            margin-bottom: 0.5rem;
            font-weight: 700;
            color: rgb(1 32 96);
          }

          .aipdccgicSub {
            font-size: 0.875rem;
            line-height: 1.25rem;
            margin-bottom: 0.75rem;
            color: rgb(107 114 128);
          }

          button {
            font-size: 0.875rem;
            line-height: 1.25rem;
            color: rgb(22 93 255);

            i {
              margin-left: 0.25rem;
            }
          }
        }
      }

      .aipdccCgItem:last-child {
        margin-bottom: 0;
      }

      .aipdccCgItem:hover {
        @media (min-width: 768px) {
          cursor: pointer;
        }
      }
    }
  }
}
</style>
