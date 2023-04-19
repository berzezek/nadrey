<template>
  <flowbite-block-header/>
<!--  <flowbite-block-aside/>-->
  <div class="lg:p-12 md:p-2 main">
    <slot/>
<!--    <div class="container flex justify-end">-->
<!--      <flowbite-ui-button-->
<!--          @click="$router.go(-1)"-->
<!--          buttonColor="blue"-->
<!--          buttonText="<-"-->
<!--      />-->
<!--      <flowbite-ui-button-->
<!--          @click="$router.go(1)"-->
<!--          buttonColor="blue"-->
<!--          buttonText="->"-->
<!--      />-->
<!--    </div>-->
  </div>
<!--  <flowbite-block-footer/>-->
</template>

<script>
export default {
  name: "index"
}
</script>

<style>
body {
  background-image: url('public/food.png');
}

</style>