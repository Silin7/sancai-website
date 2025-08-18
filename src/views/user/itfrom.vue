<script setup lang="ts">
import { reactive, ref } from 'vue'
import type { UploadFile } from 'element-plus'
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import pageJump from '@/hooks/pageJump'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  categoryLevel1: '',
  categoryLevel2: '',
  categoryLevel3: '',
  priceBeforeTax: null,
  priceAfterTax: null,
  serviceDescription: '',
})
const rules: any = reactive({
  categoryLevel1: [{ required: true, message: '请选择产品类别', trigger: 'change' }],
  categoryLevel2: [{ required: true, message: '请选择二级分类', trigger: 'change' }],
  categoryLevel3: [{ required: true, message: '请选择三级分类', trigger: 'change' }],
  priceBeforeTax: [{ required: true, message: '请输入单价（含税）', trigger: 'blur' }],
  priceAfterTax: [{ required: true, message: '请输入单价（不含税）', trigger: 'blur' }],
  serviceDescription: [{ required: true, message: '请输入材料内容介绍', trigger: 'blur' }],
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

const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)

const handleRemove = (file: UploadFile) => {
  console.log(file)
}

const handlePictureCardPreview = (file: UploadFile) => {
  dialogImageUrl.value = file.url!
  dialogVisible.value = true
}

const handleDownload = (file: UploadFile) => {
  console.log(file)
}
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-itlist')">
            <i class="fa fa-list mr-1"></i>信息化产品列表
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>上传新信息化产品</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-itlist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-upload text-primary"></i>
        上传信息化产品信息
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="产品类别" prop="categoryLevel1">
              <el-select size="large" v-model="ruleForm.categoryLevel1" placeholder="选择产品类别" clearable
                style="width: 100%">
                <el-option label="全部材质" value="all" />
                <el-option label="钢材" value="gangcai" />
                <el-option label="木材" value="mucai" />
                <el-option label="塑料" value="suliao" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="二级分类" prop="categoryLevel2">
              <el-select size="large" v-model="ruleForm.categoryLevel2" placeholder="选择二级分类" clearable
                style="width: 100%">
                <el-option label="全部材质" value="all" />
                <el-option label="钢材" value="gangcai" />
                <el-option label="木材" value="mucai" />
                <el-option label="塑料" value="suliao" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="三级分类" prop="categoryLevel3">
              <el-select size="large" v-model="ruleForm.categoryLevel3" placeholder="选择三级分类" clearable
                style="width: 100%">
                <el-option label="全部材质" value="all" />
                <el-option label="钢材" value="gangcai" />
                <el-option label="木材" value="mucai" />
                <el-option label="塑料" value="suliao" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="单价（含税）" prop="priceBeforeTax">
              <el-input-number size="large" v-model="ruleForm.priceBeforeTax" placeholder="请输入单价（含税） " :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="单价（不含税）" prop="priceAfterTax">
              <el-input-number size="large" v-model="ruleForm.priceAfterTax" placeholder="请输入单价（不含税）" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="机械图片" prop="serviceDescription">
              <el-upload action="#" :multiple="true" list-type="picture-card" :auto-upload="false">
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
                      <span v-if="!disabled" class="el-upload-list__item-delete" @click="handleDownload(file)">
                        <el-icon>
                          <Download />
                        </el-icon>
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
                <img w-full :src="dialogImageUrl" alt="Preview Image" />
              </el-dialog>
            </el-form-item>

            <p class="tips">
              <i class="fa fa-info-circle mr-1"></i>支持多张图片上传，点击图片可设置为主要展示图片
            </p>
          </el-col>
          <el-col :span="24">
            <el-form-item label="产品描述 (最多300字)" prop="serviceDescription">
              <el-input v-model="ruleForm.serviceDescription" type="textarea" :autosize="{ minRows: 5, maxRows: 10 }"
                placeholder="请输入产品详细描述，包括特性、用途、注意事项等（最多300字）" :maxlength="300" show-word-limit />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div class="form-footer">
        <button type="submit" class="submit-btn" @click="submitForm(ruleFormRef)">
          <i class="fa fa-check-circle"></i>提交产品信息
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
