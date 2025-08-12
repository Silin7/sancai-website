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
    <div class="prbannerBox">
      <img src="@/assets/ai-banner-source.jpg" alt="prbanner" style="width: 100vw; height: 40rem" />
      <div class="prbannerAbsolute">
        <div class="prbannerContent">
          <div class="prbannerTitle">专业视频课程</div>
          <div class="prbannerSubtitle">
            本系列视频聚焦数字化与AI技术深度融合的行业实践，全景呈现“技术+场景”的创新生态，助力建筑行业从传统经验模式迈向数据智能时代。
          </div>
          <button class="bannerllkcbtn">浏览课程</button>
        </div>
      </div>
    </div>

    <!-- CONTENT BOX -->
    <div class="containerBox">
      <div class="containerLeft">
        <!-- 筛选视频 -->
        <div class="containerClass">
          <div class="frbc">
            <div class="containerClassTitle">筛选视频</div>
            <div class="containerClassNumber"><span>128</span>个视频</div>
          </div>
          <div class="containerClassTbox">
            <i class="fa fa-laptop"></i>
            <div class="containerClassText">平台分类</div>
          </div>
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">BMI技术</button>
            <button class="containerClassCol">智能制造</button>
            <button class="containerClassCol">造价管理</button>
          </div>
          <div class="containerClassTbox">
            <div class="containerClassText">视频类型</div>
          </div>
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">免费</button>
            <button class="containerClassCol">付费</button>
          </div>
          <div class="containerClassTbox">
            <div class="containerClassText">视频时长</div>
          </div>
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">10分钟以内</button>
            <button class="containerClassCol">10-30分钟</button>
            <button class="containerClassCol">30分钟以上</button>
          </div>
          <el-input
            v-model="input2"
            style="width: 100%; height: 50px; font-size: 1rem"
            placeholder="搜索视频..."
            :prefix-icon="Search"
          />
        </div>
        <!-- 精选视频 -->
        <div class="containerProducts">
          <div class="containerProductsTitle">
            <div class="containerProductsTitleText">精选视频</div>
            <div class="containerProductsTitlePxfs">
              <span>排序方式：</span>
              <el-select
                v-model="selectvalue"
                placeholder="Select"
                size="large"
                style="width: 140px"
              >
                <el-option label="最新视频" value="01" />
                <el-option label="价格从低到高" value="02" />
                <el-option label="价格从高到低" value="03" />
                <el-option label="最多人学习" value="04" />
              </el-select>
            </div>
          </div>
          <div class="containerProductsBox">
            <div class="containerProductsItem" v-for="index in 4" :key="index">
              <div class="containerPiImg">
                <div v-if="index % 2 === 0" class="containerPiTime">45分钟</div>
                <div v-else class="containerPiBuy"><i class="fa fa-check"></i>已购买</div>
                <img
                  src="@/assets/photo-1560518883-ce09059eeffa.jpg"
                  alt=""
                  style="width: 100%; height: 100%"
                />
                <div class="containerPiplayerBox">
                  <div class="containerPiplayerICon">
                    <i class="fa fa-play"></i>
                  </div>
                </div>
                <div class="containerPiprogress">
                  <div class="containerPiprogressBar" style="width: 80%"></div>
                </div>
              </div>
              <div class="containerPiBox">
                <div class="supplierPiTop">
                  <div class="supplierPiTitle">杭州筑智信息技术有限公司</div>
                  <div v-if="index % 2 === 0" class="supplierPingFen">¥299</div>
                  <div v-else class="supplierPingFen2">¥299</div>
                </div>
                <div class="containerPiInfo">基于BIM技术的多专业碰撞检查服务，提前发现设计冲突</div>
                <div class="containerPiClass">
                  <div class="containerPiCitrm">人工服务</div>
                  <div class="containerPiCitrm">全建筑类别</div>
                </div>
                <div class="containerPiPbox">
                  <div class="containerPiPice">
                    <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="" />
                    <span>张老师</span>
                  </div>
                  <div class="containerPiPice">
                    <i class="fa fa-users"></i>
                    <span style="color: rgb(107 114 128)">3421</span>
                  </div>
                </div>
              </div>
              <button v-if="index % 2 === 0" class="containerPiRbtn">查看详情</button>
              <button v-else class="containerPiRbtn2">查看详情</button>
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
      <div class="containerRight">
        <!-- 用户登录 -->
        <div class="containerLogin">
          <div class="frsc">
            <div class="containerLoginIcon">
              <i class="fa fa-user"></i>
            </div>
            <div>
              <div class="containerLoginName">游客，您好</div>
              <div class="containerLoginTips">登录解锁更多功能</div>
            </div>
          </div>
          <button class="containerLoginBtn">登录 / 注册</button>
          <div class="containerLoginMy">
            <div>
              <div class="containerLoginMn">0</div>
              <div class="containerLoginMt">我的视频</div>
            </div>
            <div>
              <div class="containerLoginMn">0</div>
              <div class="containerLoginMt">学习时长</div>
            </div>
            <div>
              <div class="containerLoginMn">0</div>
              <div class="containerLoginMt">收藏视频</div>
            </div>
          </div>
        </div>
        <!-- 热门视频 -->
        <div class="containerHot">
          <div class="containerHotTitle">热门视频</div>
          <div class="containerHotItem" v-for="index in 4" :key="index">
            <div class="containerHotLeft">
              <img src="@/assets/photo-1560518883-ce09059eeffa.jpg" class="containerHimg" />
              <div class="containerHcbox">
                <div class="containerHctitle">Revit建筑建模实战</div>
                <div class="containerHcinfo">BIM技术·CAD</div>
              </div>
            </div>
            <div class="containerHpice">¥499</div>
          </div>
          <div class="containerHMore">
            <button>查看更多热门视频</button>
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
  overflow-x: hidden;

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
        padding: 10rem 2rem 6rem;
        width: 100%;
        max-width: 1536px;

        .prbannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 5vw, 3.5rem);
          font-weight: 700;
          line-height: 1.25;
          color: rgb(1 32 96);
        }

        .prbannerSubtitle {
          max-width: 42rem;
          margin-bottom: 2rem;
          font-size: clamp(1rem, 2vw, 1.25rem);
          list-style: 1.875rem;
          font-weight: 500;
          color: rgb(1 32 96 / 0.9);
        }

        .bannerllkcbtn {
          padding: 0.75rem 1.5rem;
          color: #fff;
          background-color: rgb(22 93 255 / 0.9);
          border-radius: 9999px;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        }

        .bannerllkcbtn:hover {
          transform: scale(1.05);
          box-shadow: 2px 2px 10px 0 rgb(22 93 255);
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

        .containerClassTitle {
          margin-bottom: 1.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;
        }

        .containerClassNumber {
          line-height: 1.25rem;
          color: rgb(75 85 99 / var(--tw-text-opacity, 1));

          span {
            margin-right: 0.25rem;
            font-weight: 700;
            color: rgb(22 93 255 / var(--tw-text-opacity, 1));
          }
        }

        .containerClassTbox {
          align-items: center;
          display: flex;
          margin-bottom: 0.75rem;

          i {
            margin-right: 0.5rem;
            font-size: 1rem;
            color: rgb(22 93 255);
          }

          .containerClassText {
            font-weight: 500;
            line-height: 1.5rem;
          }
        }

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

      @media (max-width: 992px) {
        .containerClass {
          padding: 1.5rem 0.75rem;
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

        @media (max-width: 992px) {
          .containerProductsTitle {
            padding: 0 0.75rem;
          }
        }

        .containerProductsBox {
          padding: 0 0.5rem 0 1.5rem;
          display: flex;
          flex-wrap: wrap;

          .containerProductsItem {
            overflow: hidden;
            margin-right: 1rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            width: calc(33.3% - 1rem);
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            border-radius: 0.75rem;
            background-color: #fff;

            .containerPiImg {
              position: relative;
              width: 100%;
              height: 12rem;

              .containerPiTime {
                position: absolute;
                top: 0.75rem;
                right: 0.75rem;
                z-index: 2;
                font-size: 0.75rem;
                line-height: 1rem;
                padding-top: 0.25rem;
                padding-bottom: 0.25rem;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
                background-color: rgb(255 255 255 / 0.8);
                border-radius: 9999px;
              }

              .containerPiBuy {
                position: absolute;
                top: 0.75rem;
                right: 0.75rem;
                z-index: 2;
                font-size: 0.75rem;
                line-height: 1rem;
                padding-top: 0.25rem;
                padding-bottom: 0.25rem;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
                color: #fff;
                background-color: rgb(22 93 255 / var(--tw-bg-opacity, 1));
                border-radius: 9999px;

                i {
                  margin-right: 0.25rem;
                }
              }

              .containerPiplayerBox {
                position: absolute;
                top: calc(50% - 1.7rem);
                left: calc(50% - 1.7rem);
                height: 3.4rem;
                width: 3.4rem;
                z-index: 2;

                .containerPiplayerICon {
                  cursor: pointer;
                  height: 3.4rem;
                  width: 3.4rem;
                  display: flex;
                  align-items: center;
                  justify-content: center;
                  border-radius: 9999px;
                  background-color: rgb(255 255 255 / 0.8);

                  i {
                    font-size: 1.5rem;
                    line-height: 2rem;
                    color: rgb(22 93 255);
                  }
                }

                .containerPiplayerICon:hover {
                  background-color: rgb(255 255 255);
                  transform: scale(1.05);
                }
              }
              .containerPiprogress {
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                height: 4px;

                .containerPiprogressBar {
                  height: 4px;
                  background-color: rgb(22 93 255);
                }
              }
            }

            .containerPiBox {
              padding: 1rem;

              .supplierPiTop {
                margin-bottom: 0.5rem;
                display: flex;
                justify-content: space-between;
                align-items: flex-start;

                .supplierPiTitle {
                  max-width: calc(100% - 3rem);
                  font-size: 1.25rem;
                  line-height: 1.75rem;
                  font-weight: 700;
                  color: rgb(1 32 96);
                }

                .supplierPingFen {
                  font-weight: 700;
                  line-height: 1.75rem;
                  color: rgb(22 93 255);
                }

                .supplierPingFen2 {
                  line-height: 1.75rem;
                  text-decoration: line-through;
                  color: rgb(156 163 175);
                }
              }

              .containerPiTitle {
                font-size: 1.25rem;
                line-height: 1.75rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
                color: rgb(1 32 96);
              }

              .containerPiInfo {
                margin-bottom: 1rem;
                font-size: 0.875rem;
                line-height: 1.25rem;
                color: rgb(75 85 99);
              }

              .containerPiClass {
                display: flex;
                flex-wrap: wrap;
                align-items: center;

                .containerPiCitrm {
                  margin-left: 0.25rem;
                  margin-right: 0.25rem;
                  margin-bottom: 0.25rem;
                  display: inline-block;
                  border-radius: 9999px;
                  background-color: rgb(243 244 246);
                  padding-left: 0.5rem;
                  padding-right: 0.5rem;
                  padding-top: 0.25rem;
                  padding-bottom: 0.25rem;
                  font-size: 0.75rem;
                  line-height: 1rem;
                  color: rgb(55 65 81);
                }
              }
            }

            .containerPiPbox {
              margin-top: 1rem;
              width: 100%;
              display: flex;
              align-items: center;
              justify-content: space-between;

              .containerPiPice {
                display: flex;
                align-items: center;

                i {
                  margin-right: 0.5rem;
                  font-size: 1rem;
                  color: rgb(107 114 128);
                }

                img {
                  border-radius: 9999px;
                  width: 2rem;
                  height: 2rem;
                  margin-right: 0.5rem;
                }

                span {
                  font-size: 0.875rem;
                  line-height: 1.25rem;
                }
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
            }

            .containerPiRbtn {
              display: inline-block;
              margin: 0 1rem;
              width: calc(100% - 2rem);
              height: 40px;
              text-align: center;
              line-height: 40px;
              color: #fff;
              background-color: rgb(22 93 255 / 0.9);
              border-radius: 0.5rem;
            }

            .containerPiRbtn2 {
              display: inline-block;
              margin: 0 1rem;
              width: calc(100% - 2rem);
              height: 40px;
              text-align: center;
              line-height: 40px;
              color: #fff;
              background-color: rgb(54 207 201 / 0.9);
              border-radius: 0.5rem;
            }
          }
        }

        @media (max-width: 992px) {
          .containerProductsBox {
            padding: 0 0.75rem;

            .containerProductsItem {
              margin-right: 0;
              width: 100%;
            }
          }
        }

        .containerPagination {
          display: flex;
          justify-content: center;
          align-items: center;
        }
      }
    }

    .containerRight {
      width: calc(33.3% - 1rem);

      .containerLogin {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: #fff;
        background-image: linear-gradient(to bottom right, #165dff, #36cfc9);
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .containerLoginIcon {
          padding: 0.5rem;
          background-color: rgb(255 255 255 / 0.2);
          border-radius: 0.5rem;
          margin-right: 0.75rem;

          i {
            font-size: 1.25rem;
            line-height: 1.75rem;
          }
        }

        .containerLoginName {
          font-weight: 700;
          line-height: 1.5rem;
        }

        .containerLoginTips {
          opacity: 0.8;
          font-size: 0.875rem;
          line-height: 1.25rem;
        }

        button {
          margin-top: 1rem;
          display: block;
          width: 100%;
          padding-top: 0.5rem;
          padding-bottom: 0.5rem;
          text-align: center;
          font-weight: 500;
          border-radius: 0.5rem;
          color: rgb(22 93 255);
          background-color: rgb(243 244 246);
        }

        .containerLoginMy {
          margin-top: 1rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .containerLoginMn {
          font-weight: 700;
          font-size: 1.5rem;
          line-height: 2rem;
          text-align: center;
        }

        .containerLoginMt {
          opacity: 0.8;
          font-size: 0.875rem;
          line-height: 1.25rem;
          text-align: center;
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

      @media (max-width: 992px) {
        .containerHot {
          padding: 1rem 0.75rem;
        }
      }
    }

    @media (max-width: 992px) {
      .containerRight {
        width: 100%;
      }
    }
  }

  @media (min-width: 992px) {
    .containerBox {
      display: flex;
      justify-content: space-between;

      .containerLeft {
        width: calc(66.7% - 1rem);
      }
    }
  }
}
</style>

<style lang="scss">
.productsPage {
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
