<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css'
import { onMounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import { itproductaddApi, itproducteditApi, solutionordersdetailApi } from '@/api/modules/admin'

const ruleFormRef: any = ref()
const ruleForm: any = reactive({
  code: '',
  product_name: '',
  cate_name: '',
  requirements: [],
  company_name: '',
  contact_person: '',
  tel: '',
  description: '',
  memo: '',
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
      if (order_id === '') {
        itproductaddApi(data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-inquirylist')
          }
        })
      } else {
        itproducteditApi(data).then((res: any) => {
          if (res) {
            ElMessage({
              type: 'success',
              message: '保存成功',
            })
            pageJump('user-inquirylist')
          }
        })
      }
    } else {
      console.log('error submit!', fields)
    }
  })
}


const routeInfo = useRoute()
const order_id: any = routeInfo.query.order_id || ''

onMounted(() => {
  // 编辑时，获取产品信息
  if (order_id) {
    solutionordersdetailApi(order_id).then((res: any) => {
      if (res) {
        Object.keys(ruleForm).forEach((key) => {
          if (Object.prototype.hasOwnProperty.call(res.data, key)) {
            ruleForm[key] = res.data[key]
          }
          // if (key === 'requirements' && ruleForm.requirements) {
          //   ruleForm['requirementskey'] = []
          //   for (let key in ruleForm.requirements) {
          //     ruleForm['requirementskey'].push(key)
          //   }
          // }
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
          <a @click="pageJump('user-inquirylist')">
            <i class="fa fa-list mr-1"></i>报价单列表
          </a>
          <span class="breadcrumb-separator">/</span>
          <span>查看报价单</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-inquirylist')">
            <i class="fa fa-arrow-left mr-1"></i>返回列表
          </button>
          <!-- <button class="action-btn draft-btn"><i class="fa fa-save mr-1"></i>保存草稿</button> -->
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-upload text-primary"></i>
        查看报价单信息
      </h2>
      <el-form label-position="top" ref="ruleFormRef" :model="ruleForm" label-width="auto">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="订单编号" prop="code">
              <el-input size="large" disabled v-model="ruleForm.code" placeholder="请输入订单编号" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="需求项目名" prop="product_name">
              <el-input size="large" disabled v-model="ruleForm.product_name" placeholder="请输入需求项目名" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="所属分类" prop="cate_name">
              <el-input size="large" disabled v-model="ruleForm.cate_name" placeholder="请输入所属分类" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="公司名称" prop="company_name">
              <el-input size="large" disabled v-model="ruleForm.company_name" placeholder="请输入公司名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="联系人" prop="contact_person">
              <el-input size="large" disabled v-model="ruleForm.contact_person" placeholder="请输入联系人" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="联系方式" prop="tel">
              <el-input size="large" disabled v-model="ruleForm.tel" placeholder="请输入联系方式" />
            </el-form-item>
          </el-col>
          <!-- <el-checkbox v-model="ruleForm.requirements" disabled>{{ item2 }}</el-checkbox> -->
          <el-col :span="24">
            <el-form-item label="需求详情" prop="cate_name">
              <div v-for="(item, index) in ruleForm.requirements" :key="index" style="width: 100%;">
                <div>
                  <span>{{ index }}：</span>
                  <span v-for="(item2, index2) in item" :key="index2" class="disabledstyle">
                    <i class="fa fa-check-square"></i>
                    {{ item2 }}
                  </span>
                </div>
              </div>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="需求描述" prop="description">
              <el-input type="textarea" disabled v-model="ruleForm.description" :autosize="{ minRows: 3, maxRows: 3 }"
                style="width: 100%;" placeholder="请输入需求描述" />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="备注信息" prop="memo">
              <el-input type="textarea" disabled v-model="ruleForm.memo" :autosize="{ minRows: 3, maxRows: 3 }"
                style="width: 100%;" placeholder="请输入备注信息" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <!-- <div class="form-footer">
        <button type="submit" class="submit-btn" @click="submitForm(ruleFormRef)">
          <i class="fa fa-check-circle"></i>提交服务产品
        </button>
      </div> -->
    </div>
  </div>
</template>

<style lang="scss" scoped>
.disabledstyle {
  margin-left: 10px;
  color: #a8abb2;
}
</style>
