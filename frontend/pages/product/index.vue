<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Продукты</h1>
    <flowbite-block-table
        :columnNames="productTableSettings.columns"
        :columnValues="products"
        :searchSelect="productCategories"
        @filterRadio="filterRadio"
        @searchItems="searchItems"
        @modalFormDetail="modalFormDetail"
        @changePage="changePage"
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
import {productAddFormSettings} from "~/utils/formSettings";
import {
  productAlertSettings,
  productDeleteAlertSettings,
  productEditAlertSettings,
  productTableSettings
} from "~/utils/productTable";

import {useProductStore} from "~/store/productStore";
import {useProductCategoryStore} from "~/store/productCategoryStore";

const productStore = useProductStore();
const productCategoryStore = useProductCategoryStore();

const {
  data: products,
  pending,
  error,
} = await useAsyncData('product', () => productStore.fetchProducts());
const {data: productCategories} = await useAsyncData('productCategory', () => productCategoryStore.fetchProductCategories());
const productsRefresh = () => refreshNuxtData('product')
const filterRadio = (categoryId) => {
  products.value = productStore.getProductsByCategory(categoryId);
}

const searchItems = (search) => {
  products.value = productStore.getProductsBySearch(search);
}


const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(productAddFormSettings);
const product = ref({});

const addModalForm = () => {
  product.value = {};
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
    await productStore.addProduct(data);
    closeModal();
    alerting(productAlertSettings);
  } else if (action === 'updateItem') {
    console.log(data)
    await productStore.updateProduct(data);
    closeModal();
    alerting(productEditAlertSettings);
  } else if (action === 'deleteItem') {
    await productStore.deleteProduct(data);
    closeModal();
    alerting(productDeleteAlertSettings);
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
  showModal.value = true;
}

const changePage = (page) => {
  console.log(page)
}

</script>

<style scoped>

</style>