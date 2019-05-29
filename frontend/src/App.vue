<template>
  <div id="app">
    <router-view></router-view>
    <app-footer v-if="show == 0"></app-footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      show: 0
    }
  },
  created() {
    var vm = this;
    vm.show = 0
    if(vm.$route.path == '/login' || vm.$route.path == '/register'){
      vm.show = 1
    }
    console.log(vm.show)
  },
  methods: {

  }
}
</script>

<style>
  /*@import 'assets/plugins/bootstrap-3.3.4/css/bootstrap.min.css';*/
  /*@import 'assets/js/plugins/datatables/dataTables.bootstrap.css';*/
  /*@import 'assets/css/font-awesome.min.css';*/
  /*@import 'assets/js/plugins/layer/skin/layer.css';*/
  /*@import 'assets/css/common.css';*/
  /*@import 'assets/css/style.css';*/
  /*@import 'assets/css/skin/default.css';*/
  /*@import 'assets/css/detail.css';*/
  /*@import 'assets/js/plugins/layer/laydate/theme/default/laydate.css';*/
  /*@import 'assets/js/plugins/layui/css/layui.css';*/
  /*@import "assets/css/icon/iconfont.css";*/

  #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  }
  .el-upload__input{
     display: none!important;
}
</style>
