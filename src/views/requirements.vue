<script setup lang="ts">
import { ref } from 'vue'

const selectvalue1: any = ref('标的名称')
const selectvalue2: any = ref('CIM+人房管理')
const selectvalue3: any = ref('')

const checkvalue1: any = ref(true)
const checkvalue2: any = ref(false)
const checkvalue3: any = ref(false)
const checkvalue4: any = ref(false)
</script>

<template>
  <div class="requirementsPage">
    <div class="requirementsHead">
      <div class="requHtitle">CIM+人房管理</div>
      <div class="requHsub">
        基于BIM模型实现工程全生命周期计算与动态信息管控，聚焦CIM+人房管理场景，助力城市空间与人口数据精细化治理，为智慧化管理提供精准支撑。
      </div>
      <div class="requirementsCont">
        <div class="requCtitle">信息化产品服务需求表(由需方填写)</div>
        <div class="supplierClassFx">
          <div class="supplierClassFxItem">
            <div class="supplierClassText">类别</div>
            <el-input v-model="selectvalue1" style="width: 100%; height: 50px; font-size: 1rem" placeholder=" "
              disabled />
          </div>
          <div class="supplierClassFxItem">
            <div class="supplierClassText">产品/服务</div>
            <el-input v-model="selectvalue2" style="width: 100%; height: 50px; font-size: 1rem" placeholder=" "
              disabled />
          </div>
        </div>
        <div class="supplierClassFx" style="margin-top: 2rem">
          <div class="supplierClassFxItem2">
            <div class="supplierClassText">应用简述（可另附页）</div>
            <el-input type="textarea" v-model="selectvalue3" :autosize="{ minRows: 3, maxRows: 3 }"
              style="width: 100%; font-size: 1rem" placeholder="请描述CIM+人房管理系统的应用场景、目标及预期效果等" />
          </div>
        </div>
        <div class="requCstitle">技术需求（可多选）</div>
        <div v-for="index in 10" :key="index">
          <div class="requCstimu">{{ index + 1 }}. 实时数据采集</div>
          <div class="requCstibox">
            <div class="requCstiItems">
              <div class="requCstiItem frcc">
                <input type="checkbox" v-model="checkvalue1" />
                <span>监控</span>
              </div>
              <div class="requCstiItem frcc">
                <input type="checkbox" v-model="checkvalue2" />
                <span>门禁</span>
              </div>
              <div class="requCstiItem frcc">
                <input type="checkbox" v-model="checkvalue3" />
                <span>道闸杆</span>
              </div>
              <div class="requCstiItem frcc">
                <input type="checkbox" v-model="checkvalue4" />
                <span>其他</span>
              </div>
            </div>
            <el-input v-model="selectvalue3" class="requCstiElInput" placeholder="请注明" />
          </div>
        </div>
        <div class="supplierClassFx2">
          <div class="supplierClassFxItem2">
            <div class="supplierClassText">其他要求</div>
            <el-input type="textarea" v-model="selectvalue3" :autosize="{ minRows: 3, maxRows: 3 }"
              style="width: 100%; font-size: 1rem" placeholder="请填写其他特殊需求或补充说明" />
          </div>
        </div>
        <button class="btmTjxq">提交需求</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.requirementsPage {
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
    box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
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
      justify-content: space-between;
      border-bottom: 1px solid rgb(229 231 235);
    }

    .supplierClassFx2 {
      height: 100%;
      margin-bottom: 1rem;
      padding-top: 1.5rem;
      display: flex;
      justify-content: space-between;
      border-top: 1px solid rgb(229 231 235);
    }

    .supplierClassFxItem {
      width: calc(50% - 0.25rem);
    }

    .supplierClassFxItem2 {
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
        font-size: 1rem;
      }
    }

    .btmTjxq {
      display: block;
      margin: 2rem auto 0;
      padding: 0.75rem 2rem;
      color: #fff;
      background-color: rgb(22 93 255);
      border-radius: 9999px;
      box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
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
