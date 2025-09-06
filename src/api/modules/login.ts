import api from '@/api/index'

// 发送手机验证码
export function sendverificationcodeApi(data: any) {
  return api.post('/api/client/sms/sms/send-verification-code', null, {
    params: {
      ...data,
    },
  })
}

// 验证手机验证码
export function verifyverificationcodeApi(data: any) {
  return api.post('/api/client/sms/sms/verify-verification-code', null, {
    params: {
      ...data,
    },
  })
}

// 手机号注册
export function baseregisterApi(data: any) {
  return api.post('/api/client/base/register', null, {
    params: {
      ...data,
    },
  })
}

// 验证码登录
export function baselogincodeApi(data: any) {
  return api.post('/api/client/base/login/code', null, {
    params: {
      ...data,
    },
  })
}

// 密码登录
export function baseloginpwdApi(data: any) {
  return api.post('/api/client/base/login/password', null, {
    params: {
      ...data,
    },
  })
}
