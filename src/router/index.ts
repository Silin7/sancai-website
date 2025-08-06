import { createRouter, createWebHashHistory, type RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/home.vue'),
    meta: {
      title: '首页',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/products',
    name: 'products',
    component: () => import('@/views/products.vue'),
    meta: {
      title: '人材机信价格库',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/products_detail',
    name: 'products_detail',
    component: () => import('@/views/products_detail.vue'),
    meta: {
      title: '人材机信价格库',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/datasolution',
    name: 'datasolution',
    component: () => import('@/views/datasolution.vue'),
    meta: {
      title: '数据方案组价',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/ai',
    name: 'ai',
    component: () => import('@/views/ai.vue'),
    meta: {
      title: 'AI赋能应用',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/video',
    name: 'video',
    component: () => import('@/views/video.vue'),
    meta: {
      title: '视频演示',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/supplier',
    name: 'supplier',
    component: () => import('@/views/supplier.vue'),
    meta: {
      title: '供应商',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/supplier_detail',
    name: 'supplier_detail',
    component: () => import('@/views/supplier_detail.vue'),
    meta: {
      title: '供应商',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/about.vue'),
    meta: {
      title: '关于三才',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/news',
    name: 'news',
    component: () => import('@/views/news.vue'),
    meta: {
      title: '热点资讯',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/requirements',
    name: 'requirements',
    component: () => import('@/views/requirements.vue'),
    meta: {
      title: 'REQUIREMENTS',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login.vue'),
    meta: {
      title: 'LOGIN',
      website: true,
      hashead: true,
      hasfoot: false,
    },
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/register.vue'),
    meta: {
      title: 'REGISTER',
      website: true,
      hashead: true,
      hasfoot: false,
    },
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  // 根据路由元信息设置文档标题
  window.document.title = (to.meta.title as string) || ''
  window.localStorage.setItem('selectedTab', to.name as string)
  next()
})

export default router
