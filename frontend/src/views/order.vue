<template>
  <div class="shopcart-content">
    <app-slider1></app-slider1>
    <div class="cart w1200">
      <template v-for="(v,k) in orders">
        <div class="cart-table-th">
          <div class="th th-chk">
            <div class="select-all" style="width: 141px;overflow: hidden;height: 40px;">
              <label>订单编号：</label><span style="width: 20px;overflow: hidden" :title="v[0].order_id">{{v[0].order_id}}</span>
            </div>
          </div>
          <div class="th th-item">商品</div>
          <div class="th th-price">付款价格</div>
          <div class="th th-amount">数量</div>
          <div class="th th-sum">付款时间</div>
          <div class="th th-op">订单状态</div>
          <div class="th th-op" v-if="username != 'admin'">售后</div>
        </div>
        <div class="OrderList">
          <div class="order-content" id="list-cont">
            <ul class="item-content layui-clear" v-for="i in v">

              <li class="th th-item">
                <div class="item-cont">
                  <router-link :to="{
                            path:'/details/'+i.goods_num+'/',query:{
                                      goods_num:i.goods_num}
                                    }"><img style="height: 98px; width: 98px;" :src="$site_url+i.img" alt="">
                  </router-link>
                  <div class="text">
                    <div class="title">{{i.goodsname}}</div>
                    <p><span>{{i.goods_material}}</span> <span>{{i.goods_size}}</span> <span>{{i.goods_color}}</span>
                    </p>
                  </div>
                </div>
              </li>
              <li class="th th-sum">
                <span class="sum">{{i.total_price}}</span>
              </li>
              <li class="th th-amount">
                <span class="th-su">{{i.num}}</span>
              </li>
              <li class="th th-amount">
                <span class="th-su">{{i.order_time}}</span>
              </li>
              <!--订单状态-->
              <li class="th th-op" v-if="username == 'admin'">
                <template v-if="i.order_status == '等待发货'">
                   <button type="button" class="king-btn mr10  king-success" @click="deliver(i.id)">点击发货</button>
                </template>
                <template v-else-if="i.order_status == '已发货' || i.order_status == '已退款'">
                  <span class="dele-btn">{{i.order_status}}</span>
                </template>
                <template v-if="i.order_status == '等待退款'">
                  <a class="king-btn-demo king-btn king-danger" @click="back_refund(v=i.id)">点击退款</a>
                </template>
              </li>
                <!--用户-->
              <li class="th th-op" v-else>
                <span class="dele-btn">{{i.order_status}}</span>
              </li>

              <!--售后-->
              <li class="th th-op" v-if="username != 'admin'">
                <button class="king-btn-demo king-btn king-warning" v-if="i.order_status == '等待发货'" @click="refund(i.id)">
                  点击退款
                </button>
                <span class="dele-btn" v-else-if="i.order_status == '已发货' || i.order_status == '已退款'">无</span>
                <span class="dele-btn" v-else>...</span>
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
    name: "order",
    data() {
      return {
        username: '',
        orders: [],
        price: 0,
        total_num: 0,
      }
    },
    created() {
      var vm = this;
      vm.username = sessionStorage.getItem('username');
      vm.gerOrder()
    },
    methods: {
      gerOrder() {
        var vm = this;
        if (vm.username == 'admin') {
          $.ajax({
            url: `${SITE_URL}goods/get_order_admin/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {},
            success: function (data) {
              if (data.code === 0) {
                vm.orders = data.data
              }
            }
          });
        }
        else{
          $.ajax({
            url: `${SITE_URL}goods/get_order/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {
              username: vm.username
            },
            success: function (data) {
              if (data.code === 0) {
                vm.orders = data.data
              }
            }
          });
        }
      },
      deliver(id) {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/deliver_goods/`,
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
              vm.gerOrder()
            }
          }
        });
      },
      refund(id) {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/refund/`,
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
              vm.gerOrder()
            }
          }
        });
      },
      back_refund (id) {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/back_refund/`,
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
              vm.gerOrder()
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

  #list-cont .th-sum {
    margin-left: 118px;
  }

  ul, ol {
    margin-bottom: 0px;
  }
  .select-all span{
    width: 20px;
    overflow: hidden;
    height: 20px;
  }
  .th-inner {
    margin-left: -230px;
  }
  .shopcart-content .th-sum {
    width: 138px;
}
  .OrderList .th-amount {
    padding-left: 71px;
    width: 165px;
}
  .OrderList .th-op {
    padding-left: 47px;
    width: 114px;
}
  .shopcart-content .th-price {
    width: 165px;
}
</style>
