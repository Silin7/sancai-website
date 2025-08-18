import router from '@/router'
import backToTop from './backToTop'

function pageJump(name: any) {
  backToTop()
  router.push({
    name,
  })
}

export default pageJump
