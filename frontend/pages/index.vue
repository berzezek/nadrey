<template>
  <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Заказы</h1>
  <flowbite-block-table
      :columnNames="orderTableSettings.columns"
      :columnValues="cards"
      @addModalForm="addModalForm"
      @modalFormDetail="modalFormDetail"
  />
</template>

<script setup>
import {orderTableSettings} from "~/utils/tables";
import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();
const {data: cards} = await useAsyncData('cards', () => kitchenStore.fetchItems('card'));

const modalFormDetail = (id) => {
  console.log('modalFormDetail', id)
}

const addModalForm = () => {
  console.log('addModalForm')
}

</script>

<style scoped>

</style>