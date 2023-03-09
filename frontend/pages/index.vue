<template>
<h1>Hello</h1>
</template>

<script setup>
import {useProductStore} from "~/store/productStore";

const productStore = useProductStore();

const {data: products} = await useAsyncData('product', () => productStore.fetchProducts());
console.log(products.value)
</script>

<style scoped>

</style>