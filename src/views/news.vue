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
  <div class="newsPage">
    <!-- BANNER -->
    <div class="bannerBox">
      <img
        src="@/assets/products-banner01.jpeg"
        alt="banner"
        mode="aspectFill"
        style="width: 100vw; height: 40rem"
      />
      <div class="bannerAbsolute">
        <div class="bannerContent">
          <div class="bannerTitle">热点资讯</div>
          <div class="bannerSubtitle">
            聚焦建筑行业数字化转型，提供最新政策、标准、案例和市场动态
          </div>
        </div>
      </div>
    </div>
    <div :class="['newsBox', windowWidth > 1140 ? 'newsFx' : '']">
      <div class="newsLeft" :style="windowWidth > 1140 ? 'width: calc(66.7% - 1rem);' : ''">
        <div class="newsClass" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="newsClassRow">
            <button class="newsClassColActive">全部</button>
            <button class="newsClassCol">政策</button>
            <button class="newsClassCol">标准</button>
            <button class="newsClassCol">竞赛</button>
            <button class="newsClassCol">案例</button>
            <button class="newsClassCol">实施</button>
          </div>
        </div>
        <div class="newsProducts" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="newsProductsTitle">
            <div class="newsProductsTitleText">最新资讯</div>
            <div class="newsProductsTitlePxfs">
              <span>排序方式：</span>
              <el-select
                v-model="selectvalue"
                placeholder="Select"
                size="large"
                style="width: 110px"
              >
                <el-option label="最新发布" value="01" />
                <el-option label="最热文章" value="02" />
                <el-option label="最多评论" value="03" />
              </el-select>
            </div>
          </div>
          <div class="newsProductsBox" :style="windowWidth > 1140 ? '' : 'padding: 0;'">
            <div
              class="newsProductsItem"
              :style="windowWidth > 1140 ? 'display: flex; justify-content: space-between;' : ''"
              v-for="index in 4"
              :key="index"
            >
              <div class="newsPiImgBox">
                <img
                  src="https://picsum.photos/200/200?random=103"
                  class="newsPiImg"
                  :style="windowWidth > 1140 ? '' : 'width: 100%;'"
                />
                <div class="newsPiImgTag">政策</div>
              </div>
              <div
                class="newsPiBox"
                :style="windowWidth > 1140 ? '' : 'margin-top:1rem; width: 100%;'"
              >
                <div class="newsPiTitle">住建部发布《建筑业数字化转型发展指南》推动行业升级</div>
                <div class="newsPiInfo">
                  近日，住房和城乡建设部正式发布《建筑业数字化转型发展指南》，提出到2025年，建筑业数字化转型取得明显进展，打造一批建筑产业互联网平台，培育一批行业级、企业级数字建造解决方案。
                </div>
                <div class="newsPiClass">
                  <div class="newsPiCleft">
                    <div class="newsPiCitrm">
                      <i class="fa fa-calendar" style="font-size: 0.875rem; color: #6b7280"></i>
                      <span class="newsPiClassSpan">2023-12-15</span>
                    </div>
                    <div class="newsPiCitrm">
                      <i class="fa fa-eye" style="font-size: 0.875rem; color: #6b7280"></i>
                      <span class="newsPiClassSpan">1568次预览</span>
                    </div>
                    <div class="newsPiCitrm">
                      <i class="fa fa-comment-o" style="font-size: 0.875rem; color: #6b7280"></i>
                      <span class="newsPiClassSpan">42条评论</span>
                    </div>
                  </div>
                  <div class="newsPiCright">
                    阅读全文
                    <i class="fa fa-angle-right" style="margin-left: 0.5rem"></i>
                  </div>
                </div>
              </div>
            </div>
            <div class="newsPagination">
              <!-- total, sizes, prev, pager, next, jumper -->
              <el-pagination
                v-model:current-page="currentPage2"
                v-model:page-size="pageSize2"
                :page-sizes="[100, 200, 300, 400]"
                size="default"
                background
                layout="prev, pager, next"
                :total="400"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="newsRight" :style="windowWidth > 1140 ? 'width: calc(33.3% - 1rem);' : ''">
        <div class="newsPice" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="newsPiceTitle">价格趋势</div>
          <div ref="echartsMain" style="width: 100%; height: 320px" />
        </div>
        <div class="newsHot" :style="windowWidth > 1140 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="newsHotTitle">热门产品</div>
          <div class="newsHotItem" v-for="index in 4" :key="index">
            <div class="newsHotLeft">
              <img src="https://picsum.photos/200/200?random=103" class="newsHimg" />
              <div class="newsHcbox">
                <div class="newsHctitle">AI生成式设计</div>
                <div class="newsHcinfo">参数化方案比选服务</div>
              </div>
            </div>
            <div class="newsHpice">¥8000</div>
          </div>
          <div class="newsHMore">
            <button>查看更多热门产品</button>
            <i class="fa fa-angle-right" style="margin-left: 0.25rem; font-size: 1.5rem"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.newsPage {
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

  .newsBox {
    margin: 0 auto;
    padding: 4rem 0.5rem;
    width: 100%;
    max-width: 1720px;

    .newsLeft {
      width: 100%;

      .newsClass {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .newsClassRow {
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          line-height: 1.5rem;

          .newsClassCol {
            margin-right: 0.75rem;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            border-radius: 9999px;
          }

          .newsClassCol:hover {
            cursor: pointer;
            background-color: rgb(243 244 246);
          }

          .newsClassColActive {
            margin-right: 0.75rem;
            padding: 0.5rem 1.25rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border-radius: 9999px;
          }
        }
      }

      .newsProducts {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .newsProductsTitle {
          margin-bottom: 1.5rem;
          display: flex;
          justify-content: space-between;
          align-items: center;

          .newsProductsTitleText {
            font-weight: 700;
            font-size: 1.25rem;
            line-height: 1.75rem;
          }

          .newsProductsTitlePxfs {
            display: flex;
            align-items: center;

            span {
              color: rgb(75 85 99);
            }
          }
        }

        .newsProductsBox {
          .newsProductsItem {
            cursor: pointer;
            margin-bottom: 1.5rem;
            padding: 1.5rem;
            box-shadow: 1px 1px 10px 0 rgb(0 0 0 / 0.1);
            border-radius: 0.75rem;

            .newsPiImgBox {
              position: relative;
              width: calc(25% - 0.75rem);

              .newsPiImg {
                width: 100%;
                height: 200px;
                border-radius: 0.5rem;
                object-fit: cover;
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
              width: calc(75% - 0.75rem);

              .newsPiTitle {
                font-size: 1.125rem;
                line-height: 1.75rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
                color: rgb(1 32 96);
              }

              .newsPiInfo {
                margin-bottom: 1rem;
                line-height: 1.5rem;
                color: rgb(75 85 99);
              }

              .newsPiClass {
                display: flex;
                align-items: center;
                justify-content: space-between;

                .newsPiCleft {
                  display: flex;
                  align-items: center;

                  .newsPiCitrm {
                    margin-right: 1rem;
                    display: flex;
                    align-items: center;

                    .newsPiClassSpan {
                      margin-left: 0.25rem;
                      color: #6b7280;
                    }
                  }
                }

                .newsPiCright {
                  display: flex;
                  align-items: center;
                  font-weight: 500;
                  line-height: 1.5rem;
                  color: #1627ff;
                }
              }
            }
          }

          .newsProductsItem:hover {
            animation: jumpUpwards 300ms ease-in-out forwards;
          }

          .newsPagination {
            display: flex;
            justify-content: center;
            align-items: center;
          }
        }
      }
    }

    .newsRight {
      width: 100%;

      .newsPice {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .newsPiceTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }
      }

      .newsHot {
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .newsHotTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }

        .newsHotItem {
          margin-bottom: 1rem;
          padding: 0.75rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: rgb(249 250 251);
          border-radius: 0.5rem;

          .newsHotLeft {
            display: flex;
            justify-content: flex-start;
            align-items: center;

            .newsHimg {
              width: 4rem;
              height: 4rem;
              border-radius: 0.5rem;
              margin-right: 1rem;
            }

            .newsHcbox {
              .newsHctitle {
                font-weight: 500;
                line-height: 1.5rem;
              }

              .newsHcinfo {
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: #6b7280;
              }
            }
          }

          .newsHpice {
            font-weight: 700;
            color: rgb(22 93 255);
          }
        }

        .newsHMore {
          cursor: pointer;
          display: flex;
          justify-content: center;
          align-items: center;
          font-weight: 500;
          color: rgb(22 93 255);

          span {
            line-height: 1.5rem;
          }
        }
      }
    }
  }

  .newsFx {
    padding: 4rem 1rem;
    display: flex;
    justify-content: space-between;
  }
}
</style>

<style lang="scss">
.newsPage {
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
