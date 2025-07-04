<script lang="ts" setup>
import { ref } from 'vue'

const expandState: any = ref(true)
const unitList: any = ref([
  { title: '汇宇建筑' },
  { title: '城科集团' },
  { title: '住建研究院' },
  { title: '绿建科技' },
  { title: '生态城市联盟' },
  { title: '智慧城市协会' },
  { title: '数字建造中心' },
  { title: '未来城市实验室' },
  { title: '现代筑建集团' },
])

function expandfunc() {
  if (expandState.value) {
    document.getElementById('content').classList.add('boxanimating2')
    document.getElementById('content').classList.remove('boxanimating1')
    expandState.value = !expandState.value
  } else {
    document.getElementById('content').classList.add('boxanimating1')
    document.getElementById('content').classList.remove('boxanimating2')
    expandState.value = !expandState.value
  }
}
</script>

<template>
  <div class="sideleft">
    <div class="thankstop" @click="expandfunc">
      <div class="thanksunit">
        <i class="fa fa-handshake-o" style="font-size: 18px; color: #165dff"></i>
        <span>鸣谢单位</span>
      </div>
      <i v-if="!expandState" class="fa fa-angle-up" style="font-size: 20px; color: #374151"></i>
      <i v-else class="fa fa-angle-down" style="font-size: 20px; color: #374151"></i>
    </div>
    <div id="content">
      <div v-if="expandState" class="scrollbox">
        <vue3-seamless-scroll
          hover-stop="true"
          :list="unitList"
          :hover="true"
          :step="0.5"
          :limitScrollNum="4"
        >
          <div v-for="(item, index) in unitList" :key="index" class="unititem">
            <i class="fa fa-building-o" style="font-size: 16px; color: #165dff"></i>
            <span>{{ item.title }}</span>
          </div>
        </vue3-seamless-scroll>
      </div>
      <div v-if="expandState" class="foldpanel frcc" @click="expandfunc">
        <i class="fa fa-angle-double-left" style="font-size: 14px; color: #165dff"></i>
        <span>收起面板</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.sideleft {
  position: fixed;
  left: 20px;
  bottom: 20vh;
  z-index: 9999;
  width: 188px;
  border-radius: 12px;
  background-color: #fff;
  box-shadow: 0 10px 10px -3px rgb(0 0 0 / 0.1);
  overflow: hidden;

  .thankstop {
    cursor: pointer;
    padding: 8px 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    line-height: 36px;
    background-color: #f3f7ff;

    .thanksunit {
      color: #012060;

      span {
        margin-left: 8px;
        font-size: 20px;
        font-weight: 700;
      }
    }
  }

  #content {
    height: 348px;
    overflow: hidden;
  }

  .boxanimating1 {
    animation: expandCollapse1 1s ease-in-out forwards; /* 应用动画并保持结束状态 */
  }

  .boxanimating2 {
    animation: expandCollapse2 1s ease-in-out forwards; /* 应用动画并保持结束状态 */
  }

  @keyframes expandCollapse1 {
    from {
      height: 0px;
    }
    to {
      height: 348px;
    }
  }

  @keyframes expandCollapse2 {
    from {
      height: 348px;
    }
    to {
      height: 0px;
    }
  }

  .scrollbox {
    padding: 8px;
    height: 300px;
    overflow: hidden;

    .unititem {
      margin: 6px 0;
      padding-left: 12px;
      height: 38px;
      display: flex;
      align-items: center;
      border-radius: 6px;
      color: #012060;
      border: 1px solid #f3f4f6;
      box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);

      span {
        display: inline-block;
        margin-left: 8px;
        font-size: 16px;
      }
    }
  }

  .foldpanel {
    height: 32px;
    background-color: #f3f7ff;

    span {
      margin-left: 4px;
      font-size: 14px;
      color: #165dff;
    }
  }

  .foldpanel:hover {
    cursor: pointer;
    background-color: #e7eeff;
  }
}
</style>
