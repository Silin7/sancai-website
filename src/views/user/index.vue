<script setup lang="ts">
import { onMounted, ref } from 'vue'
import dayjs from 'dayjs'
import 'dayjs/locale/zh-cn'
import pageJump from '@/hooks/pageJump'
import { currentuserApi } from '@/api/modules/login'
import { homestatisticApi } from '@/api/modules/admin'
import {
  secpositionsApi,
  seccontentlistApi
} from '@/api/modules/basic'

// 用户信息
const userType: any = ref(1)
const userRole: any = ref(1)

function getUserType() {
  currentuserApi().then((res: any) => {
    if (res) {
      // user_type  1-供方/2-需方
      userType.value = res.user_type
      // role  0-主管理员/1-普通管理员
      userRole.value = res.role
    }
  })
}

// 用户中心 - 首页
const homeStatistic: any = ref({})
function getHomestatistic() {
  homestatisticApi().then((res: any) => {
    if (res) {
      homeStatistic.value = res.data
    }
  })
}

// 获取用户须知
const ucenterData: any = ref({})
function getSecpositions() {
  secpositionsApi().then((res: any) => {
    if (res && res.length > 0) {
      for (let i = 0; i < res.length; i++) {
        const item = res[i]
        // 首页-人材机信价格库	home-rcjx
        if (item.url === 'ucenter') {
          seccontentlistApi(item.id).then((res: any) => {
            ucenterData.value = res
            // res.forEach((element: any) => {
            //   if (element.title === '用户须知') {
            //     ucenterData.value = element
            //   }
            // })
          })
        }
      }
    }
  })
}

onMounted(() => {
  getUserType()
  getHomestatistic()
  getSecpositions()
})
</script>

<template>
  <div class="page-main">
    <div class="welcome-section">
      <h1 class="welcome-title">欢迎回来，{{ homeStatistic.user_name || '用户' }}
        <!-- <span style="margin-left: 1rem; color: #1f69ff; cursor: pointer;" @click="pageJump('user-upgradevip')">
          升级VIP
        </span> -->
      </h1>
      <p class="welcome-message">
        今天是<span>{{ dayjs().format('YYYY年MM月DD日') }}{{ dayjs().locale('zh-cn').format('dddd') }}</span>，以下是您的平台数据概览
      </p>
    </div>
    <el-row v-if="homeStatistic.product_statistics && userRole === 0 && userType === 1" :gutter="24">
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #e8f3ff; color: #377dff">
            <i class="fa fa-dropbox"></i>
          </div>
          <div class="stat-value">{{ homeStatistic.product_statistics[0].count }}</div>
          <div class="stat-label">{{ homeStatistic.product_statistics[0].product_type_name }}</div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #e6f7ed; color: #52c41a">
            <i class="fa fa-wrench"></i>
          </div>
          <div class="stat-value">{{ homeStatistic.product_statistics[1].count }}</div>
          <div class="stat-label">{{ homeStatistic.product_statistics[1].product_type_name }}</div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #fff2e8; color: #fa8c16">
            <i class="fa fa-info-circle"></i>
          </div>
          <div class="stat-value">{{ homeStatistic.product_statistics[2].count }}</div>
          <div class="stat-label">{{ homeStatistic.product_statistics[2].product_type_name }}</div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #f6e9ff; color: #722ed1">
            <i class="fa fa-file-powerpoint-o"></i>
          </div>
          <div class="stat-value">{{ homeStatistic.product_statistics[3].count }}</div>
          <div class="stat-label">{{ homeStatistic.product_statistics[3].product_type_name }}</div>
        </div>
      </el-col>
    </el-row>
    <h2 v-if="userRole === 0 && userType === 1" class="section-title">
      <i class="fa fa-rocket"></i>
      快捷操作
    </h2>
    <el-row v-if="userRole === 0 && userType === 1" :gutter="24">
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-caifrom')">
          <div class="action-icon">
            <i class="fa fa-dropbox"></i>
          </div>
          <div class="action-text">新增建材产品</div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-machinefrom')">
          <div class="action-icon">
            <i class="fa fa-wrench"></i>
          </div>
          <div class="action-text">新增机械产品</div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-itfrom')">
          <div class="action-icon">
            <i class="fa fa-info-circle"></i>
          </div>
          <div class="action-text">新增信息化产品</div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-inquirylist')">
          <div class="action-icon">
            <i class="fa fa-file-powerpoint-o"></i>
          </div>
          <div class="action-text">处理报价单</div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-cailist')">
          <div class="action-icon">
            <i class="fa fa-list"></i>
          </div>
          <div class="action-text">管理建材产品</div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-machinelist')">
          <div class="action-icon">
            <i class="fa fa-list"></i>
          </div>
          <div class="action-text">管理机械产品</div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="8" :lg="4" :xl="3">
        <div class="action-card" @click="pageJump('user-itlist')">
          <div class="action-icon">
            <i class="fa fa-list"></i>
          </div>
          <div class="action-text">管理信息化产品</div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="24" style="margin-top: 20px">
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <h2 class="section-title">
          <i class="fa fa-history"></i>
          最新动态
        </h2>
        <div class="recent-activity">
          <ul class="activity-list">
            <li v-for="(item, index) in homeStatistic.newest_articles" :key="index" class="activity-item" @click="pageJump('news_detail', {
              articlesid: item.id,
            })">
              <div class="activity-icon" style="background-color: #fff2e8; color: #fa8c16">
                <i class="fa fa-newspaper-o"></i>
              </div>
              <div class="activity-content">
                <div class="activity-title">{{ item.title }}</div>
                <div class="activity-time">{{ item.created_at }}</div>
              </div>
            </li>
          </ul>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <h2 class="section-title">
          <i class="fa fa-history"></i>
          用户须知
        </h2>
        <div class="recent-activity">
          <div v-for="(item, index) in ucenterData" :key="index">
            <div v-html="item.content" style="margin-top: 20px; line-height: 1.5;"></div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<style lang="scss" scoped>
.welcome-section {
  margin-bottom: 32px;

  .welcome-title {
    font-size: 24px;
    font-weight: 600;
    color: #303133;
    margin-bottom: 8px;
  }

  .welcome-message {
    color: #606266;
    font-size: 14px;
  }
}

.stat-card {
  margin-bottom: 24px;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);

  .stat-icon {
    width: 48px;
    height: 48px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
  }

  .stat-value {
    font-size: 28px;
    line-height: 42px;
    font-weight: 600;
    color: #303133;
  }

  .stat-label {
    font-size: 14px;
    line-height: 21px;
    color: #606266;
  }
}

.stat-card:hover {
  cursor: pointer;
  animation: jumpUpwards 300ms ease-in-out forwards;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
  margin-top: 10px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;

  i {
    margin-right: 8px;
    color: #377dff;
  }
}

.action-card {
  margin-bottom: 12px;
  padding: 20px 16px;
  text-align: center;
  color: #303133;
  background-color: #ffffff;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  border-radius: 8px;

  .action-icon {
    font-size: 28px;
    line-height: 42px;
    color: #377dff;
    margin-bottom: 12px;
  }

  .action-text {
    font-size: 14px;
    line-height: 21px;
    font-weight: 500;
  }
}

.action-card:hover {
  cursor: pointer;
  animation: jumpUpwards 300ms ease-in-out forwards;
  box-shadow: 0 4px 16px rgba(55, 125, 255, 0.15);
}

.recent-activity {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 32px;

  .activity-list {
    list-style: none;

    .activity-item {
      display: flex;
      padding: 12px 0;
      border-bottom: 1px solid #f0f2f5;

      .activity-icon {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 12px;
        flex-shrink: 0;
      }

      .activity-content {
        flex: 1;
        cursor: pointer;

        .activity-title {
          font-size: 14px;
          font-weight: 500;
          color: #303133;
          margin-bottom: 2px;
        }

        .activity-time {
          font-size: 12px;
          color: #909399;
        }
      }
    }
  }
}
</style>
