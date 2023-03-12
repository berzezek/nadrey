<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Продукты</h1>
    <div class="md:flex mb-3">
      <flowbite-block-dropdownselect
          :select-text="'Выбрать категорию'"
          :searchSelect="'product-category'"
          @changeSelect="changeSelect"
      />
      <flowbite-block-search
          @searchItems="searchItems"
      />
    </div>
    <flowbite-block-table
        :columnNames="productTableSettings.columns"
        :columnValues="products"
        @modalFormDetail="modalFormDetail"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="productAddFormSettings"
          :fetchingData="product"
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

        <button
            type="button"
            @click="$router.push('/product-category')"
            class="mt-3 ml-3 text-white bg-green-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
          Добавить категорию
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import {productAddFormSettings} from "~/utils/forms";
import {productTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import { useKitchenStore } from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: products} = await useLazyAsyncData('product', () => kitchenStore.fetchItems('product'));
const {data: productCategories} = await useLazyAsyncData('product-category', () => kitchenStore.fetchItems('product-category'));

const productsRefresh = () => refreshNuxtData('product')
const changeSelect = (categoryId) => {
  products.value = kitchenStore.getItemsById(categoryId, 'category');
}

const searchItems = (search) => {
  products.value = kitchenStore.getItemsBySearch(search, 'product');
}

const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(productAddFormSettings);
const product = ref({});

const addProductCategorySelect = () => {
  const categorySelectField = {
    title: 'Категория',
    type: 'text',
    name: 'category',
    required: true,
    method: 'select',
    selectValue: productCategories.value,
  }
  if (formSettings.value.formFields.length === 5) {
    formSettings.value.formFields.push(categorySelectField)
  }
}

const addModalForm = () => {
  product.value = {};
  formSettings.value.modalTitle = `Добавить продукт`;
  addProductCategorySelect();
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  showModal.value = false;
  productsRefresh();
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
    await kitchenStore.addItem(data, 'product');
    closeModal();
    alerting(itemAlertSettings);
  } else if (action === 'updateItem') {
    console.log(data)
    await kitchenStore.updateItem(data, data.id, 'product');
    closeModal();
    alerting(itemEditAlertSettings);
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, 'product');
    closeModal();
    alerting(itemDeleteAlertSettings);
  }
}

const closeAlert = () => {
  showAlert.value = false;
}

const modalFormDetail = (id) => {
  product.value = products.value.find(product => product.id === id);
  formSettings.value.modalTitle = `Редактировать продукт - ${product.value.name}`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addProductCategorySelect();
  showModal.value = true;
}

</script>

<style scoped>

</style>