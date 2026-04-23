<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import pageJump from '@/hooks/pageJump'
import usePagination from '@/hooks/usePagination'
import formatCurrency from '@/hooks/formatCurrency'
import { inquiryorderslistApi } from '@/api/modules/admin'

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
  inquiryorderslistApi(parameters).then((res: any) => {
    if (res) {
      pagination.value.total = res.total
      groupData.value = res.data
      tableLoading.value = false
    }
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

const userType: any = ref(1)
const userRole: any = ref(1)

onMounted(() => {
  const userInfo: any = JSON.parse(
    localStorage.getItem('userinfo') || '{}'
  )
  // user_type  1-供方/2-需方
  userType.value = userInfo.user_type
  // role  0-主管理员/1-普通管理员
  userRole.value = userInfo.role
  getDataList()
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
          <span>询价单</span>
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
        询价单列表
      </h2>
      <div v-if="userType === 1">
        <!-- 数据表格 -->
        <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
          <el-table-column :show-overflow-tooltip="true" align="center" prop="product_name" label="产品名称" />
          <el-table-column :show-overflow-tooltip="true" align="center" prop="cate_name" label="产品类型" />
          <el-table-column :show-overflow-tooltip="true" align="center" prop="untax_price" label="不含税价格" />
          <el-table-column :show-overflow-tooltip="true" align="center" prop="tax_rate" label="税率">
            <template #default="scope">
              <span>{{ formatTaxRate(scope.row.tax_rate) }}</span>
            </template>
          </el-table-column>
          <el-table-column :show-overflow-tooltip="true" align="center" prop="quantity" label="数量" />
          <el-table-column :show-overflow-tooltip="true" align="center" label="客户姓名">
            <template #default="scope">
              {{ scope.row.customer_info.real_name }}
            </template>
          </el-table-column>
          <el-table-column :show-overflow-tooltip="true" align="center" label="联系方式">
            <template #default="scope">
              {{ scope.row.customer_info.phone }}
            </template>
          </el-table-column>
          <el-table-column :show-overflow-tooltip="true" align="center" prop="create_time" label="下单时间" />
        </el-table>
        <!-- 分页 -->
        <div class="pagination-block">
          <el-pagination size="small" :current-page="pagination.pageNo" :page-size="pagination.pageSize"
            :total="pagination.total" :page-sizes="pagination.sizes" :layout="pagination.layout" background
            @size-change="sizeChange" @current-change="currentChange" />
        </div>
      </div>
      <div v-if="userType === 2">
        <!-- 数据表格 -->
        <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
          <el-table-column :show-overflow-tooltip="true" align="center" prop="inquiry_no" label="订单编号" />
          <el-table-column align="center" label="总价">
            <template #default="scope">
              <span>¥{{ formatCurrency(scope.row.total_amount) }}</span>
            </template>
          </el-table-column>
          <el-table-column :show-overflow-tooltip="true" align="center" prop="create_time" label="创建时间" />
          <el-table-column align="center" label="操作" width="120">
            <template #default="scope">
              <div class="table-operate">
                <el-button text type="primary"
                  @click="pageJump('user-quotationfrom', { inquiry_id: scope.row.inquiry_id })">
                  查看
                </el-button>
                <!-- <el-button text type="danger">撤销</el-button> -->
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
