import { createRouter, createWebHashHistory, type RouteRecordRaw } from 'vue-router'
import useHeaderStore from '@/store/modules/header'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/home',
    name: 'home',
    component: () => import('@/views/home.vue'),
    meta: {
      title: '系统首页',
      stcode: 'home',
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
      title: '数字技术应用论证/数字实施方案论证',
      stcode: 'scheme',
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
      stcode: 'materials',
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
      stcode: 'sale',
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
      stcode: 'products',
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
      stcode: 'products',
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
      stcode: 'datasolution',
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
      stcode: 'datasolution',
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
      stcode: 'ai',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/ai_detail',
    name: 'ai_detail',
    component: () => import('@/views/ai_detail.vue'),
    meta: {
      title: 'AI赋能应用',
      stcode: 'ai',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/aicase_detail',
    name: 'aicase_detail',
    component: () => import('@/views/aicase_detail.vue'),
    meta: {
      title: 'AI赋能应用',
      stcode: 'ai',
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
      stcode: 'video',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/video_detail',
    name: 'video_detail',
    component: () => import('@/views/video_detail.vue'),
    meta: {
      title: '视频演示',
      stcode: 'video',
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
      stcode: 'supplier',
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
      stcode: 'supplier',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/supplier_al',
    name: 'supplier_al',
    component: () => import('@/views/supplier_al.vue'),
    meta: {
      title: '供应商',
      stcode: 'supplier',
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
      stcode: 'about',
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
      stcode: 'news',
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
      stcode: 'news',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/engineeringai',
    name: 'engineeringai',
    component: () => import('@/views/engineeringai.vue'),
    meta: {
      title: '工程造价+AI',
      stcode: 'engineeringai',
      website: true,
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/article_detail',
    name: 'article_detail',
    component: () => import('@/views/article_detail.vue'),
    meta: {
      title: '文章详情',
      stcode: 'article',
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
      stcode: 'login',
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
      stcode: 'register',
      website: true,
      hashead: true,
      hasfoot: false,
    },
  },
  {
    path: '/rpassword',
    name: 'rpassword',
    component: () => import('@/views/rpassword.vue'),
    meta: {
      title: '注册',
      stcode: 'rpassword',
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
      stcode: 'user-index',
      website: false,
    },
  },
  {
    path: '/user/upgradevip',
    name: 'user-upgradevip',
    component: () => import('@/views/user/upgradevip.vue'),
    meta: {
      title: '新材网-升级VIP',
      stcode: 'user-upgradevip',
      website: false,
    },
  },
  {
    path: '/user/profile',
    name: 'user-profile',
    component: () => import('@/views/user/profile.vue'),
    meta: {
      title: '新材网-企业资料',
      stcode: 'user-profile',
      website: false,
    },
  },
  {
    path: '/user/qyzzlist',
    name: 'user-qyzzlist',
    component: () => import('@/views/user/qyzzlist.vue'),
    meta: {
      title: '新材网-企业资质',
      stcode: 'user-qyzzlist',
      website: false,
    },
  },
  {
    path: '/user/qyzzfrom',
    name: 'user-qyzzfrom',
    component: () => import('@/views/user/qyzzfrom.vue'),
    meta: {
      title: '新材网-企业资质',
      stcode: 'user-qyzzlist',
      website: false,
    },
  },
  {
    path: '/user/qyallist',
    name: 'user-qyallist',
    component: () => import('@/views/user/qyallist.vue'),
    meta: {
      title: '新材网-企业案例',
      stcode: 'user-qyallist',
      website: false,
    },
  },
  {
    path: '/user/qyalfrom',
    name: 'user-qyalfrom',
    component: () => import('@/views/user/qyalfrom.vue'),
    meta: {
      title: '新材网-企业案例',
      stcode: 'user-qyallist',
      website: false,
    },
  },
  {
    path: '/user/renlist',
    name: 'user-renlist',
    component: () => import('@/views/user/renlist.vue'),
    meta: {
      title: '新材网-数字技术应用论证/数字实施方案论证',
      stcode: 'user-renlist',
      website: false,
    },
  },
  {
    path: '/user/renfrom',
    name: 'user-renfrom',
    component: () => import('@/views/user/renfrom.vue'),
    meta: {
      title: '新材网-数字技术应用论证/数字实施方案论证',
      stcode: 'user-renlist',
      website: false,
    },
  },
  {
    path: '/user/cailist',
    name: 'user-cailist',
    component: () => import('@/views/user/cailist.vue'),
    meta: {
      title: '新材网-材料/设备',
      stcode: 'user-cailist',
      website: false,
    },
  },
  {
    path: '/user/caifrom',
    name: 'user-caifrom',
    component: () => import('@/views/user/caifrom.vue'),
    meta: {
      title: '新材网-材料/设备',
      stcode: 'user-cailist',
      website: false,
    },
  },
  {
    path: '/user/machinelist',
    name: 'user-machinelist',
    component: () => import('@/views/user/machinelist.vue'),
    meta: {
      title: '新材网-智能建造装备',
      stcode: 'user-machinelist',
      website: false,
    },
  },
  {
    path: '/user/machinefrom',
    name: 'user-machinefrom',
    component: () => import('@/views/user/machinefrom.vue'),
    meta: {
      title: '新材网-智能建造装备',
      stcode: 'user-machinelist',
      website: false,
    },
  },
  {
    path: '/user/itlist',
    name: 'user-itlist',
    component: () => import('@/views/user/itlist.vue'),
    meta: {
      title: '新材网-信息化产品/服务',
      stcode: 'user-itlist',
      website: false,
    },
  },
  {
    path: '/user/itfrom',
    name: 'user-itfrom',
    component: () => import('@/views/user/itfrom.vue'),
    meta: {
      title: '新材网-信息化产品/服务',
      stcode: 'user-itlist',
      website: false,
    },
  },
  {
    path: '/user/inquirylist',
    name: 'user-inquirylist',
    component: () => import('@/views/user/inquirylist.vue'),
    meta: {
      title: '新材网-报价单',
      stcode: 'user-inquirylist',
      website: false,
    },
  },
  {
    path: '/user/inquiryfrom',
    name: 'user-inquiryfrom',
    component: () => import('@/views/user/inquiryfrom.vue'),
    meta: {
      title: '新材网-报价单',
      stcode: 'user-inquirylist',
      website: false,
    },
  },
  {
    path: '/user/quotationlist',
    name: 'user-quotationlist',
    component: () => import('@/views/user/quotationlist.vue'),
    meta: {
      title: '新材网-询价单',
      stcode: 'user-quotationlist',
      website: false,
    },
  },
  {
    path: '/user/quotationfrom',
    name: 'user-quotationfrom',
    component: () => import('@/views/user/quotationfrom.vue'),
    meta: {
      title: '新材网-询价单',
      stcode: 'user-quotationlist',
      website: false,
    },
  },
  {
    path: '/user/editpwd',
    name: 'user-editpwd',
    component: () => import('@/views/user/editpwd.vue'),
    meta: {
      title: '新材网-改密码',
      stcode: 'user-editpwd',
      website: false,
    },
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/home',
  },
  {
    path: '/user/:pathMatch(.*)*',
    redirect: '/user/index',
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  // 根据路由元信息设置文档标题
  window.document.title = (to.meta.title as string) || ''

  if (useHeaderStore) {
    const headerStore = useHeaderStore()
    headerStore.setSelectedTab(to.meta.stcode as string)
    window.localStorage.setItem('selectedTab', to.meta.stcode as string)
    window.localStorage.setItem('selectedName', to.path as string)
  }

  next()
})

export default router
