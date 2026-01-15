<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import { requirementsbycateApi, solutionordersApi } from '@/api/modules/datasolution'

// 路由信息
const route = useRoute()

const datasolutionid: any = ref('')
const datasolutionData: any = ref({})

// init 获取基本信息
function getRequirementsbycate() {
  requirementsbycateApi({
    cate_id: datasolutionid.value,
  }).then((res: any) => {
    if (res) {
      datasolutionData.value = res
      datasolutionData.value.multiitems = [
        {
          "jslb": "BIM 4D/5D/6D/7D & 数字孪生",
          "yycj": "进度-成本联动预测、运维可视化、一模多用",
          "bylzwd": "模型深度（LOD）、数据标准、4-7D 应用可行性",
          "zjlbjszc": "BIM 资深专家、注册建筑/结构/造价工程师、正高或副高",
          "selected": false
        },
        {
          "jslb": "倾斜摄影 + LiDAR 实景捕获",
          "yycj": "高精度地形/建筑模型，基坑计量、竣工核查",
          "bylzwd": "精度误差、控制点布设、点云融合",
          "zjlbjszc": "注册测绘师、UAV 摄影测量工程师、高级工程师、持有无人机驾驶执照",
          "selected": false
        },
        {
          "jslb": "机器人与自动化建造",
          "yycj": "进度巡检、自动抹灰、装配式安装",
          "bylzwd": "机械适配、安全性、ROI",
          "zjlbjszc": "机器人研发工程师、施工技术/安全专家、注册安全工程师",
          "selected": false
        },
        {
          "jslb": "AI /机器学习",
          "yycj": "进度预测、风险预警、图纸/合同语义审查",
          "bylzwd": "数据质量、模型可解释性、合规性",
          "zjlbjszc": "数据类专家、计算机视觉工程师、类似资深专家",
          "selected": false
        },
        {
          "jslb": "AR / VR / MR",
          "yycj": "虚拟样板间、沉浸式交底、远程监理培训",
          "bylzwd": "交互体验、硬件选型、BIM-XR 融合",
          "zjlbjszc": "XR 解决方案架构师、高级软件工程师",
          "selected": false
        },
        {
          "jslb": "IoT & 智慧工地",
          "yycj": "实时应力/环境监测、人员定位、报警联动",
          "bylzwd": "传感器选型、网络安全、运行管理",
          "zjlbjszc": "IoT 系统架构师、信息安全工程师、高级工程师",
          "selected": false
        },
        {
          "jslb": "参数化/生成式设计",
          "yycj": "快速方案比选，体量-能耗-成本一体优化",
          "bylzwd": "算法有效性、设计规范符合性",
          "zjlbjszc": "计算设计专家、注册建筑师/结构师、高级工程师",
          "selected": false
        },
        {
          "jslb": "3D 打印 & 数字化加工",
          "yycj": "现场打印构件，PC 构件数字溯源",
          "bylzwd": "材料性能、结构安全、质量检测",
          "zjlbjszc": "材料应用专家、正高或副高",
          "selected": false
        },
        {
          "jslb": "区块链 & 智能合约",
          "yycj": "材料追溯、自动里程碑支付、供应链协同",
          "bylzwd": "合规性、数据共享、安全",
          "zjlbjszc": "区块链开发 Lead、注册造价工程师、高级软件工程师、律师",
          "selected": false
        },
        {
          "jslb": "碳排放 & 能耗数字化",
          "yycj": "动态能耗模拟、ESG 合规评估、碳资产管理",
          "bylzwd": "碳核算边界、数据接口、监管符合性",
          "zjlbjszc": "绿色建筑专家、能源模拟工程师、高级工程师",
          "selected": false
        }
      ]
    }
  })
}

// 提交需求
function tijiaoxuqiu() {
  if (!datasolutionData.value.description) {
    ElMessage({
      type: 'error',
      message: '请填写应用简述',
    })
    return
  }
  if (!datasolutionData.value.company_name) {
    ElMessage({
      type: 'error',
      message: '请填写公司名称',
    })
    return
  }
  if (!datasolutionData.value.contact_person) {
    ElMessage({
      type: 'error',
      message: '请填写公司联系人',
    })
    return
  }
  if (!datasolutionData.value.tel) {
    ElMessage({
      type: 'error',
      message: '请填写联系人电话',
    })
    return
  }
  if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(datasolutionData.value.tel)) {
    ElMessage({
      type: 'error',
      message: '联系人电话格式错误',
    })
    return
  }
  datasolutionData.value.requirements = {}
  const requirements: any = ref({})
  for (let i = 0; i < datasolutionData.value.multiitems.length; i++) {
    const item = datasolutionData.value.multiitems[i]
    if (!item.value) {
      ElMessage({
        type: 'error',
        message: `请选择第${i + 1}条技术需求信息`,
      })
      return
    }
    item.value3 = Array.from(new Set(item.value))
    item.value3.push(`其他(${item.remark || ''})`)
    requirements.value[item.name] = item.value3
  }
  solutionordersApi({
    cate_id: datasolutionData.value.cate_id,
    description: datasolutionData.value.description,
    requirements: requirements.value,
    memo: datasolutionData.value.memo,
    company_name: datasolutionData.value.company_name,
    tel: datasolutionData.value.tel,
    contact_person: datasolutionData.value.contact_person,
    user_id: window.localStorage.getItem('userinfo')
      ? JSON.parse(window.localStorage.getItem('userinfo') || '').id
      : '',
  }).then((res: any) => {
    ElMessage({
      type: 'success',
      message: '需求提交成功',
    })
    datasolutionData.value = {}
  })
}

onMounted(() => {
  datasolutionid.value = route.query.id
  getRequirementsbycate()
})
</script>

<template>
  <div class="requirementsPage">
    <div class="requirementsHead">
      <div class="requHtitle">{{ datasolutionData.cate_name }}</div>
      <div class="requirementsCont">
        <div class="supplierClassFx">
          <div class="supplierClassFxItem2">
            <div class="supplierClassText">
              <span style="color: #f56c6c">*</span>简述
            </div>
            <el-input type="textarea" v-model="datasolutionData.description" :autosize="{ minRows: 3, maxRows: 3 }"
              style="width: 100%" placeholder="请描述应用场景、目标及预期效果等" />
          </div>
        </div>
        <div class="requCstitle">技术需求（可多选）</div>
        <el-table :data="datasolutionData.multiitems" style="width: 100%" border>
          <el-table-column type="selection" width="50" align="center" />
          <el-table-column prop="jslb" label="技术类别" min-width="200" />
          <el-table-column prop="yycj" label="应用场景" min-width="200" />
          <el-table-column prop="bylzwd" label="必要论证维度" min-width="200" />
          <el-table-column prop="zjlbjszc" label="专家类别/技术职称" min-width="200" />
        </el-table>
        <div class="supplierClassFx2">
          <div class="supplierClassFxItem">
            <div class="supplierClassText"><span style="color: #f56c6c">*</span>公司名称</div>
            <el-input v-model="datasolutionData.company_name" style="width: 100%; height: 40px" placeholder="请填写公司名称" />
          </div>
          <div class="supplierClassFxItem">
            <div class="supplierClassText"><span style="color: #f56c6c">*</span>公司联系人</div>
            <el-input v-model="datasolutionData.contact_person" style="width: 100%; height: 40px"
              placeholder="请填写公司联系人" />
          </div>
          <div class="supplierClassFxItem">
            <div class="supplierClassText"><span style="color: #f56c6c">*</span>联系人电话</div>
            <el-input v-model="datasolutionData.tel" style="width: 100%; height: 40px" placeholder="请填写联系人电话" />
          </div>
        </div>
        <div class="supplierClassFx2">
          <div class="supplierClassFxItem2">
            <div class="supplierClassText">其他要求</div>
            <el-input type="textarea" v-model="datasolutionData.memo" :autosize="{ minRows: 3, maxRows: 3 }"
              style="width: 100%" placeholder="请填写其他特殊需求或补充说明" />
          </div>
        </div>
        <button class="btmTjxq" @click="tijiaoxuqiu">提交需求</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.requirementsPage {
  min-height: calc(100vh - 120px);
  background-color: #f9fafb;
  overflow-x: hidden;

  .requirementsHead {
    padding: 6rem 2rem 2rem;
    margin: 0 auto;
    position: relative;
    width: 100%;
    max-width: 1536px;

    @media (max-width: 768px) {
      padding: 5rem 1rem 1rem;
    }

    .requHtitle {
      margin-bottom: 1rem;
      font-size: 1.875rem;
      line-height: 2.25rem;
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .requHsub {
      text-align: center;
      color: rgb(75 85 99);
      max-width: 48rem;
      margin-left: auto;
      margin-right: auto;
    }
  }

  .requirementsCont {
    margin-top: 2rem;
    padding: 2.5rem;
    background-color: rgb(255 255 255);
    box-shadow:
      0 10px 15px -3px rgb(0 0 0 / 0.1),
      0 4px 6px -4px rgb(0 0 0 / 0.1);
    border-radius: 1rem;

    @media (max-width: 768px) {
      padding: 2rem 0.5rem;
    }

    .requCtitle {
      text-align: center;
      color: rgb(1 32 96);
      font-weight: 700;
      font-size: 1.5rem;
      line-height: 2rem;
      margin-bottom: 1rem;

      @media (max-width: 768px) {
        font-size: 1.25rem;
      }
    }

    .supplierClassFx {
      height: 100%;
      margin-bottom: 1rem;
      padding-bottom: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      border-bottom: 1px solid rgb(229 231 235);
    }

    .supplierClassFx2 {
      height: 100%;
      padding-top: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      border-top: 1px solid rgb(229 231 235);
    }

    .supplierClassFxItem {
      flex-shrink: 0;
      margin-bottom: 1rem;
      width: calc(50% - 0.25rem);

      @media (max-width: 768px) {
        width: 100%;
      }
    }

    .supplierClassFxItem2 {
      flex-shrink: 0;
      margin-bottom: 1rem;
      width: 100%;
    }

    .supplierClassText {
      margin-bottom: 0.5rem;
      font-weight: 500;
      font-size: 0.875rem;
      line-height: 1.25rem;
      color: rgb(55 65 81);
    }

    .requCstitle {
      color: rgb(1 32 96);
      font-weight: 600;
      font-size: 1.125rem;
      line-height: 1.75rem;
      margin: 2rem 0 1rem;
    }

    .requCstimu {
      margin-bottom: 0.5rem;
      font-weight: 500;
      color: rgb(55 65 81);
    }

    .requCstibox {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      margin-bottom: 1.25rem;
      padding: 0.75rem;
      border-radius: 0.5rem;

      .requCstiItems {
        margin-bottom: 0.5rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;

        .requCstiItem {
          margin-right: 1rem;

          @media (max-width: 768px) {
            margin-right: 0.5rem;
          }

          input {
            width: 1.25rem;
            height: 1.25rem;

            @media (max-width: 768px) {
              width: 1rem;
              height: 1rem;
            }
          }

          span {
            color: rgb(55 65 81);
            margin-left: 0.5rem;
          }
        }
      }

      .requCstiElInput {
        margin-bottom: 0.5rem;
        width: 14rem;
        height: 34px;
      }
    }

    .btmTjxq {
      display: block;
      margin: 2rem auto 0;
      padding: 0.75rem 2rem;
      color: #fff;
      background-color: rgb(22 93 255);
      border-radius: 9999px;
      box-shadow:
        0 10px 15px -3px rgb(0 0 0 / 0.1),
        0 4px 6px -4px rgb(0 0 0 / 0.1);
    }

    .btmTjxq:hover {
      transform: scale(1.05);
    }
  }
}
</style>

<style lang="scss">
.requirementsPage {
  .el-input__wrapper {
    border-radius: 0.5rem;
  }

  .el-input.is-disabled .el-input__inner {
    -webkit-text-fill-color: rgb(1 32 96) !important;
  }

  .btn-prev {
    color: rgb(107 114 128) !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    line-height: 1.25rem !important;
    padding: 0.5rem 0.75rem !important;
    background-color: #fff !important;
    border: 1px solid rgb(209 213 219) !important;
    border-radius: 0.25rem !important;
  }

  .btn-next {
    color: rgb(107 114 128) !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    line-height: 1.25rem !important;
    padding: 0.5rem 0.75rem !important;
    background-color: #fff !important;
    border: 1px solid rgb(209 213 219) !important;
    border-radius: 0.25rem !important;
  }
}

.supplierClass {
  .el-select__wrapper {
    border-radius: 0.5rem;
  }

  .el-select__selected-item {
    color: rgb(1 32 96);
  }

  .el-select__icon {
    color: rgb(1 32 96);
  }
}

.supplierProducts {
  .el-select__wrapper {
    background-color: #e9e9ed;
    border-radius: 0.5rem;
  }

  .el-select__selected-item {
    color: rgb(1 32 96);
  }

  .el-select__icon {
    color: rgb(1 32 96);
  }
}
</style>
