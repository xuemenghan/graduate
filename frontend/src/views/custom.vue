<template>
  <div>
    <app-slider1></app-slider1>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="id"
        label="ID"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="用户昵称"
        width="180">
      </el-table-column>
      <el-table-column
        prop="sex"
        label="性别"
        width="180">
      </el-table-column>
      <el-table-column
        prop="telephone"
        label="手机号码"
        width="180">
      </el-table-column>
      <el-table-column
        prop="last_time"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址">
      </el-table-column>
      <el-table-column
      fixed="right"
      label="操作"
      width="100">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row.id)" type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
  export default {
    name: "custom",
    data() {
      return {
        tableData: [],
        username: ''
      }
    },
    created (){
      var vm = this;
      vm.getCus();
    },
    methods: {
      getCus() {
        var vm = this;
        $.ajax({
          url: `${SITE_URL}register/get_cus/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {
            goods_num: vm.goods_num
          },
          success: function (data) {
            if (data.code === 0) {
              vm.tableData = data.data
            }
          }
        });
      },
      handleClick(row) {
        console.log(row);
        var vm = this;
        $.ajax({
          url: `${SITE_URL}register/dele_cus/`,
          dataType: 'json',
          type: 'POST',
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          data: {
            id: row
          },
          success: function (data) {
            if (data.code === 0) {
              vm.getCus()
            }
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>
