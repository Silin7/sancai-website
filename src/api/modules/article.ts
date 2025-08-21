import api from '@/api/index'

// 用户端-获取所有启用的文章分类（公开接口）
export function articlescatesApi() {
  return api.get('/api/client/articles/cates')
}

// 用户端-文章列表（公开接口，支持筛选分页）
export function articlesApi(params: any) {
  return api.get('/api/client/articles', {
    params,
  })
}

// 用户端-按分类ID获取文章列表（公开接口）
export function articlescateApi(cateid: any, params: any) {
  return api.get(`/api/client/articles/cate/${cateid}`, {
    params,
  })
}

// 用户端-获取文章详情（公开接口）
export function articledetailApi(articleid: any) {
  return api.get(`/api/client/articles/${articleid}`)
}

// 用户端-收藏或取消收藏文章（需登录）
export function articlescollectApi(articleid: any) {
  return api.post(`/api/client/articles/${articleid}/collect`)
}
