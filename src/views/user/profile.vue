<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref, shallowRef, onBeforeUnmount, watch } from 'vue'
import { ElMessage } from 'element-plus'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import pageJump from '@/hooks/pageJump'
import { sysprovincesApi, syscitiesApi } from '@/api/modules/basic'
import { companyinfoApi, savecompanyinfoApi } from '@/api/modules/admin'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  company_name: '',
  province_name: '',
  city_name: '',
  company_address: '',
  tags: [],
  contact_person: '',
  tel: '',
  email: '',
  company_intro: '',
})
const rules: any = reactive({
  company_name: [{ required: true, message: '请输入公司名称', trigger: 'blur' }],
  company_address: [{ required: true, message: '请输入公司地址', trigger: 'blur' }],
  contact_person: [{ required: true, message: '请输入联系人', trigger: 'blur' }],
  tel: [
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
      savecompanyinfoApi(ruleForm).then((res: any) => {
        if (res) {
          ElMessage({
            type: 'success',
            message: '保存成功',
          })
        }
      })
    } else {
      console.log('error submit!', fields)
    }
  })
}

// 省 列表
const provincesList: any = ref([])
const citiesList: any = ref([])

function getSysprovinces() {
  sysprovincesApi().then((res: any) => {
    if (res) {
      provincesList.value = res
    }
  })
}

watch(
  () => ruleForm.province_id,
  (newVal) => {
    if (newVal) {
      syscitiesApi(newVal).then((res: any) => {
        if (res) {
          citiesList.value = res
        }
      })
    }
  },
  { immediate: true },
)

function provinceChange() {
  ruleForm.city_id = ''
}

// 编辑器实例，必须用 shallowRef
const editorRef = shallowRef()

const toolbarConfig = {
  toolbarKeys: ['fontSize', 'bold', 'underline'],
}
const editorConfig = { placeholder: '请输入内容...' }

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value
  if (editor == null) return
  editor.destroy()
})

const handleCreated = (editor: any) => {
  // 记录 editor 实例，重要！
  editorRef.value = editor
  // const allmenukeys = editor.getAllMenuKeys()
  // console.log('allmenukeys-------->', JSON.stringify(allmenukeys))
}

onMounted(() => {
  companyinfoApi('')
    .then((res: any) => {
      if (res) {
        Object.assign(ruleForm, res)
      }
    })
    .finally(() => {
      getSysprovinces()
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
          <span>企业资料</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-index')">
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-user text-primary"></i>
        编辑企业资料
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-form-item label="公司名称" prop="company_name">
          <el-input size="large" v-model="ruleForm.company_name" placeholder="请输入公司全称" />
        </el-form-item>
        <el-form-item label="所在地区" prop="county">
          <el-row :gutter="12" style="width: calc(100% + 12px)">
            <el-col :span="12">
              <el-select size="large" v-model="ruleForm.province_id" placeholder="选择省" @change="provinceChange">
                <el-option v-for="(item, index) in provincesList" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-col>
            <el-col :span="12">
              <el-select size="large" v-model="ruleForm.city_id" placeholder="选择市">
                <el-option v-for="(item, index) in citiesList" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="公司地址" prop="company_address">
          <el-input size="large" v-model="ruleForm.company_address" placeholder="请输入详细地址" />
        </el-form-item>
        <el-form-item label="产品品牌 (最多5个)" prop="tags">
          <el-input-tag size="large" v-model="ruleForm.tags" placeholder="输入品牌名称后按回车确认" />
        </el-form-item>
        <p class="tips">
          <i class="fa fa-info-circle mr-1"></i>输入品牌名称后按回车键添加，最多可添加5个品牌
        </p>
        <el-form-item label="联系人" prop="contact_person">
          <el-input size="large" v-model="ruleForm.contact_person" placeholder="请输入联系人姓名" />
        </el-form-item>
        <el-form-item label="联系电话" prop="tel">
          <el-input size="large" v-model="ruleForm.tel" type="tel" placeholder="请输入联系人电话" />
        </el-form-item>
        <el-form-item label="电子邮箱" prop="email">
          <el-input size="large" v-model="ruleForm.email" type="email" placeholder="请输入电子邮箱" />
        </el-form-item>
        <el-form-item label="公司简介 (最多500字)" prop="company_intro">
          <div style="border: 1px solid #e4e7ed; width: 100%">
            <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef" :defaultConfig="toolbarConfig"
              mode="default" />
            <Editor style="height: 500px; overflow-y: hidden" v-model="ruleForm.company_intro"
              :defaultConfig="editorConfig" mode="default" @onCreated="handleCreated" />
          </div>
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
  margin-top: -12px;
  margin-bottom: 18px;
  color: rgb(107 114 128 / var(--tw-text-opacity, 1));
  color: #c0c4cc;
}
</style>

<style>
.w-e-hover-bar {
  opacity: 0;
}
</style>
