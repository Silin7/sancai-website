<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { Search, Plus } from '@element-plus/icons-vue'
import pageJump from '@/hooks/pageJump'
import usePagination from '@/hooks/usePagination'
import formatCurrency from '@/hooks/formatCurrency'
import useDebounce from '@/utils/useDebounce'
import { solutionorderslistApi, requirementsbycateApi } from '@/api/modules/admin'

// 查询条件
const queryForm: any = reactive({
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
  if (queryForm.status) {
    parameters['status'] = queryForm.status
  }
  solutionorderslistApi(parameters).then((res: any) => {
    if (res) {
      pagination.value.total = res.total
      groupData.value = res.data
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

onMounted(() => {
  getDataList()
  requirementsbycateApi({
    cate_id: 1,
  }).then((res: any) => {
    if (res) {
      console.log('需求分类', res)
    }
  })
})
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-index')">
            <i class="fa fa-home mr-1"></i>首页
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>报价单</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-index')">
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-file-powerpoint-o"></i>
        报价单列表
      </h2>
      <!-- 查询条件 -->
      <el-form :model="queryForm">
        <el-row :gutter="20">
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
        </el-row>
      </el-form>
      <!-- 数据表格 -->
      <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
        <el-table-column :show-overflow-tooltip="true" align="center" prop="code" label="订单编号" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="product_name" label="需求项目名" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="cate_name" label="所属分类" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="pre_tax_price" label="税前价格(元)" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="after_tax_price" label="税后价格(元)" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="company_name" label="公司名称" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="contact_person" label="联系人" />
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
        <el-table-column align="center" label="操作" width="80">
          <template #default="scope">
            <div class="table-operate">
              <el-button text type="primary" @click="pageJump('user-inquiryfrom', { order_id: scope.row.id })"> 查看
              </el-button>
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

<style scoped>
.form-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 24px;
  margin-bottom: 40px;
}

/* 列表标题 */
.list-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #303133;
  display: flex;
  align-items: center;
}

.list-title i {
  margin-right: 10px;
  color: #377dff;
}
</style>
