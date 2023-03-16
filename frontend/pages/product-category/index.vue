<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Категория продуктов</h1>
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
        <flowbite-ui-button
            @click="addModalForm"
            buttonColor="blue"
            buttonText="Добавить"
        />
      </div>

    </div>
  </div>
</template>

<script setup>
import {productCategoryAddFormSettings } from "~/utils/forms";
import {productCategoryTableSettings } from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import {useKitchenStore} from "~/store/kitchenStore";
import {emitFormDataMixin} from "~/mixins/emitFormDataMixin";

const kitchenStore = useKitchenStore();


const {data: productCategories} = await useAsyncData('product-category', () => kitchenStore.fetchItems('product-category'));
const productCategoryRefresh = () => refreshNuxtData('product-category')
const searchItems = (search) => {
  productCategories.value = kitchenStore.getItemsBySearch(search, 'category');
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

const emitFormData = (data, action) => {
  emitFormDataMixin(data, action, 'product-category', closeModal, alerting);
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