<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import {
  mainadmininfoApi,
  mainadminsendcodeApi,
  mainadminchangeApi,
  normaladminlistApi,
  mainadminsearchuserApi,
  mainnormalsearchuserApi,
  mainnormaladdApi,
} from '@/api/modules/admin'

// 主管理员信息
const mainAdminInfo: any = ref({})
function getMainadmininfo() {
  mainadmininfoApi({
    company_id: company_id.value,
  }).then((res: any) => {
    if (res) {
      mainAdminInfo.value = res.data
    }
  })
}

// 普通管理员列表
const normaladminlist: any = ref([])
function getNormaladminlist() {
  normaladminlistApi({
    company_id: company_id.value,
  }).then((res: any) => {
    if (res) {
      normaladminlist.value = res.data
    }
  })
}

// 更新保存新主管理员
const changeadminVisible = ref(false)
const new_admin_email = ref('')
const code = ref('')
// 发送验证码
function sendCodeFunction() {
  if (!new_admin_email.value) {
    ElMessage.error('请输入邮箱地址')
    return
  }
  mainadminsendcodeApi({
    new_admin_email: new_admin_email.value,
    company_id: company_id.value,
  }).then((res: any) => {
    if (res) {
      ElMessage.success('验证码已发送，请查收邮箱')
    }
  })
}
// 保存新主管理员
function saveNewMainAdmin() {
  if (!new_admin_email.value) {
    ElMessage.error('请输入邮箱地址')
    return
  }
  if (!code.value) {
    ElMessage.error('请输入验证码')
    return
  }
  mainadminchangeApi({
    new_admin_email: new_admin_email.value,
    code: code.value,
    company_id: company_id.value,
  }).then((res: any) => {
    if (res) {
      ElMessage.success('主管理员已更换成功')
      changeadminVisible.value = false
      getMainadmininfo()
    }
  })
}

// 检索未绑定用户
const addadminVisible = ref(false)
const user_email = ref('silin7@foxmail.com')
const user_code = ref('')

function searchUnboundUser(email: string) {
  mainadminsearchuserApi({
    email: email,
    company_id: company_id.value,
  }).then((res: any) => {
    if (res) {
      // 处理返回的未绑定用户信息
    }
  })
}

const permissions = ref({
  "0": {
    "create": false,
    "delete": false,
    "read": false,
    "update": false
  },
  "1": {
    "create": false,
    "delete": false,
    "read": false,
    "update": false
  },
  "2": {
    "create": false,
    "delete": false,
    "read": false,
    "update": false
  },
  "3": {
    "create": false,
    "delete": false,
    "read": false,
    "update": false
  }
})

// 发送新增普通管理员验证码
function searchNormalAdminUser() {
  if (!user_email.value) {
    ElMessage.error('请输入邮箱地址')
    return
  }
  mainnormalsearchuserApi({
    email: user_email.value,
    company_id: company_id.value,
  }).then((res: any) => {
    if (res) {
      console.log('-------->', res)
    }
  })
}

function addNormalAdmin() {
  if (!user_email.value) {
    ElMessage.error('请输入邮箱地址')
    return
  }
  if (!user_code.value) {
    ElMessage.error('请输入验证码')
    return
  }
  mainnormaladdApi({
    company_id: company_id.value,
    user_email: user_email.value,
    code: user_code.value,
    permissions: permissions.value,
  }).then((res: any) => {
    if (res) {
      console.log('新增普通管理员成功', res)
    }
  })
}

const company_id: any = ref('')
onMounted(() => {
  const userinfo: any = JSON.parse(localStorage.getItem('userinfo') || '{}')
  company_id.value = userinfo?.related_companies[0]?.company_id
  if (company_id.value) {
    getMainadmininfo()
    getNormaladminlist()
    // searchUnboundUser('silin7@foxmail.com')
  } else {
    ElMessage.error('无管理员信息')
  }
})
</script>

<template>
  <div>
    <div class="page-main">
      <h1 class="page-title"><i class="fa fa-user-plus"></i>管理员管理</h1>
      <div class="page-card" style="margin-bottom: 32px">
        <div class="card-header">
          <h2 class="card-title"><i class="fa fa-diamond"></i>主管理员信息</h2>
          <button class="btn btn-primary" @click="changeadminVisible = true">
            <i class="fa fa-exchange"></i>修改主管理员
          </button>
        </div>
        <div class="admin-info">
          <div class="info-item">
            <span class="info-label">用户名：</span>
            <span class="info-value">{{ mainAdminInfo.name }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">邮箱：</span>
            <span class="info-value">{{ mainAdminInfo.email }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">创建时间：</span>
            <span class="info-value">{{ mainAdminInfo.create_time }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">最后登录：</span>
            <span class="info-value">{{ mainAdminInfo.last_login }}</span>
          </div>
        </div>
      </div>
      <div class="page-card">
        <div class="card-header">
          <h2 class="card-title"><i class="fa fa-users"></i>普通管理员管理</h2>
          <button class="btn btn-primary" @click="addadminVisible = true">
            <i class="fa fa-plus"></i>新增普通管理员
          </button>
        </div>
        <div class="table-container">
          <table class="admin-table">
            <thead>
              <tr>
                <th>姓名</th>
                <th>邮箱</th>
                <th>权限配置</th>
                <th>创建时间</th>
                <th>操作</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>李四</td>
                <td>lisi@example.com</td>
                <td>
                  <div class="permission-group">
                    <div class="permission-title">数字技工/方案论证</div>
                    <div class="permission-checkboxes">
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 创建
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 查看
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 更新
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" disabled /> 删除
                      </label>
                    </div>
                  </div>
                  <div class="permission-group">
                    <div class="permission-title">材料/设备</div>
                    <div class="permission-checkboxes">
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 创建
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 查看
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 更新
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 删除
                      </label>
                    </div>
                  </div>
                  <div class="permission-group">
                    <div class="permission-title">智能建造装备</div>
                    <div class="permission-checkboxes">
                      <label class="permission-checkbox">
                        <input type="checkbox" disabled /> 创建
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 查看
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" disabled /> 更新
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" disabled /> 删除
                      </label>
                    </div>
                  </div>
                  <div class="permission-group">
                    <div class="permission-title">信息化产品/服务</div>
                    <div class="permission-checkboxes">
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 创建
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" checked disabled /> 查看
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" disabled /> 更新
                      </label>
                      <label class="permission-checkbox">
                        <input type="checkbox" disabled /> 删除
                      </label>
                    </div>
                  </div>
                </td>
                <td>2025-03-20</td>
                <td>
                  <div class="action-buttons">
                    <button class="btn btn-outline" onclick="openEditPermissionModal()">
                      <i class="fa fa-edit"></i>编辑权限
                    </button>
                    <button class="btn btn-danger" onclick="confirmDeleteAdmin()">
                      <i class="fa fa-trash"></i>删除
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <el-dialog title="更换主管理员" v-model="changeadminVisible" width="800">
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">新主管理员邮箱</label>
          <input v-model="new_admin_email" type="email" class="form-input" placeholder="请输入新主管理员邮箱" />
        </div>
        <div class="form-group">
          <label class="form-label">验证码</label>
          <div class="verify-code-container">
            <input v-model="code" type="text" class="form-input verify-code-input" placeholder="请输入验证码" />
            <button class="send-code-btn" @click="sendCodeFunction">发送验证码</button>
          </div>
        </div>
        <p style="font-size: 12px; color: #909399; margin-top: 8px">
          注：更换主管理员后，原主管理员将变为普通管理员，新主管理员将拥有全部系统权限
        </p>
      </div>
      <div slot="footer" style="display: flex; justify-content: flex-end">
        <el-button @click="changeadminVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveNewMainAdmin">确 定</el-button>
      </div>
    </el-dialog>
    <el-dialog title="新增普通管理员" v-model="addadminVisible" width="800">
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">管理员邮箱</label>
          <input v-model="user_email" type="email" class="form-input" placeholder="请输入管理员邮箱" />
        </div>
        <div class="form-group">
          <label class="form-label">验证码</label>
          <div class="verify-code-container">
            <input v-model="user_code" type="text" class="form-input verify-code-input" placeholder="请输入验证码" />
            <button class="send-code-btn" @click="searchNormalAdminUser">发送验证码</button>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">初始权限配置</label>
          <div class="permission-group">
            <div class="permission-title">数字技工/方案论证</div>
            <div class="permission-checkboxes">
              <label class="permission-checkbox">
                <el-checkbox label="创建" v-model="permissions['0'].create" />
                <el-checkbox label="查看" v-model="permissions['0'].read" />
                <el-checkbox label="更新" v-model="permissions['0'].update" />
                <el-checkbox label="删除" v-model="permissions['0'].delete" />
              </label>
            </div>
          </div>
          <div class="permission-group">
            <div class="permission-title">材料/设备</div>
            <div class="permission-checkboxes">
              <el-checkbox label="创建" v-model="permissions['1'].create" />
              <el-checkbox label="查看" v-model="permissions['1'].read" />
              <el-checkbox label="更新" v-model="permissions['1'].update" />
              <el-checkbox label="删除" v-model="permissions['1'].delete" />
            </div>
          </div>
          <div class="permission-group">
            <div class="permission-title">智能建造装备</div>
            <div class="permission-checkboxes">
              <el-checkbox label="创建" v-model="permissions['2'].create" />
              <el-checkbox label="查看" v-model="permissions['2'].read" />
              <el-checkbox label="更新" v-model="permissions['2'].update" />
              <el-checkbox label="删除" v-model="permissions['2'].delete" />
            </div>
          </div>
          <div class="permission-group">
            <div class="permission-title">信息化产品/服务</div>
            <div class="permission-checkboxes">
              <el-checkbox label="创建" v-model="permissions['3'].create" />
              <el-checkbox label="查看" v-model="permissions['3'].read" />
              <el-checkbox label="更新" v-model="permissions['3'].update" />
              <el-checkbox label="删除" v-model="permissions['3'].delete" />
            </div>
          </div>
        </div>
      </div>
      <div slot="footer" style="display: flex; justify-content: flex-end">
        <el-button @click="addadminVisible = false">取 消</el-button>
        <el-button type="primary" @click="addadminVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped>
.page-title {
  font-size: 24px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 24px;
  display: flex;
  align-items: center;

  i {
    color: #377dff;
    margin-right: 8px;
  }
}

.card-header {}
</style>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family:
    'Inter',
    system-ui,
    -apple-system,
    sans-serif;
  background-color: #f5f7fa;
  color: #303133;
}

/* 顶部导航栏 - 与其他页面完全一致 */
.top-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background-color: #012060;
  box-shadow: 0 1px 3px rgba(7, 51, 234, 0.2);
}

.logo-area {
  display: flex;
  align-items: center;
}

.logo {
  align-items: center;
  color: #ffffff;
}

.site-name {
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
}

.user-area {
  display: flex;
  align-items: center;
}

.user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  margin-right: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-weight: 500;
}

.user-name {
  font-size: 14px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.9);
}

/* 左侧导航与整体布局 - 与其他页面完全一致 */
.container {
  display: flex;
  min-height: calc(100vh - 72px);
}

.sidebar {
  width: 240px;
  background-color: #ffffff;
  border-right: 1px solid #e6e9ed;
  padding: 16px 0;
}

.sidebar-nav {
  list-style: none;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 14px 24px;
  cursor: pointer;
  color: #606266;
  text-decoration: none;
  transition: all 0.2s ease;
  margin-bottom: 4px;
}

.nav-item i {
  margin-right: 12px;
  font-size: 16px;
  width: 20px;
  text-align: center;
}

.nav-item.active {
  background-color: #1f69ff;
  color: #ffffff;
  border-left: none;
  padding-left: 24px;
  font-weight: 500;
}

.nav-item:hover:not(.active) {
  background-color: #f3f8fc;
  color: #377dff;
}

/* 管理员管理页面主内容区域样式 */
.admin-management {
  flex: 1;
  padding: 24px 32px;
  background-color: #f5f7fa;
}

.page-title {
  font-size: 24px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
}

.page-title i {
  margin-right: 8px;
  color: #377dff;
}

/* 主管理员信息卡片 */
.main-admin-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  padding: 24px;
  margin-bottom: 32px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid #f0f2f5;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
  display: flex;
  align-items: center;
}

.card-title i {
  margin-right: 8px;
  color: #377dff;
}

.admin-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
}

.info-item {
  display: flex;
  flex-direction: column;
}

.info-label {
  font-size: 14px;
  color: #909399;
  margin-bottom: 4px;
}

.info-value {
  font-size: 16px;
  color: #303133;
  font-weight: 500;
}

.btn {
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.btn i {
  margin-right: 6px;
}

.btn-primary {
  background-color: #409eff;
  color: #ffffff;
}

.btn-primary:hover {
  background-color: #66b1ff;
}

.btn-danger {
  background-color: #f5222d;
  color: #ffffff;
}

.btn-danger:hover {
  background-color: #ff4d4f;
}

.btn-outline {
  background-color: transparent;
  color: #409eff;
  border: 1px solid #409eff;
}

.btn-outline:hover {
  background-color: #ecf5ff;
}

/* 普通管理员管理区域 */
.normal-admin-section {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  padding: 24px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.table-container {
  overflow-x: auto;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.admin-table th,
.admin-table td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #f0f2f5;
}

.admin-table th {
  background-color: #f7f8fa;
  color: #303133;
  font-weight: 600;
}

.admin-table tbody tr:hover {
  background-color: #fafafa;
}

.permission-group {
  margin-bottom: 12px;
}

.permission-title {
  font-size: 13px;
  color: #606266;
  margin-bottom: 6px;
  font-weight: 500;
}

.permission-checkboxes {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.permission-checkbox {
  display: flex;
  align-items: center;
  font-size: 12px;
  color: #606266;
}

.permission-checkbox input {
  margin-right: 4px;
  accent-color: #409eff;
}

.action-buttons {
  display: flex;
  gap: 8px;
}

/* 弹窗样式扩展 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

.modal-container {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  width: 500px;
  max-width: 90%;
  transform: translateY(-20px);
  transition: transform 0.3s ease;
}

.modal-overlay.active .modal-container {
  transform: translateY(0);
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid #eee;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
  margin-left: 10px;
}

.modal-close {
  background: none;
  border: none;
  font-size: 18px;
  color: #909399;
  cursor: pointer;
  transition: color 0.2s;
}

.modal-close:hover {
  color: #303133;
}

.modal-body {
  padding: 20px;
  color: #606266;
  line-height: 1.6;
}

.modal-footer {
  padding: 12px 20px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: flex-end;
}

.modal-btn {
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  margin-left: 10px;
  transition: all 0.2s;
}

.modal-btn-cancel {
  background-color: #f5f7fa;
  color: #606266;
  border: 1px solid #dcdfe6;
}

.modal-btn-cancel:hover {
  color: #409eff;
  border-color: #c6e2ff;
  background-color: #ecf5ff;
}

.modal-btn-confirm {
  background-color: #409eff;
  color: white;
  border: 1px solid #409eff;
}

.modal-btn-confirm:hover {
  background-color: #66b1ff;
  border-color: #66b1ff;
}

.modal-icon {
  color: #e6a23c;
  font-size: 20px;
}

/* 表单样式 */
.form-group {
  margin-bottom: 16px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-size: 14px;
  color: #303133;
  font-weight: 500;
}

.form-input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  color: #303133;
  transition: border-color 0.2s;
}

.form-input:focus {
  outline: none;
  border-color: #409eff;
  box-shadow: 0 0 0 2px rgba(64, 158, 255, 0.2);
}

.verify-code-container {
  display: flex;
  gap: 12px;
}

.verify-code-input {
  flex: 1;
}

.send-code-btn {
  padding: 10px 16px;
  background-color: #f5f7fa;
  color: #409eff;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  white-space: nowrap;
}

.send-code-btn:hover {
  background-color: #ecf5ff;
  border-color: #c6e2ff;
}

.send-code-btn.disabled {
  background-color: #f5f5f5;
  color: #c0c4cc;
  cursor: not-allowed;
  border-color: #e6e6e6;
}

/* 底部版权信息 - 与其他页面完全一致 */
.footer {
  position: fixed;
  bottom: 0;
  left: 240px;
  right: 0;
  background-color: #ffffff;
  border-top: 1px solid #e6e9ed;
  padding: 12px 32px;
  text-align: center;
  font-size: 14px;
  color: #606266;
}

/* 响应式设计 - 与其他页面保持一致 */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid #e6e9ed;
  }

  .admin-management {
    padding: 16px;
  }

  .admin-info {
    grid-template-columns: 1fr;
  }

  .permission-checkboxes {
    flex-direction: column;
  }

  .action-buttons {
    flex-direction: column;
  }

  .footer {
    left: 0;
    position: relative;
  }
}
</style>
