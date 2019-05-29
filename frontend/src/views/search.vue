<template>
  <div class="content content-nav-base commodity-content">
    <app-slider1></app-slider1>
    <div class="commod-cont-wrap">
      <div class="commod-cont w1200 layui-clear">
        <div class="right-cont-wrap">
          <div class="right-cont">
            <div class="cont-list layui-clear" id="list-cont">
              <template v-for="(v,k) in goods">
                <div class="item item1">
                  <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }">
                    <img class="img" style="width: 248px; height: 250px" :src="$site_url+v.img">

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
    name: "search",
    data() {
      return {
        name: '',
        goods: []
      }
    },
    watch: {
        '$route.params.name' (val){
           this.$router.go(0)
        }
      },
    created() {
      var vm = this;
      vm.name = vm.$route.params.name
      console.log(vm.name)
      vm.search()
    },
    methods: {
      search() {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/search/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {
            name: vm.name
          },
          success: function (data) {
            if (data.code === 0) {
              vm.goods = data.data
            }
          }
        });
      }
    }
  }
</script>

<style scoped>
.item1{float: left; width: 250px!important; height: 340px!important; border:1px solid #eaeaea; background: #fff; margin:0 47px 60px 0;}
</style>
