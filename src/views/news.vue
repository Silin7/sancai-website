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
    <div class="nsbannerBox">
      <img
        src="@/assets/products-banner01.jpeg"
        alt="nsbanner"
        style="width: 100vw; height: 40rem"
      />
      <div class="nsbannerAbsolute">
        <div class="nsbannerContent">
          <div class="nsbannerTitle">热点资讯</div>
          <div class="nsbannerSubtitle">
            聚焦建筑行业数字化转型，提供最新政策、标准、案例和市场动态
          </div>
        </div>
      </div>
    </div>
    <div :class="['newsBox', windowWidth > 992 ? 'newsFx' : '']">
      <div class="newsLeft" :style="windowWidth > 992 ? 'width: calc(66.7% - 1rem);' : ''">
        <div class="newsClass" :style="windowWidth > 992 ? '' : 'padding: 1rem 0.75rem 0.25rem;'">
          <div class="newsClassRow">
            <button class="newsClassColActive">全部</button>
            <button class="newsClassCol">政策</button>
            <button class="newsClassCol">标准</button>
            <button class="newsClassCol">竞赛</button>
            <button class="newsClassCol">案例</button>
            <button class="newsClassCol">实施</button>
          </div>
        </div>
        <div class="newsProducts" :style="windowWidth > 992 ? '' : 'padding: 1rem 0.75rem;'">
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
          <div class="newsProductsBox" :style="windowWidth > 992 ? '' : 'padding: 0;'">
            <div
              class="newsProductsItem"
              :style="windowWidth > 992 ? 'display: flex; justify-content: space-between;' : ''"
              v-for="index in 4"
              :key="index"
            >
              <div class="newsPiImgBox" :style="windowWidth > 992 ? '' : 'width: 100%;'">
                <img src="https://picsum.photos/200/200?random=401" class="newsPiImg" />
                <div class="newsPiImgTag">政策</div>
              </div>
              <div
                class="newsPiBox"
                :style="windowWidth > 992 ? '' : 'margin-top:1rem; width: 100%;'"
              >
                <div class="newsPiTitle">住建部发布《建筑业数字化转型发展指南》推动行业升级</div>
                <div class="newsPiInfo">
                  近日，住房和城乡建设部正式发布《建筑业数字化转型发展指南》，提出到2025年，建筑业数字化转型取得明显进展，打造一批建筑产业互联网平台，培育一批行业级、企业级数字建造解决方案。
                </div>
                <div class="newsPiClass">
                  <div class="newsPiCleft">
                    <div v-if="windowWidth > 480" class="newsPiCitrm">
                      <i class="fa fa-calendar"></i>
                      <span class="newsPiClassSpan">2023-12-15</span>
                    </div>
                    <div class="newsPiCitrm">
                      <i class="fa fa-eye"></i>
                      <span class="newsPiClassSpan">1568次预览</span>
                    </div>
                    <div class="newsPiCitrm">
                      <i class="fa fa-comment-o"></i>
                      <span class="newsPiClassSpan">42条评论</span>
                    </div>
                  </div>
                  <div v-if="windowWidth > 480" class="newsPiCright">
                    <button>阅读全文</button>
                    <i class="fa fa-angle-right"></i>
                  </div>
                </div>
                <div v-if="windowWidth <= 480" class="newsPiClass" style="margin-top: 1rem">
                  <div class="newsPiCleft">
                    <div class="newsPiCitrm">
                      <i class="fa fa-calendar"></i>
                      <span class="newsPiClassSpan">2023-12-15</span>
                    </div>
                    <div class="newsPiCright">
                      <button>阅读全文</button>
                      <i class="fa fa-angle-right"></i>
                    </div>
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
      <div class="newsRight" :style="windowWidth > 992 ? 'width: calc(33.3% - 1rem);' : ''">
        <div class="newsRecom" :style="windowWidth > 992 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="newsRecomTitle">推荐文章</div>
          <div class="newsRecomImgBox">
            <img
              src="https://picsum.photos/200/200?random=401"
              class="newsRecomImg"
              :style="windowWidth > 992 ? '' : 'width: 100%;'"
            />
            <div class="newsRecomImgIb">
              <span class="newsRecomImgIbTag">政策</span>
              <div class="newsRecomImgIbTitle">"十四五"建筑业发展规划解读：数字化转型是核心</div>

              <div class="newsRecomImgIbBtm">
                <div class="newsRecomImgIbitrm">
                  <i class="fa fa-calendar"></i>
                  <span class="newsRecomImgIbSpan">2023-12-15</span>
                </div>
                <div class="newsRecomImgIbitrm">
                  <i class="fa fa-eye"></i>
                  <span class="newsRecomImgIbSpan">1568次预览</span>
                </div>
              </div>
            </div>
          </div>
          <div class="newsRecomItem" v-for="index in 4" :key="index">
            <div class="newsRecomLeft">
              <img src="https://picsum.photos/200/200?random=401" class="newsRecomHimg" />
              <div class="newsRcbox">
                <div class="newsRctitle">BIM技术在大型医院建设中的应用实践</div>
                <div class="newsRcinfo">
                  <div class="newsRcinfoTag">案例</div>
                  <div class="newsRcitrm">
                    <i class="fa fa-calendar"></i>
                    <span>2023-12-15</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="newsHot" :style="windowWidth > 992 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="newsHotTitle">热门文章</div>
          <div class="newsHotItem" v-for="index in 4" :key="index">
            <div class="newsHimg">{{ index }}</div>
            <div class="newsHcbox">
              <div class="newsHctitle">智慧工地AI监控系统招投标技术要求解析{{ index }}</div>
              <div class="newsRcinfo">
                <div class="newsRcinfoTag">实施</div>
                <div class="newsRcitrm">
                  <i class="fa fa-eye"></i>
                  <span>{{ (index + 1) * 998 }}次浏览</span>
                </div>
              </div>
            </div>
          </div>
          <!-- <div class="newsHMore">
            <button>查看更多热门产品</button>
            <i class="fa fa-angle-right" style="margin-left: 0.25rem; font-size: 1.5rem"></i>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.newsPage {
  background-color: #f9fafb;

  .nsbannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .nsbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .nsbannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1720px;

        .nsbannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .nsbannerSubtitle {
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
        padding: 1.5rem 1.5rem 0.75rem 1.5rem;
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
            margin: 0 0.75rem 0.75rem 0;
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
            margin: 0 0.75rem 0.75rem 0;
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
                    color: #6b7280;
                    font-size: 0.875rem;

                    .newsPiClassSpan {
                      margin-left: 0.25rem;
                    }
                  }
                }

                .newsPiCright {
                  display: flex;
                  align-items: center;
                  font-weight: 500;
                  line-height: 1.5rem;
                  color: #1627ff;

                  button {
                    color: #1627ff;
                    margin-right: 0.5rem;
                  }
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

      .newsRecom {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .newsRecomTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }

        .newsRecomImgBox {
          overflow: hidden;
          position: relative;
          height: 16rem;
          border-radius: 0.75rem;

          .newsRecomImg {
            width: 100%;
            height: 16rem;
            border-radius: 0.75rem;
          }

          .newsRecomImgIb {
            position: absolute;
            left: 0;
            bottom: 0;
            z-index: 2;
            padding: 1.5rem;

            .newsRecomImgIbTag {
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

            .newsRecomImgIbTitle {
              margin-top: 0.5rem;
              margin-bottom: 0.75rem;
              font-weight: 700;
              font-size: 1.25rem;
              line-height: 1.75rem;
              color: #fff;
            }

            .newsRecomImgIbBtm {
              display: flex;
              align-items: center;

              .newsRecomImgIbitrm {
                margin-right: 1rem;
                display: flex;
                align-items: center;
                font-size: 0.875rem;
                color: #fff;

                .newsRecomImgIbSpan {
                  margin-left: 0.25rem;
                }
              }
            }
          }
        }

        .newsRecomItem {
          margin-top: 1rem;
          display: flex;
          justify-content: space-between;
          align-items: center;

          .newsRecomLeft {
            display: flex;
            justify-content: flex-start;
            align-items: center;

            .newsRecomHimg {
              width: 6rem;
              height: 4rem;
              border-radius: 0.5rem;
              margin-right: 1rem;
            }

            .newsRcbox {
              .newsRctitle {
                margin-bottom: 0.25rem;
                font-weight: 500;
                line-height: 1.5rem;
              }

              .newsRcinfo {
                display: flex;
                align-items: center;
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: #6b7280;

                .newsRcinfoTag {
                  margin-right: 0.5rem;
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

                .newsRcitrm {
                  display: flex;
                  align-items: center;
                  color: #6b7280;
                  font-size: 0.875rem;

                  span {
                    margin-left: 0.25rem;
                  }
                }
              }
            }
          }
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
          padding: 0.75rem 0;
          display: flex;
          justify-content: flex-start;
          border-bottom: 1px solid rgb(243 244 246);

          .newsHimg {
            margin-right: 0.75rem;
            display: flex;
            height: 2rem;
            width: 2rem;
            flex-shrink: 0;
            align-items: center;
            justify-content: center;
            border-radius: 0.5rem;
            background-color: rgb(22 93 255 / 0.1);
            font-weight: 700;
            color: rgb(22 93 255);
          }

          .newsHcbox {
            .newsHctitle {
              margin-bottom: 0.25rem;
              font-weight: 500;
              line-height: 1.5rem;
            }

            .newsRcinfo {
              display: flex;
              align-items: center;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: #6b7280;

              .newsRcinfoTag {
                margin-right: 0.5rem;
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

              .newsRcitrm {
                display: flex;
                align-items: center;
                color: #6b7280;
                font-size: 0.875rem;

                span {
                  margin-left: 0.25rem;
                }
              }
            }
          }
        }

        .newsHMore {
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
