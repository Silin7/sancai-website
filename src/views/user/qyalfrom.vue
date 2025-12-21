<script setup lang="ts">
import dayjs from 'dayjs'
import utc from 'dayjs/plugin/utc'
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import { uploadURL, fileURL } from '@/api/baseConfig'
import { casetypesApi, savecasesApi, updatecasesApi, detailcasesApi } from '@/api/modules/admin'

// utc 时间转换
dayjs.extend(utc)

const routeInfo = useRoute()
const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  id: '',
  company_id: routeInfo.query.companyid || '',
  company_name: routeInfo.query.companyname || '',
  case_type_id: '',
  name: '',
  case_tags: [],
  start_time: '',
  end_time: '',
  description: '',
  content: '',
  case_imgs: [],
})
const rules: any = reactive({
  brand: [{ required: true, message: '请输入品牌', trigger: 'blur' }],
  case_type_id: [{ required: true, message: '请选择案例类型', trigger: 'change' }],
  name: [{ required: true, message: '请输入案例名称', trigger: 'blur' }],
  start_time: [{ required: true, message: '请选择项目开始时间', trigger: 'change' }],
  end_time: [{ required: true, message: '请选择项目结束时间', trigger: 'change' }],
  description: [{ required: true, message: '请输入案例简介', trigger: 'blur' }],
  content: [{ required: true, message: '请输入详细介绍', trigger: 'blur' }],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      const data = { ...ruleForm }
      data.start_time = dayjs(data.start_time).utc().valueOf();
      data.end_time = dayjs(data.end_time).utc().valueOf();
      data.case_imgs = ruleForm.case_imgs.map((item: any) => {
        if (item.response && item.response.data.url) {
          return item.response.data.url
        } else {
          return item.name
        }
      })
      if (id === '') {
        savecasesApi(data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-qyallist')
          }
        })
      } else {
        updatecasesApi(id, data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-qyallist')
          }
        })
      }
    } else {
      console.log('error submit!', fields)
    }
  })
}

// 案例图片 - start
const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)
const uploadHeader = {
  Authorization: `Bearer ${localStorage.getItem('token') ?? ''}`
}

const handleRemove = (file: any) => {
  ruleForm.case_imgs.forEach((item: any, index: number) => {
    if (item.uid === file.uid) {
      ruleForm.case_imgs.splice(index, 1)
    }
  })
}

const handlePictureCardPreview = (file: any) => {
  dialogImageUrl.value = file.url
  dialogVisible.value = true
}
// 案例图片 - end

// 案例分类 - start
const pcateOne: any = ref([])

function getPcateOne() {
  casetypesApi().then((res: any) => {
    if (res) {
      pcateOne.value = res.data
    }
  })
}
// 案例分类 - end

const id: any = routeInfo.query.id || ''

onMounted(() => {
  // 编辑时，获取案例信息
  if (id) {
    detailcasesApi(id).then((res: any) => {
      if (res) {
        Object.keys(ruleForm).forEach((key) => {
          if (Object.prototype.hasOwnProperty.call(res, key)) {
            if (key === 'case_imgs' && res[key] && res[key].length > 0) {
              ruleForm[key] = res[key].map((item: any) => {
                return {
                  name: item,
                  url: fileURL + item,
                }
              })
            } else {
              ruleForm[key] = res[key]
            }
          }
        })
      }
    })
  }
  getPcateOne()
})
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-qyallist')"> <i class="fa fa-list mr-1"></i>案例列表 </a>
          <span class="breadcrumb-separator">/</span>
          <span>添加案例</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-qyallist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-users"></i>
        企业案例
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="关联企业" prop="company_name">
              <el-input size="large" v-model="ruleForm.company_name" placeholder="请输入关联企业" disabled />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="案例类型" prop="case_type_id">
              <el-select size="large" v-model="ruleForm.case_type_id" placeholder="选择案例类型" clearable
                style="width: 100%">
                <el-option v-for="(item, index) in pcateOne" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="案例名称" prop="name">
              <el-input size="large" v-model="ruleForm.name" placeholder="请输入案例名称" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="案例标签" prop="case_tags">
              <el-input-tag size="large" v-model="ruleForm.case_tags" placeholder="输入案例标签后按回车确认" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="项目开始时间" prop="start_time">
              <el-date-picker v-model="ruleForm.start_time" type="date" placeholder="请选择项目开始时间" value-format="x"
                style="width: 100%; height: 40px;" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="项目结束时间" prop="end_time">
              <el-date-picker v-model="ruleForm.end_time" type="date" placeholder="请选择项目结束时间" value-format="x"
                style="width: 100%; height: 40px;" />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="案例图片" prop="case_imgs">
              <el-upload :action="uploadURL + '/api/client/upload/upload/image'" :headers="uploadHeader" :multiple="true"
                v-model:file-list="ruleForm.case_imgs" list-type="picture-card" :auto-upload="true">
                <el-icon>
                  <Plus />
                </el-icon>
                <template #file="{ file }">
                  <div>
                    <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
                    <span class="el-upload-list__item-actions">
                      <span class="el-upload-list__item-preview" @click="handlePictureCardPreview(file)">
                        <el-icon><zoom-in /></el-icon>
                      </span>
                      <span v-if="!disabled" class="el-upload-list__item-delete" @click="handleRemove(file)">
                        <el-icon>
                          <Delete />
                        </el-icon>
                      </span>
                    </span>
                  </div>
                </template>
              </el-upload>
              <el-dialog v-model="dialogVisible">
                <el-image :src="dialogImageUrl" alt="Preview Image" fit="widthFix" style="width: 100%" />
              </el-dialog>
            </el-form-item>
            <!-- <p class="tips">
              <i class="fa fa-info-circle mr-1"></i>支持多张图片上传，点击图片可设置为主要展示图片
            </p> -->
          </el-col>
          <el-col :span="24">
            <el-form-item label="案例简介" prop="description">
              <el-input type="textarea" v-model="ruleForm.description" :autosize="{ minRows: 3, maxRows: 3 }"
                style="width: 100%;" placeholder="请填写其他特殊需求或补充说明" />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="详细介绍" prop="content">
              <el-input type="textarea" v-model="ruleForm.content" :autosize="{ minRows: 3, maxRows: 3 }"
                style="width: 100%;" placeholder="请填写其他特殊需求或补充说明" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div class="form-footer">
        <button type="submit" class="submit-btn" @click="submitForm(ruleFormRef)">
          <i class="fa fa-check-circle"></i>保存
        </button>
      </div>
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
