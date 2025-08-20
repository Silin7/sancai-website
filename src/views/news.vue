<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { fileURL } from '@/api/baseConfig'
import pageJump from '@/hooks/pageJump'
import { articlescatesApi, articlesApi, articlescateApi } from '@/api/modules/article'

// 可视窗口宽度
const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

// 用户端-获取所有启用的文章分类（公开接口）
const articlescates: any = ref([])

function getArticlescates() {
  articlescatesApi().then((res: any) => {
    articlescates.value = res
  })
}

// 文章分类 active
const articlesAid: any = ref('')

function articlesChange(id: string) {
  articlesAid.value = id
  getArticles()
}

// 用户端-文章列表（公开接口，支持筛选分页）

const currentPage: any = ref(1)
const pageSize: any = ref(10)
const total: any = ref(0)
const articles: any = ref([])

function getArticles() {
  articlesApi({
    page: currentPage.value,
    pageSize: pageSize.value,
    cateId: articlesAid.value,
    // IN DOUBT cateId 查询条件无效
  }).then((res: any) => {
    total.value = res.total
    articles.value = res.items
  })
}

// function aaa() {
//   articlescateApi('13').then((res: any) => {
//     console.log('-------->', res)
//   })
// }

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
  getArticlescates()
  getArticles()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
})

const selectvalue: any = ref('01')
</script>

<template>
  <div class="newsPage">
    <!-- BANNER -->
    <div class="nsbannerBox">
      <img src="@/assets/news-banner.jpg" alt="nsbanner" />
      <div class="nsbannerAbsolute">
        <div class="nsbannerContent">
          <div class="nsbannerTitle">热点资讯</div>
          <div class="nsbannerSubtitle">
            聚焦建筑行业数字化转型，提供最新政策、标准、案例和市场动态
          </div>
          <button class="nsbannerLlspbtn">浏览视频</button>
        </div>
      </div>
    </div>

    <div class="newsBox">
      <div class="newsLeft">
        <!-- 资讯分类 -->
        <div class="newsClass">
          <div class="newsClassRow">
            <button :class="articlesAid === '' ? 'newsClassColActive' : 'newsClassCol'" @click="articlesChange('')">
              全部
            </button>
            <button v-for="(item, index) in articlescates" :key="index"
              :class="articlesAid === item.id ? 'newsClassColActive' : 'newsClassCol'" @click="articlesChange(item.id)">
              {{ item.name }}
            </button>
          </div>
        </div>
        <!-- 资讯列表 -->
        <div class="newsProducts">
          <div class="newsProductsTitle">
            <div class="newsProductsTitleText">最新资讯</div>
            <div class="newsProductsTitlePxfs">
              <span v-if="windowWidth > 1140">排序方式：</span>
              <el-select v-model="selectvalue" placeholder="Select" size="large" style="width: 110px">
                <el-option label="最新发布" value="01" />
                <el-option label="最热文章" value="02" />
                <el-option label="最多评论" value="03" />
              </el-select>
            </div>
          </div>
          <div class="newsProductsBox">
            <div class="newsProductsItem" v-for="(item, index) in articles" :key="index" @click="pageJump('news_detail', {
              articlesid: item.id
            })">
              <div class="newsPiImgBox">
                <img :src="fileURL + item.thumbnail" class="newsPiImg" />
                <div class="newsPiImgTag">政策</div>
              </div>
              <div class="newsPiBox">
                <div class="newsPiTitle">{{ item.title }}</div>
                <div class="newsPiInfo">
                  {{ item.description }}
                </div>
                <div class="newsPiClass">
                  <div class="newsPiCleft">
                    <div v-if="windowWidth > 480" class="newsPiCitrm">
                      <i class="fa fa-calendar"></i>
                      <span class="newsPiClassSpan">{{ item.created_at }}</span>
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
              <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :page-sizes="[10, 20]"
                size="default" background layout="prev, pager, next" prev-text="上一页" next-text="下一页" :total="total"
                @current-change="getArticles" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.newsPage {
  background-color: #f9fafb;
  overflow-x: hidden;

  .nsbannerBox {
    position: relative;
    width: 100vw;
    height: 40rem;

    @media (max-width: 768px) {
      height: 30rem;
    }

    img {
      width: 100vw;
      height: 100%;
    }

    .nsbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;

      .nsbannerContent {
        margin: 0 auto;
        padding: 10rem 2rem 0;
        width: 100%;
        max-width: 1536px;

        @media (max-width: 768px) {
          padding: 6rem 1rem 0;
        }

        .nsbannerTitle {
          margin-bottom: 1.5rem;
          font-size: clamp(2rem, 4vw, 3rem);
          font-weight: 700;
          line-height: 1.25;
          color: rgb(1 32 96 / var(--tw-text-opacity, 1));
        }

        .nsbannerSubtitle {
          margin-bottom: 2rem;
          max-width: 42rem;
          font-size: clamp(1.25rem, 4vw, 1.5rem);
          font-weight: 500;
          color: rgb(1 32 96 / 0.9);
        }

        .nsbannerLlspbtn {
          padding: 0.75rem 2rem;
          color: #fff;
          background-color: rgb(22 93 255);
          border-radius: 9999px;
          box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

          @media (max-width: 768px) {
            padding: 0.75rem 1.5rem;
          }
        }
      }
    }
  }

  .newsBox {
    margin: 0 auto;
    padding: 1rem;
    width: 100%;
    max-width: 1536px;

    @media (min-width: 992px) {
      padding: 4rem 1rem;
    }

    .newsLeft {
      width: 100%;

      .newsClass {
        margin-bottom: 2rem;
        padding: 1.5rem 1.5rem 0.75rem 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 768px) {
          padding: 1rem 1rem 0.5rem;
        }

        .newsClassRow {
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          line-height: 1.5rem;

          .newsClassCol {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow:
              0 10px 15px -3px rgb(0 0 0 / 0.1),
              0 4px 6px -4px rgb(0 0 0 / 0.1);
            border: 1px solid rgb(243 244 246);
            border-radius: 9999px;

            @media (max-width: 768px) {
              margin: 0 0.5rem 0.5rem 0;
              padding: 0.5rem 1rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
            }
          }

          .newsClassCol:hover {
            @media (min-width: 768px) {
              background-color: rgb(243 244 246);
            }
          }

          .newsClassColActive {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border: 1px solid rgb(243 244 246);
            border-radius: 9999px;

            @media (max-width: 768px) {
              margin: 0 0.5rem 0.5rem 0;
              padding: 0.5rem 1rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
            }
          }
        }
      }

      .newsProducts {
        // margin-bottom: 2rem;
        padding: 2rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 768px) {
          padding: 1rem;
        }

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
            margin-bottom: 1.5rem;
            padding: 1.5rem;
            display: flex;
            justify-content: space-between;
            box-shadow:
              0 10px 15px -3px rgb(0 0 0 / 0.1),
              0 4px 6px -4px rgb(0 0 0 / 0.1);
            border-radius: 0.75rem;

            @media (max-width: 768px) {
              padding: 1rem;
              display: block;
            }

            .newsPiImgBox {
              position: relative;
              width: calc(25% - 0.75rem);

              @media (max-width: 768px) {
                width: 100%;
              }

              .newsPiImg {
                width: 100%;
                height: 200px;
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

              @media (max-width: 768px) {
                margin-top: 1rem;
                width: 100%;
              }

              .newsPiTitle {
                margin-bottom: 1rem;
                font-size: 1.25rem;
                line-height: 1.75rem;
                font-weight: 700;
                color: rgb(1 32 96);
              }

              .newsPiInfo {
                margin-bottom: 1rem;
                line-height: 1.25rem;
                color: rgb(75 85 99);

                @media (min-width: 768px) {
                  min-height: 7rem;
                }
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
                    color: rgb(107 114 128);
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
                  font-size: 0.875rem;
                  color: rgb(22 93 255);

                  button {
                    margin-right: 0.5rem;
                    font-size: 0.875rem;
                    color: rgb(22 93 255);
                  }
                }
              }
            }
          }

          .newsProductsItem:hover {
            @media (min-width: 768px) {
              cursor: pointer;
              animation: jumpUpwards 300ms ease-in-out forwards;
            }
          }

          .newsPagination {
            display: flex;
            justify-content: center;
            align-items: center;
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
