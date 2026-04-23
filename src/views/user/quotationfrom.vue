<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { h, onMounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import pageJump from '@/hooks/pageJump'
import formatCurrency from '@/hooks/formatCurrency'
import { inquiryordersdetailApi } from '@/api/modules/admin'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  inquiry_no: '',
  total_amount: '',
  product_items: '',
})


const routeInfo = useRoute()
const inquiry_id: any = routeInfo.query.inquiry_id || ''

onMounted(() => {
  // 编辑时，获取产品信息
  if (inquiry_id) {
    inquiryordersdetailApi(inquiry_id).then((res: any) => {
      if (res) {
        Object.keys(ruleForm).forEach((key) => {
          if (Object.prototype.hasOwnProperty.call(res.data, key)) {
            ruleForm[key] = res.data[key]
          }
          if (key === 'total_amount' && ruleForm[key]) {
            ruleForm[key] = '¥' + formatCurrency(ruleForm[key])
          }
        })
      }
    })
  }
})

// 合计行
const getSummaries = (param: any) => {
  const { columns, data } = param
  const sums: (any)[] = []
  columns.forEach((column: any, index: any) => {
    if (index === 0) {
      sums[index] = h('div', { style: { textDecoration: 'underline' } }, [
        '合计',
      ])
      return
    }
    const values = data.map((item: any) => Number(item[column.property]))
    if (!values.every((value: any) => Number.isNaN(value))) {
      sums[index] = `$ ${values.reduce((prev: any, curr: any) => {
        const value = Number(curr)
        if (!Number.isNaN(value)) {
          return prev + curr
        } else {
          return prev
        }
      }, 0)}`
    } else {
      sums[index] = 'N/A'
    }
  })

  return sums
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
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-quotationlist')">
            <i class="fa fa-list mr-1"></i>询价单列表
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>查看询价单</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-quotationlist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-upload text-primary"></i>
        查看询价单信息
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="询价单号" prop="inquiry_no">
              <el-input size="large" disabled v-model="ruleForm.inquiry_no" placeholder="请输入询价单号" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="金额合计" prop="total_amount">
              <el-input size="large" disabled v-model="ruleForm.total_amount" placeholder="金额合计" />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label=" 产品明细 " prop="product_items">
              <!-- show-summary :summary-method="getSummaries" -->
              <el-table :data="ruleForm.product_items" border highlight-current-row>
                <el-table-column :show-overflow-tooltip="true" align="center" prop="product_type" label="产品类型" />
                <el-table-column :show-overflow-tooltip="true" align="center" prop="product_name" label="产品名称" />
                <el-table-column align="center" label="税前价格">
                  <template #default="scope">
                    <span>¥{{ formatCurrency(scope.row.untax_price) }}</span>
                  </template>
                </el-table-column>
                <el-table-column align="center" label="税率">
                  <template #default="scope">
                    <span>{{ formatTaxRate(scope.row.tax_rate) }}</span>
                  </template>
                </el-table-column>
                <!-- <el-table-column  align="center" prop="shuliang" label="数量" />
                <el-table-column  align="center" prop="danwei" label="单位" />
                <el-table-column  align="center" prop="xiaoji" label="小计" /> -->
                <el-table-column :show-overflow-tooltip="true" align="center" prop="supplier_name" label="供应商" />
              </el-table>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.tips {
  font-size: 0.875rem;
  line-height: 1.25rem;
  margin-top: -0.25rem;
  color: rgb(107 114 128 / var(--tw-text-opacity, 1));
  color: #c0c4cc;
}
</style>
