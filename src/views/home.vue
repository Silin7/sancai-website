<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
// import backToTop from '@/hooks/backToTop'
// import sideleft from '@/components/sideleft.vue'
// import sideright from '@/components/sideright.vue'

const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
})
</script>

<template>
  <div>
    <!-- <component :is="sideleft" ref="sideleftRef" /> -->
    <!-- <component :is="sideright" ref="siderightRef" @goTopCallback="backToTop" /> -->
    <div class="homePage">
      <!-- BANNER -->
      <div class="bannerBox">
        <div class="bannerAnchor">
          <img
            v-if="windowWidth > 1140"
            src="@/assets/index_img_01.png"
            alt="banner"
            class="bannerImage"
          />
          <div class="bannerAbsolute">
            <div class="bannerContent">
              <div class="bannerTitle">聚焦新型城市基础设施建设再起航</div>
              <div class="bannerSubtitle">绿色化 数字化 智能化</div>
              <!-- <div class="frsc">
              <button class="bannerJgkbtn">价格库</button>
              <button class="bannerJjfabtn">
                解决方案 <i class="fa fa-arrow-right" style="margin-left: 0.5rem"></i>
              </button>
            </div> -->
              <div class="bannerCompany">杭州三才工程管理咨询有限公司</div>
              <div class="bannerGridbox">
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-database" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">人材机信价格库</div>
                    <div class="bannerGridinfo">精准数据，助力成本管控</div>
                  </div>
                </div>
                <div v-if="windowWidth > 600" class="bannerGridshu" />
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-calculator" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">数据方案组价</div>
                    <div class="bannerGridinfo">智能组价，优化方案设计</div>
                  </div>
                </div>
                <div v-if="windowWidth > 600" class="bannerGridshu" />
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-android" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">人工智能应用</div>
                    <div class="bannerGridinfo">AI赋能，提升运行效率</div>
                  </div>
                </div>
                <div v-if="windowWidth > 600" class="bannerGridshu" />
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-play-circle" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">视频演示</div>
                    <div class="bannerGridinfo">直观教学，掌握核心技能</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 系统简介 -->
      <div class="featuresBox outmostPd">
        <img src="@/assets/about00.jpeg" class="featuresImg" />
        <div class="featuresFlex">
          <div class="featuresImgTitle">系统简介</div>
          <div class="featuresRounded">
            <div class="featuresRoundedItem">
              <div class="featuresRoundedTop">
                <div class="featuresRoundedShu"></div>
                <div class="featuresRoundedTitle">创建背景</div>
              </div>
              <div class="featuresRoundedInfo1">
                当前，建筑行业正在以科技创新推动现代化转型，新一代绿色化智能化建筑材料构筑新质生产力，逐步成为推动建筑业高质量发展的重要力量之一。
              </div>
              <div class="featuresRoundedInfo2">
                尤其在
                "双碳背景和新型工业化建筑"发展模式下，需求拉动供给的同时，创新供给也创造了新需求，市场供需将发生显著变化。
              </div>
            </div>
            <div class="featuresRoundedItem">
              <div class="featuresRoundedTop">
                <div class="featuresRoundedShu"></div>
                <div class="featuresRoundedTitle">应用对象</div>
              </div>
              <div class="featuresRoundedInfo2">
                新材网价格查询系统，竭诚为货物采购单位和其他有关单位提供丰富的
                "原料"信息及其市场价格，供有关单位实施货物采购和预测工程费用参考。
              </div>
            </div>
            <div class="featuresRoundedItem">
              <div class="featuresRoundedTop">
                <div class="featuresRoundedShu"></div>
                <div class="featuresRoundedTitle">涵盖范围</div>
              </div>
              <div class="featuresRoundedInfo1">
                价格查询系统信息涵盖新技术、新材料、新工艺、新服务和造价新型要素（例如，AI、BIM、IoT、GIS、DT、VR/AR、倾斜摄影和三维扫描融合应用）。
              </div>
              <div class="featuresRoundedInfo2">
                适用于绿色低碳、数字智能等高科技含量的新兴业态，以及持续提升城市基础设施韧性和既有建筑更新改造新时代"好房子"
                的建造需求。
              </div>
            </div>
            <div class="featuresRoundedItem" style="margin-bottom: 0">
              <div class="featuresRoundedTop">
                <div class="featuresRoundedShu"></div>
                <div class="featuresRoundedTitle">系统创建</div>
              </div>
              <div class="featuresRoundedInfo2">
                本系统由
                "杭州三才工程管理咨询有限公司"创建，应用过程中如有建议，请联系我们，以便进行完善。
              </div>
            </div>
          </div>
        </div>
        <div style="opacity: 0" class="featuresImgTitle">系统简介</div>
        <div style="opacity: 0" class="featuresRounded">
          <div class="featuresRoundedItem">
            <div class="featuresRoundedTop">
              <div class="featuresRoundedShu"></div>
              <div class="featuresRoundedTitle">创建背景</div>
            </div>
            <div class="featuresRoundedInfo1">
              当前，建筑行业正在以科技创新推动现代化转型，新一代绿色化智能化建筑材料构筑新质生产力，逐步成为推动建筑业高质量发展的重要力量之一。
            </div>
            <div class="featuresRoundedInfo2">
              尤其在 "双碳背景和新型工业化建筑"
              发展模式下，需求拉动供给的同时，创新供给也创造了新需求，市场供需将发生显著变化。
            </div>
          </div>
          <div class="featuresRoundedItem">
            <div class="featuresRoundedTop">
              <div class="featuresRoundedShu"></div>
              <div class="featuresRoundedTitle">应用对象</div>
            </div>
            <div class="featuresRoundedInfo2">
              新材网价格查询系统，竭诚为货物采购单位和其他有关单位提供丰富的 "原料"
              信息及其市场价格，供有关单位实施货物采购和预测工程费用参考。
            </div>
          </div>
          <div class="featuresRoundedItem">
            <div class="featuresRoundedTop">
              <div class="featuresRoundedShu"></div>
              <div class="featuresRoundedTitle">涵盖范围</div>
            </div>
            <div class="featuresRoundedInfo1">
              价格查询系统信息涵盖新技术、新材料、新工艺、新服务和造价新型要素（例如，AI、BIM、IoT、GIS、DT、VR/AR、倾斜摄影和三维扫描融合应用）。
            </div>
            <div class="featuresRoundedInfo2">
              适用于绿色低碳、数字智能等高科技含量的新兴业态，以及持续提升城市基础设施韧性和既有建筑更新改造新时代
              "好房子" 的建造需求。
            </div>
          </div>
          <div class="featuresRoundedItem" style="margin-bottom: 0">
            <div class="featuresRoundedTop">
              <div class="featuresRoundedShu"></div>
              <div class="featuresRoundedTitle">系统创建</div>
            </div>
            <div class="featuresRoundedInfo2">
              本系统由 "杭州三才工程管理咨询有限公司"
              创建，应用过程中如有建议，请联系我们，以便进行完善。
            </div>
          </div>
        </div>
      </div>
      <!-- 人材机信价格库 -->
      <div class="containerBox outmostPd">
        <div class="containerTitle">人材机信价格库</div>
        <div class="containerHeng"></div>
        <div class="containerInfo">
          <!-- 专注于新型城市基础设施建设的人材机信资源价格数据库，为行业提供精准的成本管控信息 -->
        </div>
        <div class="containerSubBoxOut">
          <div class="containerSubBox1">
            <div class="containerSubItem containerActive">数字技工/方案论证</div>
            <div class="containerSubItem">材料/设备</div>
            <div class="containerSubItem">智能建造装备</div>
            <div class="containerSubItem">信息化产品/服务</div>
          </div>
        </div>
        <div class="containerGridbox">
          <img src="@/assets/product01.jpeg" alt="" />
          <div class="containerGridMaod">
            <div class="containerGridBox">
              <div class="containerGridItem">
                <i
                  class="fa fa-user"
                  style="font-size: 1.25rem; color: #165dff; margin-right: 0.75rem"
                ></i>
                <div class="containerGridimginfo">数字技工/方案论证</div>
              </div>
              <div class="containerGridItem">
                <i
                  class="fa fa-dot-circle-o"
                  style="font-size: 1.25rem; color: #165dff; margin-right: 0.75rem"
                ></i>
                <div class="containerGridimginfo">数字技工/方案论证</div>
              </div>
              <div class="containerGridItem">
                <i
                  class="fa fa-sitemap"
                  style="font-size: 1.25rem; color: #165dff; margin-right: 0.75rem"
                ></i>
                <div class="containerGridimginfo">数字技工/方案论证</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 数字化解决方案 -->
      <div class="solutionsBox">
        <div class="solutionsCotent outmostPd">
          <div class="solutionsTitle">数字化解决方案</div>
          <div class="solutionsHeng"></div>
          <div class="solutionsInfo">
            <!-- 探索我们的数字化应用与智慧化管理方案，为您的项目提供全方位的技术支持 -->
          </div>
          <div class="solutionsSubBoxOut">
            <div class="solutionsSubBox1">
              <div class="solutionsSubItem solutionsActive">数字化应用方案</div>
              <div class="solutionsSubItem">智慧化管理方案</div>
            </div>
          </div>
          <div class="solutionsSubBoxOut">
            <div class="solutionsSubBox2">
              <div class="solutionsSubItem solutionsActive">BIM+工程造价</div>
              <div class="solutionsSubItem">BIM+倾斜摄影</div>
              <div class="solutionsSubItem">BIM+三维扫描</div>
              <div class="solutionsSubItem">BIM+VR/AR</div>
              <div class="solutionsSubItem">BIM+物联网</div>
              <div class="solutionsSubItem">BIM+数字化加工</div>
              <div class="solutionsSubItem">BIM+地理信息</div>
              <div class="solutionsSubItem">BIM+放样机器人</div>
              <div class="solutionsSubItem">BIM+空间资产</div>
            </div>
          </div>
          <div class="solutionsImg">
            <img src="@/assets/case/fangyang.jpg" alt="banner" style="width: 100%; height: 48rem" />
            <div class="solutionsImgTitleMoud">
              <div class="solutionsImgTitle1">精准定位 自动放样 施工指导</div>
              <div class="solutionsImgTitle2">BIM+放样机器人</div>
              <div class="solutionsImgTitle3">施工精度 效率提升 质量保障</div>
            </div>
            <div class="solutionsImgInfo">
              <p>
                通过BIM技术实现工程造价的精准计算与动态管理，提高成本控制能力，减少预算超支风险，为项目全生命周期成本管理提供数据支撑。
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- 人工智能应用 -->
      <div class="aiBox outmostPd">
        <div class="aiTitle">人工智能应用</div>
        <div class="aiHeng"></div>
        <div class="aiInfo">
          <!-- 以数据、算法和算力为核心要素，驱动工程设计、工程施工和运营维护多维度创新应用，为产业转型发展注入新动能 -->
        </div>
        <div class="aiSubbox">
          <div class="aiFabox frcc">
            <i class="fa fa-cogs" style="font-size: 1.25rem; color: #165dff"></i>
          </div>
          <div class="aiSubtitle">工程管理AI应用组价</div>
        </div>
        <div class="aiClassbox">
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-pencil" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">智能化设计</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-wrench" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">辅助设计工具</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-android" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">建筑机器人</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-tasks" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">施工管理</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-check-square" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">辅助质量控制</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-sliders" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">智能化控制</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-bolt" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">能源管理</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-expand" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">场景拓展</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa frcc">
              <i class="fa fa-random" style="font-size: 1.5rem; color: #165dff"></i>
            </div>
            <div class="aiClassitemtext">跨界融合</div>
          </div>
        </div>
        <div class="aiSubbox">
          <div class="aiFabox2 frcc">
            <i class="fa fa-calculator" style="font-size: 1.25rem; color: #722ed1"></i>
          </div>
          <div class="aiSubtitle">工程管理AI应用组价</div>
        </div>
        <div class="aiClassbox">
          <div class="aiClassitem">
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-pencil" style="font-size: 1.5rem; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能复核文本</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-wrench" style="font-size: 1.5rem; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能检测漏项</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-android" style="font-size: 1.5rem; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能预警偏离</div>
          </div>
          <div class="aiClassitem">
            <div class="aiClassitemfa2 frcc">
              <i class="fa fa-tasks" style="font-size: 1.5rem; color: #722ed1"></i>
            </div>
            <div class="aiClassitemtext">智能分析指标</div>
          </div>
        </div>
      </div>
      <!-- 鸣谢单位  -->
      <div class="mxBox">
        <div class="mxContent outmostPd">
          <div class="mxTitle">鸣谢单位</div>
          <div class="mxHeng"></div>
          <div class="mxInfo">感谢以下单位对本平台的大力支持与合作</div>
          <div class="mxClassbox">
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=402" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">建筑科技有限公司</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=403" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">智能建造研究院</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=404" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">绿色建材协会</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=405" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">数字工程设计院</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=406" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">智慧城市科技</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=407" alt="" class="mxClassitemfa" />
              <div class="pyClassitemtext">建筑信息研究院</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=402" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">建筑科技有限公司</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=403" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">智能建造研究院</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=404" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">绿色建材协会</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=405" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">数字工程设计院</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=406" alt="" class="mxClassitemfa" />
              <div class="mxClassitemtext">智慧城市科技</div>
            </div>
            <div class="mxClassitem">
              <img src="https://picsum.photos/100/100?random=407" alt="" class="mxClassitemfa" />
              <div class="pyClassitemtext">建筑信息研究院</div>
            </div>
          </div>
        </div>
      </div>
      <!-- 友情链接  -->
      <div class="pyBox outmostPd">
        <div class="pyTitle">友情链接</div>
        <div class="pyHeng"></div>
        <div class="pyInfo">
          <!-- 与行业领先企业及机构建立合作，共同推动建筑行业数字化转型 -->
        </div>
        <div class="pyClassbox">
          <div class="pyClassitem">
            <img src="https://picsum.photos/100/100?random=402" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">建筑科技有限公司</div>
            <div class="pyClassiteminfo">专注建筑科技创新</div>
          </div>
          <div class="pyClassitem">
            <img src="https://picsum.photos/100/100?random=403" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">智能建造研究院</div>
            <div class="pyClassiteminfo">建筑智能化研究</div>
          </div>
          <div class="pyClassitem">
            <img src="https://picsum.photos/100/100?random=404" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">绿色建材协会</div>
            <div class="pyClassiteminfo">推广绿色建筑材料</div>
          </div>
          <div class="pyClassitem">
            <img src="https://picsum.photos/100/100?random=405" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">数字工程设计院</div>
            <div class="pyClassiteminfo">数字化工程设计</div>
          </div>
          <div class="pyClassitem">
            <img src="https://picsum.photos/100/100?random=406" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">智慧城市科技</div>
            <div class="pyClassiteminfo">智慧城市解决方案</div>
          </div>
          <div class="pyClassitem">
            <img src="https://picsum.photos/100/100?random=407" alt="" class="pyClassitemfa" />
            <div class="pyClassitemtext">建筑信息研究院</div>
            <div class="pyClassiteminfo">建筑信息研究应用</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.homePage {
  background-color: #f9fafb;
  overflow-x: hidden;

  .bannerBox {
    width: 100vw;
    height: 100%;
    background-color: #012060;

    .bannerAnchor {
      margin: 0 auto;
      position: relative;
      width: 100%;
      height: 48rem;
      max-width: 1536px;

      .bannerImage {
        position: absolute;
        right: 10%;
        top: 0;
        z-index: 0;
        width: auto;
        max-width: 50%;
        height: 100%;
        object-fit: contain;
      }

      .bannerAbsolute {
        padding-top: 10rem;
        position: absolute;
        width: 100%;
        z-index: 1;

        .bannerContent {
          margin: 0 auto;
          padding: 0 30px;
          width: 100%;
          max-width: 1536px;

          .bannerTitle {
            margin-bottom: 1.5rem;
            font-size: clamp(2rem, 5vw, 3.5rem);
            color: #fff;
            font-weight: 700;
          }

          .bannerSubtitle {
            margin-bottom: 2rem;
            font-size: clamp(2rem, 3vw, 1.5rem);
            line-height: 3rem;
            font-weight: 500;
            color: rgb(255 255 255 / 0.9);
          }

          .bannerJgkbtn {
            padding: 0.75rem 2rem;
            color: #fff;
            background-color: rgb(22 93 255);
            border-radius: 9999px;
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          }

          .bannerJjfabtn {
            margin-left: 20px;
            padding: 0.75rem 2rem;
            color: #fff;
            background-color: rgba(255 255 255 / 0.1);
            border: 1px solid rgba(255 255 255 / 0.3);
            border-radius: 9999px;
          }

          .bannerCompany {
            margin-top: 80px;
            font-size: 1.25rem;
            line-height: 1.25rem;
            color: rgba(255 255 255 / 0.7);
          }

          .bannerGridbox {
            overflow: hidden;
            margin-top: 2rem;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(103, 188, 255, 0.3);
            border-radius: 1rem;

            .bannerGriditem {
              padding: 1.5rem;
              display: flex;

              .bannerFabox {
                width: 3rem;
                height: 3rem;
                background-color: rgb(22 93 255 / 0.1);
                border-radius: 0.5rem;
              }

              .bannerGridright {
                margin-left: 1rem;

                .bannerGridtitle {
                  margin-bottom: 0.5rem;
                  font-size: 1.25rem;
                  line-height: 1.75rem;
                  font-weight: 700;
                  color: #fff;
                }

                .bannerGridinfo {
                  font-size: 1rem;
                  line-height: 1.5rem;
                  color: rgba(255 255 255 / 0.8);
                }
              }
            }

            .bannerGriditem:hover {
              cursor: pointer;
              box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
              animation: jumpUpwards 300ms ease-in-out forwards;
            }

            @media (min-width: 1140px) {
              .bannerGriditem {
                width: calc(25% - 1px);
              }
            }

            @media (max-width: 1140px) and (min-width: 600px) {
              .bannerGriditem {
                width: calc(50% - 1px);
              }
            }

            @media (max-width: 600px) {
              .bannerGriditem {
                width: 100%;
              }
            }

            .bannerGridshu {
              width: 1px;
              height: 5rem;
              background-image: linear-gradient(to bottom, #1627ff30);
            }
          }
        }
      }
    }

    @media (max-width: 600px) {
      height: 60rem;
    }
  }

  .featuresBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 2rem;
    width: 100%;
    max-width: 1536px;

    .featuresImg {
      position: absolute;
      top: 0;
      left: 2rem;
      z-index: 0;
      width: 100%;
      width: calc(100% - 4rem);
      height: 500px;
      border-radius: 1rem;
      opacity: 0.5;
    }

    @media (max-width: 1140px) {
      .featuresImg {
        width: calc(100% - 2rem);
        left: 1rem;
      }
    }

    .featuresFlex {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
      padding: 0 2rem;
    }

    @media (max-width: 1140px) {
      .featuresFlex {
        padding: 0 1rem;
      }
    }

    .featuresImgTitle {
      padding: 2rem 0;
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      line-height: 60px;
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .featuresRounded {
      margin: 0 auto;
      padding: 2.5rem;
      width: 90%;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      border-radius: 1rem;
      box-sizing:
        0 10px 15px -3px rgb(0 0 0 / 0.1),
        0 4px 6px -4px rgb(0 0 0 / 0.1);
      background-color: rgb(255 255 255 / 0.5);

      .featuresRoundedItem {
        margin-bottom: 2.5rem;
        width: 100%;

        .featuresRoundedTop {
          display: flex;
          margin-bottom: 1.5rem;

          .featuresRoundedShu {
            width: 0.5rem;
            height: 2rem;
            background-color: #165dff;
            border-radius: 0.25rem;
          }

          .featuresRoundedTitle {
            padding-left: 2rem;
            font-size: 1.5rem;
            line-height: 2rem;
            font-weight: 700;
            color: rgb(1 32 96);
          }
        }

        .featuresRoundedInfo1 {
          margin-bottom: 1rem;
          font-size: 1.25rem;
          color: rgb(75 85 99);
        }

        .featuresRoundedInfo2 {
          font-size: 1.25rem;
          color: rgb(75 85 99);
        }
      }
    }

    @media (max-width: 600px) {
      .featuresRounded {
        padding-left: 1rem;
        padding-right: 1rem;
      }
    }
  }

  .containerBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 2rem;
    width: 100%;
    max-width: 1536px;

    .containerTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .containerHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .containerInfo {
      margin: 1rem auto 0;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .containerSubBoxOut {
      padding-bottom: 1rem;
      display: flex;
      justify-content: center;

      .containerSubBox1 {
        padding-bottom: 1rem;
        overflow-x: auto;
        display: flex;
        flex-wrap: nowrap;

        .containerSubItem {
          flex-shrink: 0;
          margin: 0 0.75rem;
          line-height: 2rem;
          color: rgb(1 32 96);
          padding: 0.5rem 1.25rem;
          border-radius: 0.5rem;
          background-color: #fff;
        }

        .containerSubItem:hover {
          cursor: pointer;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          background-color: rgb(243 244 246);
        }
      }

      .containerActive {
        color: #fff !important;
        background-color: #165dff !important;
      }
    }

    .containerGridbox {
      position: relative;
      box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

      img {
        width: 100%;
        height: 38rem;
        border-radius: 1rem;
      }

      .containerGridMaod {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        padding: 2rem 2rem 1rem 2rem;
        border-radius: 1rem 1rem 0 0;
        background-color: rgb(1 32 96 / 0.4);

        .containerGridBox {
          display: flex;
          flex-wrap: wrap;

          .containerGridItem {
            margin: 0 1rem 1rem 0;
            cursor: pointer;
            display: flex;
            align-items: center;
            padding: 0.75rem;
            border-radius: 0.5rem;

            .containerGridimginfo {
              font-size: 1.25rem;
              line-height: 2rem;
              font-weight: 500;
              color: #fff;
            }
          }

          .containerGridItem:hover {
            background-color: rgb(255 255 255 / 0.1);
          }

          @media (max-width: 600px) {
            .containerGridItem {
              width: 100%;
              margin-right: 0;
            }
          }
        }
      }
    }
  }

  .solutionsBox {
    margin: 6rem auto 0;
    padding: 2.5rem;
    width: 100%;
    background-color: rgb(240 247 255 / 1);

    .solutionsCotent {
      margin: 0 auto;
      position: relative;
      padding: 0 2rem;
      width: 100%;
      max-width: 1536px;

      .solutionsTitle {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 700;
        text-align: center;
        color: rgb(1 32 96);
      }

      .solutionsHeng {
        margin: 1rem auto 0;
        width: 5rem;
        height: 0.25rem;
        border-radius: 9999px;
        background-color: rgb(22 93 255);
      }

      .solutionsInfo {
        margin: 1rem auto 2.5rem;
        text-align: center;
        max-width: 42rem;
        color: rgb(75 85 99);
      }

      .solutionsSubBoxOut {
        padding-bottom: 2rem;
        display: flex;
        justify-content: center;

        .solutionsSubBox1 {
          padding-bottom: 1rem;
          overflow-x: auto;
          display: flex;
          flex-wrap: nowrap;

          .solutionsSubItem {
            flex-shrink: 0;
            margin: 0 0.75rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            padding: 0.5rem 1.25rem;
            border-radius: 0.5rem;
            background-color: #fff;
          }

          .solutionsSubItem:hover {
            cursor: pointer;
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            background-color: rgb(243 244 246);
          }
        }

        .solutionsSubBox2 {
          padding-bottom: 1rem;
          overflow-x: auto;
          display: flex;
          flex-wrap: nowrap;

          .solutionsSubItem {
            flex-shrink: 0;
            margin: 0 0.75rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            padding: 0.5rem 1.25rem;
            border-radius: 0.5rem;
            background-color: #fff;
          }

          .solutionsSubItem:hover {
            cursor: pointer;
            box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
            background-color: rgb(243 244 246);
          }
        }

        .solutionsActive {
          color: #fff !important;
          background-color: #165dff !important;
        }
      }

      .solutionsImg {
        overflow: hidden;
        position: relative;
        width: 100%;
        height: 48rem;
        border-radius: 1rem;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);

        .solutionsImgTitleMoud {
          position: absolute;
          top: 45px;
          left: 0;
          z-index: 2;
          width: 100%;

          .solutionsImgTitle1 {
            margin-bottom: 1rem;
            font-size: 1.5rem;
            line-height: 2rem;
            font-weight: 500;
            text-align: center;
            color: rgb(1 32 96);
          }

          .solutionsImgTitle2 {
            margin-bottom: 1.25rem;
            font-size: 2.25rem;
            line-height: 2.5rem;
            font-weight: 700;
            text-align: center;
            color: rgb(1 32 96);
          }

          .solutionsImgTitle3 {
            font-size: 1.25rem;
            line-height: 1.75rem;
            opacity: 0.9;
            text-align: center;
            color: rgb(1 32 96);
          }
        }

        .solutionsImgInfo {
          position: absolute;
          bottom: 0;
          left: 0;
          z-index: 2;
          width: 100%;
          padding: 2.5rem;
          border-top: 1px solid rgb(229 231 235);
          background-color: rgb(255 255 255 / 0.8);

          p {
            text-align: center;
            margin: 0;
            line-height: 1.5rem;
            color: rgb(1 32 96);
          }
        }
      }
    }
  }

  .aiBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 2rem;
    width: 100%;
    max-width: 1536px;

    .aiTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .aiHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .aiInfo {
      margin: 1rem auto 2.5rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .aiSubbox {
      margin-bottom: 2rem;
      display: flex;
      align-items: center;

      .aiFabox {
        margin-right: 1rem;
        width: 3rem;
        height: 3rem;
        background-color: rgba(22 93 255 / 0.1);
        border-radius: 9999px;
      }

      .aiFabox2 {
        margin-right: 1rem;
        width: 3rem;
        height: 3rem;
        background-color: rgb(114 46 209 / 0.1);
        border-radius: 9999px;
      }

      .aiSubtitle {
        font-size: 1.5rem;
        line-height: 2rem;
        font-weight: 700;
        color: rgb(1 32 96);
      }
    }

    .aiClassbox {
      margin-bottom: 2.5rem;
      width: calc(100% + 1.5rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .aiClassitem {
        margin: 0 1.5rem 1.5rem 0;
        padding: 1.25rem;
        width: calc(33.3% - 1.5rem);
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        border-radius: 0.75rem;

        .aiClassitemfa {
          margin-bottom: 1rem;
          width: 4rem;
          height: 4rem;
          border-radius: 9999px;
          background-color: rgb(22 93 255 / 0.1);
        }

        .aiClassitemfa2 {
          margin-bottom: 1rem;
          width: 4rem;
          height: 4rem;
          border-radius: 9999px;
          background-color: rgb(114 46 209 / 0.1);
        }

        .aiClassitemtext {
          line-height: 1.5rem;
          font-weight: 500;
          color: rgb(1 32 96);
        }
      }

      @media (max-width: 600px) {
        .aiClassitem {
          width: calc(50% - 1.5rem);
        }
      }

      .aiClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }

  .mxBox {
    margin: 6rem auto 0;
    padding: 2.5rem;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.5);
    background-image: url('../assets/about00.jpg');

    .mxContent {
      margin: 0 auto;
      position: relative;
      padding: 0 2rem;
      width: 100%;
      max-width: 1536px;

      .mxTitle {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 700;
        text-align: center;
        color: rgb(1 32 96);
      }

      .mxHeng {
        margin: 1rem auto 0;
        width: 5rem;
        height: 0.25rem;
        border-radius: 9999px;
        background-color: rgb(22 93 255);
      }

      .mxInfo {
        margin: 1rem auto 2.5rem;
        text-align: center;
        max-width: 42rem;
        color: rgb(75 85 99);
      }

      .mxClassbox {
        width: calc(100% + 1.5rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;

        .mxClassitem {
          margin: 0 1.5rem 1.5rem 0;
          padding: 1.25rem;
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: #fff;
          // background-color: rgb(249 250 251);
          border-radius: 0.75rem;

          .mxClassitemfa {
            margin-bottom: 1rem;
            padding: 0.25rem;
            width: 5rem;
            height: 5rem;
            border-radius: 9999px;
            border: 2px solid rgb(22 93 255 / 0.2);
          }

          .mxClassitemfa2 {
            margin-bottom: 1rem;
            width: 5rem;
            height: 5rem;
            border-radius: 9999px;
            background-color: rgb(114 46 209 / 0.1);
          }

          .mxClassitemtext {
            line-height: 1.5rem;
            font-weight: 500;
            text-align: center;
            color: rgb(1 32 96);
          }

          .mxClassiteminfo {
            margin-top: 0.5rem;
            font-size: 0.875rem;
            line-height: 1.25rem;
            text-align: center;
            color: #6b7280;
          }
        }

        @media (min-width: 1140px) {
          .mxClassitem {
            width: calc(16.6% - 1.5rem);
          }
        }

        @media (max-width: 1140px) and (min-width: 600px) {
          .mxClassitem {
            width: calc(33.3% - 1.5rem);
          }
        }

        @media (max-width: 600px) {
          .mxClassitem {
            width: calc(50% - 1.5rem);
          }
        }

        .mxClassitem:hover {
          cursor: pointer;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }
    }
  }

  .pyBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 2rem 4rem;
    width: 100%;
    max-width: 1536px;

    .pyTitle {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      text-align: center;
      color: rgb(1 32 96);
    }

    .pyHeng {
      margin: 1rem auto 0;
      width: 5rem;
      height: 0.25rem;
      border-radius: 9999px;
      background-color: rgb(22 93 255);
    }

    .pyInfo {
      margin: 1rem auto 2.5rem;
      text-align: center;
      max-width: 42rem;
      color: rgb(75 85 99);
    }

    .pyClassbox {
      width: calc(100% + 1.5rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .pyClassitem {
        margin: 0 1.5rem 1.5rem 0;
        padding: 1.25rem;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        // background-color: rgb(249 250 251);
        border-radius: 0.75rem;

        .pyClassitemfa1 {
          margin-bottom: 1rem;
          padding: 0.25rem;
          width: 5rem;
          height: 5rem;
          border-radius: 9999px;
          border: 2px solid rgb(22 93 255 / 0.2);
        }

        .pyClassitemfa {
          margin-bottom: 1rem;
          width: 5rem;
          height: 5rem;
          border-radius: 9999px;
          background-color: rgb(114 46 209 / 0.1);
        }

        .pyClassitemtext {
          line-height: 1.5rem;
          font-weight: 500;
          text-align: center;
          color: rgb(1 32 96);
        }

        .pyClassiteminfo {
          margin-top: 0.5rem;
          font-size: 0.875rem;
          line-height: 1.25rem;
          text-align: center;
          color: #6b7280;
        }
      }

      @media (min-width: 1140px) {
        .pyClassitem {
          width: calc(16.6% - 1.5rem);
        }
      }

      @media (max-width: 1140px) and (min-width: 600px) {
        .pyClassitem {
          width: calc(33.3% - 1.5rem);
        }
      }

      @media (max-width: 600px) {
        .pyClassitem {
          width: calc(50% - 1.5rem);
        }
      }

      .pyClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }

  @media (max-width: 600px) {
    .solutionsBox {
      padding: 2.5rem 0;
    }

    .mxBox {
      padding: 2.5rem 0;
    }
  }

  @media (max-width: 1140px) {
    .outmostPd {
      padding-left: 1rem !important;
      padding-right: 1rem !important;
    }
  }
}
</style>
