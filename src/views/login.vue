<script setup lang="ts">
import { ref } from 'vue'

const state: any = ref('kj')

function setState(code: string) {
  state.value = code
}

const checked1: any = ref(true)
const checked2: any = ref(false)
const checked3: any = ref(false)
const phone: any = ref('')
const password: any = ref('')
const yzm: any = ref('')
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
          <img src="@/assets/register/user.png" alt="" />
          <el-input v-model="phone" style="width: 100%" placeholder="请输入手机号" clearable />
        </div>
        <div v-if="state === 'mm'" class="fromitem frsc">
          <img src="@/assets/register/pwd.png" alt="" />
          <el-input v-model="password" style="width: 100%" placeholder="请输入8-16位密码" clearable />
        </div>
        <div v-if="state === 'kj'" class="fromitem frsc">
          <img src="@/assets/register/yzm.png" alt="" />
          <el-input v-model="yzm" style="width: calc(100% - 140px)" placeholder="短信验证码" clearable />
          <button>获取验证码</button>
        </div>
        <div v-if="state === 'mm'" class="frec">
          <button class="forgotPassword">忘记密码</button>
        </div>
      </div>
      <button class="createAccount">登录</button>
      <div v-if="state === 'kj'" class="gologin">还没账户？<span>免费注册</span></div>
    </div>
    <div class="copyright">
      Copyright ©2025 新材网 版权所有 浙ICP备123456789-1号浙公网安备37000000号
    </div>
  </div>
</template>

<style lang="scss">
.loginPage {
  position: fixed;
  width: 100vw;
  height: 100vh;
  background-image: url('../assets/banner00.jpeg');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-attachment: fixed;
  background-position: right;

  .loginbox {
    position: absolute;
    top: 20%;
    right: 20%;
    padding: 30px 0 50px;
    width: 30rem;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

    .loginTitle {
      padding-left: 68px;
      border-bottom: 1px solid rgba(166, 166, 166, 1);

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
      margin: 70px 50px 0;

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
      color: rgba(56, 56, 56, 1);
      background: rgba(229, 229, 229, 1);
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
    position: absolute;
    bottom: 44px;
    width: 100%;
    font-size: 18px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 26px;
    color: rgba(245, 245, 245, 1);
    text-align: center;
  }
}
</style>
