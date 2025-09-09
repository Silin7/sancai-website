import api from '@/api/index'

// 用户端-创建视频购买支付订单（item_id=0），生成微信支付二维码
export function wxpayvideocreateApi(videoid: any, data: any) {
  return api.post(`/api/client/wxpay/video/${videoid}/create`, null, {
    params: {
      ...data,
    },
  })
}

// 用户端-查询视频支付状态（返回PayRecord的status字段）
export function deletecasesApi(videoid: any) {
  return api.get(`/api/client/wxpay/video/${videoid}/status`)
}

// 微信支付回调-更新PayRecord状态（status=1）
export function wxpaynotifywechatApi(data: any) {
  return api.post(`/api/client/wxpay/notify/wechat`, null, {
    params: {
      ...data,
    },
  })
}
// 用户端-获取视频播放地址（需PayRecord存在且status=1）
export function videoplayApi(videoid: any) {
  return api.get(`/api/client/wxpay/video/${videoid}/play`)
}

// 用户端-获取视频下载地址（需PayRecord存在且status=1）
export function videodownloadApi(videoid: any) {
  return api.get(`/api/client/wxpay/video/${videoid}/download`)
}
