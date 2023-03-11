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
        :columnNames="productCategoryTableSettings.columns"
        :columnValues="productCategories"
        @modalFormDetail="modalFormDetail"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="productCategoryAddFormSettings"
          :fetchingData="productCategory"
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
  productCategoryAddFormSettings,
  productCategoryAlertSettings,
  productCategoryDeleteAlertSettings,
  productCategoryEditAlertSettings,
  productCategoryTableSettings
} from "~/utils/productCategoryUtils";

import {useProductCategoryStore} from "~/store/productCategoryStore";

const productCategoryStore = useProductCategoryStore();


const {data: productCategories} = await useAsyncData('productCategory', () => productCategoryStore.fetchProductCategories());
const productCategoryRefresh = () => refreshNuxtData('productCategory')
const searchItems = (search) => {
  productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}


const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(productCategoryAddFormSettings);
const productCategory = ref({});

const addModalForm = () => {
  productCategory.value = {};
  formSettings.value.modalTitle = `Добавить категорию`;
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  showModal.value = false;
  productCategoryRefresh();
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
    await productCategoryStore.addProductCategory(data);
    closeModal();
    alerting(productCategoryAlertSettings);
  } else if (action === 'updateItem') {
    await productCategoryStore.updateProductCategory(data);
    closeModal();
    alerting(productCategoryEditAlertSettings);
  } else if (action === 'deleteItem') {
    await productCategoryStore.deleteProductCategory(data);
    closeModal();
    alerting(productCategoryDeleteAlertSettings);
  }
}


const closeAlert = () => {
  showAlert.value = false;

}
const modalFormDetail = (id) => {
  productCategory.value = productCategories.value.find(productCategory => productCategory.id === id);
  formSettings.value.modalTitle = `Редактировать категорию - ${productCategory.value.name}`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  showModal.value = true;
}

</script>

<style scoped>

</style>