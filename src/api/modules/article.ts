import api from '@/api/index'

// 用户端-获取所有启用的文章分类（公开接口）
export function clientarticlescates() {
  return api.get('/api/client/articles/cates')
}
