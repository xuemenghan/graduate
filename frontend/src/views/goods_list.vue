<template>
  <div class="shopcart-content">
    <app-slider1></app-slider1>
    <div class="add w1200">
      <button type="button" class="btn btn-info">
        <router-link :to="{
                            path:'/add_goods/'
                                    }">添加商品
                  </router-link>
      </button>
    </div>
    <div class="cart w1200">
      <div class="cart-table-th">
        <!--<div class="th th-chk">-->
        <!--<div class="select-all" style="width: 141px;overflow: hidden;height: 40px;">-->
        <!--<label>订单编号：</label><span style="width: 20px;overflow: hidden" :title="v[0].order_id">{{v[0].order_id}}</span>-->
        <!--</div>-->
        <!--</div>-->
        <div class="th th-item">商品</div>
        <div class="th th-price">原价</div>
        <div class="th th-amount">折扣</div>
        <div class="th th-sum">现价</div>
        <div class="th th-op">操作</div>
      </div>
      <template v-for="(v,k) in goods">
        <div class="OrderList">
          <div class="order-content" id="list-cont">
            <ul class="item-content layui-clear">

              <li class="th th-item">
                <div class="item-cont">
                  <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }"><img style="height: 98px; width: 98px;" :src="$site_url+v.img" alt="">
                  </router-link>
                  <div class="text">
                    <div class="title">{{v.goodsname}}</div>
                  </div>
                </div>
              </li>
              <li class="th th-amount">
                <span class="th-su">{{v.original_price}}</span>
              </li>
              <li class="th th-amount">
                <span class="th-su">{{v.discount}}</span>
              </li>
              <li class="th th-sum">
                <span class="sum">{{v.actual_price}}</span>
              </li>
              <li class="th th-op">
                <button class="btn btn-xs btn-warning">
                  <router-link :to="{
                            path:'/edit_goods/'+v.id
                                    }"><i class="glyphicon glyphicon-edit"></i>
                  </router-link>
                </button>
                <button class="btn btn-xs btn-danger" @click="deleteGoods(v.id)"> <i class="glyphicon glyphicon-remove"></i> </button>
                <!--<span class="dele-btn" @click="deleteGoods(v.id)">删除</span>-->
              </li>
            </ul>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
  export default {
    name: "goods_list",
    data() {
      return {
        show: true,
        username: '',
        goods: []
      }
    },
    created() {
      var vm = this;
      console.log('111')
      vm.username = sessionStorage.getItem('username');
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
      deleteGoods(id) {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/del_good/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {
            id: id
          },
          success: function (data) {
            if (data.code === 0) {
              layer.msg('删除成功!')
              vm.getGoods()
            }
          }
        });
      }
    }
  }
</script>

<style scoped>
.shopcart-content .order-content .th-item {
    left: -30px;
  }
  .shopcart-content .th-item {
    width: 409px;
  }
  .add{
    position: relative;
  }
  .add>button {
    position: absolute;
    left: 10px;
    top: -62px;
  }
  .add>button>a{
    color: white;
  }
  .btn>a{
    color: white;
  }
</style>
