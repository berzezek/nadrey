<template>
<h1>Product</h1>
  {{products}}

  <product-table />
</template>

<script setup>
import {useProductStore} from "~/store/product";
const productStore = useProductStore();
productStore.fetchProducts();
const products = computed(() => productStore.products);
</script>

<style scoped>

</style>