<template>
  <flowbite-block-hero
      :heroSettings="heroSettings"
  />
  <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Ингредиенты</h1>
  <div class="mb-3 mx-auto">
    <flowbite-block-table
        :columnNames="recipeIngredientsTableSettings.columns"
        :columnValues="recipe.products"
        @modalFormDetail="modalFormDetail"
    />
    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="ingredientsAddFormSettings"
          :fetchingData="ingredient"
          @closeModal="closeModal"
          @addModalForm="addModalForm"
          @emitFormData="emitFormData"
      />
      <div class="flex items-between">
        <flowbite-ui-button
            @click="addModalForm"
            buttonColor="blue"
            buttonText="Добавить ингредиент"
        />
      </div>
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

const heroSettings = {
  title: recipe.value.name,
  subtitle: recipe.value.description,
  image: recipe.value.image,

  button: {
    text: 'Изменить',
    link: '#',
    color: 'primary',
  },
  total_product_weight: recipe.value.total_product_weight,
  total_max_price: recipe.value.total_max_price,
  total_average_price: recipe.value.total_average_price,
  category: recipe.value.category,
}

const showModal = ref(false);

const formSettings = ref(ingredientsAddFormSettings);

const ingredient = ref({});

const addIngredientSelectField = () => {
  const productSelectField = {
    title: 'Продукт',
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
  console.log(ingredient.value)
  const product = products.value.find(item => item.id === ingredient.value.id);
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