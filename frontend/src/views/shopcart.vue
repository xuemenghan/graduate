<template>
  <div class="shopcart-content">
    <app-slider1></app-slider1>
    <div class="cart w1200">
      <div class="cart-table-th">
        <div class="th th-chk">
          <div class="select-all">
            <div class="cart-checkbox">
              <input class="check-all" id="allCheckked" type="checkbox" value="true" @click="check_all()">
            </div>
            <label>&nbsp;&nbsp;全选</label>
          </div>
        </div>
        <div class="th th-item">
          <div class="th-inner">商品</div>
        </div>
        <div class="th th-price">
          <div class="th-inner">单价</div>
        </div>
        <div class="th th-amount">
          <div class="th-inner">数量</div>
        </div>
        <div class="th th-sum">
          <div class="th-inner">小计</div>
        </div>
        <div class="th th-op">
          <div class="th-inner">操作</div>
        </div>
      </div>
      <div class="OrderList">
        <div class="order-content" id="list-cont">
          <template v-for="(v,k) in goods">
            <ul class="item-content layui-clear">
              <li class="th th-chk">
                <div class="select-all">
                  <div class="cart-checkbox">
                    <input class="CheckBoxShop check" type="checkbox" num="all" name="select-all"
                           :value="v.actual_price * v.num" @click="checked($event,v.actual_price * v.num)"
                           :data="v.goods_num">
                  </div>
                </div>
              </li>
              <li class="th th-item">
                <div class="item-cont">
                  <router-link :to="{
                            path:'/details/'+v.goods_num+'/',query:{
                                      goods_num:v.goods_num}
                                    }"><img style="height: 98px; width: 98px;" :src="$site_url+v.img" alt="">
                  </router-link>
                  <div class="text">
                    <div class="title">{{v.goodsname}}</div>
                    <p><span>{{v.goods_material}}</span> <span>{{v.goods_size}}</span> <span>{{v.goods_color}}</span>
                    </p>
                  </div>
                </div>
              </li>
              <li class="th th-price">
                <span class="th-su">{{v.actual_price}}</span>
              </li>
              <li class="th th-amount">
                <span class="th-su">{{v.num}}</span>
                <!--<el-input-number v-model="v.num" :min="1" :max="100" label="描述文字" style="transform: translateX(28px);"></el-input-number>-->
              </li>
              <li class="th th-sum">
                <span class="sum">{{v.actual_price * v.num}}</span>
              </li>
              <li class="th th-op">
                <!--<button class="btn btn-xs btn-warning"> <i class="glyphicon glyphicon-edit"></i> </button>-->
                <button class="btn btn-xs btn-danger" @click="deleteGoods(v.id)"> <i class="glyphicon glyphicon-remove"></i> </button>
                <!--<span class="dele-btn" @click="deleteGoods(v.id)">删除</span>-->
              </li>
            </ul>
          </template>
        </div>
      </div>

      <div class="FloatBarHolder layui-clear" style="height: 85px;">
        <div class="th th-chk">
          <div class="select-all">
            <label>&nbsp;&nbsp;已选<span class="Selected-pieces">{{total_num}}</span>件</label>
          </div>
        </div>
        <div class="th Settlement">
          <button class="layui-btn" @click="pay()">结算</button>
        </div>
        <div class="th total">
          <p>应付：<span class="pieces-total">{{price}}</span></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "shopcart",
    data() {
      return {
        username: '',
        goods: [],
        price: 0,
        total_num: 0,
        n:0
      }
    },
    created() {
      var vm = this;
      vm.username = sessionStorage.getItem('username');
      vm.getShopcart()
    },
    methods: {
      getShopcart() {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/get_shopcart/`,
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
              vm.goods = data.data
            }
          }
        });
      },
      deleteGoods(id) {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}goods/delete_goods/`,
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
              layer.msg('删除成功！')
              vm.getShopcart()
            }
          }
        });
      },
      check_all() {
        var vm = this
        if ($(".check-all").prop("checked") == true) {
          vm.price = 0
          $('.check').each(function (i,v) {
            vm.n++
            vm.price  += ($(this).val() - 0)
          })
          $(".check").prop("checked", "checked")
          vm.total_num = vm.n
        } else {
          $(".check").prop("checked", "")
          vm.price = 0
          vm.total_num = 0
        }
      },
      checked(t,n){
        var vm = this;
        if ($(t.target).prop("checked") == true) {
            vm.price += (n - 0)
          vm.total_num += 1
        }else{
          vm.price -= n
           vm.total_num -= 1
        }
      },
      pay(){
        var vm = this;
        var arr = []
        $('.check').each(function (i, v) {
          console.log($(this).attr('data'))
          if ($(this).prop("checked") == true) {
            arr.push($(this).attr('data'))
            console.log(arr)
          }
        })
        $.ajax({
          url: `${SITE_URL}goods/pay/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {
            arr: JSON.stringify(arr),
            price: vm.price,
            username: vm.username
          },
          success: function (data) {
            if (data.code === 0) {
              vm.getShopcart()
              vm.price = 0
              vm.total_num = 0
            }
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>
