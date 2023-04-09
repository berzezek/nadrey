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
        :filters="productCategories"
        :new-button="{text: 'Добавить категорию', color: 'blue'}"
        @modalFormDetail="modalFormDetail"
        @addModalForm="addModalForm"
        @newButtonClick="$router.push('/product-category')"
        @emitFormData="emitFormData"
        @search="searchItems"
        @filter="filter"

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

import {useKitchenStore} from "~/store/kitchenStore";
import {emitFormDataMixin} from "~/mixins/emitFormDataMixin";

const kitchenStore = useKitchenStore();

const {data: productCategories} = await useAsyncData('product-category', () => kitchenStore.fetchItems('product-category'));
const {data: products} = await useAsyncData('product', () => kitchenStore.fetchItems('product'));

const productsRefresh = () => refreshNuxtData('product')
const productCategoriesRefresh = () => refreshNuxtData('product-category')

const filter = (categoryId) => {
  console.log(categoryId)
  if (!categoryId) {
    productsRefresh();
    return;
  }
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
  productCategoriesRefresh();
  const categorySelectField = {
    title: 'Категория *',
    type: 'text',
    name: 'category',
    required: true,
    method: 'select',
    selectValue: productCategories.value,
  }
  if (!formSettings.value.formFields.find(field => field.name === 'category')) {
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
  productsRefresh();
  productCategoriesRefresh();
  showModal.value = false;
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