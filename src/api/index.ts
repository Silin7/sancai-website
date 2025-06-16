import axios from 'axios'
import { ElMessage } from 'element-plus'
import { baseURL } from './baseConfig'
import useUserStore from '@/store/modules/user'

const api = axios.create({
  baseURL,
  timeout: 1000 * 60,
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Access-Control-Allow-Origin': '*',
  },
})

api.interceptors.request.use((request) => {
  // 设置请求头
  if (request.headers && localStorage.getItem('accessToken')) {
    request.headers.Authorization = `Bearer ${localStorage.getItem('accessToken')}`
  }
  return request
})

// 401响应码 白名单
const responseWhiteList: any = []

api.interceptors.response.use(
  async (response) => {
    if (!response.data) {
      throw new Error()
    }
    // 二进制数据则直接返回
    if (response.request.responseType === 'blob' || response.request.responseType === 'arraybuffer') {
      return response.data
    }
    // 401 token失效
    else if (response.data && response.data.code === 401) {
      if (responseWhiteList.length === 0) {
        useUserStore().logout()
        return
      }
      for (let i = 0; i < responseWhiteList.length; i++) {
        if (response.request.responseURL?.indexOf(responseWhiteList[i]) > -1) {
          return Promise.reject(response.data)
        } else {
          useUserStore().logout()
        }
      }
    }
    // 403 直接退出
    else if (response.data && response.data.code === 403) {
      useUserStore().logout()
    }
    // 响应码 !=200 !==0 抛出错误信息
    else if (response.data && (response.data.code !== 200 && response.data.code !== 0)) {
      ElMessage.error(response.data.msg)
      return Promise.reject(response.data)
    }
    return Promise.resolve(response.data)
  },
  (error) => {
    ElMessage.error(error.msg)
    return Promise.reject(error)
  },
)

export default api
