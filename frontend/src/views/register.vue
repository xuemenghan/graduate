<template>
  <div class="body">
    <app-slider1></app-slider1>
    <div class="bk"></div>
    <div class="login-form" style="transform: translate(380px)">
      <h1>注册</h1>
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="ruleForm.username" class="el-form"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
          <el-input type="password" v-model="ruleForm.pass" class="el-form"></el-input>
        </el-form-item>

        <el-form-item label="确认密码" prop="pass2">
          <el-input type="password"  v-model="ruleForm.pass2" class="el-form"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="telephone">
          <el-input v-model="ruleForm.telephone" class="el-form"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-radio-group v-model="ruleForm.sex">
            <el-radio label="1" value="1">男</el-radio>
            <el-radio label="0" value="0">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="收货地址" prop="address">
          <el-input type="textarea" v-model="ruleForm.address" class="el-form"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "register",
  data() {
    let xxx = (rule, value, callback) => {
      let reg = /[0-9a-zA-Z]{4,9}/
      if(!reg.test(value)){
        callback(new Error('账号必须是由4-9位数字和字母组合'))
      }else{
        callback()
      }
    }
    let checkPass = (rule, value, callback) => {
      let reg = /^.*(?=.{6,})(?=.*\d)(?=.*[a-zA-Z]).*$/
      if(!reg.test(value)){
        callback(new Error('密码最少6位以上，包括数字和字母'))
      }else{
        callback()
      }
    }
    let checkPass2 = (rule, value, callback) =>{
      let vm = this
      if ( vm.ruleForm.pass != value){
        callback(new Error('密码不一致'))
      }else {
        callback()
      }
    }
    let checkPhone = (rule, value, callback) => {
      let reg = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/
      if(!reg.test(value)){
        callback(new Error('请输入正确的手机号'))
      }else{
        callback()
      }
    }
    return {
      ruleForm: {
        username: '',
        pass: '',
        pass2: '',
        telephone: '',
        sex: '',
        address: ''
      },
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 5, max: 15, message: '长度在 5 到 15 个字符', trigger: 'blur'},
          // {validator: xxx, trigger: 'blur'}
        ],
        pass: [
          {required: true, message: '请输入密码', trigger: 'change'},
          // {type: 'password', message: '111', trigger: 'blur'},
          {validator: checkPass, trigger: 'blur'}
        ],
        pass2: [
          {required: true, message: '请输入密码', trigger: 'change'},
          // {type: 'password', message: '111', trigger: 'blur'},
          {validator: checkPass2, trigger: 'blur'}
        ],
        telephone: [
          {required: true, message: '请输入电话', trigger: 'change'},
          {validator: checkPhone, trigger: 'blur'}
        ],
        sex: [
          {required: true, message: '请选择性别', trigger: 'change'}
        ],
        address: [
          {required: true, message: '请输入收货地址', trigger: 'blur'}
        ]
      }

    }
  },
  created() {
    // console.log(this.account)
    console.log(this)
  },
  methods: {
    submitForm(formName) {
      var vm = this;
      this.$refs[formName].validate((valid) => {
        if (valid) {
          } else {
            alert('请将信息填写完整！');
            console.log('error submit!!');
            return false;
          }
        });
      $.ajax({
        url: `${SITE_URL}register/register/`,
        dataType: 'json',
        type: 'POST',
        xhrFields: {
          withCredentials: true
        },
        crossDomain: true,
        data: {
          username: vm.ruleForm.username,
          pass: vm.ruleForm.pass,
          telephone: vm.ruleForm.telephone,
          sex: vm.ruleForm.sex,
          address: vm.ruleForm.address,
          // result: vm.ruleForm.result,
        },
        success: function (data) {
          if (data.code === 0) {
            vm.$router.push({name:'login'})
          }
        }
      });
    },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
    push() {
      console.log(111)
    }
  }
}
</script>

<style scoped>
  .body {
    font-family: 'Montserrat', sans-serif;
    font-size: 100%;
    background: url(../assets/images/bg2.jpg) no-repeat;
    background-size: 100% 125%;
    display: block;
  }

  .login-form {
    padding: 100px 0px 50px 0px;
    width: 500px;
    transform: translateX(430px);

  }
  .bk{
    background-color: white;
    width: 700px;
    z-index: 0;
  }
  .el-form{
    width: 370px;
  }
</style>
