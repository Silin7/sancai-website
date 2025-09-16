<script setup lang="ts">
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import { updayepasswordApi } from '@/api/modules/login'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  old_password: '',
  new_password: '',
  aPassword: '',
})
const rules: any = reactive({
  old_password: [{ required: true, message: '请输入当前密码', trigger: 'blur' }],
  new_password: [
    { required: true, message: '请输入新密码', trigger: 'blur' },
    {
      pattern: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$/,
      message: '请输入8-20位密码（含字母和数字）',
      trigger: 'blur',
    },
  ],
  aPassword: [
    { required: true, message: '请再次输入新密码', trigger: 'blur' },
    {
      validator: (rule: any, value: any, callback: any) => {
        if (value !== ruleForm.new_password) {
          callback(new Error('两次密码输入不一致'))
        } else {
          callback()
        }
      },
      trigger: 'change',
    },
  ],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      console.log('submit!')
      updayepasswordApi(ruleForm).then((res: any) => {
        if (res) {
          ElMessage({
            type: 'success',
            message: '修改成功，请重新登录',
          })
          pageJump('login')
        }
      })
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
          <a @click="pageJump('user-index')">
            <i class="fa fa-home mr-1"></i>首页
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>改密码</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-index')">
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-key text-primary"></i>
        修改登录密码
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-form-item label="当前密码" prop="old_password">
          <el-input size="large" v-model="ruleForm.old_password" type="password" show-password placeholder="请输入当前密码" />
        </el-form-item>
        <el-form-item label="新密码" prop="new_password">
          <el-input size="large" v-model="ruleForm.new_password" type="password" show-password placeholder="请输入新密码" />
        </el-form-item>
        <div class="password-rules">
          <div class="rule-item">
            <i class="fa fa-circle rule-icon"></i>
            <span>8-20个字符</span>
          </div>
          <div class="rule-item">
            <i class="fa fa-circle rule-icon"></i>
            <span>包含字母</span>
          </div>
          <div class="rule-item">
            <i class="fa fa-circle rule-icon"></i>
            <span>包含数字</span>
          </div>
          <div class="rule-item">
            <i class="fa fa-circle rule-icon"></i>
            <span>包含特殊字符(!@#$%^&amp;*)</span>
          </div>
        </div>
        <el-form-item label="确认新密码" prop="aPassword">
          <el-input size="large" v-model="ruleForm.aPassword" type="password" show-password placeholder="请再次输入新密码" />
        </el-form-item>
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
