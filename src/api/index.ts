import axios from 'axios'
import { ElMessage } from 'element-plus'
import { baseURL } from './baseConfig'

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
  if (request.headers && localStorage.getItem('token')) {
    request.headers.token = `Bearer ${localStorage.getItem('token') ?? ''}`
  }
  return request
})

api.interceptors.response.use(
  async (response) => {
    if (!response.data) {
      throw new Error()
    } else {
      return Promise.resolve(response.data)
    }
  },
  (error) => {
    ElMessage.error(error.response.data.msg)
    return Promise.reject(error)
  },
)

export default api
