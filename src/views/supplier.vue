<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
import router from '@/router'
import backToTop from '@/hooks/backToTop'

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

const input2: any = ref()

function pageJump() {
  backToTop()
  router.push({
    name: 'supplier_detail'
  })
}
</script>

<template>
  <div class="supplierPage">
    <!-- BANNER -->
    <div class="srbannerBox">
      <img src="@/assets/partner_banner.jpg" alt="srbanner" style="width: 100vw; height: 40rem" />
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
      <!-- 供应商筛选 -->
      <div class="supplierClass">
        <div class="supplierClassTitle">供应商筛选</div>
        <div class="supplierClassFx">
          <div class="supplierClassFxItem">
            <div class="supplierClassText">所在省份</div>
            <el-select v-model="selectvalue" placeholder="Select" size="large">
              <el-option label="全部省份" value="01" />
              <el-option label="山东省" value="02" />
              <el-option label="山西省" value="03" />
            </el-select>
          </div>
          <div class="supplierClassFxItem">
            <div class="supplierClassText">所在城市</div>
            <el-select v-model="selectvalue" placeholder="Select" size="large">
              <el-option label="全部城市" value="01" />
            </el-select>
          </div>
        </div>
        <div class="supplierClassText">类别</div>
        <div class="supplierClassRow">
          <button class="supplierClassColActive">全部</button>
          <button class="supplierClassCol">数字技工/方案论证</button>
          <button class="supplierClassCol">材料/设备</button>
          <button class="supplierClassCol">智能建造装备</button>
          <button class="supplierClassCol">信息化产品/服务</button>
        </div>
        <el-input
          v-model="input2"
          style="width: 100%; height: 50px; font-size: 1rem"
          placeholder="搜索供应商名称或主营项目..."
          :prefix-icon="Search"
        />
      </div>
      <!-- 供应商列表 -->
      <div class="supplierProducts">
        <div class="supplierProductsTitle">
          <div class="supplierProductsTitleText">供应商列表</div>
          <div class="supplierProductsTitlePxfs">
            <span>排序方式：</span>
            <el-select v-model="selectvalue" placeholder="Select" size="large" style="width: 110px">
              <el-option label="默认排序" value="01" />
              <el-option label="名称升序" value="02" />
              <el-option label="名称降序" value="03" />
              <el-option label="按地区" value="04" />
              <el-option label="按评分" value="05" />
            </el-select>
          </div>
        </div>
        <div class="supplierProductsBox">
          <div class="supplierProductsItem" v-for="index in 5" :key="index">
            <div class="supplierPiContent">
              <div class="supplierPiImgBox">
                <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" class="supplierPiImg" />
                <!-- <div class="supplierPiImgTag">政策</div> -->
              </div>
              <div class="supplierPiBox">
                <div class="supplierPiTop">
                  <div class="supplierPiTitle">杭州筑智信息技术有限公司</div>
                  <div class="supplierPingFen">
                    <i class="fa fa-star"></i>
                    <span>4.8</span>
                  </div>
                </div>
                <div class="supplierPiInfo">
                  <i class="fa fa-tags"></i>
                  主营：BIM技术服务、工程数字化咨询、智能设计方案
                </div>
                <div class="supplierPiInfo">
                  <i class="fa fa-map-marker"></i>
                  所在地：浙江省 杭州市滨江区
                  <i class="fa fa-building-o"></i>
                  成立于2015年
                </div>
                <div class="supplierPiTags">
                  <div class="supplierPiTag">甲级BIM咨询资质</div>
                  <div class="supplierPiTag">施工模拟</div>
                  <div class="supplierPiTag">数字孪生建模</div>
                </div>
                <div class="supplierPiFuwu">
                  <i class="fa fa-check-circle"></i>
                  服务过300+大型项目，含市政、商业综合体领域
                </div>
              </div>
            </div>
            <div class="supplierPiClass">
              <div class="supplierPiCitrm">
                <i class="fa fa-phone"></i>
                <span class="supplierPiClassSpan">400-888-9001 </span>
              </div>
              <div class="supplierPiCright" @click="pageJump">
                <button>查看详情</button>
                <i class="fa fa-angle-right"></i>
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
          color: rgb(1 32 96);
          font-weight: 700;
        }

        .srbannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1rem, 2vw, 1.25rem);
          font-weight: 500;
          color: rgb(1 32 96 / 0.9);
        }
      }
    }
  }

  .supplierBox {
    margin: 0 auto;
    padding: 4rem 1rem;
    width: 100%;
    max-width: 1536px;

    .supplierClass {
      margin-bottom: 2rem;
      padding: 1.5rem;
      border-radius: 1rem;
      color: rgb(1 32 96);
      background-color: #fff;
      box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

      .supplierClassTitle {
        margin-bottom: 1.5rem;
        font-weight: 700;
        font-size: 1.25rem;
        line-height: 1.75rem;
      }

      .supplierClassFx {
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;

        .supplierClassFxItem {
          width: calc(50% - 0.5rem);
        }
      }

      .supplierClassText {
        margin-bottom: 0.5rem;
        font-weight: 500;
        font-size: 0.875rem;
        line-height: 1.25rem;
        color: rgb(55 65 81);
      }

      .supplierClassRow {
        margin-bottom: 0.5rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        line-height: 1.5rem;

        .supplierClassCol {
          margin: 0 0.75rem 0.75rem 0;
          padding: 0.5rem 1.25rem;
          color: rgb(1 32 96);
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          border-radius: 0.25rem;
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
          border-radius: 0.25rem;
        }
      }
    }

    @media (max-width: 992px) {
      .supplierClass {
        padding: 1rem 0.75rem;
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
          flex-shrink: 0;
          cursor: pointer;
          margin-bottom: 1.5rem;
          padding: 1.5rem;
          box-shadow: 1px 1px 10px 0 rgb(0 0 0 / 0.1);
          border-radius: 0.75rem;
          width: calc(50% - 1rem);

          .supplierPiContent {
            .supplierPiImgBox {
              position: relative;
              width: 5rem;
              height: 5rem;

              .supplierPiImg {
                width: 100%;
                height: 5rem;
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
              width: calc(100% - 6rem);

              .supplierPiTop {
                margin-bottom: 0.5rem;
                display: flex;
                justify-content: space-between;
                align-items: center;

                .supplierPiTitle {
                  max-width: calc(100% - 3rem);
                  font-size: 1.25rem;
                  line-height: 1.75rem;
                  font-weight: 700;
                  color: rgb(1 32 96);
                }

                .supplierPingFen {
                  display: flex;
                  align-items: center;
                  color: rgb(245 158 11);

                  i {
                    font-size: 0.875rem;
                    margin-right: 0.25rem;
                  }
                }
              }

              .supplierPiInfo {
                margin-bottom: 0.25rem;
                line-height: 1.25rem;
                color: rgb(75 85 99);

                i:first-child {
                  margin-right: 0.5rem;
                  font-size: 1rem;
                  color: rgb(22 93 255);
                }

                i:nth-child(2) {
                  margin: 0 0.25rem 0 0.75rem;
                  font-size: 0.85rem;
                  color: rgb(75 85 99);
                }
              }

              .supplierPiTags {
                margin: 0.75rem 0;
                display: flex;

                .supplierPiTag {
                  margin-right: 0.5rem;
                  padding: 0.25rem 0.5rem;
                  font-size: 0.75rem;
                  line-height: 1rem;
                  color: rgb(22 93 255);
                  background-color: rgb(22 93 255 / 0.1);
                  border-radius: 0.25rem;
                }
              }

              .supplierPiFuwu {
                font-size: 0.85rem;
                color: rgb(107 114 128);

                i {
                  margin-right: 0.25rem;
                  color: rgb(34 197 94);
                }
              }
            }

            @media (max-width: 992px) {
              .supplierPiImgBox {
                width: 100%;
              }

              .supplierPiBox {
                margin-top: 1rem;
                width: 100%;
              }
            }
          }

          @media (min-width: 992px) {
            .supplierPiContent {
              display: flex;
              justify-content: space-between;
            }
          }

          .supplierPiClass {
            margin-top: 1rem;
            padding-top: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-top: 1px solid rgb(243 244 246);

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

            .supplierPiCright {
              display: flex;
              align-items: center;
              font-weight: 500;
              line-height: 1.5rem;
              color: #1627ff;

              button {
                color: #1627ff;
                margin-right: 0.25rem;
              }
            }
          }
        }

        @media (max-width: 992px) {
          .supplierProductsItem {
            padding: 0.75rem;
            width: 100%;
          }
        }

        .supplierProductsItem:hover {
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }

      @media (min-width: 992px) {
        .supplierProductsBox {
          display: flex;
          justify-content: space-between;
          flex-wrap: wrap;
        }
      }
    }

    @media (max-width: 992px) {
      .supplierProducts {
        padding: 1rem 0.5rem;
      }
    }

    .supplierPagination {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }

  @media screen {
    .supplierBox {
      padding: 4rem 0.5rem;
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
}
.supplierClass {
  .el-select__wrapper {
    border-radius: 0.5rem;
  }

  .el-select__selected-item {
    color: rgb(1 32 96);
  }

  .el-select__icon {
    color: rgb(1 32 96);
  }
}
.supplierProducts {
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
