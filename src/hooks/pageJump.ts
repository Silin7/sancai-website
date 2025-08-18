import router from '@/router'
import backToTop from './backToTop'

function pageJump(name: any) {
  console.log('-------->', name)
  backToTop()
  router.push({
    name,
  })
}

export default pageJump
