<template>
<div>
  <app-slider1></app-slider1>
  <div class="container">
    <!--<app-slider2></app-slider2>-->
    <div class="panel panel-default">
        <div class="panel-body">
            <div class="col-md-9">
                <p>名字：</p>
                <input type="text" placeholder="请输入商品名称" v-model="good.goodsname">
            </div>
            <div class="col-md-9">
                <p>编号：</p>
                <input type="text" placeholder="请输入商品编号" v-model="good.goods_num">
            </div>
            <div class="col-md-9">
                <p>原价：</p>
                <input type="text" placeholder="请输入原价" v-model="good.original_price">
            </div>
            <div class="col-md-9">
                <p>折扣：</p>
                <input type="text" placeholder="请输入折扣" v-model="good.discount">
            </div>
          <!--<div class="col-md-9">-->
                <!--<p>折扣：</p>-->
                <!--<input type="text" placeholder="请输入邮箱" v-model="item.email">-->
            <!--</div>-->
          <div class="col-md-9">
            <p>类别：</p>
            <!--<input type="text" placeholder="请输入邮箱" v-model="item.email">-->
            <div class="col-sm-3">
              <select class="form-control bk-valign-top" v-model="good.category">
                <template v-for="(v,k) in cates">
                  <option :value="v.category">{{v.category}}</option>
                </template>
              </select>
            </div>
          </div>
          <div class="col-md-9">
            <p>颜色：</p>
            <input type="text" placeholder="请输入颜色" v-model="good.color">
          </div>
          <div class="col-md-9">
            <p>商品图片：</p>
            <el-upload
              class="avatar-uploader"
              :action="$site_url+'/goods/add_goods/'"
              :show-file-list="false"
              :on-change="befor1"
              :auto-upload="false">
              <!--:on-success=""-->
              <img :src="$site_url+good.img" class="avatar">
              <!--<i v-else class="el-icon-plus avatar-uploader-icon"></i>-->
            </el-upload>
          </div>
          <div class="col-md-9">
                <p>材质：</p>
                <input type="text" placeholder="请输入材质" v-model="good.material">
            </div>
          <div class="col-md-9">
                <p>规格：</p>
                <input type="text" placeholder="请输入规格" v-model="good.size">
            </div>
          <div class="col-md-9">
                <p>库存：</p>
                <input type="text" placeholder="请输入库存" v-model="good.stock">
            </div>

            <div class="col-md-6" style="text-align:center;">
                <button class="layui-btn layui-btn-normal layui-btn-lg" @click="save()">保存</button>
            </div>
            <div class="col-md-6" style="text-align:center;"><button class="layui-btn layui-btn-primary layui-btn-lg" @click="goback()">取消</button></div>
        </div>
    </div>
</div>
  </div>
</template>

<script>
export default {
    name: "add",

    data() {
      return {
        id: '',
        item: {
          material: '',
          size: '',
          color: '',
          category: '',
          disc: '',
          goodsname: '',
          goods_num: '',
          original_price: '',
          imageUrl: '',
          stock: ''
        },
        imageUrl: '',
        good: [],
        cate: []
      };
    },
    created() {
      var vm = this
      vm.id = vm.$route.params.id

      vm.get_cate()
    },
    mounted() {
      var vm = this
      vm.get_good()
    },
    methods: {
      get_good() {
        var vm = this;
        $.ajax({
            url: `${SITE_URL}goods/get_goods_1/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {
              id: vm.id
            },
            success: function (data) {
              if (data.code === 0) {
                vm.good = data.data
              }
            }
          });
      },
      get_cate() {
        var vm = this;
        $.ajax({
            url: `${SITE_URL}goods/get_cate/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {},
            success: function (data) {
              if (data.code === 0) {
                vm.cates = data.data
              }
            }
          });
      },
      befor1(file) {
        var vm = this;
        let form_data = new FormData();
        form_data.append("file", file.raw);
        $.ajax({
          url: `${SITE_URL}goods/save_img/`,
          type: 'POST',
          contentType: false,
          processData: false,
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: form_data,
          success: function (data) {
            if (data.code === 0) {
              vm.good.img = data.data.img
            }
          }
        });
      },
      goback(){
          this.$router.go(-1)
      },
      save() {
        var vm = this;
        $.ajax({
            url: `${SITE_URL}goods/edit_good/`,
            dataType: 'json',
            type: 'POST',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: vm.good,
            success: function (data) {
              if (data.code === 0) {
                layer.msg('修改成功!')
                setTimeout(function () {
                  vm.$router.go(-1)
                },2000)
              }
            }
          });
      }
    }
};
</script>

<style scoped>
  .form-control {
    /*display: inline-block;*/
    width: 600px!important;
    margin-left: -13px;
}

.layui-btn{
    margin:30px auto;
}
input::-webkit-input-placeholder {
          /* placeholder颜色  */
         color: black;

}
.panel-body>.col-md-8 input{
    width: 50%;
}
.panel-body>.col-md-8 select{
    width: calc(50% - 115px);
}
.panel-body>div{
    min-height: 50px;
    margin: 7px 0px;
}
.panel-body>div>p{
    float: left;
    width: 200px;
    font-size: 14px;
    height: 100%;
    line-height: 50px;
    text-align: center;
}
.panel-body>div input{
    float: left;
    width: calc(100% - 200px);
    font-size: 14px;
    height: 35px;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #DCDFE6;
}

.panel-body>div>select{
    float: left;
    width: calc(100% - 200px);
    font-size: 14px;
    height: 35px;
    padding:0 10px;
    margin-top: 5px;
    border: 1px solid #DCDFE6;
}
.panel-body>div>textarea{
    float: left;
    width: calc(100% - 200px);
    font-size: 14px;
    height: 60px;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #DCDFE6;
}
.panel-heading {
    height: 46px;
    padding: 0;
}
.sub-nav{
    position:initial
}
.ss {
    margin-left: -3px;
    margin-top: -2px;
    height: 34px;
}

.rights {
    float: right;
    height: 32px;
}

.search {
    margin-bottom: 10px;
}

.el-date-editor {
    width: 250px;
    height: 34px;
}

.el-date-editor * {
    line-height: 30px !important;
    height: 34px;
}

.el-input__inner {
    height: 34px;
}

.el-input__icon {
    line-height: 29px !important;
}

.panel-default>.panel-heading {
    background-color: white;
}

.layui-btn {
    height: 34px;
    line-height: 34px;
}

.form-control {
    display: inline-block;
    width: 200px;
}

.content {
    top: 50px;
}

a {
    text-decoration: none;
}

.chart_li {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

[v-cloak] {
    display: none;
}

a {
    text-decoration: none;
}

.wrap-content>.wrap-scroll-box>.wrap-scroll-content>.home {
    padding-top: 0;
}

.small-box {
    border-radius: 2px;
    position: relative;
    display: block;
    margin-bottom: 20px;
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
    height: 155px;
    color: #fff;
}

.small-box-h {
    position: absolute;
    top: 0;
    right: 0;
    width: 35%;
    height: 100%;
    padding-top: 20px;
}

.small-box-c {
    padding: 5px 30px;
}

.box-detail {
    color: white;
    text-decoration: none;
}

.box-detail:hover {
    text-decoration: none;
}

.bg-aqua {
    background-color: #4c9cff !important;
}

.bg-green {
    background-color: #7c79b6 !important;
}

.bg-yellow {
    background-color: #58c386 !important;
}

.bg-red {
    background-color: #efb04e !important;
}

.bg-aqua-h {
    background-color: #4790eb !important;
}

.bg-green-h {
    background-color: #7270a8 !important;
}

.bg-yellow-h {
    background-color: #51b47b !important;
}

.bg-red-h {
    background-color: #dca249 !important;
}

.home .panel {
    border-radius: 0;
    border: 1px solid #eee;
    box-shadow: none;
}

.home *[class^="col-md"] {
    padding-left: 10px;
    padding-right: 10px;
}

.line-chart {
    position: relative;
}

.panel-btns1 {
    position: absolute;
    top: 0;
    right: 10px;
}

.panel-btns1 a {
    display: block;
    margin-bottom: 5px;
    text-decoration: none;
}

.panel-title2 {
    float: left;
}

.panel-btns2 {
    float: right;
}

.layui-form-label {
    width: auto;
}
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
    border: 1px solid;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }

</style>
