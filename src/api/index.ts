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
  if (request.headers && localStorage.getItem('accessToken')) {
    request.headers.Authorization = `Bearer ${localStorage.getItem('accessToken')}`
  }
  // const params = request.params || {}
  // console.log('-------->', request.params)
  // // get参数编码
  // if (request.method?.toUpperCase() === 'GET' && params) {
  //   let url = `${request.url}?`
  //   for (const propName of Object.keys(params)) {
  //     const value = params[propName]
  //     if (
  //       value !== ''
  //       && value !== null
  //       && value !== 'undefined'
  //       && typeof value !== 'undefined'
  //     ) {
  //       if (typeof value === 'object') {
  //         for (const val of Object.keys(value)) {
  //           const params = `${propName}[${val}]`
  //           const subPart = `${encodeURIComponent(params)}=`
  //           url += `${subPart + encodeURIComponent(value[val])}&`
  //         }
  //       }
  //       else {
  //         url += `${propName}=${encodeURIComponent(value)}&`
  //       }
  //     }
  //   }
  //   // 给 get 请求加上时间戳参数，避免从缓存中拿数据
  //   // const now = new Date().getTime()
  //   // params = params.substring(0, url.length - 1) + `?_t=${now}`
  //   url = url.slice(0, -1)
  //   request.params = {}
  //   request.url = url
  // }
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
    ElMessage.error(error.msg)
    return Promise.reject(error)
  },
)

export default api
