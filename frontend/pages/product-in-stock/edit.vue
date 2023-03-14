<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Транзакции продуктов на складе</h1>
    <div class="md:flex mb-3">

      <flowbite-block-search
          @searchItems="searchItems"
      />
    </div>
    <flowbite-block-table
        :columnNames="productStockEditTableSettings.columns"
        :columnValues="productsStock"
        @modalFormDetail="modalFormDetail"
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
      <div class="flex items-between">
        <flowbite-ui-button
            @click="addModalForm"
            buttonColor="blue"
            buttonText="Добавить транзакцию"
        />
      </div>

    </div>
  </div>
</template>

<script setup>
import {productStockAddFormSettings} from "~/utils/forms";
import {productStockEditTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: productsStock} = await useAsyncData('product-stock', () => kitchenStore.fetchItems('product-in-stock'));
const productsStockRefresh = () => refreshNuxtData('product-stock');


const {data: store} = await useAsyncData('stock', () => kitchenStore.fetchItems('stock'));
const {data: products} = await useAsyncData('products', () => kitchenStore.fetchItems('product'));
const searchItems = (search) => {
  console.log(search);
  // productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}

const showModal = ref(false);


const showAlert = ref(false);
const formSettings = ref(productStockAddFormSettings);

const productStock = ref({});
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

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    console.log(data)
    await kitchenStore.addItem(data, 'product-in-stock');
    closeModal();
    alerting(itemAlertSettings);
  } else if (action === 'updateItem') {
    await kitchenStore.updateItem(data, data.id, 'product-in-stock');
    closeModal();
    alerting(itemEditAlertSettings);
  } else if (action === 'deleteItem') {
    console.log(data)
    await kitchenStore.deleteItem(data, 'product-in-stock');
    closeModal();
    alerting(itemDeleteAlertSettings);
  }
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