<template>
  <div>
    <div class="content" style="padding-top: 100px">
      <div class="main-nav">
        <div class="inner-cont0">
          <div class="inner-cont1 w1200">
            <div class="inner-cont2">
              <a href=""><router-link :to="{path:'/commodity'}">所有商品</router-link></a>
              <a href=""><router-link :to="{path:'/discount'}">今日团购</router-link></a>
              <a href="">木业资讯</a>
              <a href="">关于我们</a>
            </div>
          </div>
        </div>
      </div>
      <div class="category-con">
        <div class="category-inner-con w1200">
          <div class="category-type">
            <h3 style="transform: translateY(-6px)">全部分类</h3>
          </div>
          <div class="category-tab-content">
            <div class="nav-con">
              <ul class="normal-nav layui-clear">
                <li class="nav-item">
                  <div class="title">凉亭</div>
                  <p>
                    <router-link :to="{
                            path:'/search/'+'欧式凉亭'+'/',query:{
                                      name: '欧式凉亭'}
                                    }">欧式凉亭
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'中式凉亭'+'/',query:{
                                      name: '中式凉亭'}
                                    }">中式凉亭
                    </router-link>
                  </p>
                  <i class="layui-icon layui-icon-right"></i>
                </li>
                <li class="nav-item">
                  <div class="title">地板</div>
                  <p>
                    <router-link :to="{
                            path:'/search/'+'樟子松'+'/',query:{
                                      name: '樟子松'}
                                    }">樟子松
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'菠萝格'+'/',query:{
                                      name: '菠萝格'}
                                    }">菠萝格
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'碳化木'+'/',query:{
                                      name: '碳化木'}
                                    }">碳化木
                    </router-link>
                  </p>
                  <i class="layui-icon layui-icon-right"></i>
                </li>
                <li class="nav-item">
                  <div class="title">宠物房</div>
                  <p>
                    <router-link :to="{
                            path:'/search/'+'室内小型'+'/',query:{
                                      name: '室内小型'}
                                    }">室内小型
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'室外大型'+'/',query:{
                                      name: '室外大型'}
                                    }">室外大型
                    </router-link>
                  </p>
                  <i class="layui-icon layui-icon-right"></i>
                </li>
                <li class="nav-item">
                  <div class="title">花架</div>
                  <p>
                    <router-link :to="{
                            path:'/search/'+'壁挂式花架'+'/',query:{
                                      name: '壁挂式花架'}
                                    }">壁挂式花架
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'阶梯花架'+'/',query:{
                                      name: '阶梯花架'}
                                    }">阶梯花架
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'移动式花架'+'/',query:{
                                      name: '移动式花架'}
                                    }">移动式花架
                    </router-link>
                  </p>
                  <i class="layui-icon layui-icon-right"></i>
                </li>
                <li class="nav-item">
                  <div class="title">廊架</div>
                  <p>
                    <router-link :to="{
                            path:'/search/'+'市区廊架'+'/',query:{
                                      name: '市区廊架'}
                                    }">市区廊架
                    </router-link>
                    <router-link :to="{
                            path:'/search/'+'景区廊架'+'/',query:{
                                      name: '景区廊架'}
                                    }">景区廊架
                    </router-link>
                  </p>
                  <i class="layui-icon layui-icon-right"></i>
                </li>
                <li class="nav-item nobor">
                  <div class="title">栈道</div>
                  <p>
                    <router-link :to="{
                            path:'/search/'+'水上栈道'+'/',query:{
                                      name: '水上栈道'}
                                    }">水上栈道
                    </router-link>
                  </p>
                  <i class="layui-icon layui-icon-right"></i>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="category-banner">
          <div class="w1200">
            <img src="../../assets/images/banner1.jpg">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "header1"
    }
</script>

<style scoped>

</style>
