<template>
  <div class="content content-nav-base datails-content commodity-content">
    <app-slider1></app-slider1>
    <app-slider2></app-slider2>

    <div class="data-cont-wrap w1200" style="text-align: left;">
      <div class="crumb">
        <router-link :to="{path:'/'}">首页</router-link>
        <span>></span>
        <router-link :to="{path:'/commodity'}">所有商品</router-link>
        <span>></span>
        <a href="javascript:;">产品详情</a>
      </div>
      <div class="product-intro layui-clear">
        <div class="preview-wrap">
          <a href="javascript:;"><img style="height: 400px; width: 400px" :src="$site_url+goods.list.img"></a>
        </div>
        <div class="itemInfo-wrap">
          <div class="itemInfo">
            <div class="title">
              <h4>{{goods.list.goodsname}}</h4>
            </div>

            <div class="summary" v-if="goods.list.discount != 1" style="height: 180px">
              <p class="reference"><span>参考价</span>
                <del style="text-decoration:line-through">￥{{goods.list.original_price}}</del>
              </p>
              <p class="activity"><span>活动价</span><strong class="price"><i>￥</i>{{goods.list.actual_price}}</strong></p>
              <p class="reference"><span>库存</span>
                <del>{{goods.list.stock}}</del>
              </p>
            </div>
            <div class="summary" style="height: 120px" v-else>
              <p class="activity"><span>价格：</span><strong class="price"><i>￥</i>{{goods.list.actual_price}}</strong></p>
              <p class="reference"><span>库存</span>
                <del>{{goods.list.stock}}</del>
              </p>
            </div>

            <div class="choose-attrs">
              <div class="color layui-clear"><span class="title">材&nbsp;&nbsp;&nbsp;&nbsp;质</span>
                <div class="color-cont material-value">
                  <template v-for="(v,k) in goods.material">
                    <span class="btn" @click="addclass($event)">{{v.material}}</span>
                  </template>
                </div>
              </div>
            </div>
            <div class="choose-attrs">
              <div class="color layui-clear"><span class="title">颜&nbsp;&nbsp;&nbsp;&nbsp;色</span>
                <div class="color-cont color-value">
                  <template v-for="(v,k) in goods.color">
                    <span class="btn" @click="addclass($event)">{{v.color}}</span>
                  </template>
                </div>
              </div>
            </div>
            <div class="choose-attrs">
              <div class="color layui-clear"><span class="title">规&nbsp;&nbsp;&nbsp;&nbsp;格</span>
                <div class="color-cont size-value" >
                  <template v-for="(v,k) in goods.size">
                    <span class="btn" @click="addclass($event)">{{v.size}}</span>
                  </template>
                </div>
              </div>
            </div>

            <div class="number layui-clear" style="margin-left: 35px;"><span class="title">数&nbsp;&nbsp;&nbsp;&nbsp;量</span>
              <el-input-number v-model="num" :min="1" :max="goods.list.stock" label="描述文字" style="transform: translateX(28px);"></el-input-number>
            </div>

            <div class="choose-btns">
              <button class="layui-btn  layui-btn-danger car-btn" @click="submitForm()" style="transform: translateX(100px);"><i class="layui-icon layui-icon-cart-simple" ></i>加入购物车
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div class="commod-cont-wrap">
      <div class="commod-cont w1200 layui-clear">
        <div class="right-cont-wrap">
          <div class="right-cont">
            <div class="cont-list layui-clear" id="list-cont">
              <template v-for="(v,k) in goodss">
                <div class="item">
                  <!-- <div class="img"> -->
                  <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }">
                    <img class="img" style="width: 279px; height: 280px" :src="$site_url+v.img">

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
      name: "details.vue",
      data() {
        return {
          goods_num: '',
          goods: {},
          goodss: {},
          num: 1,
          username: ''
        }
      },
      created() {
        var vm = this;
        vm.goods_num = vm.$route.params.goods_num
        vm.username = sessionStorage.getItem('username');
        vm.getDetailGoods();
        vm.get_3();
      },
      watch: {
        '$route.params.goods_num' (val){
           this.$router.go(0)
        }
      },
      mounted() {
        var vm = this;
      },
      methods: {
        getDetailGoods() {
          var vm = this;
          $.ajax({
            url: `${SITE_URL}goods/get_details/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {
              goods_num: vm.goods_num
            },
            success: function (data) {
              if (data.code === 0) {
                vm.goods = data.data
              }
            }
          });
        },
        addclass (t) {
          var vm = this;
          $(t.target).siblings("span").removeClass("intro");
          $(t.target).addClass("intro");
        },
        submitForm() {
          let vm = this;
          let material, color, size;
          material = $('.material-value').find('span.intro').text()
          color = $('.color-value').find('span.intro').text()
          size = $('.size-value').find('span.intro').text()
          if(vm.username == null){
            layer.msg('请先登录')
            return
          }
          if (material != '' && color != '' && size != '') {
            $.ajax({
              url: `${SITE_URL}goods/in_cart/`,
              dataType: 'json',
              type: 'POST',
              xhrFields: {
                withCredentials: true
              },
              crossDomain: true,
              data: {
                goods_num: vm.goods_num,
                goodsname: vm.goods.list.goodsname,
                material: material,
                color: color,
                size: size,
                num: vm.num,
                username: vm.username
              },
              success: function (data) {
                if (data.code === 0) {
                  layer.msg('添加成功！')
                }
              }
            });
          }else{
              layer.msg('请将参数选择完整!')
          }
        },
        get_3() {
          var vm = this;
          $.ajax({
            url: `${SITE_URL}goods/get_3/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {
              goods_num: vm.goods_num
            },
            success: function (data) {
              if (data.code === 0) {
                vm.goodss = data.data
              }
            }
          });
        }
      },

    }
</script>

<style type="text/css">
.intro
{
  border-color: #ff5500!important;
}
</style>
