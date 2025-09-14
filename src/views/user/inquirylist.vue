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
  itname: '',
  thetype: '',
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
  if (queryForm.itname) {
    parameters['itname'] = queryForm.itname
  }
  if (queryForm.thetype) {
    parameters['thetype'] = queryForm.thetype
  }
  if (queryForm.status) {
    parameters['status'] = queryForm.status
  }
  solutionorderslistApi(parameters).then((res: any) => {
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

onMounted(() => {
  getDataList()
  requirementsbycateApi({
    cate_id : 1,
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
              <el-input size="large" v-model="queryForm.name" placeholder="搜索订单号、客户名称..." clearable
                :prefix-icon="Search" @input="useDebounce().fn(getDataList)" />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.status" placeholder="选择状态" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
                <el-option label="全部状态" value="all" />
                <el-option label="待报价" value="pending" />
                <el-option label="已报价" value="completed" />
                <el-option label="已取消" value="canceled" />
              </el-select>
            </el-form-item>
          </el-col>
          <!-- <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.state" placeholder="选择日期" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
                <el-option label="全部日期" value="all" />
                <el-option label="今天" value="today" />
                <el-option label="本周" value="week" />
                <el-option label="本月" value="month" />
                <el-option label="自定义" value="custom" />
              </el-select>
            </el-form-item>
          </el-col> -->
        </el-row>
      </el-form>
      <!-- 数据表格 -->
      <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data1" label="服务名称" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data2" label="订单号" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data3" label="订购客户" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data4" label="联系方式" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data5" label="下单日期" />
        <el-table-column align="center" label="状态" width="120">
          <template #default="scope">
            <el-tag v-if="scope.row.data7 === 'yishangjia'" type="success" style="border-radius: 50px">
              <i class="fa fa-check-circle"></i>
              <span style="margin-left: 5px">已上架</span>
            </el-tag>
            <el-tag v-if="scope.row.data7 === 'caogao'" type="warning" style="border-radius: 50px">
              <i class="fa fa-edit"></i>
              <span style="margin-left: 5px">草稿</span>
            </el-tag>
            <el-tag v-if="scope.row.data7 === 'yixiajia'" type="danger" style="border-radius: 50px">
              <i class="fa fa-ban"></i>
              <span style="margin-left: 5px">已下架</span>
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column align="center" label="操作" width="160">
          <template #default="scope">
            <div class="table-operate">
              <!-- @click="groupAddOrUpdateFunc('edit', scope.row.id)" -->
              <el-button text type="info"> 查看 </el-button>
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
