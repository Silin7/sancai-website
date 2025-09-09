import api from '@/api/index'

// 获取当前用户的企业信息
export function companyinfoApi(params: any) {
  return api.get('/api/client/ucompany/my-company', {
    params,
  })
}

// 保存当前用户的企业信息（创建/更新）
export function savecompanyinfoApi(data: any) {
  return api.post('/api/client/ucompany/my-company', null, {
    params: {
      ...data,
    },
  })
}

// 获取当前用户企业的资质列表
export function certificatesApi(params: any) {
  return api.get('/api/client/ucompany/certificates', {
    params,
  })
}

// 新增企业资质
export function savecertificatesApi(data: any) {
  return api.post('/api/client/ucompany/certificates', null, {
    params: {
      ...data,
    },
  })
}

// 更新企业资质
export function updatecertificatesApi(certid: any) {
  return api.put(`/api/client/ucompany/certificates/${certid}`)
}

// 删除企业资质
export function deletecertificatesApi(certid: any) {
  return api.delete(`/api/client/ucompany/certificates/${certid}`)
}

// 获取当前用户企业的案例列表
export function casesApi(params: any) {
  return api.get('/api/client/ucompany/cases', {
    params,
  })
}

// 新增企业案例
export function savecasesApi(data: any) {
  return api.post('/api/client/ucompany/cases', null, {
    params: {
      ...data,
    },
  })
}

// 更新企业案例
export function updatecasesApi(certid: any) {
  return api.put(`/api/client/ucompany/cases/${certid}`)
}

// 删除企业案例
export function deletecasesApi(certid: any) {
  return api.delete(`/api/client/ucompany/cases/${certid}`)
}

// 查询企业列表（公开）
export function ucompanylistApi(params: any) {
  return api.get('/api/client/ucompany/list', {
    params,
  })
}

// 查询企业详情（公开）
export function ucompanydetailApi(companyid: any) {
  return api.get(`/api/client/ucompany/${companyid}`)
}
