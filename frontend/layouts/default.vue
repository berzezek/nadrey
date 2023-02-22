<template>
  <nav-main-header/>
  <nav-main-sidebar/>
  <div class="sm:ml-64">
    <slot />
  </div>
  <nav-main-footer/>
</template>

<script>
export default {
  name: "default"
}
</script>

<style scoped>

</style>