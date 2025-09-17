<script setup lang="ts">
import { ref } from 'vue';
import pageJump from '@/hooks/pageJump'

// 支付方式状态管理
const selectedMethod = ref('wechat');

// 处理支付逻辑
const handlePayment = () => {
  alert(`您选择了${selectedMethod.value === 'wechat' ? '微信支付' : '支付宝支付'}，金额为99元/年`);
  // 实际项目中这里会跳转到对应的支付页面或调用支付接口
};
</script>

<template>
  <div class="page-main">
    <div class="page-card">
      <!-- 顶部导航栏 -->
      <div class="form-nav">
        <div class="breadcrumb">
          <a @click="pageJump('user-index')"> <i class="fa fa-home mr-1"></i>首页 </a>
          <span class="breadcrumb-separator">/</span>
          <span>用户升级VIP</span>
        </div>
        <div class="action-buttons">
          <button class="action-btn back-btn" @click="pageJump('user-index')">
            <i class="fa fa-arrow-left mr-1"></i>返回首页
          </button>
        </div>
      </div>
      <!-- 列表标题 -->
      <h2 class="list-title">
        <i class="fa fa-trophy"></i>
        用户升级VIP会员
      </h2>
      <!-- 会员权益表格 -->
      <table class="rights-table">
        <thead>
          <tr>
            <th>会员权限</th>
            <th>普通会员</th>
            <th>VIP会员</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>查看材料/设备基础信息</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 支持</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 支持</td>
          </tr>
          <tr>
            <td>下载材料报价单</td>
            <td><span class="cross-mark"><i class="fa fa-close"></i></span> 限制（每月3次）</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 无限次下载</td>
          </tr>
          <tr>
            <td>优先匹配供应商需求</td>
            <td><span class="cross-mark"><i class="fa fa-close"></i></span> 不支持</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 支持</td>
          </tr>
          <tr>
            <td>智能建造装备推荐</td>
            <td><span class="cross-mark"><i class="fa fa-close"></i></span> 基础推荐</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 精准推荐</td>
          </tr>
          <tr>
            <td>专属客服咨询服务</td>
            <td><span class="cross-mark"><i class="fa fa-close"></i></span> 不支持</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 1对1专属客服</td>
          </tr>
          <tr>
            <td>信息化产品折扣优惠</td>
            <td><span class="cross-mark"><i class="fa fa-close"></i></span> 不支持</td>
            <td><span class="check-mark"><i class="fa fa-check"></i></span> 享9折优惠</td>
          </tr>
        </tbody>
      </table>

      <!-- 会员费用部分 -->
      <div class="fee-section">
        <h3>VIP会员升级费用</h3>
        <div class="fee-amount">¥ <span class="price">99</span> /年</div>
        <p class="fee-desc">一次性支付，全年有效，到期前7天提醒续费</p>
      </div>

      <!-- 支付方式部分 -->
      <div class="payment-section">
        <h3>选择支付方式</h3>
        <div class="payment-methods">
          <button class="payment-btn" :class="{ selected: selectedMethod === 'wechat' }"
            @click="selectedMethod = 'wechat'">
            <img src="@/assets/user/weixin.png" alt="" style="width: 18px; height: 18px;"> 微信支付
          </button>
          <button class="payment-btn" :class="{ selected: selectedMethod === 'alipay' }"
            @click="selectedMethod = 'alipay'">
            <img src="@/assets/user/alipay.png" alt="" style="width: 18px; height: 18px;"> 支付宝支付 </button>
        </div>
        <button class="confirm-btn" @click="handlePayment"><i class="fa fa-credit-card mr-2"></i>确认支付并升级</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.app-container {
  // width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
  padding-bottom: 10px;
  border-bottom: 2px solid #f0f0f0;
}

/* 会员权益表格样式 */
.rights-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 30px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  color: #303133;
}

.rights-table th,
.rights-table td {
  border: 1px solid #e5e7eb;
  padding: 12px 15px;
  text-align: left;
}

.rights-table th {
  background-color: #f9fafb;
  font-weight: 600;
  color: #4b5563;
}

.rights-table tr:nth-child(even) {
  background-color: #f9fafb;
}

.check-mark {
  color: #10b981;
  margin-right: 8px;
  font-weight: bold;
}

.cross-mark {
  color: #909399;
  margin-right: 8px;
  font-weight: bold;
}

/* 会员费用部分样式 */
.fee-section {
  text-align: center;
  margin-bottom: 30px;
  padding: 25px;
  background-color: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.fee-section h3 {
  margin-bottom: 15px;
  color: #909399;
  font-size: 14px;
}

.fee-amount {
  font-size: 14px;
  font-weight: bold;
  margin: 10px 0;
  color: #1e293b;
}

.price {
  font-size: 32px;
  color: #377dff;
}

.fee-desc {
  font-size: 14px;
  color: #909399;
  margin: 0;
}

/* 支付方式部分样式 */
.payment-section {
  text-align: center;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.payment-section h3 {
  margin-bottom: 20px;
  color: #334155;
  font-size: 18px;
}

.payment-methods {
  display: flex;
  justify-content: center;
  gap: 25px;
  margin-bottom: 25px;
}

.payment-btn {
  padding: 12px 25px;
  border: 2px solid #e2e8f0;
  border-radius: 6px;
  background-color: #ffffff;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.payment-btn.selected {
  border-color: #3b82f6;
  background-color: #eff6ff;
}

.wechat-icon {
  color: #07c160;
}

.alipay-icon {
  color: #377dff;
}

.confirm-btn {
  padding: 12px 40px;
  background-color: #74b6f7;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.confirm-btn:hover {
  background-color: #377dff;
}
</style>
