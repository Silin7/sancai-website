<script setup lang="ts">
import dayjs from 'dayjs'
import { useHead } from '@vueuse/head'
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import pageJump from '@/hooks/pageJump'
import windowOpen from '@/hooks/windowOpen'
import formatCurrency from '@/hooks/formatCurrency'
import { fileURL } from '@/api/baseConfig'
import {
  bannerlistApi,
  secpositionsApi,
  syspseoApi,
} from '@/api/modules/basic'
import {
  productmaterialssearchApi,
  productmaterialssearchkeywordApi,
} from '@/api/modules/product'

const route = useRoute()

function getRouteKeywords() {
  const keywords = route.query.keywords
  if (Array.isArray(keywords)) {
    return keywords[0] || ''
  }
  return typeof keywords === 'string' ? keywords : ''
}

// 用户端-获取所有启用的板块位置（含完整字段，按排序升序、创建时间倒序）
const positionid: any = ref('')
const bannerData: any = ref([])

function getSecpositions() {
  secpositionsApi().then((res: any) => {
    if (res && res.length > 0) {
      for (let i = 0; i < res.length; i++) {
        if (res[i].url == window.localStorage.getItem('selectedName')) {
          positionid.value = res[i].id
          getBannerlist()
          break
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
        ],
      })
    }
  })
}

// 数据查询
const tableLoading = ref(false)
const currentPage: any = ref(1)
const pageSize: any = ref(10)
const total: any = ref(0)
const productDataList: any = ref([])

// function getProductmaterialssearch() {
//   tableLoading.value = true
//   productmaterialsApi({
//     page: currentPage.value,
//     pageSize: pageSize.value,
//   }).then((res: any) => {
//     if (res) {
//       total.value = res.total
//       productDataList.value = res.items
//     }
//   }).finally(() => {
//     tableLoading.value = false
//   })
// }

function getProductmaterialssearch() {
  tableLoading.value = true
  const keyword = getRouteKeywords()
  const params = {
    page: currentPage.value,
    pageSize: pageSize.value,
  }
  const request = keyword
    ? productmaterialssearchkeywordApi({ ...params, keyword })
    : productmaterialssearchApi(params)

  request
    .then((res: any) => {
      if (res) {
        total.value = res.total
        productDataList.value = res.items
      }
    })
    .finally(() => {
      tableLoading.value = false
    })
}

// current-page 改变时触发
function handleCurrentChange(val: number) {
  currentPage.value = val
  getProductmaterialssearch()
}

// page-size 改变时触发
function handleSizeChange(val: number) {
  pageSize.value = val
  getProductmaterialssearch()
}

// 产品详情
function goProductsDetail(row: any) {
  pageJump('products_detail', {
    id: row.id,
    name: 'materials',
  })
}

// 格式化税率
function formatTaxRate(taxrate: any) {
  const rate = Number(taxrate)
  if (!Number.isFinite(rate)) {
    return '--'
  }

  const percent = rate * 100
  const maxFiniteDecimals = 8
  const epsilon = 1e-10

  for (let decimals = 0; decimals <= maxFiniteDecimals; decimals++) {
    const factor = 10 ** decimals
    if (Math.abs(percent * factor - Math.round(percent * factor)) < epsilon) {
      return `${percent.toFixed(decimals).replace(/\.?0+$/, '')}%`
    }
  }

  return `${percent.toFixed(2)}%`
}

watch(
  () => route.query.keywords,
  () => {
    currentPage.value = 1
    getProductmaterialssearch()
  },
)

onMounted(() => {
  getSecpositions()
  getProductmaterialssearch()
})
</script>

<template>
  <div class="materialsPage">
    <!-- BANNER -->
    <div class="bannerBox" @click="windowOpen(bannerData.url, bannerData.istourl)">
      <img :src="bannerData.imgurl" />
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
    <div class="containerBox">
      <div class="containerLeft">
        <div class="containerProducts">
          <!-- 数据表格 -->
          <el-table v-loading="tableLoading" :data="productDataList" highlight-current-row>
            <el-table-column align="center" label="材料名称">
              <template #default="scope">
                <span @click="goProductsDetail(scope.row)" style="color: #165dff; cursor: pointer;">
                  {{ scope.row.materialname }}
                </span>
              </template>
            </el-table-column>
            <el-table-column :show-overflow-tooltip="true" align="center" prop="specification" label="规格型号" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="technical_params" label="技术参数" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="brand" label="品牌" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="unit_name" label="单位" />
            <el-table-column align="center" label="除税价">
              <template #default="scope">
                <span style="color: #165dff; font-weight: 700">¥{{ formatCurrency(scope.row.pretaxprice, 2) }}</span>
              </template>
            </el-table-column>
            <!-- <el-table-column align="center" label="未含税价">
              <template #default="scope">
                <span style="color: #00b42a; font-weight: 700">¥{{ formatCurrency(scope.row.afertaxprice, 2) }}</span>
              </template>
            </el-table-column> -->
            <el-table-column align="center" label="税率">
              <template #default="scope">
                <span>{{ formatTaxRate(scope.row.taxrate) }}</span>
              </template>
            </el-table-column>
            <el-table-column :show-overflow-tooltip="true" align="center" prop="supplier_name" label="供应商" />
            <el-table-column align="center" label="报价时间">
              <template #default="scope">
                <span>{{ dayjs(scope.row.quote_time).format('YYYY-MM-DD') }}</span>
              </template>
            </el-table-column>
            <el-table-column :show-overflow-tooltip="true" align="center" prop="memo" label="备注" />
          </el-table>
          <!-- 分页 -->
          <div class="containerPagination">
            <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :page-sizes="[10, 20]"
              size="default" background layout="prev, pager, next" prev-text="上一页" next-text="下一页" :total="total"
              @size-change="handleSizeChange" @current-change="handleCurrentChange" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.materialsPage {
  min-height: calc(100vh - 120px);
  background-color: #f9fafb;

  .containerBox {
    margin: 0 auto;
    padding: 1rem;
    width: 100%;
    max-width: 1536px;

    @media (min-width: 1140px) {
      padding: 2rem 1rem 4rem;
      display: flex;
      justify-content: space-between;
    }

    .containerLeft {
      width: 100%;

      // @media (min-width: 1140px) {
      //   width: calc(66.7% - 1rem);
      // }

      .containerProducts {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 1140px) {
          padding: 1rem;
        }

        .containerPagination {
          margin-top: 2rem;
          display: flex;
          justify-content: center;
          align-items: center;
        }
      }
    }
  }
}
</style>

<style lang="scss">
.materialsPage {
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

  .containerProductsTitlePxfs {
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

}
</style>
