<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import pageJump from '@/hooks/pageJump'
import {
  sendverificationcodeApi,
  // verifyverificationcodeApi,
  baselogincodeApi,
  baseloginpwdApi,
} from '@/api/modules/login'
import { sysinfosApi } from '@/api/modules/basic'

const sys_filing: any = ref('')
onMounted(() => {
  sysinfosApi().then((res: any) => {
    if (res) {
      sys_filing.value = res.filter((item: any) => item.ky === 'sys_filing')[0].val
    }
  })
})

const state: any = ref('kj')

function setState(code: string) {
  state.value = code
}

const email: any = ref('')
const password: any = ref('')
const code: any = ref('')

function getCode() {
  if (!email.value) {
    ElMessage({
      type: 'error',
      message: '请输入邮箱',
    })
    return
  }
  if (!/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(email.value)) {
    ElMessage({
      type: 'error',
      message: '邮箱格式错误',
    })
    return
  }
  sendverificationcodeApi({
    email: email.value,
    scene: 'login',
  }).then((res: any) => {
    if (res) {
      countdownChange()
    }
  })
}

// 验证码倒计时
const countdown: any = ref(60)
const verificationTimer: any = ref(null)

function countdownChange() {
  verificationTimer.value = setInterval(() => {
    countdown.value -= 1
    // 清除定时器
    if (countdown.value === 0) {
      clearInterval(verificationTimer.value)
      countdown.value = 60
    }
  }, 1000)
}

// 验证码登录
function loginByCoode() {
  if (!email.value) {
    ElMessage({
      type: 'error',
      message: '请输入邮箱',
    })
    return
  }
  if (!/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(email.value)) {
    ElMessage({
      type: 'error',
      message: '邮箱格式错误',
    })
    return
  }
  // 快捷登录
  if (state.value === 'kj') {
    if (!code.value) {
      ElMessage({
        type: 'error',
        message: '请输入验证码',
      })
      return
    }
    // verifyverificationcodeApi({
    //   email: email.value,
    //   code: code.value,
    // }).then((res: any) => {
    //   if (res) {
    //   }
    // })
    getBaselogincode()
  }
  // 密码登录
  if (state.value === 'mm') {
    if (!password.value) {
      ElMessage({
        type: 'error',
        message: '请输入密码',
      })
      return
    }
    baseloginpwdApi({
      email: email.value,
      password: password.value,
    }).then((res: any) => {
      if (res) {
        ElMessage({
          type: 'success',
          message: '登录成功',
        })
        window.localStorage.setItem('token', res.token)
        window.localStorage.setItem('userinfo', JSON.stringify(res.user_info))
        window.localStorage.setItem('permission', JSON.stringify(res.permission))
        pageJump('home')
      }
    })
  }
}

// 验证码登录
function getBaselogincode() {
  baselogincodeApi({
    email: email.value,
    code: code.value,
  }).then((res: any) => {
    if (res) {
      ElMessage({
        type: 'success',
        message: '登录成功',
      })
      window.localStorage.setItem('token', res.token)
      window.localStorage.setItem('userinfo', JSON.stringify(res.user_info))
      window.localStorage.setItem('permission', JSON.stringify(res.permission))
      pageJump('home')
    }
  })
}

onUnmounted(() => {
  clearInterval(verificationTimer.value)
})
</script>

<template>
  <div class="loginPage">
    <div class="loginbox">
      <div class="loginTitle frsc">
        <div :class="['hyzc', state === 'kj' ? 'hyzcActive' : '']" @click="setState('kj')">
          快捷登录
        </div>
        <div :class="['hyzc', state === 'mm' ? 'hyzcActive' : '']" @click="setState('mm')">
          密码登录
        </div>
      </div>
      <div class="fromBox">
        <div class="fromitem frsc">
          <img src="@/assets/register/user.png" />
          <el-input v-model="email" style="width: 100%" placeholder="请输入邮箱" clearable />
        </div>
        <div v-if="state === 'mm'" class="fromitem frsc">
          <img src="@/assets/register/pwd.png" />
          <el-input type="password" show-password v-model="password" style="width: 100%" placeholder="请输入8-16位密码"
            clearable />
        </div>
        <div v-if="state === 'kj'" class="fromitem frsc">
          <img src="@/assets/register/yzm.png" />
          <el-input v-model="code" style="width: calc(100% - 140px)" placeholder="邮箱验证码" clearable />
          <div v-if="countdown < 60 && countdown > 0" class="djsTimeStyle">
            已发送（{{ countdown }}）
          </div>
          <button v-else @click="getCode">获取验证码</button>
        </div>
        <div v-if="state === 'mm'" class="frec">
          <button class="forgotPassword" @click="pageJump('rpassword')">忘记密码</button>
        </div>
      </div>
      <button class="createAccount" @click="loginByCoode">登录</button>
      <div v-if="state === 'kj'" class="gologin">
        还没账户？<span @click="pageJump('register')">免费注册</span>
      </div>
    </div>
    <div class="copyright">
      {{ sys_filing }}
    </div>
  </div>
</template>

<style lang="scss">
.loginPage {
  position: fixed;
  overflow-y: auto;
  padding: 1rem;
  width: 100vw;
  height: 100vh;
  background-image: url('../assets/login-banner.jpg');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-attachment: fixed;
  background-position: right;

  .loginbox {
    margin: 4rem 0 2rem;
    padding: 2rem 1rem;
    background: rgba(255, 255, 255, 1);
    box-shadow:
      0 10px 15px -3px rgb(0 0 0 / 0.1),
      0 4px 6px -4px rgb(0 0 0 / 0.1);

    @media (min-width: 768px) {
      position: absolute;
      top: 20%;
      right: 20%;
      padding: 30px 50px 50px;
      width: 30rem;
    }

    .loginTitle {
      padding-left: 20px;
      border-bottom: 1px solid rgba(166, 166, 166, 1);

      @media (min-width: 768px) {
        padding-left: 68px;
      }

      .hyzc {
        padding-bottom: 25px;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 0px;
        line-height: 20px;
        color: rgba(0, 0, 0, 1);
        text-align: left;
        vertical-align: top;
        border-bottom: 3px solid #fff;
      }

      .hyzc:first-child {
        margin-right: 60px;
      }

      .hyzc:hover {
        @media (min-width: 768px) {
          cursor: pointer;
        }
      }

      .hyzcActive {
        border-color: rgba(0, 42, 201, 1);
      }
    }

    .fromBox {
      margin: 20px 0;

      @media (min-width: 768px) {
        margin: 70px 50px 0;
      }

      .fromitem {
        padding: 0 18px;
        height: 48px;
        background: rgba(255, 255, 255, 1);
        border: 1px solid rgba(224, 224, 224, 1);

        img {
          margin-right: 20px;
          width: 16px;
          height: 16px;
          object-fit: fill;
        }

        .el-input__wrapper {
          border: none !important;
          box-shadow: none !important;
          padding: 0px;
        }

        button {
          margin-left: 10px;
          font-size: 16px;
          font-weight: 400;
          letter-spacing: 0px;
          line-height: 16px;
          color: rgba(42, 130, 228, 1);
        }

        .djsTimeStyle {
          font-size: 0.85rem;
          color: rgba(128, 128, 128, 1);
        }
      }

      .fromitem:first-child {
        margin-bottom: 40px;
      }
    }

    .forgotPassword {
      margin-top: 12px;
      font-size: 17px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 24px;
      color: rgba(42, 130, 228, 1);
    }

    .statement {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      font-size: 16px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 24px;
      color: rgba(128, 128, 128, 1);

      img {
        margin-right: 10px;
        width: 18px;
        height: 18px;
      }

      span {
        color: rgba(42, 130, 228, 1);
      }

      span:hover {
        @media (min-width: 768px) {
          cursor: pointer;
        }
      }
    }

    .createAccount {
      margin: 124px 50px 0;
      width: calc(100% - 100px);
      height: 48px;
      border-radius: 111px;
      color: #fff;
      background:
        linear-gradient(117.41deg, rgba(2, 93, 244, 1) 0%, rgba(7, 91, 237, 1) 100%),
        rgba(204, 204, 204, 1);
      box-shadow: -1px 4px 6px rgba(4, 71, 177, 0.29);
    }

    .gologin {
      margin-top: 24px;
      text-align: center;
      font-size: 16px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 24px;
      color: rgba(128, 128, 128, 1);

      span {
        color: rgba(42, 130, 228, 1);
      }

      span:hover {
        @media (min-width: 768px) {
          cursor: pointer;
        }
      }
    }
  }

  .copyright {
    margin-top: calc(100vh - 41.25rem);
    font-size: 18px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 26px;
    color: rgba(0, 0, 0, 1);
    text-align: center;

    @media (min-width: 768px) {
      position: absolute;
      bottom: 44px;
      width: 100%;
    }
  }
}
</style>
