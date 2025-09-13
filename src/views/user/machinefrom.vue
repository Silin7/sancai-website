<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref, shallowRef, onBeforeUnmount, watch } from 'vue'
import { useRoute } from 'vue-router'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import { unitApi } from '@/api/modules/common'
import { productpcatechildrenApi } from '@/api/modules/product'
import { sysprovincesApi, syscitiesApi } from '@/api/modules/basic'
import { equipmentaddApi, equipmenteditApi, equipmentdetailApi } from '@/api/modules/admin'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  id: '',
  equipmentname: '',
  brand: '',
  cate_id: '',
  sub_cate_id: '',
  scene: '',
  technical_params: '',
  pretaxprice: null,
  afertaxprice: null,
  taxrate: null,
  unit_id: '',
  province_id: '',
  city_id: '',
  solution: '',
  description: '',
  imgs: ['https://www.silin7.cn/fucheng-files/systemModule/logo.png'],
})
const rules: any = reactive({
  equipmentname: [{ required: true, message: '请输入装备名称', trigger: 'blur' }],
  brand: [{ required: true, message: '请输入品牌', trigger: 'blur' }],
  cate_id: [{ required: true, message: '请选择主类别', trigger: 'change' }],
  sub_cate_id: [{ required: true, message: '请选择子类别', trigger: 'change' }],
  scene: [{ required: true, message: '请输入应用场景', trigger: 'blur' }],
  technical_params: [{ required: true, message: '请输入技术参数', trigger: 'blur' }],
  pretaxprice: [{ required: true, message: '请输入税前价格', trigger: 'blur' }],
  afertaxprice: [{ required: true, message: '请输入税后价格', trigger: 'blur' }],
  taxrate: [{ required: true, message: '请输入税率', trigger: 'blur' }],
  unit_id: [{ required: true, message: '请选择单位', trigger: 'change' }],
  province_id: [{ required: true, message: '请选择省份', trigger: 'change' }],
  city_id: [{ required: true, message: '请选择城市', trigger: 'change' }],
  solution: [{ required: true, message: '请输入解决方案', trigger: 'blur' }],
  description: [{ required: true, message: '请输入装备描述', trigger: 'blur' }],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      if (product_id === '') {
        equipmentaddApi(ruleForm).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-machinelist')
          }
        })
      } else {
        equipmenteditApi(ruleForm).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-machinelist')
          }
        })
      }
    } else {
      console.log('error submit!', fields)
    }
  })
}

// 产品分类 - start
const pcateOne: any = ref([])
const pcateTwo: any = ref([])

function getPcateOne(pid: any = 0) {
  productpcatechildrenApi({
    page: 1,
    pageSize: 999,
    parent_id: pid,
  }).then((res: any) => {
    if (res && res.items.length > 0) {
      const levelone = res.items.filter((element: any) => element.item_id === 2)
      pcateOne.value = levelone
    }
  })
}

watch(
  () => ruleForm.cate_id,
  (newVal) => {
    if (newVal) {
      productpcatechildrenApi({
        page: 1,
        pageSize: 999,
        parent_id: newVal,
      }).then((res: any) => {
        if (res && res.items.length > 0) {
          pcateTwo.value = res.items
        }
      })
    }
  },
  { immediate: true },
)

function pcateOneChange() {
  ruleForm.sub_cate_id = ''
}
// 产品分类 - end

// 省市区 - start
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
// 省市区 - end

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

// 产品图片 - start
const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)

const handleRemove = (file: any) => {
  console.log(file)
}

const handlePictureCardPreview = (file: any) => {
  dialogImageUrl.value = file.url
  dialogVisible.value = true
}

const handleDownload = (file: any) => {
  console.log(file)
}
// 产品图片 - end

const routeInfo = useRoute()
const product_id: any = routeInfo.query.product_id || ''
const unitlist: any = ref([])

onMounted(() => {
  getPcateOne()
  getSysprovinces()
  // 编辑时，获取产品信息
  if (product_id) {
    equipmentdetailApi({ product_id }).then((res: any) => {
      if (res) {
        Object.keys(ruleForm).forEach((key) => {
          if (Object.prototype.hasOwnProperty.call(res, key)) {
            ruleForm[key] = res[key]
          }
        })
      }
    })
  }
  // 单位列表
  unitApi({
    type: 3
  }).then((res: any) => {
    if (res) {
      unitlist.value = res
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
          <a @click="pageJump('user-machinelist')">
            <i class="fa fa-list mr-1"></i>机械产品列表
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>上传新机械</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-machinelist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-upload text-primary"></i>
        上传机械产品信息
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="装备名称" prop="equipmentname">
              <el-input size="large" v-model="ruleForm.equipmentname" placeholder="请输入装备名称" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="品牌" prop="brand">
              <el-input size="large" v-model="ruleForm.brand" placeholder="请输入品牌" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="主类别" prop="cate_id">
              <el-select size="large" v-model="ruleForm.cate_id" placeholder="选择主类别" clearable style="width: 100%"
                @change="pcateOneChange">
                <el-option v-for="(item, index) in pcateOne" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="子类别" prop="sub_cate_id">
              <el-select size="large" v-model="ruleForm.sub_cate_id" placeholder="选择子类别" clearable style="width: 100%">
                <el-option v-for="(item, index) in pcateTwo" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="应用场景" prop="scene">
              <el-input size="large" v-model="ruleForm.scene" placeholder="请输入应用场景" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="技术参数" prop="technical_params">
              <el-input size="large" v-model="ruleForm.technical_params" placeholder="请输入技术参数" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="税前价格(元)" prop="pretaxprice">
              <el-input-number size="large" v-model="ruleForm.pretaxprice" placeholder="请输入税前价格(元)" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="税后价格(元)" prop="afertaxprice">
              <el-input-number size="large" v-model="ruleForm.afertaxprice" placeholder="请输入税后价格(元)" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="税率(%)" prop="taxrate">
              <el-input-number size="large" v-model="ruleForm.taxrate" placeholder="请输入税率(%)" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="单位" prop="unit_id">
              <el-select size="large" v-model="ruleForm.unit_id" placeholder="选择单位">
                <el-option v-for="(item, index) in unitlist" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="省份" prop="province_id">
              <el-select size="large" v-model="ruleForm.province_id" placeholder="选择省份" @change="provinceChange">
                <el-option v-for="(item, index) in provincesList" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="城市" prop="city_id">
              <el-select size="large" v-model="ruleForm.city_id" placeholder="选择城市">
                <el-option v-for="(item, index) in citiesList" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="解决方案" prop="solution">
              <div style="border: 1px solid #e4e7ed; width: 100%">
                <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef1" :defaultConfig="toolbarConfig"
                  mode="default" />
                <Editor style="height: 300px; overflow-y: hidden" v-model="ruleForm.solution"
                  :defaultConfig="editorConfig1" mode="default" @onCreated="handleCreated1" />
              </div>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="装备描述" prop="description">
              <div style="border: 1px solid #e4e7ed; width: 100%">
                <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef2" :defaultConfig="toolbarConfig"
                  mode="default" />
                <Editor style="height: 300px; overflow-y: hidden" v-model="ruleForm.description"
                  :defaultConfig="editorConfig2" mode="default" @onCreated="handleCreated2" />
              </div>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="产品图片" prop="imgs">
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
        </el-row>
      </el-form>
      <div class="form-footer">
        <button type="submit" class="submit-btn" @click="submitForm(ruleFormRef)">
          <i class="fa fa-check-circle"></i>提交服务产品
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
