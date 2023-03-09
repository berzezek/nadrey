<template>
  <flowbite-block-header/>
<!--  <flowbite-block-aside/>-->
  <div class="lg:p-12 md:p-2">
    <slot/>
  </div>
  <flowbite-block-footer/>
</template>

<script>
export default {
  name: "index"
}
</script>

<style scoped>

</style>