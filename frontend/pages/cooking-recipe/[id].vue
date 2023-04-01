<template>
  <flowbite-block-hero
      :heroSettings="heroSettings"
  />
  <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Добавить ингредиенты к рецепту</h1>
  <div class="mb-3 mx-auto">
    <flowbite-block-table
        :columnNames="recipeIngredientsTableSettings.columns"
        :columnValues="recipe.products"
        @modalFormDetail="modalFormDetail"
        @addModalForm="addModalForm"
        @search="searchItems"
    />
    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="ingredientsAddFormSettings"
          :fetchingData="ingredient"
          @closeModal="closeModal"
          @emitFormData="emitFormData"
      />
    </div>
  </div>

</template>

<script setup>
import {useKitchenStore} from "~/store/kitchenStore";
import {recipeIngredientsTableSettings} from "~/utils/tables";
import {ingredientsAddFormSettings} from "~/utils/forms";

const kitchenStore = useKitchenStore();
const router = useRouter();
const id = router.currentRoute.value.params.id;

const {data: recipe} = await useAsyncData('recipe', () => kitchenStore.fetchItems(`recipe-balance?id=${id}`));
const recipeRefresh = () => refreshNuxtData('recipe');
const {data: products} = await useAsyncData('products', () => kitchenStore.fetchItems('product'));
const {data: ingredients} = await useAsyncData('ingredients', () => kitchenStore.fetchItems('ingredients'));

const searchItems = async (searchText) => {
  if (!searchText) {
    recipeRefresh();
  } else {
    recipe.value.products = recipe.value.products.filter(item => item.name.toLowerCase().includes(searchText.toLowerCase()))
  }
}

const heroSettings = ref({
  title: recipe.value.name,
  image: recipe.value.image,

  button: {
    text: 'Изменить',
    link: '#',
    color: 'primary',
  },
  options: [
    { title: "Категория", value: recipe.value.category },
    { title: "Цена", value: recipe.value.price ? recipe.value.price : 'Не указана' },
    { title: "Средняя цена", value: recipe.value.total_average_price },
    { title: "Максимальная цена", value: recipe.value.total_max_price },
    { title: "Общий вес продуктов", value: recipe.value.total_product_weight },
    { title: "Рецепт", value: recipe.value.description ? recipe.value.description : 'В строжайшем секрете' },
  ],
})

const showModal = ref(false);

const formSettings = ref(ingredientsAddFormSettings);

const ingredient = ref({});

const addIngredientSelectField = () => {
  const productSelectField = {
    title: 'Продукт *',
    type: 'text',
    name: 'product',
    required: true,
    method: 'select',
    selectValue: products.value,
  }
  if (!formSettings.value.formFields.some(field => field.title === 'Продукт')) {
    formSettings.value.formFields.unshift(productSelectField)
  }
}

const modalFormDetail = (id) => {
  ingredient.value = ingredients.value.find(item => item.id === id);
  formSettings.value.modalTitle = `Редактировать ингредиент`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addIngredientSelectField();
  showModal.value = true;
}

const addModalForm = () => {
  ingredient.value = {};
  formSettings.value.modalTitle = 'Добавить ингредиент';
  formSettings.value.addMode = true;
  addIngredientSelectField();
  showModal.value = true;
}

const closeModal = () => {
  showModal.value = false;
}

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    const res = await kitchenStore.addItem(data, 'ingredients');
    const recipeData = await kitchenStore.getItemById(id, 'cooking-recipe');
    recipeData.products.push(res.id);
    delete recipeData.image;
    await kitchenStore.updateItem(recipeData, id, 'cooking-recipe');
    recipeRefresh();
    showModal.value = false;
  } else if (action === 'updateItem') {
    await kitchenStore.updateItem(data, data.id, 'ingredients');
    recipeRefresh();
    showModal.value = false;
  }
}
</script>


<style scoped>

</style>