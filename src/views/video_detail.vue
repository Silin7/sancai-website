<script setup lang="ts">
import dayjs from 'dayjs'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import pageJump from '@/hooks/pageJump'
import { fileURL } from '@/api/baseConfig'
import formatCurrency from '@/hooks/formatCurrency'
import { videodetailApi } from '@/api/modules/video'

// 路由信息
const route = useRoute()
const videoid: any = ref("")
const videoDetails: any = ref({})

function getVideodetail() {
  videodetailApi(videoid.value).then((res: any) => {
    if (res) {
      videoDetails.value = res
    }
  })
}

onMounted(() => {
  videoid.value = route.query.id
  getVideodetail()
})

const value1 = ref(4.8)
</script>

<template>
  <div class="pdPage">
    <div class="pdCbox">
      <div class="pdcLeft">
        <div class="pdclJbcs">
          <img v-if="videoDetails.imgs" :src="fileURL + videoDetails.imgs[0]" alt="产品图片" />
          <img v-else src="" alt="产品图片" />
          <div class="pdcljCenter">
            <div class="pdcljcTop">
              <div class="pdcljctItem">
                <span>除税价：</span>
                <span class="pdcljctiSp1">¥{{ formatCurrency(videoDetails.afertaxprice, 2) }}</span>
              </div>
              <div class="pdcljctItem">
                <span>含税价：</span>
                <span class="pdcljctiSp2">¥{{ formatCurrency(videoDetails.pretaxprice, 2) }}</span>
              </div>
              <div class="pdcljctItem">
                <span>税率：</span>
                <span class="pdcljctiSp1">{{ videoDetails.taxrate }}%</span>
              </div>
            </div>
            <button class="pdcljcLxgys">
              <i class="fa fa-phone"></i>
              <span>联系视频</span>
            </button>
            <!-- <button class="pdcljcJrgwc">
              <i class="fa fa-shopping-cart"></i>
              <span>加入购物车</span>
            </button> -->
          </div>
          <div class="pdcljRight">
            <div class="pdcljrTitle">基本参数</div>
            <div class="pdcljrItem">
              <span>品牌名称：</span>
              <span>{{ videoDetails.brand }}</span>
            </div>
            <!-- <div class="pdcljrItem">
              <span>服务周期：</span>
              <span>5-7个工作日</span>
            </div>
            <div class="pdcljrItem">
              <span>服务方式：</span>
              <span>线上+线下结合</span>
            </div>
            <div class="pdcljrItem">
              <span>交付成果：</span>
              <span>碰撞检查报告+优化建议</span>
            </div> -->
            <div class="pdcljrItem">
              <span>报价时间：</span>
              <span>{{ dayjs(videoDetails.quote_time).format('YYYY-MM-DD') }}</span>
            </div>
          </div>
        </div>
        <div class="pdclXq">
          <div class="pdclxTitle">介绍</div>
          <div class="" v-html="videoDetails.content"></div>
        </div>
      </div>
      <div class="pdcRight">
        <div class="pdcrTitle">视频信息</div>
        <div class="pdcrTop frsc">
          <img v-if="videoDetails.supplier_info && videoDetails.supplier_info.company_imgs"
            :src="fileURL + videoDetails.supplier_info.company_imgs[0]" alt="" />
          <div>
            <div v-if="videoDetails.supplier_info" class="pdcrtTitle">
              {{ videoDetails.supplier_info.company_name }}
            </div>
            <!-- <div class="pdcrtRate">
              <el-rate v-model="value1" allow-half />
              <span> 4.8</span>
            </div> -->
            <div v-if="videoDetails.supplier_info" class="pdcrtTag">
              <span v-for="(item, index) in videoDetails.supplier_info.tags" :key="index">{{
                item
                }}</span>
              <span v-for="(item, index) in videoDetails.supplier_info.tags" :key="index" class="pdcrtagShu">|</span>
            </div>
          </div>
        </div>
        <div class="pdcrItem">
          <div class="pdcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="pdcrPbox">
            <p>公司地址</p>
            <p v-if="videoDetails.supplier_info">
              {{ videoDetails.supplier_info.company_address }}
            </p>
          </div>
        </div>
        <div class="pdcrItem">
          <div class="pdcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="pdcrPbox">
            <p>联系电话</p>
            <p v-if="videoDetails.supplier_info">{{ videoDetails.supplier_info.tel }}</p>
          </div>
        </div>
        <div class="pdcrItem">
          <div class="pdcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="pdcrPbox">
            <p>电子邮箱</p>
            <p v-if="videoDetails.supplier_info">{{ videoDetails.supplier_info.email }}</p>
          </div>
        </div>
        <div class="pdcrItem">
          <div class="pdcrIbox frcc">
            <i class="fa fa-check"></i>
          </div>
          <div class="pdcrPbox">
            <p>成立时间</p>
            <p v-if="videoDetails.supplier_info">
              {{ dayjs(videoDetails.supplier_info.establish_time).format('YYYY年MM月DD日') }}
            </p>
          </div>
        </div>
        <button class="pdcrGysxq">
          <span>查看视频详情</span>
        </button>
        <button class="pdcrZxzx">
          <i class="fa fa-comment"></i>
          <span>在线咨询</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.pdPage {
  background-color: #f9fafb;
  overflow-x: hidden;

  .pdCbox {
    position: relative;
    margin: 0 auto;
    padding: 5rem 1rem 1rem;
    width: 100%;
    max-width: 1536px;
    color: rgb(1 32 96);

    @media (min-width: 992px) {
      padding: 6rem 2rem 2rem;
      display: flex;
      justify-content: space-between;
    }

    .pdcLeft {
      margin-bottom: 2rem;
      width: 100%;

      @media (min-width: 992px) {
        margin-bottom: 0;
        width: calc(66.7% - 1rem);
      }

      .pdclJbcs {
        margin-bottom: 2rem;
        padding: 1rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (min-width: 992px) {
          padding: 1.5rem;
          display: flex;
          justify-content: space-between;
        }

        img {
          width: 100%;
          height: 16rem;
          border-radius: 0.5rem;

          @media (min-width: 992px) {
            width: calc(33.4% - 2rem);
            height: 16rem;
            border-radius: 0.5rem;
          }
        }

        .pdcljCenter {
          margin-top: 1rem;
          width: 100%;

          @media (min-width: 992px) {
            margin-top: 0;
            width: calc(33.3%);
          }

          .pdcljcTop {
            padding: 1rem;
            background-color: rgb(249 250 251);
            border-radius: 0.5rem;

            .pdcljctItem {
              margin-bottom: 0.25rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
              color: rgb(107 114 128);

              .pdcljctiSp1 {
                font-weight: 500;
                font-size: 1.125rem;
                line-height: 1.75rem;
                color: rgb(1 32 96);
              }

              .pdcljctiSp2 {
                font-weight: 700;
                font-size: 1.25rem;
                line-height: 1.75rem;
                color: rgb(22 93 255);
              }
            }
          }

          .pdcljcLxgys {
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

          .pdcljcJrgwc {
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

        .pdcljRight {
          margin-top: 1rem;
          width: 100%;

          @media (min-width: 992px) {
            margin-top: 0;
            width: calc(33.3%);
          }

          .pdcljrTitle {
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
            margin-bottom: 1rem;
          }

          .pdcljrItem {
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

      .pdclXq {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 768px) {
          padding: 1rem;
        }

        .pdclxTitle {
          margin-bottom: 1.5rem;
          padding-bottom: 0.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;
          border-bottom: 1px solid rgb(243 244 246);
        }

        .pdclxSub {
          line-height: 1.5rem;
        }

        .pdclxItem {
          margin-top: 1.5rem;

          .pdclxiTitle {
            margin-bottom: 0.75rem;
            font-weight: 700;
            font-size: 1.125rem;
            line-height: 1.75rem;
          }

          .pdclxiInfo {
            position: relative;
            display: flex;
            line-height: 1.5rem;
            padding-bottom: 1rem;

            .pdclxiDian {
              flex-shrink: 0;
              margin-right: 10px;
              margin-top: 0.6rem;
              width: 6px;
              height: 6px;
              border-radius: 9999px;
              background-color: rgb(1 32 96);
            }

            .pdclxiIbox {
              flex-shrink: 0;
              margin-right: 0.75rem;
              width: 2rem;
              height: 2rem;
              color: rgb(22 93 255);
              background-color: rgb(22 93 255 / 0.1);
              border-radius: 9999px;
            }

            .pdclxiNbox {
              position: absolute;
              top: 0;
              left: -1rem;
              width: 2rem;
              height: 2rem;
              color: #fff;
              background-color: rgb(22 93 255);
              border-radius: 9999px;
            }

            .pdclxiPbox {
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

          .pdclxiCgBox {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;

            .pdclxiCgItem {
              overflow: hidden;
              margin-bottom: 1rem;
              width: 100%;
              background-color: rgb(255 255 255);
              border-radius: 0.5rem;
              box-shadow:
                0 10px 15px -3px rgb(0 0 0 / 0.1),
                0 4px 6px -4px rgb(0 0 0 / 0.1);
              border: 1px solid rgb(229 231 235);

              @media (min-width: 992px) {
                margin-bottom: 0;
                width: calc(50% - 0.5rem);
              }

              img {
                width: 100%;
                height: 10rem;
              }

              .pdclxicIp {
                font-size: 0.875rem;
                line-height: 1.25rem;
                text-align: center;
                padding: 0.75rem;
              }
            }

            .pdclxiCgItem:last-child {
              margin-bottom: 0;
            }

            .pdclxiCgItem:hover {
              @media (min-width: 768px) {
                cursor: pointer;
              }
            }
          }
        }
      }

      .pdcCptj {
        padding: 1.5rem;
        padding-bottom: 0.5rem;
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 768px) {
          padding: 1rem 1rem 0 1rem;
        }

        .pdccTitle {
          margin-bottom: 1.5rem;
          // padding-bottom: 0.5rem;
          font-weight: 700;
          font-size: 1.25rem;
          line-height: 1.75rem;

          @media (max-width: 768px) {
            margin-bottom: 1rem;
          }
        }

        .pdccCgBox {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;

          .pdccCgItem {
            overflow: hidden;
            margin-bottom: 1rem;
            width: 100%;
            background-color: rgb(255 255 255);
            border-radius: 0.5rem;
            box-shadow:
              0 10px 15px -3px rgb(0 0 0 / 0.1),
              0 4px 6px -4px rgb(0 0 0 / 0.1);
            border: 1px solid rgb(229 231 235);

            @media (min-width: 992px) {
              // margin-bottom: 0;
              width: calc(50% - 0.5rem);
            }

            img {
              width: 100%;
              height: 10rem;
            }

            .pdccgiContent {
              padding: 1rem;

              .pdccgicTitle {
                margin-bottom: 0.5rem;
                font-weight: 700;
                color: rgb(1 32 96);
              }

              .pdccgicSub {
                font-size: 0.875rem;
                line-height: 1.25rem;
                margin-bottom: 0.75rem;
                color: rgb(107 114 128);
              }

              .pdccgicPice {
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

          .pdccCgItem:hover {
            @media (min-width: 768px) {
              cursor: pointer;
            }
          }
        }
      }
    }

    .pdcRight {
      padding: 1rem;
      width: 100%;
      height: 100%;
      background-color: rgb(255 255 255);
      border-radius: 1rem;
      box-shadow:
        0 10px 15px -3px rgb(0 0 0 / 0.1),
        0 4px 6px -4px rgb(0 0 0 / 0.1);

      @media (min-width: 992px) {
        padding: 1.5rem;
        width: calc(33.3% - 1rem);
      }

      .pdcrTitle {
        margin-bottom: 1.5rem;
        font-weight: 700;
        font-size: 1.25rem;
        line-height: 1.75rem;

        @media (max-width: 768px) {
          margin-bottom: 1rem;
        }
      }

      .pdcrTop {
        margin-bottom: 1.5rem;

        img {
          margin-right: 1rem;
          width: 4rem;
          height: 4rem;
          border-radius: 0.75rem;
        }

        .pdcrtTitle {
          font-weight: 700;
          font-size: 1.125rem;
          line-height: 1.75rem;
        }

        .pdcrtRate {
          display: flex;
          align-items: center;

          span {
            margin-left: 0.25rem;
            font-size: 0.875rem;
            line-height: 1.25rem;
            color: rgb(75 85 99);
          }
        }

        .pdcrtTag {
          margin-top: 0.5rem;
          color: rgb(107 114 128);
          font-size: 0.875rem;
          line-height: 1.25rem;

          .pdcrtagShu {
            margin: 0.25rem;
          }

          span:last-child {
            display: none;
          }
        }
      }

      .pdcrItem {
        position: relative;
        display: flex;
        line-height: 1.5rem;
        padding-bottom: 1rem;

        .pdcrIbox {
          flex-shrink: 0;
          margin-right: 0.75rem;
          width: 2rem;
          height: 2rem;
          color: rgb(22 93 255);
          background-color: rgb(22 93 255 / 0.1);
          border-radius: 9999px;
        }

        .pdcrPbox {
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

      .pdcrGysxq {
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

      .pdcrZxzx {
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
  }
}
</style>

<style>
/* 评分 style */
.el-rate {
  padding-bottom: 0.25rem !important;
}

.pdcrTop .el-rate__icon {
  margin-right: 0 !important;
}
</style>
