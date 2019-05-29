<template>

</template>

<script>
  export default {
    name: "test",
    methods: {
      left() {
        $("button").click(function () {
          $("#cs").animate({left: '250px'});
        });
      }
    }
  }
</script>

<style scoped>

</style>
