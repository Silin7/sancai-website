<script setup lang="ts">
import { reactive, ref } from 'vue'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  serviceName: '',
  mainCategory: '',
  subCategory: '',
  priceBeforeTax: '',
  priceAfterTax: '',
  serviceDescription: '',
})
const rules: any = reactive({
  serviceName: [{ required: true, message: '请输入服务名称', trigger: 'blur' }],
  mainCategory: [{ required: true, message: '请选择主类别', trigger: 'change' }],
  subCategory: [{ required: true, message: '请选择子类别', trigger: 'change' }],
  priceBeforeTax: [{ required: true, message: '请输入税前价格', trigger: 'blur' }],
  priceAfterTax: [{ required: true, message: '请输入税后价格', trigger: 'blur' }],
  serviceDescription: [{ required: true, message: '请输入服务内容介绍', trigger: 'blur' }],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!', fields)
    }
  })
}
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a> <i class="fa fa-list mr-1"></i>产品列表 </a>
          <span class="breadcrumb-separator">/</span>
          <span>发布新服务</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn"><i class="fa fa-arrow-left mr-1"></i>返回列表</button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-key text-primary"></i>
        修改登录密码
      </h2>
      <el-form
        label-position="top"
        ref="ruleFormRef"
        :model="ruleForm"
        :rules="rules"
        label-width="auto"
      >
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="服务名称" prop="serviceName">
              <el-input size="large" v-model="ruleForm.serviceName" placeholder="请输入服务名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="主类别" prop="mainCategory">
              <el-select
                size="large"
                v-model="ruleForm.mainCategory"
                placeholder="选择主类别"
                clearable
                style="width: 100%"
              >
                <el-option label="全部材质" value="all" />
                <el-option label="钢材" value="gangcai" />
                <el-option label="木材" value="mucai" />
                <el-option label="塑料" value="suliao" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="子类别" prop="subCategory">
              <el-select
                size="large"
                v-model="ruleForm.subCategory"
                placeholder="选择子类别"
                clearable
                style="width: 100%"
              >
                <el-option label="全部材质" value="all" />
                <el-option label="钢材" value="gangcai" />
                <el-option label="木材" value="mucai" />
                <el-option label="塑料" value="suliao" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="税前价格(元)" prop="priceBeforeTax">
              <el-input-number
                size="large"
                v-model="ruleForm.priceBeforeTax"
                placeholder="请输入税前价格(元) "
                :min="0"
                style="width: 100%"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="税后价格(元)" prop="priceAfterTax">
              <el-input-number
                size="large"
                v-model="ruleForm.priceAfterTax"
                placeholder="请输入税后价格(元) "
                :min="0"
                style="width: 100%"
              />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="服务内容介绍" prop="serviceDescription">
              <el-input
                v-model="ruleForm.serviceDescription"
                type="textarea"
                :autosize="{ minRows: 5, maxRows: 10 }"
                placeholder="请详细描述服务内容、流程、交付物等"
                :maxlength="1000"
                show-word-limit
              />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div class="form-footer">
        <button type="submit" class="submit-btn" @click="submitForm(ruleFormRef)">
          <i class="fa fa-save"></i>确认修改
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.password-rules {
  margin: 8px 0 14px;
  font-size: 12px;
  color: #909399;

  .rule-item {
    display: flex;
    align-items: center;
    margin-bottom: 4px;

    .rule-icon {
      color: #f5222d;
      margin-right: 6px;
      font-size: 12px;
    }
  }
}
</style>
