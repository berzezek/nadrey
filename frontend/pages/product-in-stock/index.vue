<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Продукты на складе</h1>
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
          :formSettings="productStockAddFormSettings"
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
        <button
            type="button"
            @click="$router.push('/stock')"
            class="mt-3 ml-3 text-white bg-green-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
          Добавить склад
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import {productStockAddFormSettings} from "~/utils/forms";
import {productStokeTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: productsStock} = await useAsyncData('product-stock', () => kitchenStore.fetchItems('product-in-stock'));
const {data: store} = await useAsyncData('stock', () => kitchenStore.fetchItems('stock'));
const {data: products} = await useAsyncData('products', () => kitchenStore.fetchItems('product'));
const productStockRefresh = () => refreshNuxtData('product-stock');
const searchItems = (search) => {
  console.log(search);
  // productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}

const showModal = ref(false);


const showAlert = ref(false);
const formSettings = ref(productStockAddFormSettings);

const productStoke = ref({});
const addFormSelect = () => {
  const productSelectField = {
    title: 'Продукт',
    type: 'text',
    name: 'product',
    required: true,
    method: 'select',
    selectValue: products.value,
  }
  const stockSelectField = {
    title: 'Склад',
    type: 'text',
    name: 'store',
    required: true,
    method: 'select',
    selectValue: store.value,
  }
  if (!formSettings.value.formFields.some(field => field.title === 'Склад')) {
    formSettings.value.formFields.unshift(stockSelectField)
  }
  if (!formSettings.value.formFields.some(field => field.title === 'Продукт')) {
    formSettings.value.formFields.unshift(productSelectField)
  }
}

const addModalForm = () => {
  productStoke.value = {};
  formSettings.value.modalTitle = `Добавить продукт на склад`;
  addFormSelect();
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
    data.transaction_type = 'in'
    await kitchenStore.addItem(data, 'product-in-stock');
    closeModal();
    alerting(itemAlertSettings);
  } else if (action === 'updateItem') {
    // await productStockStore.updateProductCategory(data);
    closeModal();
    alerting(itemEditAlertSettings);
  } else if (action === 'deleteItem') {
    // await productStockStore.deleteProductCategory(data);
    closeModal();
    alerting(itemDeleteAlertSettings);
  }
}


const closeAlert = () => {
  showAlert.value = false;

}
const modalFormDetail = (id) => {
  productStoke.value = productsStock.value.find(product => product.id === id);
  formSettings.value.modalTitle = `Редактировать продукт - `;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addFormSelect();
  showModal.value = true;
}

</script>

<style scoped>

</style>