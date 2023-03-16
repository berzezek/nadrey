<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Рецепты</h1>
    <flowbite-block-table
        :columnNames="recipeTableSettings.columns"
        :columnValues="receipts"
        @modalFormDetail="modalFormDetail"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="recipeAddFormSettings"
          :fetchingData="recipe"
          @closeModal="closeModal"
          @addModalForm="addModalForm"
          @emitFormData="emitFormData"
      />
      <div class="flex items-between">
        <flowbite-ui-button
            @click="addModalForm"
            buttonColor="blue"
            buttonText="Добавить рецепт"
        />
        <flowbite-ui-button
            @click="$router.push('/category-cooking-recipe')"
            buttonColor="blue"
            buttonText="Добавить категорию рецептов"
        />
      </div>

    </div>
  </div>
</template>

<script setup>
import {recipeAddFormSettings} from "~/utils/forms";
import {recipeTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import {useKitchenStore} from "~/store/kitchenStore";

const router = useRouter();

const kitchenStore = useKitchenStore();

const {data: receipts} = await useAsyncData('recipe', () => kitchenStore.fetchItems('recipe-balance'));
const recipeRefresh = () => refreshNuxtData('recipe');
const searchItems = (search) => {
  console.log(search);
  // productCategories.value = productCategoryStore.getProductCategoryBySearch(search);
}

const showModal = ref(false);


const showAlert = ref(false);
const formSettings = ref(recipeAddFormSettings);

const recipe = ref({});


const addModalForm = () => {
  recipe.value = {};
  formSettings.value.modalTitle = `Добавить рецепт`;
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  showModal.value = false;
  recipeRefresh();
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
    await kitchenStore.addItem(data, 'recipe');
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
  router.push(`/cooking-recipe/${id}`);
}

</script>

<style scoped>

</style>