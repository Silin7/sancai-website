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
    } else {
      return Promise.resolve(response.data)
    }
  },
  (error) => {
    ElMessage.error(error.msg)
    return Promise.reject(error)
  },
)

export default api
