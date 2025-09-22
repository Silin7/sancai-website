<script setup lang="ts">
import { useHead } from '@vueuse/head'
import { onBeforeUnmount, onMounted, ref } from 'vue'
import pageJump from '@/hooks/pageJump'
import windowOpen from '@/hooks/windowOpen'
import { fileURL } from '@/api/baseConfig'
import { bannerlistApi, secpositionsApi, syspseoApi, seccontentlistApi } from '@/api/modules/basic'

// 可视窗口宽度
const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

// 用户端-获取所有启用的板块位置（含完整字段，按排序升序、创建时间倒序）
const positionid: any = ref('')
const bannerData: any = ref([])

function getSecpositions() {
  secpositionsApi().then((res: any) => {
    if (res && res.length > 0) {
      seccontentList.value = []
      for (let i = 0; i < res.length; i++) {
        const item = res[i]
        if (item.url === window.localStorage.getItem('selectedName')) {
          positionid.value = item.id
          getBannerlist()
        }
        // 工程造价+AI-板块001
        if (item.url === 'eai-card') {
          getSeccontentlist(item.id)
        }
      }
    }
  })
}

function getBannerlist() {
  // 用户端-按板块位置ID获取所有启用的Banner（含位置名称）
  bannerlistApi(positionid.value).then((res: any) => {
    bannerData.value = res[0]
  })
  // 用户端-根据页面ID（page_id）获取启用的SEO配置详情（含页面名称）
  syspseoApi(positionid.value).then((res: any) => {
    if (res) {
      useHead({
        title: res.page_name,
        meta: [
          { name: 'description', content: res.description },
          { name: 'keywords', content: res.keywords },
        ]
      })
    }
  })
}

// 代表成果
const seccontentList: any = ref([])

function getSeccontentlist(id: any) {
  seccontentlistApi(id).then((res: any) => {
    seccontentList.value.unshift(...res)
  })
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
  getSecpositions()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
})
</script>

<template>
  <div class="engineeringaiPage">
    <!-- BANNER -->
    <div class="bannerBox" @click="windowOpen(bannerData.url, bannerData.istourl)">
      <img :src="fileURL + bannerData.imgurl" alt="" />
      <div class="bannerAbsolute">
        <div class="bannerContent">
          <div class="bannerTitle">{{ bannerData.maintitle }}</div>
          <div v-if="bannerData.subtitle" class="bannerSubtitle">
            {{ bannerData.subtitle }}
          </div>
          <div class="frsc">
            <button v-if="bannerData.leftbtn && !bannerData.leftbtn_url" class="bannerLeftBtn">
              {{ bannerData.leftbtn }}
            </button>
            <button v-if="bannerData.leftbtn && bannerData.leftbtn_url" class="bannerLeftBtn"
              @click.stop="pageJump(bannerData.leftbtn_url)">
              {{ bannerData.leftbtn }}
            </button>
            <button v-if="bannerData.rightbtn && !bannerData.rightbtn_url" class="bannerRightBtn">
              {{ bannerData.rightbtn }}
            </button>
            <button v-if="bannerData.rightbtn && bannerData.rightbtn_url" class="bannerRightBtn"
              @click.stop="pageJump(bannerData.rightbtn_url)">
              {{ bannerData.rightbtn }}
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="aiClassbox">
      <div v-for="(item, index) in seccontentList" :key="index" class="aiClassitem">
        <div class="aiClassitemtext">{{ item.title }}</div>
        <div class="">{{ item.descriptioncontent }}</div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.engineeringaiPage {
  overflow-x: hidden;
  min-height: calc(100vh - 120px);
  background-color: #f9fafb;

  .aiClassbox {
    margin-bottom: 2.5rem;
    width: calc(100% + 1rem);
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;

    @media (max-width: 768px) {
      margin-bottom: 1.5rem;
    }

    .aiClassitem {
      margin: 0 1rem 1rem 0;
      padding: 1.25rem;
      width: calc(33.3% - 1rem);
      display: flex;
      flex-flow: column;
      justify-content: center;
      align-items: center;
      background-color: rgb(249 250 251);
      border-radius: 0.75rem;

      @media (max-width: 768px) {
        padding: 1.25rem 1rem;
        width: calc(50% - 1rem);
      }

      .aiClassitemfa {
        margin-bottom: 1rem;
        width: 4rem;
        height: 4rem;
        border-radius: 9999px;
        background-color: rgb(22 93 255 / 0.1);

        @media (max-width: 768px) {
          width: 3rem;
          height: 3rem;
        }

        i {
          font-size: 1.5rem;
          color: #165dff;
        }
      }

      .aiClassitemfa2 {
        margin-bottom: 1rem;
        width: 4rem;
        height: 4rem;
        border-radius: 9999px;
        background-color: rgb(114 46 209 / 0.1);

        @media (max-width: 768px) {
          width: 3rem;
          height: 3rem;
        }

        i {
          font-size: 1.5rem;
          color: #722ed1;
        }
      }

      .aiClassitemtext {
        line-height: 1.5rem;
        font-weight: 500;
        text-align: center;
        color: rgb(1 32 96);
      }
    }

    .aiClassitem:hover {
      @media (min-width: 768px) {
        cursor: pointer;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }

  .aiClassbox:last-child {
    margin-bottom: 0rem;
  }
}
</style>