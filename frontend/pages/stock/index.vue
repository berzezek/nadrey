<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Склады</h1>
    <div class="md:flex mb-3">
      <flowbite-block-search
          @searchItems="searchItems"
      />
    </div>
    <flowbite-block-table
        :columnNames="stockTableSettings.columns"
        :columnValues="stocks"
        @modalFormDetail="modalFormDetail"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="stockAddFormSettings"
          :fetchingData="stock"
          @closeModal="closeModal"
          @addModalForm="addModalForm"
          @emitFormData="emitFormData"
      />
      <div class="flex items-between">

        <button
            type="button"
            @click="addModalForm"
            class="mt-3 ml-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
          Добавить
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import {stockAddFormSettings} from "~/utils/forms";
import {stockTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import { useKitchenStore } from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: stocks} = await useLazyAsyncData('stock', () => kitchenStore.fetchItems('stock'));

const stocksRefresh = () => refreshNuxtData('stock')

const searchItems = (search) => {
  stocks.value = kitchenStore.getItemsBySearch(search, 'name');
}

const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(stockAddFormSettings);
const stock = ref({});

const addModalForm = () => {
  stock.value = {};
  formSettings.value.modalTitle = `Добавить склад`;
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  showModal.value = false;
  stocksRefresh();
}

const alerting = (data) => {
  alertSettings.value = data
  showAlert.value = true;
    setTimeout(() => {
      showAlert.value = false;
    }, 5000)
}

const alertSettings = ref({});

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    await kitchenStore.addItem(data, 'stock');
    closeModal();
    alerting(itemAlertSettings);
  } else if (action === 'updateItem') {
    console.log(data)
    await kitchenStore.updateItem(data, data.id, 'stock');
    closeModal();
    alerting(itemEditAlertSettings);
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, 'stock');
    closeModal();
    alerting(itemDeleteAlertSettings);
  }
}

const closeAlert = () => {
  showAlert.value = false;
}

const modalFormDetail = (id) => {
  stock.value = stocks.value.find(stock => stock.id === id);
  formSettings.value.modalTitle = `Редактировать склад`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  showModal.value = true;
}

</script>

<style scoped>

</style>