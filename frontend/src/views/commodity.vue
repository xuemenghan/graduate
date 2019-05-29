<template>
  <div class="content content-nav-base commodity-content">
    <app-slider1></app-slider1>
    <app-slider2></app-slider2>

    <div class="commod-cont-wrap">
      <div class="commod-cont w1200 layui-clear">
        <div class="left-nav">
          <div class="title">所有分类</div>
          <div class="list-box">
            <dl>
              <dt>花架</dt>
              <dd>
                <router-link :to="{
                            path:'/search/'+'壁挂式花架'+'/',query:{
                                      name: '壁挂式花架'}
                                    }">壁挂式花架
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'移动式花架'+'/',query:{
                                      name: '移动式花架'}
                                    }">移动式花架
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'阶梯花架'+'/',query:{
                                      name: '阶梯花架'}
                                    }">阶梯花架
                </router-link>
              </dd>
            </dl>
            <dl>
              <dt>凉亭</dt>
              <dd>
                <router-link :to="{
                            path:'/search/'+'中式凉亭'+'/',query:{
                                      name: '中式凉亭'}
                                    }">中式凉亭
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'欧式凉亭'+'/',query:{
                                      name: '欧式凉亭'}
                                    }">欧式凉亭
                </router-link>
              </dd>
            </dl>
            <dl>
              <dt>地板</dt>
              <dd>
                <router-link :to="{
                            path:'/search/'+'碳化木'+'/',query:{
                                      name: '碳化木'}
                                    }">碳化木
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'樟子松'+'/',query:{
                                      name: '樟子松'}
                                    }">樟子松
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'菠萝格'+'/',query:{
                                      name: '菠萝格'}
                                    }">菠萝格
                </router-link>
              </dd>
            </dl>
            <dl>
              <dt>宠物房</dt>
              <dd>
                <router-link :to="{
                            path:'/search/'+'室内小型'+'/',query:{
                                      name: '室内小型'}
                                    }">室内小型
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'室外大型'+'/',query:{
                                      name: '室外大型'}
                                    }">室外大型
                </router-link>
              </dd>
            </dl>
            <dl>
              <dt>廊架</dt>
              <dd>
                <router-link :to="{
                            path:'/search/'+'市区廊架'+'/',query:{
                                      name: '市区廊架'}
                                    }">市区廊架
                </router-link>
              </dd>
              <dd>
                <router-link :to="{
                            path:'/search/'+'景区廊架'+'/',query:{
                                      name: '景区廊架'}
                                    }">景区廊架
                </router-link>
              </dd>
            </dl>
            <dl>
              <dt>栈道</dt>
              <dd>
                <router-link :to="{
                            path:'/search/'+'水上栈道'+'/',query:{
                                      name: '水上栈道'}
                                    }">水上栈道
                </router-link>
              </dd>
            </dl>
          </div>
        </div>
        <div class="right-cont-wrap">
          <div class="right-cont">
            <div class="cont-list layui-clear" id="list-cont">
              <template v-for="(v,k) in goods">
                <div class="item">
                 <!-- <div class="img"> -->
                  <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }">
                    <img class="img" style="width: 280px; height: 280px" :src="$site_url+v.img">

                    <div class="text">
                      <p class="title" style="font-size: 12px">{{v.goodsname}}</p>
                      <p class="price">
                        <span class="pri">￥{{v.actual_price}}</span>
                        <del style=" padding-left: 40px;text-decoration:line-through;color: #726868;"
                             v-if="v.discount != 1">￥{{v.original_price}}
                        </del>
                      </p>
                    </div>
                  </router-link>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "commodity",
    data() {
      return {
        show: true,
        username: '',
        goods: [],
        disgood: []
        // site_url: `${SITE_URL}`
      }
    },
    created() {
      var vm = this;
      vm.getGoods()
    },
    methods: {
      getGoods() {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/show/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {
            type: 'all_show'
          },
          success: function (data) {
            if (data.code === 0) {
              vm.goods = data.data
            }
          }
        });
      },
    }
  }
</script>

<style scoped>

</style>
