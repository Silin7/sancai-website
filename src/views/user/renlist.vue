<script setup lang="ts"></script>

<template>
  <div class="renlist-page">
    <div class="form-card">
      <h2 class="list-title">
        <i class="fa fa-users"></i>
        方案类服务
      </h2>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.renlist-page {
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

/* 列表标题 */
.list-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #303133;
  display: flex;
  align-items: center;
}

.list-title i {
  margin-right: 10px;
  color: #377dff;
}
</style>
