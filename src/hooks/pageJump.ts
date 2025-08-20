import router from '@/router'
import backToTop from './backToTop'

function pageJump(name: any, query?: any) {
  console.log('-------->', name)
  backToTop()
  router.push({
    name,
    query
  })
}

export default pageJump
