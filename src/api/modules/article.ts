import api from '@/api/index'

// 用户端-获取所有启用的文章分类（公开接口）
export function articlescatesApi() {
  return api.get('/api/client/articles/cates')
}

// 用户端-文章列表（公开接口，支持筛选分页）
export function articlesApi(params: any) {
  return api.get('/api/client/articles', {
    params
  })
}
