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
        :new-button="{text: 'Добавить категорию рецептов', color: 'blue'}"
        @modalFormDetail="modalFormDetail"
        @addModalForm="addModalForm"
        @newButtonClick="$router.push('/category-cooking-recipe')"
        @emitFormData="emitFormData"
        @search="searchItems"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="recipeIngredientAddFormSettings"
          :fetchingData="recipe"
          @closeModal="closeModal"
          @emitFormData="emitFormData"
      />

    </div>
  </div>
</template>

<script setup>
import {recipeIngredientAddFormSettings} from "~/utils/forms";
import {recipeTableSettings} from "~/utils/tables";
import {
  itemAlertSettings,
  itemDeleteAlertSettings,
  itemEditAlertSettings,
} from "~/utils/alerts";

import {useKitchenStore} from "~/store/kitchenStore";

const router = useRouter();

const kitchenStore = useKitchenStore();

const {data: receiptsCategory} = await useAsyncData('category-cooking-recipe', () => kitchenStore.fetchItems('category-cooking-recipe'));
const {data: receipts} = await useAsyncData('recipe', () => kitchenStore.fetchItems('recipe-balance'));

const recipeCategoryRefresh = () => refreshNuxtData('category-cooking-recipe');
const recipeRefresh = () => refreshNuxtData('recipe');

const searchItems = (searchText) => {
  recipe.value = kitchenStore.getRecipeBySearch(searchText, 'name');
}

const showModal = ref(false);

const showAlert = ref(false);
const formSettings = ref(recipeIngredientAddFormSettings);

const recipe = ref({});

const addRecipeCategorySelect = () => {
  const categorySelectField = {
    title: 'Категория рецепта *',
    type: 'text',
    name: 'category',
    required: true,
    method: 'select',
    selectValue: receiptsCategory.value,
  }
  if (!formSettings.value.formFields.find(field => field.name === 'category')) {
    formSettings.value.formFields.push(categorySelectField)
  }
}

const addModalForm = () => {
  recipe.value = {};
  formSettings.value.modalTitle = `Добавить рецепт`;
  addRecipeCategorySelect();
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  recipeRefresh();
  recipeCategoryRefresh();
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
    data.products = []
    const addRecipe = await kitchenStore.addItem(data, 'cooking-recipe');
    router.push(`/cooking-recipe/${addRecipe.id}`);
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