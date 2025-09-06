import api from '@/api/index'

// 发送手机验证码
export function sendverificationcodeApi(params2: any) {
  return api.post('/api/client/sms/sms/send-verification-code', null, {
    params: {
      ...params2,
    },
  })
}

// 验证手机验证码
export function verifyverificationcodeApi(params2: any) {
  return api.post('/api/client/sms/sms/verify-verification-code', null, {
    params: {
      ...params2,
    },
  })
}
