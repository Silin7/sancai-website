import { defineStore } from 'pinia'
import { ref } from 'vue'

const useHeaderStore = defineStore('counter', () => {
  const selectedTab = ref(window.localStorage.getItem('selectedTab') || 'home')

  function setSelectedTab(name: string) {
    selectedTab.value = name
  }

  return { selectedTab, setSelectedTab }
})

export default useHeaderStore
