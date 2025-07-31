<script setup lang="ts">
import { ref } from 'vue'

const checked1: any = ref(true)
const checked2: any = ref(false)
const checked3: any = ref(false)
const phone: any = ref('')
const password: any = ref('')
const yzm: any = ref('')
</script>

<template>
  <div class="registerPage">
    <div class="registerbox">
      <div class="hyzc">欢迎注册</div>
      <div class="typebox frsc">
        <div>
          <img v-if="checked1" src="@/assets/register/checked.png" alt="" />
          <img v-else src="@/assets/register/unchecked.png" alt="" />
          <span>供方</span>
        </div>
        <div>
          <img v-if="checked2" src="@/assets/register/checked.png" alt="" />
          <img v-else src="@/assets/register/unchecked.png" alt="" />
          <span>需方</span>
        </div>
      </div>
      <div class="fromitem frsc">
        <img src="@/assets/register/user.png" alt="" />
        <el-input v-model="phone" style="width: 100%" placeholder="请输入手机号" clearable />
      </div>
      <div class="fromitem frsc">
        <img src="@/assets/register/pwd.png" alt="" />
        <el-input v-model="password" style="width: 100%" placeholder="请输入8-16位密码" clearable />
      </div>
      <div class="fromitem frsc">
        <img src="@/assets/register/yzm.png" alt="" />
        <el-input
          v-model="yzm"
          style="width: calc(100% - 140px)"
          placeholder="短信验证码"
          clearable
        />
        <button>获取验证码</button>
      </div>
      <div class="statement">
        <img v-if="checked3" src="@/assets/register/checked.png" alt="" />
        <img v-else src="@/assets/register/unchecked.png" alt="" />
        我已阅读并同意<span>《新材网用户服务协议》</span>和<span>《新材网隐私政策声明》</span>
      </div>
      <button class="createAccount">创建账号</button>
      <div class="gologin">已有账号？<span>立即登录</span></div>
    </div>
    <div class="copyright">
      Copyright ©2025 新材网 版权所有 浙ICP备123456789-1号浙公网安备37000000号
    </div>
  </div>
</template>

<style lang="scss">
.registerPage {
  position: fixed;
  width: 100vw;
  height: 100vh;
  background-image: url('../assets/banner00.jpeg');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-attachment: fixed;
  background-position: right;

  .registerbox {
    position: absolute;
    top: 20%;
    right: 20%;
    padding: 30px 50px 50px;
    width: 30rem;
    background: rgba(255, 255, 255, 1);
    box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

    .hyzc {
      margin-bottom: 25px;
      font-size: 20px;
      font-weight: 700;
      letter-spacing: 0px;
      line-height: 30px;
      color: rgba(0, 0, 0, 1);
      text-align: left;
      vertical-align: top;
    }

    .typebox {
      margin-bottom: 20px;

      div {
        display: flex;
        align-items: center;

        img {
          margin-right: 10px;
          width: 18px;
          height: 18px;
        }

        span {
          font-size: 18px;
          font-weight: 500;
          letter-spacing: 0px;
          line-height: 18px;
          color: rgba(0, 0, 0, 1);
          text-align: left;
        }
      }

      div:first-child {
        margin-right: 80px;
      }
    }

    .fromitem {
      margin-bottom: 40px;
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
        cursor: pointer;
        color: rgba(42, 130, 228, 1);
      }
    }

    .createAccount {
      margin-top: 24px;
      width: 100%;
      height: 48px;
      border-radius: 111px;
      color: #fff;
      background:
        linear-gradient(117.41deg, rgba(2, 93, 244, 1) 0%, rgba(7, 91, 237, 1) 100%),
        rgba(204, 204, 204, 1);
      box-shadow: -1px 4px 6px rgba(4, 71, 177, 0.29);
    }

    .gologin {
      margin-top: 15px;
      text-align: center;
      font-size: 16px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 24px;
      color: rgba(128, 128, 128, 1);

      span {
        cursor: pointer;
        color: rgba(42, 130, 228, 1);
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
