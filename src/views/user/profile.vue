<script setup lang="ts">
import { reactive, ref } from 'vue'
import eventBus from '@/utils/eventBus'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  cname: '',
  province: '',
  city: '',
  county: '',
  address: '',
  branding: [],
  contacts: '',
  phone: '',
  email: '',
  desc: '',
})
const rules: any = reactive({
  cname: [
    { required: true, message: '请输入公司名称', trigger: 'blur' },
    { min: 3, max: 5, message: 'Length should be 3 to 5', trigger: 'blur' },
  ],
  county: [{ required: true, message: '请选择所在地区', trigger: 'change' }],
  address: [{ required: true, message: '请输入公司地址', trigger: 'blur' }],
  contacts: [{ required: true, message: '请输入联系人', trigger: 'blur' }],
  phone: [
    { required: true, message: '请输入联系电话', trigger: 'blur' },
    { pattern: /^(?:(?:\+|00)86)?1[3-9]\d{9}$/, message: '手机号码格式错误', trigger: 'blur' },
  ],
  email: [
    {
      pattern: /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/,
      message: '电子邮箱格式错误',
      trigger: 'blur',
    },
  ],
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
          <a @click="eventBus.emit('set-router-store', 'user-index')">
            <i class="fa fa-home mr-1"></i>首页
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>用户资料</span>
        </div>
        <div class="action-buttons">
          <button
            class="action-btn back-btn"
            @click="eventBus.emit('set-router-store', 'user-index')"
          >
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
          <!-- <button class="action-btn save-btn"><i class="fa fa-save mr-1"></i>保存资料</button> -->
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-user text-primary"></i>
        编辑用户资料
      </h2>
      <el-form
        label-position="top"
        ref="ruleFormRef"
        :model="ruleForm"
        :rules="rules"
        label-width="auto"
      >
        <el-form-item label="公司名称" prop="cname">
          <el-input size="large" v-model="ruleForm.cname" placeholder="请输入公司全称" />
        </el-form-item>
        <el-form-item label="所在地区" prop="county">
          <el-row :gutter="12" style="width: calc(100% + 12px)">
            <el-col :span="8">
              <el-select size="large" v-model="ruleForm.province" placeholder="选择省">
                <el-option label="Zone one" value="shanghai" />
                <el-option label="Zone two" value="beijing" />
              </el-select>
            </el-col>
            <el-col :span="8">
              <el-select size="large" v-model="ruleForm.city" placeholder="选择市">
                <el-option label="Zone one" value="shanghai" />
                <el-option label="Zone two" value="beijing" />
              </el-select>
            </el-col>
            <el-col :span="8">
              <el-select size="large" v-model="ruleForm.county" placeholder="选择县/区">
                <el-option label="Zone one" value="shanghai" />
                <el-option label="Zone two" value="beijing" />
              </el-select>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="公司地址" prop="address">
          <el-input size="large" v-model="ruleForm.address" placeholder="请输入详细地址" />
        </el-form-item>
        <el-form-item label="产品品牌 (最多5个)" prop="branding">
          <el-input
            size="large"
            v-model="ruleForm.branding"
            placeholder="输入品牌名称后按回车确认"
          />
          <!-- <el-select
            v-model="ruleForm.cname"
            multiple
            collapse-tags
            collapse-tags-tooltip
            :max-collapse-tags="5"
            placeholder="输入品牌名称后按回车确认"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select> -->
        </el-form-item>
        <p class="tips">
          <i class="fa fa-info-circle mr-1"></i>输入品牌名称后按回车键添加，最多可添加5个品牌
        </p>
        <el-form-item label="联系人" prop="contacts">
          <el-input size="large" v-model="ruleForm.contacts" placeholder="请输入联系人姓名" />
        </el-form-item>
        <el-form-item label="联系电话" prop="phone">
          <el-input
            size="large"
            v-model="ruleForm.phone"
            type="tel"
            placeholder="请输入联系人电话"
          />
        </el-form-item>
        <el-form-item label="电子邮箱" prop="email">
          <el-input
            size="large"
            v-model="ruleForm.email"
            type="email"
            placeholder="请输入电子邮箱"
          />
        </el-form-item>
        <el-form-item label="公司简介 (最多500字)" prop="desc">
          <el-input
            v-model="ruleForm.desc"
            type="textarea"
            :autosize="{ minRows: 3, maxRows: 10 }"
            placeholder="请输入公司简介，包括主营业务、优势等（最多500字）"
            :maxlength="500"
            show-word-limit
          />
        </el-form-item>
      </el-form>
      <div class="form-footer" @click="submitForm(ruleFormRef)">
        <button class="submit-btn"><i class="fa fa-check-circle"></i>保存资料</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tips {
  font-size: 0.875rem;
  line-height: 1.25rem;
  margin-top: -0.25rem;
  color: rgb(107 114 128 / var(--tw-text-opacity, 1));
  color: #c0c4cc;
}
</style>
