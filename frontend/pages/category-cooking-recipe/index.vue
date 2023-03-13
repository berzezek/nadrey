<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Категории рецептов</h1>
    <div class="md:flex mb-3">

      <flowbite-block-search
          @searchItems="searchItems"
      />
    </div>
    <flowbite-block-table
        :columnNames="recipeCategoryTableSettings.columns"
        :columnValues="receiptsCategory"
        @modalFormDetail="modalFormDetail"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="recipeAddFormSettings"
          :fetchingData="recipeCategory"
          @closeModal="closeModal"
          @addModalForm="addModalForm"
          @emitFormData="emitFormData"
      />
      <div class="flex items-between">
        <flowbite-ui-button
            @click="addModalForm"
            buttonColor="blue"
            buttonText="Добавить категорию рецептов"
        />
      </div>

    </div>
  </div>
</template>

<script setup>
import {recipeCategoryAddFormSettings} from "~/utils/forms";
import {recipeCategoryTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: receiptsCategory} = await useAsyncData('category-cooking-recipe', () => kitchenStore.fetchItems('category-cooking-recipe'));
const recipeCategoryRefresh = () => refreshNuxtData('category-cooking-recipe');
const searchItems = (search) => {
  console.log(search);
  // productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}

const showModal = ref(false);


const showAlert = ref(false);
const formSettings = ref(recipeAddFormSettings);

const recipeCategory = ref({});
const addFormSelect = () => {

}

const addModalForm = () => {
  recipeCategory.value = {};
  formSettings.value.modalTitle = `Добавить рецепт`;
  addFormSelect();
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  showModal.value = false;
  recipeCategoryRefresh();
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
    await kitchenStore.addItem(data, 'category-cooking-recipe');
    closeModal();
    alerting(itemAlertSettings);
  } else if (action === 'updateItem') {
    await kitchenStore.updateItem(data, data.id,'category-cooking-recipe');
    closeModal();
    alerting(itemEditAlertSettings);
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, 'category-cooking-recipe');
    closeModal();
    alerting(itemDeleteAlertSettings);
  }
}


const closeAlert = () => {
  showAlert.value = false;

}
const modalFormDetail = (id) => {
  recipeCategory.value = receiptsCategory.value.find(product => product.id === id);
  formSettings.value.modalTitle = `Редактировать категорию рецептов`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addFormSelect();
  showModal.value = true;
}

</script>

<style scoped>

</style>