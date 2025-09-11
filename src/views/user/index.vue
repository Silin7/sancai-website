<script setup lang="ts">
import { onMounted, ref } from 'vue'
import dayjs from 'dayjs'
import 'dayjs/locale/zh-cn'
import pageJump from '@/hooks/pageJump'

const data1: any = ref({
  jcnum: 23,
  jxnum: 18,
  itnum: 12,
  bjnum: 5,
})

const data2: any = ref([
  { state: 'add', title: '新增建材产品「高强度钢筋」', date: '今天 14:30' },
  { state: 'edit', title: '编辑信息化产品「智慧工地管理系统」', date: '昨天 09:15' },
  { state: 'del', title: '下架机械产品「混凝土搅拌机」', date: '2025-07-05 16:45' },
  { state: 'scuss', title: '处理报价单 #20250704001', date: '2025-07-04 11:20' },
])
</script>

<template>
  <div class="page-main">
    <div class="welcome-section">
      <h1 class="welcome-title">欢迎回来，用户名</h1>
      <p class="welcome-message">
        今天是<span>{{ dayjs().format('YYYY年MM月DD日') }}{{ dayjs().locale('zh-cn').format('dddd') }}</span>，以下是您的平台数据概览
      </p>
    </div>
    <el-row :gutter="24">
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #e8f3ff; color: #377dff">
            <i class="fa fa-dropbox"></i>
          </div>
          <div class="stat-value">{{ data1.jcnum }}</div>
          <div class="stat-label">已发布建材产品</div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #e6f7ed; color: #52c41a">
            <i class="fa fa-wrench"></i>
          </div>
          <div class="stat-value">{{ data1.jxnum }}</div>
          <div class="stat-label">已发布机械产品</div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #fff2e8; color: #fa8c16">
            <i class="fa fa-info-circle"></i>
          </div>
          <div class="stat-value">{{ data1.itnum }}</div>
          <div class="stat-label">已发布信息化产品</div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="6">
        <div class="stat-card">
          <div class="stat-icon" style="background-color: #f6e9ff; color: #722ed1">
            <i class="fa fa-file-powerpoint-o"></i>
          </div>
          <div class="stat-value">{{ data1.bjnum }}</div>
          <div class="stat-label">待处理报价单</div>
        </div>
      </el-col>
    </el-row>
    <h2 class="section-title">
      <i class="fa fa-rocket"></i>
      快捷操作
    </h2>
    <el-row :gutter="12">
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
    <h2 class="section-title" style="margin-top: 20px">
      <i class="fa fa-history"></i>
      最近活动
    </h2>
    <div class="recent-activity">
      <ul class="activity-list">
        <li v-for="(item, index) in data2" :key="index" class="activity-item">
          <div v-if="item.state === 'add'" class="activity-icon" style="background-color: #e8f3ff; color: #377dff">
            <i class="fa fa-plus"></i>
          </div>
          <div v-if="item.state === 'edit'" class="activity-icon" style="background-color: #fff2e8; color: #fa8c16">
            <i class="fa fa-edit"></i>
          </div>
          <div v-if="item.state === 'del'" class="activity-icon" style="background-color: #fef0f0; color: #f5222d">
            <i class="fa fa-ban"></i>
          </div>
          <div v-if="item.state === 'scuss'" class="activity-icon" style="background-color: #e6f7ed; color: #52c41a">
            <i class="fa fa-check"></i>
          </div>
          <div class="activity-content">
            <div class="activity-title">{{ item.title }}</div>
            <div class="activity-time">{{ item.date }}</div>
          </div>
        </li>
      </ul>
    </div>
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
