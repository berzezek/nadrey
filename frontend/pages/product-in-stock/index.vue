<template>
  <div class="">
    <h1 class="text-xl text-blue-800 text-center mb-4">Продукты на складе</h1>
    <flowbite-block-table
        :columnNames="productStockTableSettings.columns"
        :columnValues="productsBalance"
        :newButton="{text: 'Добавить продукт на склад', color: 'blue'}"
        @new-button-click="$router.push('/product-in-stock/edit')"
        @addModalForm="$router.push('/stock')"
        @search="searchItems"
    />


  </div>
</template>

<script setup>
import {productStockTableSettings} from "~/utils/tables";

import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: productsBalance} = await useAsyncData('product-balance', () => kitchenStore.fetchItems('stock-balance'));
const searchItems = (search) => {
  productsBalance.value = kitchenStore.getItemsBySearch(search, 'product__name');
}


</script>

<style scoped>

</style>