<template>
  <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Заказы</h1>
  <flowbite-block-table
      :columnNames="orderTableSettings.columns"
      :columnValues="cards"
      @modalFormDetail="modalFormDetail"
  />
</template>

<script setup>
import {orderTableSettings} from "~/utils/tables";
import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();
const {data: cards} = await useAsyncData('cards', () => kitchenStore.fetchItems('card'));

console.log('orders', cards.value)
const modalFormDetail = (id) => {
  console.log('modalFormDetail', id)
}

</script>

<style scoped>

</style>