<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { Search, Plus } from '@element-plus/icons-vue'
import pageJump from '@/hooks/pageJump'
import usePagination from '@/hooks/usePagination'
import formatCurrency from '@/hooks/formatCurrency'
import useDebounce from '@/utils/useDebounce'

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
    data1: 'https://www.silin7.cn/lbxx.jpg',
    data2: '优质螺纹钢',
    data3: '宝钢/Φ16-25mm',
    data4: '4850',
    data5: '吨',
    data6: '已上架',
    data7: 'yishangjia',
    data8: '2025-07-01',
  },
  {
    data1: 'https://www.silin7.cn/lbxx.jpg',
    data2: 'PVC管材',
    data3: '联塑/DN25',
    data4: '12.5',
    data5: '米',
    data6: '草稿',
    data7: 'caogao',
    data8: '2025-06-28',
  },
  {
    data1: 'https://www.silin7.cn/lbxx.jpg',
    data2: '环保实木地板',
    data3: '大自然/1210×165×15mm',
    data4: '298',
    data5: '㎡',
    data6: '已下架',
    data7: 'yixiajia',
    data8: '2025-04-02',
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
          <span>信息化产品服务</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-index')">
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-info-circle"></i>
        信息化产品管理
      </h2>
      <!-- 查询条件 -->
      <el-form :model="queryForm">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-form-item>
              <el-input size="large" v-model="queryForm.name" placeholder="搜索产品名称、类型..." clearable :prefix-icon="Search"
                @input="useDebounce().fn(getDataList)" />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.state" placeholder="选择类型" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
                <el-option label="全部类型" value="all" />
                <el-option label="信息化产品" value="xxhcp" />
                <el-option label="信息化服务" value="xxhfw" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.status" placeholder="选择材质" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
                <el-option label="全部状态" value="all" />
                <el-option label="已上架" value="yishangjia" />
                <el-option label="已下架" value="yixiajia" />
                <el-option label="草稿" value="caigao" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-button size="large" :icon="Plus" color="#377dff" @click="pageJump('user-itfrom')">新增</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <!-- 数据表格 -->
      <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
        <el-table-column align="center" label="产品图片">
          <template #default="scope">
            <img :src="scope.row.data1" style="width: 40px; height: 40px; border-radius: 5px" />
          </template>
        </el-table-column>
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data2" label="产品名称" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data3" label="类型/服务" />
        <el-table-column align="center" label="价格" width="120">
          <template #default="scope">
            <span>¥{{ formatCurrency(scope.row.data4) }}/{{ scope.row.data5 }}</span>
          </template>
        </el-table-column>
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
        <el-table-column :show-overflow-tooltip="true" align="center" prop="data8" label="更新时间" />
        <el-table-column align="center" label="操作" width="160">
          <template #default="scope">
            <div class="table-operate">
              <!-- @click="groupAddOrUpdateFunc('edit', scope.row.id)" -->
              <el-button text type="primary"> 编辑 </el-button>
              <el-button v-if="scope.$index % 2 === 0" text type="danger"> 删除 </el-button>
              <el-button v-else text type="danger"> 下架 </el-button>
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
