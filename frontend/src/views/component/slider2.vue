<template>
    <div class="main-nav">
      <div class="inner-cont0">
        <div class="inner-cont1 w1200">
          <div class="inner-cont2">
            <router-link :to="{path:'/commodity'}">所有商品</router-link>
            <router-link :to="{path:'/discount'}"><a>今日团购</a></router-link>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "slider2"
    }
</script>

<style scoped>

</style>
