<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { Search, Plus } from '@element-plus/icons-vue'
import pageJump from '@/hooks/pageJump'
import usePagination from '@/hooks/usePagination'
import useDebounce from '@/utils/useDebounce'
import { currentcompanyApi } from '@/api/modules/login'
import { certificatesApi } from '@/api/modules/admin'
import { ElMessage } from 'element-plus'

// 查询条件
const queryForm: any = reactive({
  name: '',
  qualification_type_id: '',
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
  if (queryForm.name) {
    parameters['name'] = queryForm.name
  }
  if (queryForm.qualification_type_id) {
    parameters['qualification_type_id'] = queryForm.qualification_type_id
  }
  if (queryForm.status) {
    parameters['status'] = queryForm.status
  }
  certificatesApi(parameters).then((res: any) => {
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

const companyid: any = ref('')
const companyname: any = ref('')

onMounted(() => {
  // 获取当前用户的企业信息
  currentcompanyApi().then((res: any) => {
    if (res && res.status) {
      companyid.value = res.data.id
      companyname.value = res.data.company_name
      getDataList()
    } else {
      ElMessage({
        type: 'error',
        message: '请先维护企业信息',
      })
      pageJump('user-profile')
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
          <a @click="pageJump('user-index')"> <i class="fa fa-home mr-1"></i>首页 </a>
          <span class="breadcrumb-separator">/</span>
          <span>企业资质</span>
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
        企业资质
      </h2>
      <!-- 查询条件 -->
      <el-form :model="queryForm">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-form-item>
              <el-input size="large" v-model="queryForm.name" placeholder="搜索服务名称..." clearable :prefix-icon="Search"
                @input="useDebounce().fn(getDataList)" />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-select size="large" v-model="queryForm.qualification_type_id" placeholder="资质类型" clearable
                @change="useDebounce().fn(getDataList)">
                <template #prefix>
                  <el-icon>
                    <Search />
                  </el-icon>
                </template>
                <el-option label="全部资质" value="" />
                <el-option label="营业执照" value="1" />
                <el-option label="行业资质证书" value="2" />
                <el-option label="荣誉证书" value="3" />
                <el-option label="其他证书" value="4" />
              </el-select>
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
                <el-option label="全部状态" value="" />
                <el-option label="待审核" value="0" />
                <el-option label="审核通过" value="1" />
                <el-option label="驳回" value="2" />
                <el-option label="关闭" value="3" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item>
              <el-button size="large" :icon="Plus" color="#377dff" @click="pageJump('user-qyzzfrom', {
                companyid,
                companyname
              })">新增</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <!-- 数据表格 -->
      <el-table v-loading="tableLoading" :data="groupData" border highlight-current-row>
        <el-table-column :show-overflow-tooltip="true" align="center" prop="name" label="资质名称" />
        <el-table-column :show-overflow-tooltip="true" align="center" prop="qualification_type_name" label="资质类型" />
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
              <el-button text type="primary" @click="pageJump('user-qyzzfrom', {
                id: scope.row.id,
                companyid,
                companyname
              })"> 编辑
              </el-button>
              <!-- <el-button v-if="scope.$index % 2 === 0" text type="danger"> 删除 </el-button>
              <el-button v-else text type="danger"> 下架 </el-button> -->
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
