<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useHead } from '@vueuse/head'
import { Search } from '@element-plus/icons-vue'
import { fileURL } from '@/api/baseConfig'
import pageJump from '@/hooks/pageJump'
import windowOpen from '@/hooks/windowOpen'
import { bannerlistApi, secpositionsApi, syspseoApi } from '@/api/modules/basic'
import formatCurrency from '@/hooks/formatCurrency'
import usePagination from '@/hooks/usePagination'

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
      for (let i = 0; i < res.length; i++) {
        // IN DOUBT 根据路由判断 尽量不根据 name 判断
        if (res[i].name === window.localStorage.getItem('selectedName')) {
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
        ]
      })
    }
  })
}

// 高级搜索状态
const searchState: any = ref(false)

function searchStateClick() {
  searchState.value = !searchState.value
}

// 数据查询
const tableLoading = ref(false)
const groupData = ref([
  {
    data1: '高强度螺纹钢',
    data2: 'HRB400E Φ25mm',
    data3: '首钢',
    data4: '吨',
    data5: '4400',
    data6: '523.23',
    data7: '10%',
    data8: '北京首钢股份',
    data9: '2025-06-18',
    data10: '抗震达标',
  },
  {
    data1: 'C30预拌高性能混凝土',
    data2: 'C30 泵送型',
    data3: '中建商砼',
    data4: '立方米',
    data5: '8800',
    data6: '6423.24',
    data7: '10%',
    data8: '中建商品混凝土有限公司',
    data9: '2025-06-15',
    data10: '抗渗',
  },
  {
    data1: '挤塑保温板',
    data2: '30mm 阻燃型',
    data3: '欧文斯科',
    data4: '平方米',
    data5: '480',
    data6: '3453',
    data7: '10%',
    data8: '欧文斯科宁中国',
    data9: '2025-06-10',
    data10: '阻燃',
  },
  {
    data1: '智能安防系统套装',
    data2: 'SH-8000 家庭版',
    data3: '海康威视',
    data4: '套',
    data5: '22000',
    data6: '1280',
    data7: '10%',
    data8: '海康威视数字技术有限公司',
    data9: '2025-06-05',
    data10: '高清',
  },
])

function getDataList() {
  tableLoading.value = true
  // groupPage({
  //   ...queryForm,
  //   pageNo: pagination.value.pageNo,
  //   pageSize: pagination.value.pageSize,
  // }).then((res: any) => {
  //   if (res && res.code === 0) {
  //     pagination.value.total = res.data.total
  //     groupData.value = res.data.list
  //     tableLoading.value = false
  //   }
  //   else {
  //     message.error(res.msg)
  //     tableLoading.value = false
  //   }
  // })
}

// 分页
const { pagination, onSizeChange, onCurrentChange } = usePagination()

// 每页数量切换
function sizeChange(pageSize: number) {
  onSizeChange(pageSize).then(() => getDataList())
}

// 当前页码切换（翻页）
function currentChange(pageNo = 1) {
  onCurrentChange(pageNo).then(() => getDataList())
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
  getSecpositions()
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
  <div class="materialsPage">
    <!-- BANNER -->
    <div class="prbannerBox" @click="windowOpen(bannerData.url, bannerData.istourl)">
      <img :src="fileURL + bannerData.imgurl" alt="mabanner" />
      <div class="prbannerAbsolute">
        <div class="prbannerContent">
          <!-- <div class="prbannerTitle">材料/设备</div> -->
          <!-- <div class="prbannerSubtitle">绿色化 数字化 智能化</div> -->
        </div>
      </div>
    </div>
    <div class="containerBox">
      <div class="containerLeft">
        <div class="containerClass">
          <div class="containerClassRow">
            <button class="containerClassCol">数字技工/方案论证</button>
            <button class="containerClassColActive">材料/设备</button>
            <button class="containerClassCol">智能建造装备</button>
            <button class="containerClassCol">信息化产品/服务</button>
          </div>
          <div class="containerClassRow">
            <button class="containerClassColActive">全部</button>
            <button class="containerClassCol">城市更新</button>
            <button class="containerClassCol">四好建设</button>
            <button class="containerClassCol">智能家居</button>
            <button class="containerClassCol">智能建造</button>
            <button class="containerClassCol">节能系统</button>
            <button class="containerClassCol">其他</button>
          </div>
          <div class="containerGjss">
            <button v-if="searchState" class="" @click="searchStateClick">
              <i class="fa fa-search-minus"></i>
              <span>收起高级搜索</span>
            </button>
            <button v-if="!searchState" class="" @click="searchStateClick">
              <i class="fa fa-search-plus"></i>
              <span>展开高级搜索</span>
            </button>
            <div v-if="searchState">
              <el-row :gutter="10">
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb10">
                  <div class="supplierClassText">所在省份</div>
                  <el-select v-model="selectvalue" placeholder="Select" size="large">
                    <el-option label="全部省份" value="01" />
                    <el-option label="山东省" value="02" />
                    <el-option label="山西省" value="03" />
                  </el-select>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb10">
                  <div class="supplierClassText">所在城市</div>
                  <el-select v-model="selectvalue" placeholder="Select" size="large">
                    <el-option label="全部省份" value="01" />
                    <el-option label="山东省" value="02" />
                    <el-option label="山西省" value="03" />
                  </el-select>
                </el-col>
              </el-row>
              <el-row :gutter="10">
                <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="8" class="mb10">
                  <div class="supplierClassText">材料名称</div>
                  <el-input v-model="input2" style="width: 100%; height: 40px" placeholder="请输入材料名称..." />
                </el-col>
                <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="8" class="mb10">
                  <div class="supplierClassText">规格型号</div>
                  <el-input v-model="input2" style="width: 100%; height: 40px" placeholder="请输入规格型号..." />
                </el-col>
                <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="8" class="mb10">
                  <div class="supplierClassText">品牌名称</div>
                  <el-input v-model="input2" style="width: 100%; height: 40px" placeholder="请输入品牌名称..." />
                </el-col>
              </el-row>
              <el-row :gutter="10">
                <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="8" class="mb10">
                  <div class="supplierClassText">报价开始日期</div>
                  <el-date-picker v-model="input2" type="date" placeholder="yyyy/mm/dd"
                    style="width: 100%;; height: 40px" />
                </el-col>
                <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="8" class="mb10">
                  <div class="supplierClassText">报价结束日期</div>
                  <el-date-picker v-model="input2" type="date" placeholder="yyyy/mm/dd"
                    style="width: 100%;; height: 40px" />
                </el-col>
                <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="8" class="mb10">
                  <div class="supplierClassText">价格区间</div>
                  <div class="frbc">
                    <el-input v-model="input2" style="width: calc(50% - 0.5rem); height: 40px" placeholder="最低价" />
                    -
                    <el-input v-model="input2" style="width: calc(50% - 0.5rem); height: 40px" placeholder="最低价" />
                  </div>
                </el-col>
              </el-row>
              <button class="searchBtn"><i class="fa fa-search "></i>搜索</button>
            </div>
          </div>
          <!-- <el-input v-model="input2" style="width: 100%; height: 50px; font-size: 1rem" placeholder="搜索产品..."
            :prefix-icon="Search" /> -->
        </div>
        <div class="containerProducts">
          <!-- 数据表格 -->
          <el-table v-loading="tableLoading" :data="groupData" highlight-current-row>
            <el-table-column :show-overflow-tooltip="true" align="center" label="材料名称" width="120">
              <template #default="scope">
                <span style="color: #165DFF;">{{ scope.row.data1 }}</span>
              </template>
            </el-table-column>
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data2" label="规格" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data3" label="品牌" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data4" label="单位" />
            <el-table-column align="center" label="含税价">
              <template #default="scope">
                <span style="color: #165DFF; font-weight: 700;">¥{{ formatCurrency(scope.row.data5) }}</span>
              </template>
            </el-table-column>
            <el-table-column align="center" label="未含税价">
              <template #default="scope">
                <span style="color: #00B42A; font-weight: 700;">¥{{ formatCurrency(scope.row.data6) }}</span>
              </template>
            </el-table-column>
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data7" label="税率" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data8" label="供应商" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data9" label="报价时间" />
            <el-table-column :show-overflow-tooltip="true" align="center" prop="data10" label="备注" />
          </el-table>
          <!-- 分页 -->
          <div class="containerPagination">
            <el-pagination v-model:current-page="currentPage2" v-model:page-size="pageSize2" :page-sizes="[10, 20]"
              size="default" background layout="prev, pager, next" prev-text="上一页" next-text="下一页" :total="400"
              @size-change="handleSizeChange" @current-change="handleCurrentChange" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.materialsPage {
  background-color: #f9fafb;

  .prbannerBox {
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

    .prbannerAbsolute {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 2;
      width: 100vw;

      .prbannerContent {
        margin: 0 auto;
        padding: 10rem 2rem 0;
        width: 100%;
        max-width: 1536px;

        @media (max-width: 768px) {
          padding: 6rem 1rem 0;
        }

        .prbannerTitle {
          margin-bottom: 2rem;
          font-size: clamp(2rem, 4vw, 3rem);
          font-weight: 700;
          color: #fff;
        }

        .prbannerSubtitle {
          margin-bottom: 2rem;
          font-size: clamp(1.25rem, 4vw, 1.5rem);
          font-weight: 500;
          color: rgb(255 255 255 / 0.9);
        }
      }
    }
  }

  .containerBox {
    margin: 0 auto;
    padding: 1rem;
    width: 100%;
    max-width: 1536px;

    @media (min-width: 1140px) {
      padding: 4rem 1rem;
      display: flex;
      justify-content: space-between;
    }

    .containerLeft {
      width: 100%;

      // @media (min-width: 1140px) {
      //   width: calc(66.7% - 1rem);
      // }

      .containerClass {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

        @media (max-width: 1140px) {
          padding: 1rem;
        }

        .containerClassRow {
          margin-bottom: 1rem;
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          line-height: 1.5rem;

          .containerClassCol {
            margin: 0 0.75rem 0.75rem 0;
            padding: 0.5rem 1.25rem;
            color: rgb(1 32 96);
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
            border: 1px solid rgb(243 244 246);
            border-radius: 9999px;
            ;

            @media (max-width: 768px) {
              margin: 0 0.5rem 0.5rem 0;
              padding: 0.5rem 1rem;
              font-size: 0.875rem;
              line-height: 1.25rem;
            }
          }

          .containerClassCol:hover {
            @media (min-width: 768px) {
              background-color: rgb(243 244 246);
            }
          }

          .containerClassColActive {
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

        .containerGjss {

          button {
            margin-bottom: 1rem;
            color: rgb(22 93 255);

            i {
              margin-right: 0.5rem;
            }
          }

          .supplierClassText {
            margin-bottom: 0.5rem;
            font-weight: 500;
            font-size: 0.875rem;
            line-height: 1.25rem;
            color: rgb(55 65 81);
          }

          .searchBtn {
            margin-bottom: 0;
            display: block;
            margin: 0 auto;
            color: #fff;
            background-color: rgb(22 93 255 / 0.9);
            width: 7.5rem;
            height: 2.5rem;
            border-radius: 0.5rem;
          }
        }
      }

      .containerProducts {
        margin-bottom: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        color: rgb(1 32 96);
        background-color: #fff;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

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

  .containerGjss {
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
}
</style>
