<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { Search, Plus } from '@element-plus/icons-vue'
import pageJump from '@/hooks/pageJump'
import usePagination from '@/hooks/usePagination'
import formatCurrency from '@/hooks/formatCurrency'
import useDebounce from '@/utils/useDebounce'
import { humanresourcelistApi } from '@/api/modules/admin'
import { productpcatechildrenApi } from '@/api/modules/product'

// 查询条件
const queryForm: any = reactive({
  // servicename: '',
  // sub_cate_id: '',
  status: '',
})

// 数据查询
const tableLoading = ref(false)
const groupData = ref([])

function getDataList() {
  tableLoading.value = true
  const parameters: any = {
    page: pagination.value.pageNo,
    page_size: pagination.value.pageSize,
  }
  // if (queryForm.servicename) {
  //   parameters['servicename'] = queryForm.servicename
  // }
  // if (queryForm.sub_cate_id) {
  //   parameters['sub_cate_id'] = queryForm.sub_cate_id
  // }
  if (queryForm.status) {
    parameters['status'] = queryForm.status
  }
  humanresourcelistApi(parameters).then((res: any) => {
    if (res) {
      pagination.value.total = res.total
      groupData.value = res.items
      tableLoading.value = false
    }
  })
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

const pcateOne: any = ref([])

function getPcateOne(pid: any = 0) {
  productpcatechildrenApi({
    page: 1,
    pageSize: 999,
    parent_id: pid,
  }).then((res: any) => {
    if (res && res.items.length > 0) {
      const levelone = res.items.filter((element: any) => element.item_id === 0)
      pcateOne.value = levelone
    }
  })
}

onMounted(() => {
  getPcateOne()
  getDataList()
})
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-index')"> <i class="fa fa-home mr-1"></i>首页 </a>
          <span class="breadcrumb-separator">/</span>
          <span>数字技工/方案论证</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-index')">
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-users"></i>
        方案类服务
      </h2>
      <!-- 查询条件 -->
      <el-form :model="queryForm">
        <el-row :gutter="20">
          <!-- <el-col :span="6">
            <el-form-item>
              <el-input size="large" v-model="queryForm.servicename" placeholder="服务名称" clearable :prefix-icon="Search"
                @input="useDebounce().fn(getDataList)" />
            </el-form-item>
          </el-col> -->
          <!-- <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.sub_cate_id" placeholder="选择类别" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
<el-option label="全部类别" value="" />
<el-option v-for="(item, index) in pcateOne" :key="index" :label="item.name" :value="item.id" />
</el-select>
</el-form-item>
</el-col> -->
          <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.status" placeholder="选择状态" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
                <el-option label="待审核" value="0" />
                <el-option label="审核通过" value="1" />
                <el-option label="驳回" value="2" />
                <el-option label="关闭" value="3" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-button size="large" :icon="Plus" color="#377dff" @click="pageJump('user-renfrom')">新增</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <!-- 数据表格 -->
      <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
        <el-table-column :show-overflow-tooltip="true" align="center" prop="servicename" label="服务名称" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="cate_name" label="类别" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="sub_cate_name" label="子类别" />
        <el-table-column align="center" label="税前价格" width="120">
          <template #default="scope">
            <span>¥{{ formatCurrency(scope.row.pretaxprice) }}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="税后价格" width="120">
          <template #default="scope">
            <span>¥{{ formatCurrency(scope.row.afertaxprice) }}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="状态" width="120">
          <template #default="scope">
            <el-tag v-if="scope.row.status === 0" type="warning" style="border-radius: 50px">
              <i class="fa fa-check-circle"></i>
              <span style="margin-left: 5px">待审核</span>
            </el-tag>
            <el-tag v-if="scope.row.status === 1" type="success" style="border-radius: 50px">
              <i class="fa fa-edit"></i>
              <span style="margin-left: 5px">审核通过</span>
            </el-tag>
            <el-tag v-if="scope.row.status === 2" type="danger" style="border-radius: 50px">
              <i class="fa fa-ban"></i>
              <span style="margin-left: 5px">驳回</span>
            </el-tag>
            <el-tag v-if="scope.row.status === 3" type="info" style="border-radius: 50px">
              <i class="fa fa-ban"></i>
              <span style="margin-left: 5px">关闭</span>
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column align="center" label="操作" width="160">
          <template #default="scope">
            <div class="table-operate">
              <el-button text type="primary" @click="pageJump('user-renfrom', { product_id: scope.row.id })"> 编辑
              </el-button>
              <!-- <el-button text type="warning"> 下架 </el-button>
              <el-button text type="success"> 上架 </el-button>
              <el-button text type="danger"> 删除 </el-button> -->
            </div>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页 -->
      <div class="pagination-block">
        <el-pagination size="small" :current-page="pagination.pageNo" :page-size="pagination.pageSize"
          :total="pagination.total" :page-sizes="pagination.sizes" :layout="pagination.layout" background
          @size-change="sizeChange" @current-change="currentChange" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>
