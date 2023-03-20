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
    </div>
    <flowbite-block-table
        :columnNames="productTableSettings.columns"
        :columnValues="products"
        :new-button="{color: 'blue', text: 'Добавить категорию'}"
        @modalFormDetail="modalFormDetail"
        @addModalForm="addModalForm"
        @emitFormData="emitFormData"
        @search="searchItems"
        @new-button-click="$router.push('/product-category')"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="productAddFormSettings"
          :fetchingData="product"
          @closeModal="closeModal"
          @emitFormData="emitFormData"
      />

    </div>
  </div>
</template>

<script setup>
import {productAddFormSettings} from "~/utils/forms";
import {productTableSettings} from "~/utils/tables";

import { useKitchenStore } from "~/store/kitchenStore";
import {emitFormDataMixin} from "~/mixins/emitFormDataMixin";

const kitchenStore = useKitchenStore();

const router = useRouter();

const {data: products} = await useLazyAsyncData('product', () => kitchenStore.fetchItems('product'));
const {data: productCategories} = await useLazyAsyncData('product-category', () => kitchenStore.fetchItems('product-category'));

const productsRefresh = () => refreshNuxtData('product')
const changeSelect = (categoryId) => {
  products.value = kitchenStore.getItemsById(categoryId, 'category');
}

const searchItems = (searchText) => {
  products.value = kitchenStore.getItemsBySearch(searchText, 'name');
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

const alertSettings = ref({});
const alerting = (data) => {
  alertSettings.value = data
  showAlert.value = true;
  setTimeout(() => {
      showAlert.value = false;
    }, 5000)

}

const emitFormData = (data, action) => {
  emitFormDataMixin(data, action, 'product', closeModal, alerting);
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