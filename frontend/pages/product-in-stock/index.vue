<template>
  <div class="">
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Продукты на складе</h1>
    <div class="md:flex mb-3">
      <flowbite-block-search
          @searchItems="searchItems"
      />
    </div>
    <flowbite-block-table
        :columnNames="productStockTableSettings.columns"
        :columnValues="productsBalance"
    />

    <div class="flex items-center">
      <flowbite-ui-button
          @click="$router.push('/stock')"
          buttonColor="green"
          buttonText="Добавить склад"
      />
      <flowbite-ui-button
          @click="$router.push('/product-in-stock/edit')"
          buttonColor="blue"
          buttonText="Редактировать склад"
      />
    </div>

  </div>
</template>

<script setup>
import {productStockTableSettings} from "~/utils/tables";

import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: productsBalance} = await useAsyncData('product-balance', () => kitchenStore.fetchItems('stock-balance'));
const searchItems = (search) => {
  console.log(search);
  // productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}


</script>

<style scoped>

</style>