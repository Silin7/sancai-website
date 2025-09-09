<script setup lang="ts">
import dayjs from 'dayjs'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import pageJump from '@/hooks/pageJump'
import { fileURL } from '@/api/baseConfig'
// import formatCurrency from '@/hooks/formatCurrency'
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

// 时分秒过滤器
function convertSecondsToHMS(seconds: any) {
  var hours = Math.floor(seconds / 3600)
  var minutes = Math.floor((seconds % 3600) / 60)
  var remainingSeconds = seconds % 60
  var returnStr = ''
  if (hours) {
    returnStr += hours + '小时'
  }
  returnStr += minutes + '分钟'
  if (remainingSeconds) {
    returnStr += remainingSeconds + '秒 '
  }
  return returnStr
}
</script>

<template>
  <div class="pdPage">
    <div class="pdCbox">
      <div class="pdcLeft">
        <div class="pdclJbcs">
          <video v-if="videoDetails.vurl" :poster="fileURL + videoDetails.thumbnail" controls="true"
            preload="metadata">
            <!-- 示例视频源（实际项目中替换为真实视频地址） -->
            <source :src="videoDetails.vurl" type="video/mp4">
            您的浏览器不支持HTML5视频播放，请升级浏览器
          </video>
          <div class="videoInfoBox">
            <div class="videoTitle">{{ videoDetails.title }}</div>
            <div class="videoTags">
              <div class="videoTagItem">
                <i class="fa fa-clock-o mr-2 text-primary"></i>
                <span>总时长：{{ convertSecondsToHMS(videoDetails.vlength) }}</span>
              </div>
              <div class="videoTagItem">
                <i class="fa fa-eye mr-2 text-primary"></i>
                <span>播放量：12,840次</span>
              </div>
              <div class="videoTagItem">
                <i class="fa fa-calendar mr-2 text-primary"></i>
                <span>更新时间：2024-03-15</span>
              </div>
              <div class="videoTagItem">
                <i class="fa fa-tag mr-2 text-primary"></i>
                <span>分类：BIM技术 / CAD / 造价工程师</span>
              </div>
            </div>
            <button>
              <i class="fa fa-shopping-cart"></i>
              <span>立即购买 ¥{{ videoDetails.price }}</span>
            </button>
          </div>
        </div>
        <div class="pdclXq">
          <div class="pdclxTitle">介绍</div>
          <div class="" v-html="videoDetails.content"></div>
        </div>
      </div>
      <div class="pdcRight">
        <div class="pdcrTitle"><i class="fa fa-info-circle"></i>视频信息</div>
        <div class="pdcrItem">
          <p>形式</p>
          <p>录播</p>
        </div>
        <div class="pdcrItem">
          <p>时长</p>
          <p>{{ convertSecondsToHMS(videoDetails.vlength) }}</p>
        </div>
        <div class="pdcrItem">
          <p>适合人群</p>
          <p>造价工程师、BIM初学者、建筑从业者</p>
        </div>
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
        background-color: rgb(255 255 255);
        border-radius: 1rem;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        video {
          width: 100%;
        }

        .videoInfoBox {
          padding: 1.5rem;

          @media (max-width: 768px) {
            padding: 1rem;
          }

          .videoTitle {
            margin-bottom: 1rem;
            color: rgb(1 32 96 / var(--tw-text-opacity, 1));
            font-weight: 700;
            font-size: clamp(1.5rem, 3vw, 2.25rem);
          }

          .videoTags {
            color: rgb(107 114 128 / var(--tw-text-opacity, 1));
            display: flex;
            flex-wrap: wrap;

            i {
              margin-right: 0.5rem;
              color: rgb(22 93 255 / var(--tw-text-opacity, 1));
            }

            .videoTagItem {
              margin-bottom: 1rem;
              margin-right: 1rem;
            }
          }

          button {
            padding: 0.75rem 1.5rem;
            color: #fff;
            background-color: rgb(22 93 255 / 0.9);
            border-radius: 0.5rem;

            i {
              margin-right: 0.5rem;
            }
          }

          button:hover {
            @media (min-width: 768px) {
              cursor: pointer;
              transform: scale(1.05);
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

        i {
          margin-right: 0.5rem;
          color: rgb(22 93 255 / var(--tw-text-opacity, 1));
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
        justify-content: space-between;
        align-items: center;
        line-height: 1.5rem;
        padding-bottom: 1rem;

        p:first-child {
          color: rgb(107 114 128 / var(--tw-text-opacity, 1));
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
