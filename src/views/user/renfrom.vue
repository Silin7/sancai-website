<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref, shallowRef, onBeforeUnmount, watch } from 'vue'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import pageJump from '@/hooks/pageJump'
import { productpcatechildrenApi } from '@/api/modules/product'
import { sysprovincesApi, syscitiesApi } from '@/api/modules/basic'
import { humanresourceaddApi } from '@/api/modules/admin'
import { unitApi } from '@/api/modules/common'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  servicename: '',
  brand: '',
  cate_id: '',
  sub_cate_id: '',
  scene: '',
  technical_params: '',
  pretaxprice: null,
  afertaxprice: null,
  taxrate: null,
  unit_id: 1, // 默认1，暂时未用
  province_id: '',
  city_id: '',
  solution: '',
  description: '',
  imgs: ['https://www.silin7.cn/fucheng-files/systemModule/logo.png'],
})
const rules: any = reactive({
  servicename: [{ required: true, message: '请输入服务名称', trigger: 'blur' }],
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
  description: [{ required: true, message: '请输入服务内容介绍', trigger: 'blur' }],
})

const submitForm = async (formEl: any) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      humanresourceaddApi(ruleForm).then((res: any) => {
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

// 一级分类
const pcateOne: any = ref([])
const pcateTwo: any = ref([])

function getPcateOne(pid: any = 0) {
  productpcatechildrenApi({
    page: 1,
    pageSize: 999,
    parent_id: pid,
  }).then((res: any) => {
    if (res && res.items.length > 0) {
      const levelone = res.items.filter((element: any) => element.item_id === 0)
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
const editorRef1 = shallowRef()
const editorRef2 = shallowRef()

const toolbarConfig = {
  toolbarKeys: ['fontSize', 'bold', 'underline'],
}
const editorConfig1 = { placeholder: '请详细描述解决方案' }
const editorConfig2 = { placeholder: '请详细描述服务内容、流程、交付物等' }

// 组件销毁时，也及时销毁编辑器
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

onMounted(() => {
  getPcateOne()
  getSysprovinces()
  // unitApi().then((res: any) => {
  //   if (res) {
  //     console.log('单位列表-------->', res)
  //   }
  // })
})
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-renlist')"> <i class="fa fa-list mr-1"></i>产品列表 </a>
          <span class="breadcrumb-separator">/</span>
          <span>发布新服务</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-renlist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-users"></i>
        解决方案类服务产品
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="服务名称" prop="servicename">
              <el-input size="large" v-model="ruleForm.servicename" placeholder="请输入服务名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="品牌" prop="brand">
              <el-input size="large" v-model="ruleForm.brand" placeholder="请输入品牌" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="主类别" prop="cate_id">
              <el-select size="large" v-model="ruleForm.cate_id" placeholder="选择主类别" clearable style="width: 100%"
                @change="pcateOneChange">
                <el-option v-for="(item, index) in pcateOne" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="子类别" prop="sub_cate_id">
              <el-select size="large" v-model="ruleForm.sub_cate_id" placeholder="选择子类别" clearable style="width: 100%">
                <el-option v-for="(item, index) in pcateTwo" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="应用场景" prop="scene">
              <el-input size="large" v-model="ruleForm.scene" placeholder="请输入应用场景" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="技术参数" prop="technical_params">
              <el-input size="large" v-model="ruleForm.technical_params" placeholder="请输入技术参数" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="税前价格(元)" prop="pretaxprice">
              <el-input-number size="large" v-model="ruleForm.pretaxprice" placeholder="请输入税前价格(元)" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="税后价格(元)" prop="afertaxprice">
              <el-input-number size="large" v-model="ruleForm.afertaxprice" placeholder="请输入税后价格(元)" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="税率(%)" prop="taxrate">
              <el-input-number size="large" v-model="ruleForm.taxrate" placeholder="请输入税率(%)" :min="0"
                style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="单位" prop="unit_id">
              <el-select size="large" v-model="ruleForm.unit_id" placeholder="选择单位">
                <el-option label="件" :value="1" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="省份" prop="province_id">
              <el-select size="large" v-model="ruleForm.province_id" placeholder="选择省份" @change="provinceChange">
                <el-option v-for="(item, index) in provincesList" :key="index" :label="item.name" :value="item.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
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
            <el-form-item label="服务内容介绍" prop="description">
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
          <i class="fa fa-check-circle"></i>提交服务产品
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
