<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import backToTop from '@/hooks/backToTop'
// import sideleft from '@/components/sideleft.vue'
import sideright from '@/components/sideright.vue'

const windowWidth = ref(window.innerWidth)

function updateWindowWidth() {
  windowWidth.value = window.innerWidth
}

onMounted(() => {
  // headerStore.setSelectedTab('home')
  window.addEventListener('resize', updateWindowWidth)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateWindowWidth)
})
</script>

<template>
  <div>
    <!-- <component :is="sideleft" ref="sideleftRef" /> -->
    <component :is="sideright" ref="siderightRef" @goTopCallback="backToTop" />
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
              <div class="bannerSubtitle">
                <span>绿色化</span>
                <span>数字化</span>
                <span>智能化</span>
              </div>
              <!-- <div class="frsc">
              <button class="bannerJgkbtn">价格库</button>
              <button class="bannerJjfabtn">
                解决方案 <i class="fa fa-arrow-right" style="margin-left: 0.5rem"></i>
              </button>
            </div> -->
              <div class="bannerCompany">杭州三才-----------有限公司</div>
              <div class="bannerGridbox">
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-database" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">人材机信价格库</div>
                    <!-- <div class="bannerGridinfo">精准数据，助力成本管控</div> -->
                  </div>
                </div>
                <div v-if="windowWidth > 600" class="bannerGridshu" />
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-calculator" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">数据方案组价</div>
                    <!-- <div class="bannerGridinfo">智能组价，优化方案设计</div> -->
                  </div>
                </div>
                <div v-if="windowWidth > 600" class="bannerGridshu" />
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-android" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">人工智能应用</div>
                    <!-- <div class="bannerGridinfo">AI赋能，提升运行效率</div> -->
                  </div>
                </div>
                <div v-if="windowWidth > 600" class="bannerGridshu" />
                <div class="bannerGriditem">
                  <div class="bannerFabox frcc">
                    <i class="fa fa-play-circle" style="font-size: 1.25rem; color: #fff"></i>
                  </div>
                  <div class="bannerGridright">
                    <div class="bannerGridtitle">视频演示</div>
                    <!-- <div class="bannerGridinfo">直观教学，掌握核心技能</div> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 系统简介 -->
      <div class="featuresBox">
        <div class="featuresImgTitleBox">
          <img src="@/assets/index_about.jpg" class="featuresImg" />
          <div class="featuresImgTitle">
            <div class="featuresImgTitleCentent">系统简介</div>
          </div>
        </div>
        <div class="featuresContent">
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
                尤其在 “双碳背景和新型工业化建筑”
                发展模式下，需求拉动供给的同时，创新供给也创造了新需求，市场供需将发生显著变化，具有绿色化、集成化和智能化特征的新材料新产品与新服务，已逐步迈向市场，将极大地影响生产方式、建造成本和运行管理模式的创新。
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
            <div class="featuresRoundedItem" style="margin-bottom: 0">
              <div class="featuresRoundedTop">
                <div class="featuresRoundedShu"></div>
                <div class="featuresRoundedTitle">系统创建</div>
              </div>
              <div class="featuresRoundedInfo2">
                本系统由 “杭州三才-----------有限公司”
                创建，应用过程中如有建议，请联系我们，以便进行完善。
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 人材机信价格库 -->
      <div class="containerBox">
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
          <img src="@/assets/product02.jpeg" alt="" />
          <div class="containerGridMaod">
            <div class="containerGridContent">
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
        <div class="solutionsCotent">
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
            <img src="@/assets/case/fangyang.jpg" alt="banner" style="width: 100%; height: 44rem" />
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
      <div class="aiBox">
        <div class="aiContent">
          <div class="aiTitle">人工智能应用</div>
          <div class="aiHeng"></div>
          <div class="aiInfo">
            <!-- 以数据、算法和算力为核心要素，驱动工程设计、工程施工和运营维护多维度创新应用，为产业转型发展注入新动能 -->
          </div>
          <div class="aiSubbox">
            <div class="aiFabox frcc">
              <i class="fa fa-cogs"></i>
            </div>
            <div class="aiSubtitle">业务管理+AI赋能组价</div>
          </div>
          <div class="aiClassbox">
            <div class="aiClassitem">
              <div class="aiClassitemfa frcc">
                <i class="fa fa-paint-brush" style="font-size: 1.5rem; color: #165dff"></i>
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
                <i class="fa fa-arrows-alt" style="font-size: 1.5rem; color: #165dff"></i>
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
              <i class="fa fa-calculator"></i>
            </div>
            <div class="aiSubtitle">招标造价+AI应用服务</div>
          </div>
          <div class="aiClassbox">
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-check-circle" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能校核施工图</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-calculator" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能识别工程量与计算</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-line-chart" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能分析模型计量结果</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-sliders" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能管控动态成本</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-history" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">全过程造价数据追溯</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-file-text" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能生成招标文件</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-file-text-o" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能生成投标文件</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-balance-scale" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能对比投标响应程度</div>
            </div>
            <div class="aiClassitem">
              <div class="aiClassitemfa2 frcc">
                <i class="fa fa-list" style="font-size: 1.5rem; color: #722ed1"></i>
              </div>
              <div class="aiClassitemtext">智能生成评标分析表</div>
            </div>
          </div>
        </div>
      </div>
      <!-- 鸣谢单位  -->
      <div class="mxBox">
        <div class="mxContent">
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
      <div class="pyBox">
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
      max-width: 1536px;
      height: 44rem;
      @media (max-width: 600px) {
        height: 50rem;
      }

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
        position: absolute;
        z-index: 1;
        padding-top: 10rem;
        width: 100%;
        @media (max-width: 600px) {
          padding-top: 6rem;
        }

        .bannerContent {
          margin: 0 auto;
          padding: 2rem;
          width: 100%;
          max-width: 1536px;
          @media (max-width: 600px) {
            padding: 1rem;
          }

          .bannerTitle {
            margin-bottom: 1.5rem;
            font-size: clamp(1.8rem, 4vw, 3rem);
            color: #fff;
            font-weight: 700;
          }

          .bannerSubtitle {
            margin-bottom: 2rem;
            font-size: clamp(1.5rem, 4vw, 1.8rem);
            line-height: 3rem;
            font-weight: 500;
            color: rgb(255 255 255 / 0.9);

            span {
              margin-right: 2rem;
              @media (max-width: 600px) {
                margin-right: 1rem;
              }
            }

            span:last-child {
              margin-right: 0;
            }
          }

          // .bannerJgkbtn {
          //   padding: 0.75rem 2rem;
          //   color: #fff;
          //   background-color: rgb(22 93 255);
          //   border-radius: 9999px;
          //   box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          // }

          // .bannerJjfabtn {
          //   margin-left: 20px;
          //   padding: 0.75rem 2rem;
          //   color: #fff;
          //   background-color: rgba(255 255 255 / 0.1);
          //   border: 1px solid rgba(255 255 255 / 0.3);
          //   border-radius: 9999px;
          // }

          .bannerCompany {
            margin-top: 80px;
            font-size: 1.25rem;
            line-height: 1.25rem;
            color: rgba(255 255 255 / 0.7);
            @media (max-width: 600px) {
              margin-top: 50px;
            }
          }

          .bannerGridbox {
            overflow: hidden;
            margin-top: 1rem;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(103, 188, 255, 0.3);
            border-radius: 1rem;

            .bannerGriditem {
              padding: 1.5rem;
              display: flex;
              align-items: center;

              .bannerFabox {
                width: 3rem;
                height: 3rem;
                background-color: rgb(22 93 255 / 0.1);
                border-radius: 0.5rem;
              }

              .bannerGridright {
                margin-left: 1rem;

                .bannerGridtitle {
                  // margin-bottom: 0.5rem;
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
  }

  .featuresBox {
    margin: 20px auto 0;
    width: 100%;

    .featuresImgTitleBox {
      position: relative;
      height: 200px;
      display: flex;
      justify-content: center;

      .featuresImg {
        width: 100%;
        height: 200px;
      }

      .featuresImgTitle {
        position: absolute;
        bottom: 0;
        padding: 0 2rem;
        width: 100%;
        max-width: 1536px;
        height: 120px;
        @media (max-width: 600px) {
          padding: 0;
        }

        .featuresImgTitleCentent {
          margin: 0 auto;
          padding-left: 1.5rem;
          width: 90%;
          font-size: clamp(1.6rem, 4vw, 2.5rem);
          line-height: 120px;
          font-weight: 700;
          color: #fff;
          background-color: rgba(1, 98, 105, 0.5);
          @media (max-width: 600px) {
            width: calc(100% - 2rem);
          }
        }
      }
    }

    .featuresContent {
      margin: 0 auto;
      position: relative;
      padding: 0 2rem;
      width: 100%;
      max-width: 1536px;
      @media (max-width: 600px) {
        padding: 0;
      }

      .featuresRounded {
        margin: 0 auto;
        padding: 2.5rem;
        width: 90%;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        border-radius: 0 0 1rem 1rem;
        box-sizing:
          0 10px 15px -3px rgb(0 0 0 / 0.1),
          0 4px 6px -4px rgb(0 0 0 / 0.1);
        background-color: rgba(230, 250, 250, 0.5);
        @media (max-width: 600px) {
          padding: 1rem;
          width: calc(100% - 2rem);
        }

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
              padding-left: 1rem;
              font-size: clamp(1.25rem, 4vw, 1.5rem);
              line-height: 2rem;
              font-weight: 700;
              color: rgb(1 32 96);
            }
          }

          .featuresRoundedInfo1 {
            margin-bottom: 1rem;
            font-size: clamp(1rem, 4vw, 1.25rem);
            color: rgb(75 85 99);
          }

          .featuresRoundedInfo2 {
            font-size: clamp(1rem, 4vw, 1.25rem);
            color: rgb(75 85 99);
          }
        }
      }
    }
  }

  .containerBox {
    position: relative;
    margin: 6rem auto 0;
    padding: 0 2rem;
    width: 100%;
    max-width: 1536px;
    @media (max-width: 600px) {
      margin: 4rem 0;
      padding: 0 1rem;
    }

    .containerTitle {
      font-size: clamp(1.6rem, 4vw, 2.5rem);
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
      margin: 1rem auto 2.5rem;
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
          margin: 0 0.5rem;
          padding: 0.5rem 1rem;
          line-height: 2rem;
          color: rgb(1 32 96);
          background-color: #fff;
          border-radius: 0.5rem;
          @media (max-width: 600px) {
            margin: 0 0.25rem;
          }
        }

        .containerSubItem:first-child {
          margin-left: 0;
        }

        .containerSubItem:last-child {
          margin-right: 0;
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
      height: 700px;

      img {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 700px;
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
        @media (max-width: 600px) {
          padding: 1rem 1rem 0 1rem;
        }

        .containerGridContent {
          display: flex;
          flex-wrap: wrap;

          .containerGridItem {
            margin: 0 1rem 1rem 0;
            cursor: pointer;
            display: flex;
            align-items: center;
            padding: 0.75rem;
            border-radius: 0.5rem;
            @media (max-width: 600px) {
              padding: 0.5rem;
            }

            .containerGridimginfo {
              font-size: clamp(1rem, 4vw, 1.25rem);
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
    @media (max-width: 600px) {
      margin: 4rem auto 0;
      padding: 2.5rem 0;
    }

    .solutionsCotent {
      margin: 0 auto;
      position: relative;
      padding: 0 2rem;
      width: 100%;
      max-width: 1536px;
      @media (max-width: 600px) {
        padding: 0 1em;
      }

      .solutionsTitle {
        font-size: clamp(1.6rem, 4vw, 2.5rem);
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
            margin: 0 0.5rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            background-color: #fff;
            @media (max-width: 600px) {
              margin: 0 0.25rem;
            }
          }

          .solutionsSubItem:first-child {
            margin-left: 0;
          }

          .solutionsSubItem:last-child {
            margin-right: 0;
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
            margin: 0 0.5rem;
            line-height: 2rem;
            color: rgb(1 32 96);
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            background-color: #fff;
            @media (max-width: 600px) {
              margin: 0 0.25rem;
            }
          }

          .solutionsSubItem:first-child {
            margin-left: 0;
          }

          .solutionsSubItem:last-child {
            margin-right: 0;
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
        height: 44rem;
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
            font-size: clamp(1.25rem, 4vw, 1.5rem);
            line-height: 2rem;
            font-weight: 500;
            text-align: center;
            color: rgb(1 32 96);
          }

          .solutionsImgTitle2 {
            margin-bottom: 1.25rem;
            font-size: clamp(1.5rem, 4vw, 2.25rem);
            line-height: 2.5rem;
            font-weight: 700;
            text-align: center;
            color: rgb(1 32 96);
          }

          .solutionsImgTitle3 {
            font-size: clamp(1rem, 4vw, 1.5rem);
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
          padding: clamp(1.5rem, 4vw, 2.5rem);
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
    padding: 4rem 2.5rem;
    width: 100%;
    background-color: rgba(255, 255, 255, 1);
    @media (max-width: 600px) {
      padding: 4rem 0;
    }

    .aiContent {
      position: relative;
      margin: 0 auto;
      padding: 0 2rem;
      width: 100%;
      max-width: 1536px;
      @media (max-width: 600px) {
        padding: 0 1rem;
      }

      .aiTitle {
        font-size: clamp(1.6rem, 4vw, 2.5rem);
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

          i {
            font-size: 1.25rem;
            color: #165dff;
          }
        }

        .aiFabox2 {
          margin-right: 1rem;
          width: 3rem;
          height: 3rem;
          background-color: rgb(114 46 209 / 0.1);
          border-radius: 9999px;

          i {
            font-size: 1.25rem;
            color: #722ed1;
          }
        }

        .aiSubtitle {
          font-size: clamp(1.25rem, 4vw, 1.5rem);
          line-height: 2rem;
          font-weight: 700;
          color: rgb(1 32 96);
        }
      }

      .aiClassbox {
        margin-bottom: 2.5rem;
        width: calc(100% + 1rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        @media (max-width: 600px) {
          margin-bottom: 1.5rem;
        }

        .aiClassitem {
          margin: 0 1rem 1rem 0;
          padding: 1.25rem;
          width: calc(33.3% - 1rem);
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: rgb(249 250 251);
          border-radius: 0.75rem;
          @media (max-width: 600px) {
            padding: 1.25rem 1rem;
            width: calc(50% - 1rem);
          }

          .aiClassitemfa {
            margin-bottom: 1rem;
            width: 4rem;
            height: 4rem;
            border-radius: 9999px;
            background-color: rgb(22 93 255 / 0.1);
            @media (max-width: 600px) {
              width: 3rem;
              height: 3rem;
            }
          }

          .aiClassitemfa2 {
            margin-bottom: 1rem;
            width: 4rem;
            height: 4rem;
            border-radius: 9999px;
            background-color: rgb(114 46 209 / 0.1);
            @media (max-width: 600px) {
              width: 3rem;
              height: 3rem;
            }
          }

          .aiClassitemtext {
            line-height: 1.5rem;
            font-weight: 500;
            text-align: center;
            color: rgb(1 32 96);
          }
        }

        .aiClassitem:hover {
          cursor: pointer;
          box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
          animation: jumpUpwards 300ms ease-in-out forwards;
        }
      }

      .aiClassbox:last-child {
        margin-bottom: 0rem;
      }
    }
  }

  .mxBox {
    margin: 0 auto;
    padding: 2.5rem;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.5);
    background-image: url('../assets/about00.jpg');
    @media (max-width: 600px) {
      padding: 2.5rem 0;
    }

    .mxContent {
      margin: 0 auto;
      position: relative;
      padding: 0 2rem;
      width: 100%;
      max-width: 1536px;
      @media (max-width: 600px) {
        padding: 0 1rem;
      }

      .mxTitle {
        font-size: clamp(1.6rem, 4vw, 2.5rem);
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
        width: calc(100% + 1rem);
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;

        .mxClassitem {
          margin: 0 1rem 1rem 0;
          padding: 1.25rem;
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
          background-color: #fff;
          border-radius: 0.75rem;
          @media (min-width: 1140px) {
            width: calc(16.6% - 1rem);
          }
          @media (max-width: 1140px) and (min-width: 600px) {
            width: calc(33.3% - 1rem);
          }
          @media (max-width: 600px) {
            padding: 1rem 0.5rem;
            width: calc(50% - 1rem);
          }

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
    @media (max-width: 600px) {
      margin: 4rem auto 0;
      padding: 0 1rem 4rem;
    }

    .pyTitle {
      font-size: clamp(1.6rem, 4vw, 2.5rem);
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
      width: calc(100% + 1rem);
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;

      .pyClassitem {
        margin: 0 1rem 1rem 0;
        padding: 1.25rem 1rem;
        display: flex;
        flex-flow: column;
        justify-content: center;
        align-items: center;
        background-color: #fff;
        border-radius: 0.75rem;
        @media (min-width: 1140px) {
          width: calc(16.6% - 1rem);
        }
        @media (max-width: 1140px) and (min-width: 600px) {
          width: calc(33.3% - 1rem);
        }
        @media (max-width: 600px) {
          padding: 1rem 0.5rem;
          width: calc(50% - 1rem);
        }

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

      .pyClassitem:hover {
        cursor: pointer;
        box-shadow: 2px 2px 10px 0 rgb(0 0 0 / 0.1);
        animation: jumpUpwards 300ms ease-in-out forwards;
      }
    }
  }

  // @media (max-width: 1140px) {
  //   .outmostPd {
  //     padding-left: 0.5rem !important;
  //     padding-right: 0.5rem !important;
  //   }
  // }
}
</style>
