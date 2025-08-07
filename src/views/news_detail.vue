<script setup lang="ts">
import { ref } from 'vue'

const value1 = ref(4.8)
</script>

<template>
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
      <div class="ndcLeft">
        <div class="ndclJbcs">
          <img
            src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
            alt=""
          />
          <div class="ndcljCenter">
            <div class="ndcljcTop">
              <div class="ndcljctItem">
                <span>除税价：</span>
                <span class="ndcljctiSp1">¥4,500.00</span>
              </div>
              <div class="ndcljctItem">
                <span>含税价：</span>
                <span class="ndcljctiSp2">¥5,000.00</span>
              </div>
              <div class="ndcljctItem">
                <span>税率：</span>
                <span class="ndcljctiSp1">13%</span>
              </div>
            </div>
            <button class="ndcljcLxgys">
              <i class="fa fa-phone"></i>
              <span>联系供应商</span>
            </button>
            <button class="ndcljcJrgwc">
              <i class="fa fa-shopping-cart"></i>
              <span>加入购物车</span>
            </button>
          </div>
          <div class="ndcljRight">
            <div class="ndcljrTitle">基本参数</div>
            <div class="ndcljrItem">
              <span>格型号：</span>
              <span>全专业模型整合V2.0</span>
            </div>
            <div class="ndcljrItem">
              <span>品牌名称：</span>
              <span>筑智科技</span>
            </div>
            <div class="ndcljrItem">
              <span>服务周期：</span>
              <span>5-7个工作日</span>
            </div>
            <div class="ndcljrItem">
              <span>服务方式：</span>
              <span>线上+线下结合</span>
            </div>
            <div class="ndcljrItem">
              <span>交付成果：</span>
              <span>碰撞检查报告+优化建议</span>
            </div>
            <div class="ndcljrItem">
              <span>报价时间：</span>
              <span>2025-06-15</span>
            </div>
          </div>
        </div>
        <div class="ndclXq">
          <div class="ndclxTitle">服务详情</div>
          <div class="ndclxSub">
            BIM+多专业碰撞检查服务是基于建筑信息模型（BIM）技术，对建筑、结构、机电等各专业模型进行整合分析，提前发现并解决设计中的碰撞冲突，减少施工阶段的返工和变更，降低工程成本。
          </div>
          <div class="ndclxItem">
            <div class="ndclxiTitle">服务内容</div>
            <div class="ndclxiInfo">
              <span class="ndclxiDian"></span>
              <span>各专业BIM模型整合与校验（建筑、结构、给排水、电气、暖通等）</span>
            </div>
            <div class="ndclxiInfo">
              <span class="ndclxiDian"></span>
              <span>多维度碰撞检测（硬碰撞、间隙碰撞、净空碰撞等）</span>
            </div>
            <div class="ndclxiInfo">
              <span class="ndclxiDian"></span>
              <span>碰撞点可视化标注与分类统计</span>
            </div>
            <div class="ndclxiInfo">
              <span class="ndclxiDian"></span>
              <span>优化方案建议与模型调整指导</span>
            </div>
            <div class="ndclxiInfo">
              <span class="ndclxiDian"></span>
              <span>详细碰撞检查报告编制与解读</span>
            </div>
            <div class="ndclxiInfo">
              <span class="ndclxiDian"></span>
              <span>1次线上成果汇报与问题解答</span>
            </div>
          </div>
          <div class="ndclxItem">
            <div class="ndclxiTitle">服务优势</div>
            <div class="">
              <div class="ndclxiInfo alignCenter">
                <div class="ndclxiIbox frcc">
                  <i class="fa fa-check"></i>
                </div>
                <div class="ndclxiPbox">
                  <p>提前规避风险</p>
                  <p>施工前发现设计问题，减少现场返工</p>
                </div>
              </div>
              <div class="ndclxiInfo alignCenter">
                <div class="ndclxiIbox frcc">
                  <i class="fa fa-check"></i>
                </div>
                <div class="ndclxiPbox">
                  <p>专业分析团队</p>
                  <p>5年以上BIM工程师团队全程服务</p>
                </div>
              </div>
              <div class="ndclxiInfo alignCenter">
                <div class="ndclxiIbox frcc">
                  <i class="fa fa-check"></i>
                </div>
                <div class="ndclxiPbox">
                  <p>可视化成果</p>
                  <p>三维可视化碰撞点展示，直观易懂</p>
                </div>
              </div>
              <div class="ndclxiInfo alignCenter">
                <div class="ndclxiIbox frcc">
                  <i class="fa fa-check"></i>
                </div>
                <div class="ndclxiPbox">
                  <p>优化建议</p>
                  <p>提供专业解决方案，不止于发现问题</p>
                </div>
              </div>
            </div>
          </div>
          <div class="ndclxItem">
            <div class="ndclxiTitle">服务流程</div>
            <div class="">
              <div class="ndclxiInfo fwlcBorder">
                <div class="ndclxiNbox frcc">1</div>
                <div class="ndclxiPbox">
                  <p>需求沟通与资料收集</p>
                  <p>确认服务范围，收集各专业BIM模型及相关资料</p>
                </div>
              </div>
              <div class="ndclxiInfo fwlcBorder">
                <div class="ndclxiNbox frcc">2</div>
                <div class="ndclxiPbox">
                  <p>模型整合与校验</p>
                  <p>对接收的模型进行检查、修复与整合</p>
                </div>
              </div>
              <div class="ndclxiInfo fwlcBorder">
                <div class="ndclxiNbox frcc">3</div>
                <div class="ndclxiPbox">
                  <p>碰撞检测与分析</p>
                  <p>运用专业软件进行全专业碰撞检测与分类</p>
                </div>
              </div>
              <div class="ndclxiInfo fwlcBorder">
                <div class="ndclxiNbox frcc">4</div>
                <div class="ndclxiPbox">
                  <p>报告编制与优化建议</p>
                  <p>生成详细报告并提供专业优化方案</p>
                </div>
              </div>
              <div class="ndclxiInfo fwlcBorder" style="padding-bottom: 0px">
                <div class="ndclxiNbox frcc">5</div>
                <div class="ndclxiPbox">
                  <p>成果交付与答疑</p>
                  <p>交付报告并进行线上成果解读与答疑</p>
                </div>
              </div>
            </div>
          </div>
          <div class="ndclxItem">
            <div class="ndclxiTitle">交付成果示例</div>
            <div class="ndclxiCgBox">
              <div class="ndclxiCgItem">
                <img
                  src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                  alt=""
                />
                <div class="ndclxicIp">碰撞检查报告（ndF版）</div>
              </div>
              <div class="ndclxiCgItem">
                <img
                  src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                  alt=""
                />
                <div class="ndclxicIp">碰撞点可视化模型（BIM格式）</div>
              </div>
            </div>
          </div>
        </div>
        <div class="ndcCptj">
          <div class="ndccTitle">相关产品推荐</div>
          <div class="ndccCgBox">
            <div class="ndccCgItem">
              <img
                src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                alt=""
              />
              <div class="ndccgiContent">
                <div class="ndccgicTitle">施工进度模拟论证服务</div>
                <div class="ndccgicSub">4D进度模拟与关键节点可行性分析</div>
                <div class="frbc">
                  <div class="ndccgicPice">¥10,000.00</div>
                  <button>查看详情</button>
                </div>
              </div>
            </div>
            <div class="ndccCgItem">
              <img
                src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
                alt=""
              />
              <div class="ndccgiContent">
                <div class="ndccgicTitle">施工进度模拟论证服务</div>
                <div class="ndccgicSub">4D进度模拟与关键节点可行性分析</div>
                <div class="frbc">
                  <div class="ndccgicPice">¥10,000.00</div>
                  <button>查看详情</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="ndcRight">
        <div class="ndcrTitle">供应商信息</div>
        <div class="ndcrTop frss">
          <img
            src="https://fastly.picsum.photos/id/905/400/400.jpg?hmac=w2m1CjOADMCbUtrQDbyCuKR7_PNl9koTsKiL89xet5c"
            alt=""
          />
          <div>
            <div class="ndcrtTitle">杭州筑智信息技术有限公司</div>
            <div class="ndcrtRate">
              <el-rate v-model="value1" allow-half />
              <span> 4.8</span>
            </div>
            <div class="ndcrtTag">
              <span>优质供应商</span>
              <span class="ndcrtagShu">|</span>
              <span>BIM技术服务</span>
            </div>
          </div>
        </div>
        <div class="ndcrItem">
          <div class="ndcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="ndcrPbox">
            <p>公司地址</p>
            <p>浙江省杭州市滨江区江南大道1000号智慧大厦15层</p>
          </div>
        </div>
        <div class="ndcrItem">
          <div class="ndcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="ndcrPbox">
            <p>联系电话</p>
            <p>400-888-9001</p>
          </div>
        </div>
        <div class="ndcrItem">
          <div class="ndcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="ndcrPbox">
            <p>电子邮箱</p>
            <p>service@zhuzhi.com</p>
          </div>
        </div>
        <div class="ndcrItem">
          <div class="ndcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="ndcrPbox">
            <p>成立时间</p>
            <p>2025年</p>
          </div>
        </div>
        <button class="ndcrGysxq">
          <span>查看供应商详情</span>
        </button>
        <button class="ndcrZxzx">
          <i class="fa fa-comment"></i>
          <span>在线咨询</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ndPage {
  background-color: #f9fafb;
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

      .ndNavigation {
        margin: 0 auto;
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

        .ndNavigationXg {
          margin: 0 0.5rem;
        }

        .ndNavigationSp {
          color: rgb(22 93 255);
        }
      }
    }

    @media (max-width: 992px) {
      .ndHcontent {
        padding: 6rem 1rem 2rem;
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

    .ndcLeft {
      margin-bottom: 2rem;
      width: 100%;

      .ndclJbcs {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        img {
          width: 100%;
          height: 16rem;
          border-radius: 0.5rem;
        }

        .ndcljCenter {
          margin-top: 1rem;
          width: 100%;

          .ndcljcTop {
            padding: 1rem;
            background-color: rgb(249 250 251);
            border-radius: 0.5rem;

            .ndcljctItem {
              margin-bottom: 0.25rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: rgb(107 114 128);

              .ndcljctiSp1 {
                font-weight: 500;
                font-size: 1.125rem;
                line-height: 1.75rem;
                color: rgb(1 32 96);
              }

              .ndcljctiSp2 {
                font-weight: 700;
                font-size: 1.25rem;
                line-height: 1.75rem;
                color: rgb(22 93 255);
              }
            }
          }

          .ndcljcLxgys {
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

          .ndcljcJrgwc {
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

        .ndcljRight {
          margin-top: 1rem;
          width: 100%;

          .ndcljrTitle {
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
            margin-bottom: 1rem;
          }

          .ndcljrItem {
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

      @media (min-width: 992px) {
        .ndclJbcs {
          display: flex;
          justify-content: space-between;

          img {
            width: calc(33.4% - 2rem);
            height: 16rem;
            border-radius: 0.5rem;
          }

          .ndcljCenter {
            margin-top: 0;
            width: calc(33.3%);
          }

          .ndcljRight {
            margin-top: 0;
            width: calc(33.3%);
          }
        }
      }

      .ndclXq {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .ndclxTitle {
          margin-bottom: 1.5rem;
          padding-bottom: 0.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;
          border-bottom: 1px solid rgb(243 244 246);
        }

        .ndclxSub {
          line-height: 1.5rem;
        }

        .ndclxItem {
          margin-top: 1.5rem;

          .ndclxiTitle {
            margin-bottom: 0.75rem;
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
          }

          .ndclxiInfo {
            position: relative;
            display: flex;
            line-height: 1.5rem;
            padding-bottom: 1rem;

            .ndclxiDian {
              flex-shrink: 0;
              margin-right: 10px;
              margin-top: 0.6rem;
              width: 6px;
              height: 6px;
              border-radius: 999px;
              background-color: rgb(1 32 96);
            }

            .ndclxiIbox {
              flex-shrink: 0;
              margin-right: 0.75rem;
              width: 2rem;
              height: 2rem;
              color: rgb(22 93 255);
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 999px;
            }

            .ndclxiNbox {
              position: absolute;
              top: 0;
              left: -1rem;
              width: 2rem;
              height: 2rem;
              color: #fff;
              background-color: rgb(22 93 255);
              border-radius: 999px;
            }

            .ndclxiPbox {
              p {
                margin: 0;
              }

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

          .ndclxiCgBox {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;

            .ndclxiCgItem {
              cursor: pointer;
              overflow: hidden;
              margin-bottom: 1rem;
              width: 100%;
              background-color: rgb(255 255 255);
              border-radius: 0.5rem;
              box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
              border: 1px solid rgb(229 231 235);

              img {
                width: 100%;
                height: 10rem;
              }

              .ndclxicIp {
                font-size: 0.875rem;
                line-height: 1.25rem;
                text-align: center;
                padding: 0.75rem;
              }
            }

            .ndclxiCgItem:last-child {
              margin-bottom: 0;
            }

            @media (min-width: 992px) {
              .ndclxiCgItem {
                margin-bottom: 0;
                width: calc(50% - 0.5rem);
              }
            }
          }
        }
      }

      .ndcCptj {
        padding: 1.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .ndccTitle {
          margin-bottom: 1.5rem;
          padding-bottom: 0.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;
        }

        .ndccCgBox {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;

          .ndccCgItem {
            cursor: pointer;
            overflow: hidden;
            margin-bottom: 1rem;
            width: 100%;
            background-color: rgb(255 255 255);
            border-radius: 0.5rem;
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            border: 1px solid rgb(229 231 235);

            img {
              width: 100%;
              height: 10rem;
            }

            .ndccgiContent {
              padding: 1rem;

              .ndccgicTitle {
                margin-bottom: 0.5rem;
                font-weight: 700;
                color: rgb(1 32 96);
              }

              .ndccgicSub {
                font-size: 0.875rem;
                line-height: 1.25rem;
                margin-bottom: 0.75rem;
                color: rgb(107 114 128);
              }

              .ndccgicPice {
                line-height: 1.5rem;
                font-weight: 700;
                color: rgb(22 93 255);
              }

              button {
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: rgb(22 93 255);
              }
            }
          }

          .ndccCgItem:last-child {
            margin-bottom: 0;
          }

          @media (min-width: 992px) {
            .ndccCgItem {
              margin-bottom: 0;
              width: calc(50% - 0.5rem);
            }
          }
        }
      }
    }

    @media (min-width: 992px) {
      .ndcLeft {
        margin-bottom: 0;
        width: calc(66.7% - 1rem);
      }
    }

    .ndcRight {
      padding: 1.5rem;
      width: 100%;
      height: 100%;
      background-color: rgb(255 255 255);
      border-radius: 1rem;
      box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

      .ndcrTitle {
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        font-weight: 700;
        font-size: 1.25rem;
        line-height: 1.75rem;
      }

      .ndcrTop {
        margin-bottom: 1.5rem;

        img {
          margin-right: 1rem;
          width: 4rem;
          height: 4rem;
          border-radius: 0.75rem;
        }

        .ndcrtTitle {
          font-weight: 700;
          font-size: 1.125rem;
          line-height: 1.75rem;
        }

        .ndcrtRate {
          display: flex;
          align-items: center;

          span {
            margin-left: 0.25rem;
            font-size: 0.875rem;
            line-height: 1.25rem;
            color: rgb(75 85 99);
          }
        }

        .ndcrtTag {
          color: rgb(107 114 128);
          font-size: 0.875rem;
          line-height: 1.25rem;

          .ndcrtagShu {
            margin: 0.25rem;
          }
        }
      }

      .ndcrItem {
        position: relative;
        display: flex;
        line-height: 1.5rem;
        padding-bottom: 1rem;

        .ndcrIbox {
          flex-shrink: 0;
          margin-right: 0.75rem;
          width: 2rem;
          height: 2rem;
          color: rgb(22 93 255);
          background-color: rgb(22 93 255 / 0.1);
          border-radius: 999px;
        }

        .ndcrPbox {
          p {
            margin: 0;
          }

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

      .ndcrGysxq {
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

      .ndcrZxzx {
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

    @media (min-width: 992px) {
      .ndcRight {
        width: calc(33.3% - 1rem);
      }
    }
  }

  @media (min-width: 992px) {
    .ndCbox {
      padding: 2.5rem 2rem;
      display: flex;
      justify-content: space-between;
    }
  }
}
</style>

<style>
/* 评分 style */
.el-rate {
  padding-bottom: 0.25rem !important;
}
.ndcrTop .el-rate__icon {
  margin-right: 0 !important;
}
</style>
