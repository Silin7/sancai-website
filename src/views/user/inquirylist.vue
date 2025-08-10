<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { Search, Plus } from '@element-plus/icons-vue'
import usePagination from '@/hooks/usePagination'

// 查询条件
const queryForm: any = reactive({
  name: '',
  state: 'all',
  status: 'all',
})

// 数据查询
const tableLoading = ref(false)
const groupData = ref([
  {
    data1: 'BIM技术应用论证',
    data2: '数字技术应用论证',
    data3: 'BIM+应用',
    data4: '15000',
    data5: '16500',
    data6: '已上架',
    data7: 'yishangjia',
  },
  {
    data1: '智慧工地实施方案论证',
    data2: '数字实施方案论证',
    data3: '实施流程与进度计划论证',
    data4: '8000',
    data5: '8800',
    data6: '草稿',
    data7: 'caogao',
  },
  {
    data1: 'AI赋能应用论证',
    data2: '数字技术应用论证',
    data3: 'AI赋能应用',
    data4: '20000',
    data5: '22000',
    data6: '已下架',
    data7: 'yixiajia',
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
  getDataList()

  setTimeout(() => {
    tableLoading.value = false
  }, 1000)
})

// 金额格式化
function formatCurrency(value: any) {
  return new Intl.NumberFormat('en-US', {
    // style: 'currency',
    // currency: 'CNY', // 可以改为其他货币，如 'EUR', 'CNY' 等
    useGrouping: true,
    minimumFractionDigits: 0, // 最小小数位数
    maximumFractionDigits: 2, // 最大小数位数
  }).format(value)
}
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a> <i class="fa fa-home mr-1"></i>首页 </a>
          <span class="breadcrumb-separator">/</span>
          <span>报价单</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn"><i class="fa fa-arrow-left mr-1"></i>返回首页</button>
          <!-- <button class="action-btn save-btn"><i class="fa fa-save mr-1"></i>保存资料</button> -->
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
              <el-input
                size="large"
                v-model="queryForm.name"
                placeholder="搜索订单号、客户名称..."
                clearable
                :prefix-icon="Search"
              />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-select
                size="large"
                v-model="queryForm.status"
                placeholder="选择状态"
                clearable
                style="width: 100%"
              >
                <!-- <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template> -->
                <el-option label="全部状态" value="all" />
                <el-option label="待报价" value="pending" />
                <el-option label="已报价" value="completed" />
                <el-option label="已取消" value="canceled" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-select
                size="large"
                v-model="queryForm.state"
                placeholder="选择日期"
                clearable
                style="width: 100%"
              >
                <!-- <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template> -->
                <el-option label="全部日期" value="all" />
                <el-option label="今天" value="today" />
                <el-option label="本周" value="week" />
                <el-option label="本月" value="month" />
                <el-option label="自定义" value="custom" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <!-- <el-button size="large" :icon="Search"> 查询 </el-button> -->
              <el-button size="large" :icon="Plus" color="#377dff">新增</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <!-- 数据表格 -->
      <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
        <el-table-column
          :show-overflow-tooltip="true"
          align="center"
          prop="data1"
          label="服务名称"
        />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data2" label="订单号" />
        <el-table-column
          :show-overflow-tooltip="true"
          align="center"
          prop="data3"
          label="订购客户"
        />
        <el-table-column
          :show-overflow-tooltip="true"
          align="center"
          prop="data4"
          label="联系方式"
        />
        <el-table-column
          :show-overflow-tooltip="true"
          align="center"
          prop="data5"
          label="下单日期"
        />
        <el-table-column align="center" label="状态" width="120">
          <template #default="scope">
            <el-tag
              v-if="scope.row.data7 === 'yishangjia'"
              type="success"
              style="border-radius: 50px"
            >
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
              <!-- <el-button text type="info"> 查看 </el-button> -->
              <el-button text type="primary"> 编辑 </el-button>
              <el-button v-if="scope.$index % 2 === 0" text type="danger"> 删除 </el-button>
              <el-button v-else text type="danger"> 下架 </el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页 -->
      <div class="pagination-block">
        <el-pagination
          size="small"
          :current-page="pagination.pageNo"
          :page-size="pagination.pageSize"
          :total="pagination.total"
          :page-sizes="pagination.sizes"
          :layout="pagination.layout"
          background
          @size-change="sizeChange"
          @current-change="currentChange"
        />
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
