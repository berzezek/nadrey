<template>
  <flowbite-block-hero
      :heroSettings="heroSettings"
  />
  <h1 class="text-xl text-blue-800 text-center mb-4">Добавить ингредиенты к рецепту</h1>
  <div class="mb-3 mx-auto">
    <flowbite-block-table
        :columnNames="recipeIngredientsTableSettings.columns"
        :columnValues="ingredientsForRecipe"
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

const {data: recipe} = await useAsyncData('recipe', () => kitchenStore.fetchItems(`cooking-recipe/${id}`));
const {data: products} = await useAsyncData('products', () => kitchenStore.fetchItems('product'));
const {data: ingredients} = await useAsyncData('ingredients', () => kitchenStore.fetchItems('ingredients'));
const recipeRefresh = () => refreshNuxtData('recipe');
const productRefresh = () => refreshNuxtData('products');
const ingredientRefresh = () => refreshNuxtData('ingredients');

const ingredientsForRecipe = computed(() => recipe.value.products);
const maxPrice = computed(() => ingredientsForRecipe.value.reduce((acc, item) => acc + item.max_price, 0));
const averagePrice = computed(() => ingredientsForRecipe.value.reduce((acc, item) => acc + item.average_price, 0));
const lastPrice = computed(() => ingredientsForRecipe.value.reduce((acc, item) => acc + item.last_price, 0));
const totalWeight = computed(() => ingredientsForRecipe.value.reduce((acc, item) => acc + item.ingredient_weight, 0));

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
    {title: "Категория", value: recipe.value.category_name},
    {title: "Утвержденная цена", value: recipe.value.price ? recipe.value.price : 'Не указана'},
    {title: "Средняя цена", value: averagePrice.value},
    {title: "Максимальная цена", value: maxPrice.value},
    {title: "Последняя цена", value: lastPrice.value},
    {title: "Общий вес продуктов", value: totalWeight.value},
    {title: "Рецепт", value: recipe.value.description ? recipe.value.description : 'В строжайшем секрете'},
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
  formSettings.value.formFields.splice(formSettings.value.formFields.findIndex(field => field.name === 'product'), 1, productSelectField)

}

const modalFormDetail = (id) => {
  ingredient.value = ingredients.value.find(item => item.id === id);
  formSettings.value.modalTitle = `Редактировать ингредиент рецепта`
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addIngredientSelectField();
  showModal.value = true;
}

const addModalForm = () => {
  ingredient.value = {};
  formSettings.value.modalTitle = `Добавить ингредиент к рецепту`
  formSettings.value.addMode = true;
  addIngredientSelectField();
  showModal.value = true;
}

const closeModal = () => {
  recipeRefresh();
  productRefresh();
  ingredientRefresh();
  showModal.value = false;
}

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    const res = await kitchenStore.addItem(data, 'ingredients');
    const recipeData = await kitchenStore.getItemById(id, 'cooking-recipe');
    recipeData.products.push(res.id);
    delete recipeData.image;
    await kitchenStore.updateItem(recipeData, id, 'cooking-recipe');
    closeModal();
  } else if (action === 'updateItem') {
    await kitchenStore.updateItem(data, data.id, 'ingredients');
    closeModal();
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(id, 'ingredients');
    closeModal();
  }
}
</script>


<style scoped>

</style>