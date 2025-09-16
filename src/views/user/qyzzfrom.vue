<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref, shallowRef, onBeforeUnmount, watch } from 'vue'
import { useRoute } from 'vue-router'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import { baseURL, fileURL } from '@/api/baseConfig'
import { savecertificatesApi, updatecertificatesApi, detailcertificatesApi } from '@/api/modules/admin'

const routeInfo = useRoute()
const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  id: '',
  company_id: routeInfo.query.companyid || '',
  company_name: routeInfo.query.companyname || '',
  qualification_type_id: '',
  name: '',
  obtain_time: '',
  valid_start: '',
  valid_end: '',
  description: '',
  qualification_imgs: [],
})
const rules: any = reactive({
  brand: [{ required: true, message: '请输入品牌', trigger: 'blur' }],
  qualification_type_id: [{ required: true, message: '请选择资质类型', trigger: 'change' }],
  name: [{ required: true, message: '请输入资质名称', trigger: 'blur' }],
  obtain_time: [{ required: true, message: '请选择获得时间', trigger: 'change' }],
  valid_start: [{ required: true, message: '请选择有效期开始', trigger: 'change' }],
  valid_end: [{ required: true, message: '请选择有效期结束', trigger: 'change' }],
  description: [{ required: true, message: '请输入资质描述', trigger: 'blur' }],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      const data = { ...ruleForm }
      data.qualification_imgs = ruleForm.qualification_imgs.map((item: any) => {
        if (item.response && item.response.data.url) {
          return item.response.data.url
        } else {
          return item.name
        }
      })
      if (id === '') {
        savecertificatesApi(data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-qyzzlist')
          }
        })
      } else {
        updatecertificatesApi(id, data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-qyzzlist')
          }
        })
      }
    } else {
      console.log('error submit!', fields)
    }
  })
}

// 编辑器实例 - start
const editorRef1 = shallowRef()
const editorRef2 = shallowRef()

const toolbarConfig = {
  toolbarKeys: ['fontSize', 'bold', 'underline'],
}
const editorConfig1 = { placeholder: '请详细描述解决方案' }
const editorConfig2 = { placeholder: '请详细描述服务内容、流程、交付物等' }

onBeforeUnmount(() => {
  const editor1 = editorRef1.value
  if (editor1 == null) return
  editor1.destroy()
  const editor2 = editorRef2.value
  if (editor2 == null) return
  editor2.destroy()
})

const handleCreated1 = (editor: any) => {
  editorRef1.value = editor
}
const handleCreated2 = (editor: any) => {
  editorRef2.value = editor
}
// 编辑器实例 - end

// 资质图片 - start
const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)
const uploadHeader = {
  Authorization: `Bearer ${localStorage.getItem('token') ?? ''}`
}

const handleRemove = (file: any) => {
  ruleForm.qualification_imgs.forEach((item: any, index: number) => {
    if (item.uid === file.uid) {
      ruleForm.qualification_imgs.splice(index, 1)
    }
  })
}

const handlePictureCardPreview = (file: any) => {
  dialogImageUrl.value = file.url
  dialogVisible.value = true
}
// 资质图片 - end

const id: any = routeInfo.query.id || ''

onMounted(() => {
  // 编辑时，获取资质信息
  if (id) {
    detailcertificatesApi(id).then((res: any) => {
      if (res) {
        Object.keys(ruleForm).forEach((key) => {
          if (Object.prototype.hasOwnProperty.call(res, key)) {
            if (key === 'qualification_imgs' && res[key] && res[key].length > 0) {
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
})
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-qyzzlist')"> <i class="fa fa-list mr-1"></i>资质列表 </a>
          <span class="breadcrumb-separator">/</span>
          <span>添加资质</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-qyzzlist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-users"></i>
        企业资质
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="关联企业" prop="company_name">
              <el-input size="large" v-model="ruleForm.company_name" placeholder="请输入关联企业" disabled />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="资质类型" prop="qualification_type_id">
              <el-select size="large" v-model="ruleForm.qualification_type_id" placeholder="选择资质类型" clearable
                style="width: 100%">
                <el-option label="营业执照" :value="1" />
                <el-option label="行业资质资质" :value="2" />
                <el-option label="荣誉资质" :value="3" />
                <el-option label="其他资质" :value="4" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="资质名称" prop="name">
              <el-input size="large" v-model="ruleForm.name" placeholder="请输入资质名称" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="获得时间" prop="obtain_time">
              <el-date-picker v-model="ruleForm.obtain_time" type="date" placeholder="请选择获得时间" value-format="x"
                style="width: 100%;" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="有效期开始" prop="valid_start">
              <el-date-picker v-model="ruleForm.valid_start" type="date" placeholder="请选择有效期开始" value-format="x"
                style="width: 100%;" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="有效期结束" prop="valid_end">
              <el-date-picker v-model="ruleForm.valid_end" type="date" placeholder="请选择有效期结束" value-format="x"
                style="width: 100%;" />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="资质图片" prop="qualification_imgs">
              <el-upload :action="baseURL + '/api/client/upload/upload/image'" :headers="uploadHeader" :multiple="true"
                v-model:file-list="ruleForm.qualification_imgs" list-type="picture-card" :auto-upload="true">
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
            <el-form-item label="资质描述" prop="description">
              <div style="border: 1px solid #e4e7ed; width: 100%">
                <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef2" :defaultConfig="toolbarConfig"
                  mode="default" />
                <Editor style="height: 300px; overflow-y: hidden" v-model="ruleForm.description"
                  :defaultConfig="editorConfig2" mode="default" @onCreated="handleCreated2" />
              </div>
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
