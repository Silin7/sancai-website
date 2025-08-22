function windowOpen(url: any, istourl: boolean = true) {
  console.log('windowOpen-------->', url, istourl)
  if (!url || !istourl) {
    return
  }
  window.open(url, '_blank')
}

export default windowOpen
