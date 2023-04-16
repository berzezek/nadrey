<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Транзакции продуктов на складе</h1>

    <flowbite-block-table
        :columnNames="productStockEditTableSettings.columns"
        :columnValues="productsStock"
        @modalFormDetail="modalFormDetail"
        @addModalForm="addModalForm"
        @search="searchItems"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="productStockAddFormSettings"
          :fetchingData="productStock"
          @closeModal="closeModal"
          @addModalForm="addModalForm"
          @emitFormData="emitFormData"
      />

    </div>
  </div>
</template>

<script setup>
import {productStockAddFormSettings} from "~/utils/forms";
import {productStockEditTableSettings} from "~/utils/tables";

import {useKitchenStore} from "~/store/kitchenStore";
import {emitFormDataMixin} from "~/mixins/emitFormDataMixin";

const kitchenStore = useKitchenStore();

const {data: store} = await useAsyncData('stock', () => kitchenStore.fetchItems('stock'));
const {data: products} = await useAsyncData('products', () => kitchenStore.fetchItems('product'));

const {data: productsStock} = await useAsyncData('product-stock', () => kitchenStore.fetchItems('product-in-stock'));
const productsStockRefresh = () => refreshNuxtData('product-stock');

const searchItems = (searchText) => {
  productsStock.value = kitchenStore.getItemsBySearch(searchText, 'product_name');
}

const showModal = ref(false);


const showAlert = ref(false);
const formSettings = ref(productStockAddFormSettings);

const productStock = ref({});
const addFormSelect = () => {
  const productSelectField = {
    title: 'Продукт *',
    type: 'text',
    name: 'product',
    required: true,
    method: 'select',
    selectValue: products.value,
  }
  const stockSelectField = {
    title: 'Склад *',
    type: 'text',
    name: 'store',
    required: true,
    method: 'select',
    selectValue: store.value,
  }
  formSettings.value.formFields.splice(formSettings.value.formFields.findIndex(
      field => field.name === 'product'), 1, productSelectField)
  formSettings.value.formFields.splice(formSettings.value.formFields.findIndex(
      field => field.name === 'store'), 1, stockSelectField)

}

const addModalForm = () => {
  productStock.value = {};
  formSettings.value.modalTitle = `Добавить продукт на склад`;
  addFormSelect();
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  productsStockRefresh();
  showModal.value = false;
}

const alerting = (data) => {
  alertSettings.value = data
  showAlert.value = true;
  setTimeout(() => {
    showAlert.value = false;
  }, 5000)
}

const alertSettings = ref({});

const emitFormData = (data, action) => {
  emitFormDataMixin(data, action, 'product-in-stock', closeModal, alerting);
}

const closeAlert = () => {
  showAlert.value = false;

}
const modalFormDetail = (id) => {
  productStock.value = productsStock.value.find(product => product.id === id);
  formSettings.value.modalTitle = `Редактировать продукт - `;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addFormSelect();
  showModal.value = true;
}

</script>

<style scoped>

</style>