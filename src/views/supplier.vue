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
  <div class="supplierPage">
    <!-- BANNER -->
    <div class="srbannerBox">
      <img
        src="@/assets/products-banner01.jpeg"
        alt="srbanner"
        style="width: 100vw; height: 40rem"
      />
      <div class="srbannerAbsolute">
        <div class="srbannerContent">
          <div class="srbannerTitle">供应商列表</div>
          <div class="srbannerSubtitle">
            汇聚优质建筑行业供应商资源，提供全方位的人材机信服务，助力项目高效推进
          </div>
        </div>
      </div>
    </div>
    <div class="supplierBox">
      <div class="supplierLeft">
        <div class="supplierClass" :style="windowWidth > 992 ? '' : 'padding: 1rem 0.75rem 0.25rem;'">
          <div class="supplierClassRow">
            <button class="supplierClassColActive">全部</button>
            <button class="supplierClassCol">政策</button>
            <button class="supplierClassCol">标准</button>
            <button class="supplierClassCol">竞赛</button>
            <button class="supplierClassCol">案例</button>
            <button class="supplierClassCol">实施</button>
          </div>
        </div>
        <div class="supplierProducts" :style="windowWidth > 992 ? '' : 'padding: 1rem 0.75rem;'">
          <div class="supplierProductsTitle">
            <div class="supplierProductsTitleText">供应商列表</div>
            <div class="supplierProductsTitlePxfs">
              <span>排序方式：</span>
              <el-select
                v-model="selectvalue"
                placeholder="Select"
                size="large"
                style="width: 110px"
              >
                <el-option label="默认排序" value="01" />
                <el-option label="名称升序" value="02" />
                <el-option label="名称降序" value="03" />
                <el-option label="按地区" value="04" />
                <el-option label="按评分" value="05" />
              </el-select>
            </div>
          </div>
          <div class="supplierProductsBox" :style="windowWidth > 992 ? '' : 'padding: 0;'">
            <div
              class="supplierProductsItem"
              :style="windowWidth > 992 ? 'display: flex; justify-content: space-between;' : ''"
              v-for="index in 4"
              :key="index"
            >
              <div class="supplierPiImgBox" :style="windowWidth > 992 ? '' : 'width: 100%;'">
                <img src="https://picsum.photos/200/200?random=401" class="supplierPiImg" />
                <div class="supplierPiImgTag">政策</div>
              </div>
              <div
                class="supplierPiBox"
                :style="windowWidth > 992 ? '' : 'margin-top:1rem; width: 100%;'"
              >
                <div class="supplierPiTitle">住建部发布《建筑业数字化转型发展指南》推动行业升级</div>
                <div class="supplierPiInfo">
                  近日，住房和城乡建设部正式发布《建筑业数字化转型发展指南》，提出到2025年，建筑业数字化转型取得明显进展，打造一批建筑产业互联网平台，培育一批行业级、企业级数字建造解决方案。指南明确了数字化转型的重点任务和保障措施，为行业发展指明方向。
                </div>
                <div class="supplierPiClass">
                  <div class="supplierPiCleft">
                    <div v-if="windowWidth > 480" class="supplierPiCitrm">
                      <i class="fa fa-calendar"></i>
                      <span class="supplierPiClassSpan">2023-12-15</span>
                    </div>
                    <div class="supplierPiCitrm">
                      <i class="fa fa-eye"></i>
                      <span class="supplierPiClassSpan">1568次预览</span>
                    </div>
                    <div class="supplierPiCitrm">
                      <i class="fa fa-comment-o"></i>
                      <span class="supplierPiClassSpan">42条评论</span>
                    </div>
                  </div>
                  <div v-if="windowWidth > 480" class="supplierPiCright">
                    <button>阅读全文</button>
                    <i class="fa fa-angle-right"></i>
                  </div>
                </div>
                <div v-if="windowWidth <= 480" class="supplierPiClass" style="margin-top: 1rem">
                  <div class="supplierPiCleft">
                    <div class="supplierPiCitrm">
                      <i class="fa fa-calendar"></i>
                      <span class="supplierPiClassSpan">2023-12-15</span>
                    </div>
                    <div class="supplierPiCright">
                      <button>阅读全文</button>
                      <i class="fa fa-angle-right"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="supplierPagination">
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
    </div>
  </div>
</template>

<style lang="scss" scoped>
.supplierPage {
  background-color: #f9fafb;

  .srbannerBox {
    position: relative;
    width: 100vw;
    height: 100%;

    .srbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;
      height: 100%;

      .srbannerContent {
        margin: 0 auto;
        padding: 10rem 30px 6rem;
        width: 100%;
        max-width: 1536px;

        .srbannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          color: #fff;
          font-weight: 700;
        }

        .srbannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 3vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }
      }
    }
  }

  .supplierBox {
    margin: 0 auto;
    padding: 4rem 1rem;
    width: 100%;
    max-width: 1536px;

    .supplierLeft {
      width: 100%;

      .supplierClass {
        margin-bottom: 2rem;
        padding: 1.5rem 1.5rem 0.75rem 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .supplierClassRow {
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          line-height: 1.5rem;

          .supplierClassCol {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            border-radius: 9999px;
          }

          .supplierClassCol:hover {
            cursor: pointer;
            background-color: rgb(243 244 246);
          }

          .supplierClassColActive {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border-radius: 9999px;
          }
        }
      }

      .supplierProducts {
        margin-bottom: 2rem;
        padding: 2rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .supplierProductsTitle {
          margin-bottom: 1.5rem;
          display: flex;
          justify-content: space-between;
          align-items: center;

          .supplierProductsTitleText {
            font-weight: 700;
            font-size: 1.25rem;
            line-height: 1.75rem;
          }

          .supplierProductsTitlePxfs {
            display: flex;
            align-items: center;

            span {
              color: rgb(75 85 99);
            }
          }
        }

        .supplierProductsBox {
          .supplierProductsItem {
            cursor: pointer;
            margin-bottom: 1.5rem;
            padding: 1.5rem;
            // display: flex;
            // align-items: center;
            box-shadow: 1px 1px 10px 0 rgb(0 0 0 / 0.1);
            border-radius: 0.75rem;

            .supplierPiImgBox {
              position: relative;
              width: calc(25% - 0.75rem);

              .supplierPiImg {
                width: 100%;
                height: 200px;
                border-radius: 0.5rem;
              }

              .supplierPiImgTag {
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

            .supplierPiBox {
              width: calc(75% - 0.75rem);

              .supplierPiTitle {
                font-size: 1.5rem;
                line-height: 2rem;
                font-weight: 700;
                margin: 0.75rem 0;
                color: rgb(1 32 96);
              }

              .supplierPiInfo {
                margin-bottom: 1rem;
                line-height: 1.5rem;
                color: rgb(75 85 99);
              }

              .supplierPiClass {
                display: flex;
                align-items: center;
                justify-content: space-between;

                .supplierPiCleft {
                  display: flex;
                  align-items: center;

                  .supplierPiCitrm {
                    margin-right: 1rem;
                    display: flex;
                    align-items: center;
                    color: #6b7280;
                    font-size: 0.875rem;

                    .supplierPiClassSpan {
                      margin-left: 0.25rem;
                    }
                  }
                }

                .supplierPiCright {
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

          .supplierProductsItem:hover {
            animation: jumpUpwards 300ms ease-in-out forwards;
          }

          @media (max-width: 600px) {
            .supplierProductsItem {
              padding: 0.75rem;
            }
          }

          .supplierPagination {
            display: flex;
            justify-content: center;
            align-items: center;
          }
        }
      }

      @media (max-width: 600px) {
        .supplierProducts {
          padding: 1rem;
        }
      }
    }

    .supplierRight {
      width: 100%;

      .supplierRecom {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .supplierRecomTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }

        .supplierRecomImgBox {
          overflow: hidden;
          position: relative;
          height: 16rem;
          border-radius: 0.75rem;

          .supplierRecomImg {
            width: 100%;
            height: 16rem;
            border-radius: 0.75rem;
          }

          .supplierRecomImgIb {
            position: absolute;
            left: 0;
            bottom: 0;
            z-index: 2;
            padding: 1.5rem;

            .supplierRecomImgIbTag {
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

            .supplierRecomImgIbTitle {
              margin-top: 0.5rem;
              margin-bottom: 0.75rem;
              font-weight: 700;
              font-size: 1.25rem;
              line-height: 1.75rem;
              color: #fff;
            }

            .supplierRecomImgIbBtm {
              display: flex;
              align-items: center;

              .supplierRecomImgIbitrm {
                margin-right: 1rem;
                display: flex;
                align-items: center;
                font-size: 0.875rem;
                color: #fff;

                .supplierRecomImgIbSpan {
                  margin-left: 0.25rem;
                }
              }
            }
          }
        }

        .supplierRecomItem {
          margin-top: 1rem;
          display: flex;
          justify-content: space-between;
          align-items: center;

          .supplierRecomLeft {
            display: flex;
            justify-content: flex-start;
            align-items: center;

            .supplierRecomHimg {
              width: 6rem;
              height: 4rem;
              border-radius: 0.5rem;
              margin-right: 1rem;
            }

            .supplierRcbox {
              .supplierRctitle {
                margin-bottom: 0.25rem;
                font-weight: 500;
                line-height: 1.5rem;
              }

              .supplierRcinfo {
                display: flex;
                align-items: center;
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: #6b7280;

                .supplierRcinfoTag {
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

                .supplierRcitrm {
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

      .supplierHot {
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .supplierHotTitle {
          margin-bottom: 1.5rem;
          font-size: 1.25rem;
          line-height: 1.75rem;
          font-weight: 700;
        }

        .supplierHotItem {
          margin-bottom: 1rem;
          padding: 0.75rem 0;
          display: flex;
          justify-content: flex-start;
          border-bottom: 1px solid rgb(243 244 246);

          .supplierHimg {
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

          .supplierHcbox {
            .supplierHctitle {
              margin-bottom: 0.25rem;
              font-weight: 500;
              line-height: 1.5rem;
            }

            .supplierRcinfo {
              display: flex;
              align-items: center;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: #6b7280;

              .supplierRcinfoTag {
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

              .supplierRcitrm {
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

        .supplierHMore {
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

  .supplierFx {
    padding: 4rem 1rem;
    display: flex;
    justify-content: space-between;
  }
}
</style>

<style lang="scss">
.supplierPage {
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
