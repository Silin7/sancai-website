<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { Search } from '@element-plus/icons-vue'

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
    <div class="bannerBox">
      <img src="@/assets/products-banner01.jpeg" alt="banner" mode="aspectFill"
        :style="['width: 100vw;', windowWidth < 600 ? 'height: 60rem;' : 'height: 48rem;']" />
      <div class="bannerAbsolute">
        <div class="bannerContent">
          <div class="bannerTitle">聚焦新型城市基础设施建设再起航</div>
          <div class="bannerSubtitle">绿色化 数字化 智能化</div>
        </div>
      </div>
    </div>
    <div :class="['containerBox', windowWidth > 1140 ? 'containerFx' : '']">
      <div class="containerLeft" :style="windowWidth > 1140 ? 'width: calc(66.7% - 1rem);' : ''">
        <div class="containerClass">
          <div class="containerClassRow">
            <div class="containerClassColActive">全部</div>
            <div class="containerClassCol">人</div>
            <div class="containerClassCol">材</div>
            <div class="containerClassCol">机</div>
            <div class="containerClassCol">信</div>
          </div>
          <div class="containerClassRow">
            <div class="containerClassColActive">全部</div>
            <div class="containerClassCol">一般建筑</div>
            <div class="containerClassCol">医疗建筑</div>
            <div class="containerClassCol">体育场馆</div>
            <div class="containerClassCol">超高层建筑</div>
          </div>
          <!-- 0.75rem -->
          <el-input v-model="input2" style="width: 100%; height: 50px; font-size: 1rem;" placeholder="搜索产品..."
            :prefix-icon="Search" />
        </div>
        <div class="containerProducts">
          <div class="containerProductsTitle">
            <div class="containerProductsTitleText">产品列表</div>
            <div class="containerProductsTitlePxfs">
              <span>排序方式：</span>
              <el-select v-model="selectvalue" placeholder="Select" size="large" style="width: 140px;">
                <el-option label="价格从低到高" value="01" />
                <el-option label="价格从高到低" value="02" />
                <el-option label="最新更新" value="03" />
              </el-select>
            </div>
          </div>
          <div class="containerProductsBox">
            <div class="containerProductsItem">
              <img src="https://picsum.photos/200/200?random=103" alt="" class="containerPiImg">
              <div class="containerPiBox">
                <div class="containerPiTitle">BIM+多专业碰撞检查</div>
                <div class="containerPiInfo">基于BIM技术的多专业碰撞检查服务，提前发现设计冲突</div>
                <div class="containerPiClass">
                  <div class="containerPiCitrm">
                    <i class="fa fa-user-o"></i>
                    <span class="containerPiClassSpan"> 人工服务</span>
                  </div>
                  <div class="containerPiCitrm">
                    <i class="fa fa-building-o"></i>
                    <span class="containerPiClassSpan"> 全建筑类别</span>
                  </div>
                </div>
              </div>
              <div class="containerPiPbox">
                <div class="containerPiPice">¥5000</div>
                <div class="containerPiUnit">/项目</div>
              </div>
              <div class="containerPiRbox">
                <div class="containerPiRbtn">查看详情</div>
              </div>
            </div>
            <!-- total, sizes, prev, pager, next, jumper -->
            <el-pagination v-model:current-page="currentPage2" v-model:page-size="pageSize2"
              :page-sizes="[100, 200, 300, 400]" size="default" background layout="prev, pager, next" :total="400"
              @size-change="handleSizeChange" @current-change="handleCurrentChange" style="width: 100%; " />
          </div>
        </div>
      </div>
      <div class="containerRight" :style="windowWidth > 1140 ? 'width: calc(33.3% - 1rem);' : ''">
        <div class="containerPice">
          <div class="containerPiceTitle">价格趋势</div>
          <div class="">这个是图表</div>
        </div>
        <div class="containerHot">
          <div class="containerHotTitle">热门产品</div>
          <div class="containerHotItem">
            <img src="https://picsum.photos/200/200?random=103" alt="containerHimg">
            <div class="containerHcbox">
              <div class="containerHctitle">AI生成式设计</div>
              <div class="containerHcinfo">参数化方案比选服务</div>
            </div>
            <div class="containerHpice">¥8000</div>
          </div>
          <div class="">
            <span>查看更多热门产品</span>
            <i class="fa fa-angle-right"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.productsPage {
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
      }
    }
  }

  .containerBox {
    margin: 0 auto;
    padding: 6rem 1rem;
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
        box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);

        .containerClassRow {
          margin-bottom: 1.5rem;
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          line-height: 1.5rem;

          .containerClassCol {
            margin-right: 0.75rem;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
            border-radius: 9999px;
          }

          .containerClassCol:hover {
            cursor: pointer;
            background-color: rgb(243 244 246);
          }

          .containerClassColActive {
            margin-right: 0.75rem;
            padding: 0.5rem 1.25rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border-radius: 9999px;
          }
        }
      }

      .containerProducts {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);

        .containerProductsTitle {
          margin-bottom: 1.5rem;
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
        box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
      }

      .containerHot {
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 2px 0 rgb(0 0 0 / 0.1);
      }
    }
  }

  .containerFx {
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
    border-radius: 0.5rem;
  }
}
</style>
