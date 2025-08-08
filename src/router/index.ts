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
    path: '/scheme',
    name: 'scheme',
    component: () => import('@/views/scheme.vue'),
    meta: {
      title: '数字技工/方案论证',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/materials',
    name: 'materials',
    component: () => import('@/views/materials.vue'),
    meta: {
      title: '材料/设备',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/sale',
    name: 'sale',
    component: () => import('@/views/sale.vue'),
    meta: {
      title: '智能建造装备',
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
      title: '信息化产品/服务',
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
      title: '信息化产品/服务',
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
    path: '/requirements',
    name: 'requirements',
    component: () => import('@/views/requirements.vue'),
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
    path: '/news_detail',
    name: 'news_detail',
    component: () => import('@/views/news_detail.vue'),
    meta: {
      title: '热点资讯',
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
      title: '登录',
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
      title: '注册',
      website: true,
      hashead: true,
      hasfoot: false,
    },
  },
  {
    path: '/user/index',
    name: 'user-index',
    component: () => import('@/views/user/index.vue'),
    meta: {
      title: '新材网-首页',
      website: false,
    },
  },
  {
    path: '/user/profile',
    name: 'user-profile',
    component: () => import('@/views/user/profile.vue'),
    meta: {
      title: '新材网-用户资料',
      website: false,
    },
  },
  {
    path: '/user/renlist',
    name: 'user-renlist',
    component: () => import('@/views/user/renlist.vue'),
    meta: {
      title: '新材网-数字技工/方案论证',
      website: false,
    },
  },
  {
    path: '/user/cailist',
    name: 'user-cailist',
    component: () => import('@/views/user/cailist.vue'),
    meta: {
      title: '新材网-材料/设备',
      website: false,
    },
  },
  {
    path: '/user/machinelist',
    name: 'user-machinelist',
    component: () => import('@/views/user/machinelist.vue'),
    meta: {
      title: '新材网-智能建造装备',
      website: false,
    },
  },
  {
    path: '/user/itlist',
    name: 'user-itlist',
    component: () => import('@/views/user/itlist.vue'),
    meta: {
      title: '新材网-信息化产品/服务',
      website: false,
    },
  },
  {
    path: '/user/inquirylist',
    name: 'user-inquirylist',
    component: () => import('@/views/user/inquirylist.vue'),
    meta: {
      title: '新材网-报价单',
      website: false,
    },
  },
  {
    path: '/user/editpwd',
    name: 'user-editpwd',
    component: () => import('@/views/user/editpwd.vue'),
    meta: {
      title: '新材网-改密码',
      website: false,
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
