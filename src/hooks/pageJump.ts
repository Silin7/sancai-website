import router from '@/router'

function pageJump(name: any) {
  router.push({
    name,
  })
}

export default pageJump
