<template>
  <body class="bg-white" data-bg-color="bg-white">
  <app-slider1></app-slider1>
  <div class="king-page-box">
    <div class="king-container clearfix">
      <div class="panel panel-default mb0">
        <div class="panel-heading" style="height: 40px"><p style="float: left;">我的信息</p></div>
        <div class="panel-body">
          <form class="form-horizontal"  style="margin: 50px;">
            <div class="form-group clearfix ">
              <label class="col-sm-3 control-label bk-lh30 pt0">昵称：</label>
              <div class="col-sm-5">
                <input type="text" class="form-control bk-valign-top" placeholder="提示信息" v-model="info.name"></div>
            </div>
            <div class="form-group clearfix ">
              <label class="col-sm-3 control-label bk-lh30 pt0">密码：</label>
              <div class="col-sm-5">
                <input type="password" class="form-control bk-valign-top" id="" placeholder="提示信息" v-model="info.password">
                <p class="help-block">密码最少6位以上，包括数字和字母</p>
              </div>
            </div>
            <div class="form-group clearfix ">
              <label class="col-sm-3 control-label bk-lh30 pt0">电话：</label>
              <div class="col-sm-5">
                <input type="text" class="form-control bk-valign-top" id="" placeholder="提示信息" v-model="info.telephone"></div>
            </div>
            <div class="form-group clearfix ">
              <label class="col-sm-3 control-label bk-lh30 pt0">地址：</label>
              <div class="col-sm-5">
                <input type="text" class="form-control bk-valign-top" id="" placeholder="提示信息" v-model="info.address"></div>
            </div>
            <div class="form-group clearfix ">
              <label class="control-label col-sm-3 bk-lh30 pt0">性别：</label>
              <div class="col-sm-5">
                <div class="radio pt0">
                  <label class="mr10">
                    <input type="radio" name="optionsRadios" id="" class="bk-top5" value="0" v-model="info.sex">
                    <span class="bk-lh30">女</span>
                  </label>
                  <label class="mr10">
                    <input type="radio" name="optionsRadios" id="" class="bk-top5" value="1" v-model="info.sex">
                    <span class="bk-lh30">男</span>
                  </label>
                </div>
              </div>
            </div>
            <div class="form-group clearfix" >
              <div class="col-sm-9 col-sm-offset-3" style="margin-left: 70px;">
                <button type="button" class="king-btn mr10  king-success" @click="submit()">保存</button>
                <button type="button" class="king-btn king-default ">取消</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
  export default {
    name: "information",
    data() {
      return {
        username: '',
        info: []
      }
    },
    created() {
      var vm = this;
      vm.username = sessionStorage.getItem('username');
      vm.getInfo()
    },
    methods: {
      getInfo() {
        var vm = this;
        $.ajax({
            url: `${SITE_URL}register/get_info/`,
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
                vm.info = data.data
                console.log(vm.info)
              }
            }
          });
      },
      submit() {
        var vm = this;
        $.ajax({
            url: `${SITE_URL}register/edit_info/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {
              info: JSON.stringify(vm.info)
            },
            success: function (data) {
              if (data.code === 0) {
                vm.getInfo()
              }
            }
          });
      }
    }
  }
</script>

<style scoped>
form .clearfix{
  margin-left: 150px;
}
</style>
