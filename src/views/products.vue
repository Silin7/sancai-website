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
    title: {
      text: 'Stacked Area Chart',
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
      data: ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine'],
    },
    toolbox: {
      feature: {
        saveAsImage: {},
      },
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true,
    },
    xAxis: [
      {
        type: 'category',
        boundaryGap: false,
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      },
    ],
    yAxis: [
      {
        type: 'value',
      },
    ],
    series: [
      {
        name: 'Email',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [120, 132, 101, 134, 90, 230, 210],
      },
      {
        name: 'Union Ads',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [220, 182, 191, 234, 290, 330, 310],
      },
      {
        name: 'Video Ads',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [150, 232, 201, 154, 190, 330, 410],
      },
      {
        name: 'Direct',
        type: 'line',
        stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [320, 332, 301, 334, 390, 330, 320],
      },
      {
        name: 'Search Engine',
        type: 'line',
        stack: 'Total',
        label: {
          show: true,
          position: 'top',
        },
        areaStyle: {},
        emphasis: {
          focus: 'series',
        },
        data: [820, 932, 901, 934, 1290, 1330, 1320],
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
  <div class="productsPage">
    <!-- BANNER -->
    <div class="prbannerBox">
      <img src="@/assets/products-banner01.jpeg" alt="prbanner" style="width: 100vw; height: 40rem" />
      <div class="prbannerAbsolute">
        <div class="prbannerContent">
          <div class="prbannerTitle">聚焦新型城市基础设施建设再起航</div>
          <div class="prbannerSubtitle">绿色化 数字化 智能化</div>
        </div>
      </div>
    </div>
    <div :class="['containerBox', windowWidth > 1140 ? 'containerFx' : '']">
      <div class="containerLeft" :style="windowWidth > 1140 ? 'width: calc(66.7% - 1rem);' : ''">
        <div class="containerClass" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">人</button>
            <button class="containerClassCol">材</button>
            <button class="containerClassCol">机</button>
            <button class="containerClassCol">信</button>
          </div>
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">一般建筑</button>
            <button class="containerClassCol">医疗建筑</button>
            <button class="containerClassCol">体育场馆</button>
            <button class="containerClassCol">超高层建筑</button>
          </div>
          <!-- 0.75rem -->
          <el-input v-model="input2" style="width: 100%; height: 50px; font-size: 1rem" placeholder="搜索产品..."
            :prefix-icon="Search" />
        </div>
        <div class="containerProducts" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="containerProductsTitle" :style="windowWidth > 1140 ? '' : 'padding: 0;'">
            <div class="containerProductsTitleText">产品列表</div>
            <div class="containerProductsTitlePxfs">
              <span>排序方式：</span>
              <el-select v-model="selectvalue" placeholder="Select" size="large" style="width: 140px">
                <el-option label="价格从低到高" value="01" />
                <el-option label="价格从高到低" value="02" />
                <el-option label="最新更新" value="03" />
              </el-select>
            </div>
          </div>
          <div class="containerProductsBox" :style="windowWidth > 1140 ? '' : 'padding: 0;'">
            <div class="containerProductsItem"
              :style="windowWidth > 1140 ? 'display: flex; justify-content: space-between;' : ''" v-for="index in 4"
              :key="index">
              <img src="https://picsum.photos/200/200?random=103" alt="" class="containerPiImg"
                :style="windowWidth > 1140 ? '' : 'width: 100%;'" />
              <div class="containerPiBox" :style="windowWidth > 1140 ? '' : 'margin-top:1rem; width: 100%;'">
                <div class="containerPiTitle">BIM+多专业碰撞检查</div>
                <div class="containerPiInfo">基于BIM技术的多专业碰撞检查服务，提前发现设计冲突</div>
                <div class="containerPiClass">
                  <div class="containerPiCitrm">
                    <i class="fa fa-user-o" style="font-size: 0.875rem; color: #6b7280"></i>
                    <span class="containerPiClassSpan">人工服务</span>
                  </div>
                  <div class="containerPiCitrm">
                    <i class="fa fa-building-o" style="font-size: 0.875rem; color: #6b7280"></i>
                    <span class="containerPiClassSpan">全建筑类别</span>
                  </div>
                </div>
              </div>
              <div class="containerPiPbox" :style="windowWidth > 1140 ? '' : 'margin-top:1rem; width: 100%;'">
                <div class="containerPiPice">¥5000</div>
                <div class="containerPiUnit">/项目</div>
              </div>
              <div class="containerPiRbox" :style="windowWidth > 1140 ? '' : 'margin-top:1rem; width: 100%;'">
                <button class="containerPiRbtn">查看详情</button>
              </div>
            </div>
            <div class="containerPagination">
              <!-- total, sizes, prev, pager, next, jumper -->
              <el-pagination v-model:current-page="currentPage2" v-model:page-size="pageSize2"
                :page-sizes="[100, 200, 300, 400]" size="default" background layout="prev, pager, next" :total="400"
                @size-change="handleSizeChange" @current-change="handleCurrentChange" />
            </div>
          </div>
        </div>
      </div>
      <div class="containerRight" :style="windowWidth > 1140 ? 'width: calc(33.3% - 1rem);' : ''">
        <div class="containerPice" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="containerPiceTitle">价格趋势</div>
          <div ref="echartsMain" style="width: 100%; height: 320px" />
        </div>
        <div class="containerHot" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="containerHotTitle">热门产品</div>
          <div class="containerHotItem" v-for="index in 4" :key="index">
            <div class="containerHotLeft">
              <img src="https://picsum.photos/200/200?random=103" class="containerHimg" />
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
.productsPage {
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
        max-width: 1720px;

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
    max-width: 1720px;

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
            border-radius: 9999px;
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
            border-radius: 9999px;
          }
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

        .containerProductsBox {
          padding: 0 1.5rem;

          .containerProductsItem {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid rgb(243 244 246);

            .containerPiImg {
              width: calc(20% - 1rem);
              height: 160px;
              border-radius: 0.5rem;
            }

            .containerPiBox {
              width: calc(40% - 1rem);

              .containerPiTitle {
                font-size: 1.125rem;
                line-height: 1.75rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
                color: rgb(1 32 96);
              }

              .containerPiInfo {
                margin-bottom: 1rem;
                line-height: 1.5rem;
                color: rgb(75 85 99);
              }

              .containerPiClass {
                display: flex;
                align-items: center;

                .containerPiCitrm {
                  margin-right: 1rem;
                  display: flex;
                  align-items: center;

                  .containerPiClassSpan {
                    margin-left: 0.25rem;
                    color: #6b7280;
                  }
                }
              }
            }

            .containerPiPbox {
              width: calc(20% - 1rem);
              display: flex;
              flex-flow: column;
              align-items: center;

              .containerPiPice {
                font-size: 1.5rem;
                line-height: 2rem;
                font-weight: 700;
                color: rgb(22 93 255);
              }

              .containerPiUnit {
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: #6b7280;
              }
            }

            .containerPiRbox {
              width: calc(20% - 1rem);
              display: flex;
              flex-flow: column;
              justify-content: flex-end;

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
.productsPage {
  .el-input__wrapper {
    border-radius: 0.5rem;
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
