<script setup lang="ts">
import * as echarts from 'echarts'
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { Search } from '@element-plus/icons-vue'

var myChart: any = null

const echartsMain = ref(null)

function echartsInit() {
  // 基于准备好的dom，初始化echarts实例
  myChart = echarts.init(echartsMain.value)
  // 指定图表的配置项和数据
  const option = {
    color: ['#3B82F690', '#10B98190', '#f59e0b90'],
    title: {
      text: '',
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: '#6a7985',
        },
      },
    },
    legend: {
      bottom: 0,
      data: ['BIM服务', '高性能材料', '智能建造装备'],
    },
    grid: {
      left: 10,
      right: 20,
      top: 20,
      bottom: 40,
      containLabel: true,
    },
    xAxis: [
      {
        type: 'category',
        boundaryGap: false,
        data: ['1月', '2月', '3月', '4月', '5月', '6月'],
      },
    ],
    yAxis: [
      {
        type: 'value',
        offset: 0,
        splitNumber: 8,
        scale: true,
        axisLine: {
          show: true,
          lineStyle: {
            cap: 'round',
          },
        },
        axisLabel: {
          formatter: function (value: any, index: number) {
            return value / 100 + 'k'
          },
        },
      },
    ],
    series: [
      {
        name: 'BIM服务',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [4200, 4500, 4300, 4800, 4600, 5000],
      },
      {
        name: '高性能材料',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [800, 820, 850, 840, 870, 850],
      },
      {
        name: '智能建造装备',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [11000, 11500, 12000, 11800, 12200, 12000],
      },
    ],
  }
  myChart.setOption(option)
}

const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
  if (myChart) {
    myChart.resize()
  }
}

onMounted(() => {
  echartsInit()
  window.addEventListener('resize', updateWindowWidth)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
  if (myChart != null && myChart.dispose) {
    myChart.dispose()
  }
})

const input2: any = ref()
const selectvalue: any = ref('01')

const currentPage2 = ref(2)
const pageSize2 = ref(100)
const handleSizeChange = (val: number) => {
  console.log(`${val} items per page`)
}
const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
}
</script>

<template>
  <div class="materialsPage">
    <!-- BANNER -->
    <div class="prbannerBox">
      <img
        src="@/assets/products-banner01.jpeg"
        alt="prbanner"
        style="width: 100vw; height: 40rem"
      />
      <div class="prbannerAbsolute">
        <div class="prbannerContent">
          <div class="prbannerTitle">聚焦新型城市基础设施建设再起航</div>
          <div class="prbannerSubtitle">绿色化 数字化 智能化</div>
        </div>
      </div>
    </div>
    <div :class="['containerBox', windowWidth > 1140 ? 'containerFx' : '']">
      <div class="containerLeft">
        <div class="containerClass">
          <div class="containerClassRow">
            <button class="containerClassCol">数字技工/方案论证</button>
            <button class="containerClassColActive">材料/设备</button>
            <button class="containerClassCol">智能建造装备</button>
            <button class="containerClassCol">信息化产品/服务</button>
          </div>
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">城市更新</button>
            <button class="containerClassCol">四好建设</button>
            <button class="containerClassCol">智能家居</button>
            <button class="containerClassCol">智能建造</button>
            <button class="containerClassCol">节能系统</button>
            <button class="containerClassCol">其他</button>
          </div>
          <el-input
            v-model="input2"
            style="width: 100%; height: 50px; font-size: 1rem"
            placeholder="搜索产品..."
            :prefix-icon="Search"
          />
        </div>
        <div class="containerProducts">
          <div class="containerProductsTitle">
            <div class="containerProductsTitleText">产品列表</div>
            <div class="containerProductsTitlePxfs">
              <span>排序方式：</span>
              <el-select
                v-model="selectvalue"
                placeholder="Select"
                size="large"
                style="width: 140px"
              >
                <el-option label="价格从低到高" value="01" />
                <el-option label="价格从高到低" value="02" />
                <el-option label="最新更新" value="03" />
              </el-select>
            </div>
          </div>
          <div class="containerProductsBox">
            <div class="containerProductsItem" v-for="index in 4" :key="index">
              <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" alt="" class="containerPiImg" />
              <div class="containerPiBox">
                <div class="containerPiTitle">BIM+多专业碰撞检查</div>
                <div class="containerPiFx">
                  <div class="containerPiFxItem">
                    <span>规格型号：</span>
                    <span>全专业模型整合V2.0</span>
                  </div>
                  <div class="containerPiFxItem">
                    <span>品牌名称：</span>
                    <span>筑智科技</span>
                  </div>
                  <div class="containerPiFxItem">
                    <span>单位：</span>
                    <span>项</span>
                  </div>
                  <div class="containerPiFxItem">
                    <span>供应商：</span>
                    <span>杭州筑智信息技术有限公司</span>
                  </div>
                  <div class="containerPiFxItem">
                    <span>报价时间：</span>
                    <span>2025-06-15</span>
                  </div>
                  <div class="containerPiFxItem">
                    <span>备注：</span>
                    <span>含模型审查报告</span>
                  </div>
                </div>
              </div>
              <div class="containerPiRbox">
                <div class="containerPiRTop">
                  <div class="containerPiRTitem">
                    <span>除税价：</span>
                    <span>¥4,500.00</span>
                  </div>
                  <div class="containerPiRTitem">
                    <span>含税价：</span>
                    <span>¥5,000.00</span>
                  </div>
                  <div class="containerPiRTitem">
                    <span>税率：</span>
                    <span>13%</span>
                  </div>
                </div>
                <button class="containerPiRbtn">查看详情</button>
              </div>
            </div>
            <div class="containerPagination">
              <el-pagination
                v-model:current-page="currentPage2"
                v-model:page-size="pageSize2"
                :page-sizes="[100, 200, 300, 400]"
                size="default"
                background
                layout="prev, pager, next"
                prev-text="上一页"
                next-text="下一页"
                :total="400"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="containerRight">
        <div class="containerPice">
          <div class="containerPiceTitle">价格趋势</div>
          <div ref="echartsMain" style="width: 100%; height: 320px" />
        </div>
        <div class="containerHot">
          <div class="containerHotTitle">热门产品</div>
          <div class="containerHotItem" v-for="index in 4" :key="index">
            <div class="containerHotLeft">
              <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" class="containerHimg" />
              <div class="containerHcbox">
                <div class="containerHctitle">AI生成式设计</div>
                <div class="containerHcinfo">参数化方案比选服务</div>
              </div>
            </div>
            <div class="containerHpice">¥8000</div>
          </div>
          <div class="containerHMore">
            <button>查看更多热门产品</button>
            <i class="fa fa-angle-right" style="margin-left: 0.25rem; font-size: 1.5rem"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.materialsPage {
  background-color: #f9fafb;

  .prbannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .prbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .prbannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1536px;

        .prbannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .prbannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }
      }
    }
  }

  .containerBox {
    margin: 0 auto;
    padding: 4rem 0.5rem;
    width: 100%;
    max-width: 1536px;

    .containerLeft {
      width: 100%;

      .containerClass {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .containerClassRow {
          margin-bottom: 0.75rem;
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          line-height: 1.5rem;

          .containerClassCol {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            border-radius: 0.25rem;
          }

          .containerClassCol:hover {
            cursor: pointer;
            background-color: rgb(243 244 246);
          }

          .containerClassColActive {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border-radius: 0.25rem;
          }
        }
      }

      @media (max-width: 1140px) {
        .containerClass {
          padding: 1rem 0.75rem;
        }
      }

      .containerProducts {
        margin-bottom: 2rem;
        padding: 1.5rem 0;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .containerProductsTitle {
          margin-bottom: 1.5rem;
          padding: 0 1.5rem;
          display: flex;
          justify-content: space-between;
          align-items: center;

          .containerProductsTitleText {
            font-weight: 700;
            font-size: 1.25rem;
            line-height: 1.75rem;
          }

          .containerProductsTitlePxfs {
            display: flex;
            align-items: center;

            span {
              color: rgb(75 85 99);
            }
          }
        }

        @media (max-width: 1140px) {
          .containerProductsTitle {
            padding: 0;
          }
        }

        .containerProductsBox {
          padding: 0 1.5rem;

          .containerProductsItem {
            cursor: pointer;
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid rgb(243 244 246);

            .containerPiImg {
              width: calc(20% - 1rem);
              height: 160px;
              border-radius: 0.5rem;
            }

            @media (max-width: 1140px) {
              .containerPiImg {
                width: 100%;
              }
            }

            .containerPiBox {
              width: calc(60% - 1rem);

              .containerPiTitle {
                margin-bottom: 0.5rem;
                font-size: 1.25rem;
                line-height: 1.75rem;
                font-weight: 700;
                color: rgb(1 32 96);
              }

              .containerPiFx {
                display: flex;
                flex-wrap: wrap;

                .containerPiFxItem {
                  margin-bottom: 0.5rem;
                  width: 50%;
                  font-size: 0.875rem;
                  line-height: 1.25rem;
                  color: rgb(1 32 96);

                  span:first-child {
                    color: rgb(107 114 128);
                  }
                }
              }
            }

            @media (max-width: 1140px) {
              .containerPiBox {
                margin-top: 1rem;
                width: 100%;
              }
            }

            .containerPiRbox {
              width: calc(20% - 1rem);
              display: flex;
              flex-flow: column;

              .containerPiRTop {
                margin-bottom: 0.75rem;
                padding: 0.75rem;
                border-radius: 0.5rem;
                background-color: rgb(249 250 251);

                .containerPiRTitem {
                  margin-bottom: 0.25rem;
                  font-size: 0.875rem;
                  line-height: 1.25rem;
                  color: rgb(107 114 128);
                }
              }

              .containerPiRbtn {
                width: 100%;
                height: 40px;
                text-align: center;
                line-height: 40px;
                color: #fff;
                background-color: rgb(22 93 255);
                border-radius: 0.5rem;
              }
            }

            @media (max-width: 1140px) {
              .containerPiRbox {
                margin-top: 1rem;
                width: 100%;
              }
            }
          }

          @media (min-width: 1140px) {
            .containerProductsItem {
              display: flex;
              justify-content: space-between;
            }
          }

          .containerProductsItem:hover {
            animation: jumpUpwards 300ms ease-in-out forwards;
          }

          .containerPagination {
            display: flex;
            justify-content: center;
            align-items: center;
          }
        }

        @media (max-width: 1140px) {
          .containerProductsBox {
            padding: 0;
          }
        }
      }

      @media (max-width: 1140px) {
        .containerProducts {
          padding: 1rem 0.75rem;
        }
      }
    }

    @media (min-width: 1140px) {
      .containerLeft {
        width: calc(66.7% - 1rem);
      }
    }

    .containerRight {
      width: 100%;

      .containerPice {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .containerPiceTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }
      }

      .containerHot {
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .containerHotTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }

        .containerHotItem {
          cursor: pointer;
          margin-bottom: 1rem;
          padding: 0.75rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: rgb(249 250 251);
          border-radius: 0.5rem;

          .containerHotLeft {
            display: flex;
            justify-content: flex-start;
            align-items: center;

            .containerHimg {
              width: 4rem;
              height: 4rem;
              border-radius: 0.5rem;
              margin-right: 1rem;
            }

            .containerHcbox {
              .containerHctitle {
                font-weight: 500;
                line-height: 1.5rem;
              }

              .containerHcinfo {
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: #6b7280;
              }
            }
          }

          .containerHpice {
            font-weight: 700;
            color: rgb(22 93 255);
          }
        }

        .containerHotItem:hover {
          animation: jumpUpwards 300ms ease-in-out forwards;
        }

        .containerHMore {
          cursor: pointer;
          display: flex;
          justify-content: center;
          align-items: center;
          font-weight: 500;
          color: rgb(22 93 255);

          button {
            color: rgb(22 93 255);
            line-height: 1.5rem;
          }
        }
      }

      @media (max-width: 1140px) {
        .containerPice {
          padding: 1rem 0.75rem;
        }

        .containerHot {
          padding: 1rem 0.75rem;
        }
      }
    }

    @media (min-width: 1140px) {
      .containerRight {
        width: calc(33.3% - 1rem);
      }
    }
  }

  .containerFx {
    padding: 4rem 1rem;
    display: flex;
    justify-content: space-between;
  }
}
</style>

<style lang="scss">
.materialsPage {
  .el-input__wrapper {
    border-radius: 0.5rem;
  }

  .btn-prev {
    color: rgb(107 114 128) !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    line-height: 1.25rem !important;
    padding: 0.5rem 0.75rem !important;
    background-color: #fff !important;
    border: 1px solid rgb(209 213 219) !important;
    border-radius: 0.25rem !important;
  }

  .btn-next {
    color: rgb(107 114 128) !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    line-height: 1.25rem !important;
    padding: 0.5rem 0.75rem !important;
    background-color: #fff !important;
    border: 1px solid rgb(209 213 219) !important;
    border-radius: 0.25rem !important;
  }

  .el-select__wrapper {
    background-color: #e9e9ed;
    border-radius: 0.5rem;
  }

  .el-select__selected-item {
    color: rgb(1 32 96);
  }

  .el-select__icon {
    color: rgb(1 32 96);
  }
}
</style>
