<script setup lang="ts"></script>

<template>
  <div class="user-profile-page">
    <div class="form-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a> <i class="fa fa-home mr-1"></i>首页 </a>
          <span class="breadcrumb-separator">/</span>
          <span>用户资料</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn"><i class="fa fa-arrow-left mr-1"></i>返回首页</button>
          <button class="action-btn save-btn"><i class="fa fa-save mr-1"></i>保存资料</button>
        </div>
      </div>
      <h2 class="form-title">
        <i class="fa fa-key text-primary"></i>
        修改登录密码
      </h2>

      <div class="form-footer">
        <button type="submit" class="submit-btn"><i class="fa fa-save"></i>确认修改</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.user-profile-page {
  padding: 24px;
  border: 1px solid red;
}
</style>

<style scoped>
.form-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  padding: 24px;
  margin-bottom: 40px;
}

.form-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #e6e9ed;
}

.breadcrumb {
  display: flex;
  align-items: center;
  font-size: 14px;
  color: #606266;
}

.breadcrumb i {
  font-size: 1rem;
}

.breadcrumb a {
  color: #377dff;
  text-decoration: none;
  transition: color 0.2s ease;
  display: flex;
  align-items: center;
}

.breadcrumb a:hover {
  color: #2b68d8;
}

.breadcrumb-separator {
  margin: 0 8px;
  color: #909399;
}

.action-buttons {
  display: flex;
  gap: 12px;
}

.action-btn {
  height: 40px;
  display: flex;
  align-items: center;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-btn {
  background-color: #f5f7fa;
  color: #606266;
  border: 1px solid #dcdfe6;
}

.back-btn:hover {
  background-color: #ebeef5;
}

.save-btn {
  background-color: #377dff;
  color: white;
  border: 1px solid #377dff;
}

.save-btn:hover {
  background-color: #2b68d8;
  border-color: #2b68d8;
}

.form-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #303133;
  display: flex;
  align-items: center;
  gap: 10px;
}

/* 表单提交按钮 */
.form-footer {
  margin-top: 32px;
  display: flex;
  justify-content: center;
}

.submit-btn {
  padding: 12px 48px;
  background-color: #377dff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.submit-btn:hover {
  background-color: #2b68d8;
}
</style>
