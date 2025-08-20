import api from '@/api/index'

// 用户端-获取所有启用的板块位置（含完整字段，按排序升序、创建时间倒序）
export function secpositionsApi() {
  return api.get('/api/client/sysbase/sec-positions')
}
// 用户端-按板块位置ID获取最新启用的板块内容（含完整位置信息）
export function seccontentApi(positionid: any) {
  return api.get(`/api/client/sysbase/sec-content/${positionid}`)
}

// 用户端-按板块位置ID获取所有启用的Banner（含位置名称）
export function bannerlistApi(positionid: any) {
  return api.get(`/api/client/sysbase/banner-list/${positionid}`)
}

// 用户端-获取所有有效合作单位（按排序升序、创建时间倒序）
export function vippartnersApi() {
  return api.get('/api/client/sysbase/vip-partners')
}

// 用户端-获取所有有效系统信息（如系统名称、版权信息等，按Key排序）
export function sysinfosApi() {
  return api.get('/api/client/sysbase/sysinfos')
}
