<template>
  <div>
    <div class="site-nav-bg">
      <div class="site-nav w1200">
        <p class="sn-back-home">
          <i class="layui-icon layui-icon-home"></i>
          <router-link :to="{path:'/'}">首页</router-link>
        </p>
        <div class="sn-quick-menu">
          <div class="login">
              <router-link :to="{path:'/login'}" v-if="username == null">登录</router-link>
              <p v-else>欢迎您，{{username}}</p>
          </div>
          <div class="sp-cart"><router-link :to="{path:'/shopcart'}">购物车</router-link></div>
          <div class="sp-cart" style="margin-left: 15px"><router-link :to="{path:'/order'}">订单页</router-link></div>
          <div class="sp-cart" style="margin-left: 15px" v-if="username == 'admin'"><router-link :to="{path:'/custom'}">客户管理</router-link></div>
          <div class="sp-cart" style="margin-left: 15px" v-if="username == 'admin'"><router-link :to="{path:'/goods_list'}">商品管理</router-link></div>
          <div class="sp-cart" style="margin-left: 15px"><router-link :to="{path:'/information'}" v-if="username != null">我的信息</router-link></div>
          <div class="sp-cart" style="margin-left: 15px" @click="logout()" v-if="username != null"><a>注销</a></div>
        </div>
      </div>
    </div>
    <div class="header" v-if="login == 0">
      <div class="headerLayout w1200">
        <div class="headerCon">
          <h1 class="mallLogo">
            <a href="#" title="母婴商城">
              <!--<img src="../res/static/img/logo.png">-->
            </a>
          </h1>
          <div class="mallSearch">
            <form action="" class="layui-form u-b-c" novalidate>
              <input type="text" name="title" required lay-verify="required" autocomplete="off" class="layui-input"
                     placeholder="请输入需要的商品" v-model="name">
              <router-link :to="{
                            path:'/search/'+name+'/',query:{
                                      name:name}
                                    }">
              <button class="layui-btn xx" lay-submit lay-filter="formDemo">
                <i class="layui-icon layui-icon-search"></i>
              </button>
              </router-link>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
      name: "slider1",
      data() {
        return {
          username: '',
          name: '',
          login: 0
        }
      },
      created() {
        var vm = this;
        vm.username = sessionStorage.getItem('username');
        vm.login = 0
        if(vm.$route.path == '/login' || vm.$route.path == '/custom' || vm.$route.path == '/register'){
          vm.login = 1
        }
      },
      methods: {
        logout() {
          var vm = this;
          sessionStorage.clear()
          vm.username = sessionStorage.getItem('username');
          console.log(vm.username)
          layer.msg('注销成功！')
          this.$router.go(0)
        }
      }
    }
</script>

<style scoped>
.u-b-c{
  /*border-color: #5c8d89!important;*/
  border:2px solid #5c8d89!important;
  height: 40px!important;
}
  .xx {
    background-color: #5c8d89!important;
    /*transform: translateY(-1px);*/
    transform: translateX(3px);
  }
</style>
