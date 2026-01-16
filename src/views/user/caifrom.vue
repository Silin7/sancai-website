<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref, shallowRef, onBeforeUnmount, watch } from 'vue'
import { useRoute } from 'vue-router'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import { uploadURL, fileURL } from '@/api/baseConfig'
import { unitApi } from '@/api/modules/common'
import { productpcatechildrenApi } from '@/api/modules/product'
import { sysprovincesApi, syscitiesApi } from '@/api/modules/basic'
import { materialaddApi, materialeditApi, materialdetailApi } from '@/api/modules/admin'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  id: '',
  materialname: '',
  brand: '',
  cate_id: '',
  sub_cate_id: '',
  three_cate_id: '',
  scene: '',
  material: '',
  specification: '',
  pretaxprice: null,
  afertaxprice: null,
  taxrate: null,
  unit_id: '',
  lowest: null,
  province_id: '',
  city_id: '',
  technical_params: '',
  solution: '',
  description: '',
  imgs: [],
  memo: '',
})
const rules: any = reactive({
  materialname: [{ required: true, message: '请输入材料名称', trigger: 'blur' }],
  brand: [{ required: true, message: '请输入品牌', trigger: 'blur' }],
  cate_id: [{ required: true, message: '请选择主分类', trigger: 'change' }],
  sub_cate_id: [{ required: true, message: '请选择二级分类', trigger: 'change' }],
  three_cate_id: [{ required: true, message: '请选择三级分类', trigger: 'change' }],
  scene: [{ required: true, message: '请输入应用场景', trigger: 'blur' }],
  material: [{ required: true, message: '请输入材质', trigger: 'blur' }],
  specification: [{ required: true, message: '请输入规格型号', trigger: 'blur' }],
  pretaxprice: [{ required: true, message: '税前价格', trigger: 'blur' }],
  afertaxprice: [{ required: true, message: '税后价格', trigger: 'blur' }],
  taxrate: [{ required: true, message: '请输入税率', trigger: 'blur' }],
  unit_id: [{ required: true, message: '请选择单位', trigger: 'change' }],
  lowest: [{ required: true, message: '请输入最低采购数量', trigger: 'blur' }],
  province_id: [{ required: true, message: '请选择省份', trigger: 'change' }],
  city_id: [{ required: true, message: '请选择城市', trigger: 'change' }],
  technical_params: [{ required: true, message: '请输入技术参数', trigger: 'blur' }],
  solution: [{ required: true, message: '请输入解决方案', trigger: 'blur' }],
  description: [{ required: true, message: '请输入产品描述', trigger: 'blur' }],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      const data = { ...ruleForm }
      data.imgs = ruleForm.imgs.map((item: any) => {
        if (item.response && item.response.data.url) {
          return item.response.data.url
        } else {
          return item.name
        }
      })
      if (product_id === '') {
        materialaddApi(data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-cailist')
          }
        })
      } else {
        materialeditApi(data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-cailist')
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
const pcateThree: any = ref([])

function getPcateOne(pid: any = 0) {
  productpcatechildrenApi({
    page: 1,
    pageSize: 999,
    parent_id: pid,
  }).then((res: any) => {
    if (res && res.items.length > 0) {
      const levelone = res.items.filter((element: any) => element.item_id === 1)
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

watch(
  () => ruleForm.sub_cate_id,
  (newVal) => {
    if (newVal) {
      productpcatechildrenApi({
        page: 1,
        pageSize: 999,
        parent_id: newVal,
      }).then((res: any) => {
        if (res && res.items.length > 0) {
          pcateThree.value = res.items
        }
      })
    }
  },
  { immediate: true },
)

function pcateTwoChange() {
  ruleForm.three_cate_id = ''
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

// 产品图片 - start
const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)
const uploadHeader = {
  Authorization: `Bearer ${localStorage.getItem('token') ?? ''}`
}

const handleRemove = (file: any) => {
  ruleForm.imgs.forEach((item: any, index: number) => {
    if (item.uid === file.uid) {
      ruleForm.imgs.splice(index, 1)
    }
  })
}

const handlePictureCardPreview = (file: any) => {
  dialogImageUrl.value = file.url
  dialogVisible.value = true
}
// 产品图片 - end

// 编辑器实例 - start
const editorRef1 = shallowRef()
const editorRef2 = shallowRef()
const editorRef3 = shallowRef()

const toolbarConfig = {
  toolbarKeys: ['fontSize', 'bold', 'underline'],
}
const editorConfig1 = { placeholder: '请详细描述材料技术参数(如:屈服强度2400MPa，抗拉强度>540MPa)' }
const editorConfig2 = { placeholder: '请描述材料适用的解决方案(如:适用于高层建筑框架结构，配台混凝土浇筑使用)' }
const editorConfig3 = { placeholder: '请详细描述产品特性、用途、执行标准等' }

onBeforeUnmount(() => {
  const editor1 = editorRef1.value
  if (editor1 == null) return
  editor1.destroy()
  const editor2 = editorRef2.value
  if (editor2 == null) return
  editor2.destroy()
  const editor3 = editorRef3.value
  if (editor3 == null) return
  editor3.destroy()
})

const handleCreated1 = (editor: any) => {
  editorRef1.value = editor
}
const handleCreated2 = (editor: any) => {
  editorRef2.value = editor
}
const handleCreated3 = (editor: any) => {
  editorRef3.value = editor
}
// 编辑器实例 - end


const routeInfo = useRoute()
const product_id: any = routeInfo.query.product_id || ''
const unitlist: any = ref([])

onMounted(() => {
  getPcateOne()
  getSysprovinces()
  // 编辑时，获取产品信息
  if (product_id) {
    materialdetailApi({ product_id }).then((res: any) => {
      if (res) {
        Object.keys(ruleForm).forEach((key) => {
          if (Object.prototype.hasOwnProperty.call(res, key)) {
            if (key === 'imgs' && res[key] && res[key].length > 0) {
              ruleForm[key] = res[key].map((item: any) => {
                return {
                  name: item,
                  url: item,
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
  // 单位列表
  unitApi({
    type: 2
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
          <a @click="pageJump('user-cailist')">
            <i class="fa fa-list mr-1"></i>建材产品列表
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>上传新产品</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-cailist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-upload text-primary"></i>
        上传建材产品信息
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="材料名称" prop="materialname">
              <el-input size="large" v-model="ruleForm.materialname" placeholder="请输入材料名称" />
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
            <el-form-item label="二级分类" prop="sub_cate_id">
              <el-select size="large" v-model="ruleForm.sub_cate_id" placeholder="选择二级分类" clearable style="width: 100%"
                @change="pcateTwoChange">
                <el-option v-for="(item, index) in pcateTwo" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="三级分类" prop="three_cate_id">
              <el-select size="large" v-model="ruleForm.three_cate_id" placeholder="选择三级分类" clearable
                style="width: 100%">
                <el-option v-for="(item, index) in pcateThree" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="应用场景" prop="scene">
              <el-input size="large" v-model="ruleForm.scene" placeholder="请输入应用场景" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="材质" prop="material">
              <el-input size="large" v-model="ruleForm.material" placeholder="请输入材质" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="规格型号" prop="specification">
              <el-input size="large" v-model="ruleForm.specification" placeholder="请输入规格型号" />
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
            <el-form-item label="最低采购数量" prop="lowest">
              <el-input-number size="large" v-model="ruleForm.lowest" placeholder="请输入最低采购数量" :min="0"
                style="width: 100%" />
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
            <el-form-item label="技术参数" prop="technical_params">
              <div style="border: 1px solid #e4e7ed; width: 100%">
                <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef1" :defaultConfig="toolbarConfig"
                  mode="default" />
                <Editor style="height: 300px; overflow-y: hidden" v-model="ruleForm.technical_params"
                  :defaultConfig="editorConfig1" mode="default" @onCreated="handleCreated1" />
              </div>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="解决方案" prop="solution">
              <div style="border: 1px solid #e4e7ed; width: 100%">
                <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef2" :defaultConfig="toolbarConfig"
                  mode="default" />
                <Editor style="height: 300px; overflow-y: hidden" v-model="ruleForm.solution"
                  :defaultConfig="editorConfig2" mode="default" @onCreated="handleCreated2" />
              </div>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="产品描述" prop="description">
              <div style="border: 1px solid #e4e7ed; width: 100%">
                <Toolbar style="border-bottom: 1px solid #e4e7ed" :editor="editorRef3" :defaultConfig="toolbarConfig"
                  mode="default" />
                <Editor style="height: 300px; overflow-y: hidden" v-model="ruleForm.description"
                  :defaultConfig="editorConfig3" mode="default" @onCreated="handleCreated3" />
              </div>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="产品图片" prop="imgs">
              <el-upload :action="uploadURL + '/api/client/upload/upload/image'" :headers="uploadHeader"
                :multiple="true" v-model:file-list="ruleForm.imgs" list-type="picture-card" :auto-upload="true">
                <el-icon>
                  <Plus />
                </el-icon>
                <template #file="{ file }">
                  <div>
                    <img class="el-upload-list__item-thumbnail" :src="file.url" />
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
                <el-image :src="dialogImageUrl" fit="widthFix" style="width: 100%" />
              </el-dialog>
            </el-form-item>
            <!-- <p class="tips">
              <i class="fa fa-info-circle mr-1"></i>支持多张图片上传，点击图片可设置为主要展示图片
            </p> -->
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
