import { createApp } from 'vue'

import App from './App.vue'
const app = createApp(App)

// 自定义样式 custom style
import '@/styleSheet/index.scss'

// font-awesome style
import 'font-awesome/css/font-awesome.min.css'

// 路由 router
import router from './router'
app.use(router)

// 状态管理工具 pinia
import pinia from './store'
app.use(pinia)

// UI Element Plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
app.use(ElementPlus)

// 图标 Element Plus
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.mount('#app')
