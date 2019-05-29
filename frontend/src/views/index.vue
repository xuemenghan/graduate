<template>
  <div class="content">
    <app-slider1></app-slider1>
    <app-change></app-change>
    <app-header1></app-header1>
    <!--今日必抢-->
    <div class="floors">
      <div class="sk">
        <div class="sk_inner w1200">
          <div class="sk_hd">
            <a href="javascript:;">
              <router-link :to="{
                            path:'/discount'
                                    }">
              <img src="../assets/images/s_img1_1.jpg">
              </router-link>
            </a>
          </div>
          <div class="sk_bd">
            <div class="item">
              <template v-for="(v,k) in disgood">
                <div style="float: left; padding: 0px 6px 0px 6px;">
                  <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }">
                    <img style="width: 190px; height: 190px" :src="$site_url+v.img">
                    <div class="title">{{v.goodsname}}</div>
                  </router-link>
                  <div class="price">
                    <span>￥{{v.actual_price}}</span>
                    <del>￥{{v.original_price}}</del>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--首页下方更多推荐-->
  <div class="product-list-box" id="product-list-box">
      <div class="product-list-cont w1200">
        <h4 style="margin-top: 80px">更多推荐</h4>
        <div class="product-item-box layui-clear">
          <template v-for="(v,k) in goods">
            <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }">
              <div class="list-item">
                <img style="width: 160px; height: 190px" :src="$site_url+v.img">
                <p>{{v.goodsname}}</p>
                <span>￥{{v.actual_price}}</span>
              </div>
            </router-link>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        show: true,
        username: '',
        goods: [],
        disgood: [],
      }
    },
    created () {
      var vm = this;
      vm.username = sessionStorage.getItem('username');
      vm.getGoods();
      vm.discount();
    },
    mounted() {
    },
    methods: {
      left() {
        var vm = this;
        vm.show = !vm.show;
      },
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
            type: 'index_show'
          },
          success: function (data) {
            if (data.code === 0) {
              vm.goods = data.data
            }
          }
        });
      },
      discount() {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/discount/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {},
          success: function (data) {
            if (data.code === 0) {
              vm.disgood = data.data
            }
          }
        });
      }
    }
  }


  // layui.config({
  //   base: '../../static/static/js/util/' //你存放新模块的目录，注意，不是layui的模块目录
  // }).use(['mm', 'carousel'], function () {
  //   var carousel = layui.carousel,
  //     mm = layui.mm;
  //   var option = {
  //     elem: '#test1'
  //     , width: '100%' //设置容器宽度
  //     , arrow: 'always'
  //     , height: '298'
  //     , indicator: 'none'
  //   }
  //   carousel.render(option);
  //   // 模版引擎导入
  //   // var ins = carousel.render(option);
  //   // var html = demo.innerHTML;
  //   // var listCont = document.getElementById('list-cont');
  //   // // console.log(layui.router("#/about.html"))
  //   //  mm.request({
  //   //    url: '../json/index.json',
  //   //    success : function(res){
  //   //      console.log(res)
  //   //      listCont.innerHTML = mm.renderHtml(html,res)
  //   //      ins.reload(option);
  //   //    },
  //   //    error: function(res){
  //   //      console.log(res);
  //   //    }
  //   //  })
  // });



  /*layui.use(['carousel', 'form'], function(){
  var carousel = layui.carousel
  ,form = layui.form;

  //常规轮播
  carousel.render({
    elem: '#test1'
    ,arrow: 'always'
  });

  //改变下时间间隔、动画类型、高度
  carousel.render({
    elem: '#test2'
    ,interval: 1800
    ,anim: 'fade'
    ,height: '120px'
  });

  //设定各种参数
  var ins3 = carousel.render({
    elem: '#test3'
    ,width: '778px'
    ,height: '440px'
    ,interval: 5000
  });
  //图片轮播
  carousel.render({
    elem: '#test10'
    ,width: '778px'
    ,height: '440px'
    ,interval: 5000
  });

  //事件
  carousel.on('change(test4)', function(res){
    console.log(res)
  });

  var $ = layui.$, active = {
    set: function(othis){
      var THIS = 'layui-bg-normal'
      ,key = othis.data('key')
      ,options = {};

      othis.css('background-color', '#5FB878').siblings().removeAttr('style');
      options[key] = othis.data('value');
      ins3.reload(options);
    }
  };

  //监听开关
  form.on('switch(autoplay)', function(){
    ins3.reload({
      autoplay: this.checked
    });
  });

  $('.demoSet').on('keyup', function(){
    var value = this.value
    ,options = {};
    if(!/^\d+$/.test(value)) return;

    options[this.name] = value;
    ins3.reload(options);
  });

  //其它示例
  $('.demoTest .layui-btn').on('click', function(){
    var othis = $(this), type = othis.data('type');
    active[type] ? active[type].call(this, othis) : '';
  });
});*/

</script>
<!-- 注意：如果你直接复制所有代码到本地，上述js路径需要改成你本地的 -->
<style scoped>

</style>
