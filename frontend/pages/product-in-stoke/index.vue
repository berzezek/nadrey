<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Категория продуктов</h1>
    <div class="md:flex mb-3">

      <flowbite-block-search
          @searchItems="searchItems"
      />
    </div>
    <flowbite-block-table
        :columnNames="productStokeTableSettings.columns"
        :columnValues="productsStock"
        @modalFormDetail="modalFormDetail"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="productCategoryAddFormSettings"
          :fetchingData="productStoke"
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
import {
  productStokeAddFormSettings,
  productStokeAlertSettings,
  productStokeDeleteAlertSettings,
  productStokeEditAlertSettings,
  productStokeTableSettings
} from "~/utils/productStokeUtils";

import { useProductStokeStore } from "~/store/productStockStore";
import { useProductCategoryStore } from "~/store/productCategoryStore";

const productStockStore = useProductStokeStore();
const productCategoryStore = useProductCategoryStore();

const { data: productsStock } = await useAsyncData('productsStock', () => productStockStore.fetchProductsStoke());
const { data: productCategory } = await useAsyncData('productCategory', () => productCategoryStore.fetchProductCategories())
const productStockRefresh = () => refreshNuxtData('productsStoke');
const searchItems = (search) => {
  console.log(search);
  // productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}


const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(productCategoryAddFormSettings);
const productStoke = ref({});

const addModalForm = () => {
  productStoke.value = {};
  formSettings.value.modalTitle = `Добавить продукт на склад`;
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  showModal.value = false;
  productStockRefresh();
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
    // await productStockStore.addProductCategory(data);
    closeModal();
    alerting(productCategoryAlertSettings);
  } else if (action === 'updateItem') {
    // await productStockStore.updateProductCategory(data);
    closeModal();
    alerting(productCategoryEditAlertSettings);
  } else if (action === 'deleteItem') {
    // await productStockStore.deleteProductCategory(data);
    closeModal();
    alerting(productCategoryDeleteAlertSettings);
  }
}


const closeAlert = () => {
  showAlert.value = false;

}
const modalFormDetail = (id) => {
  productStoke.value = productStoke.value.find(productStoke => productStoke.id === id);
  formSettings.value.modalTitle = `Редактировать продукт - ${productStoke.value.name}`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  showModal.value = true;
}

</script>

<style scoped>

</style>