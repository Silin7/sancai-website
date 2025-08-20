function windowOpen(url: any) {
  if (!url) {
    return
  }
  window.open(url, '_blank')
}

export default windowOpen
