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

const {data: recipes} = await useAsyncData('recipe', () => kitchenStore.fetchItems('recipe-balance'));
const {data: products} = await useAsyncData('products', () => kitchenStore.fetchItems('product'));
const recipe = recipes.value.find((item) => item.id.toString() === id);
const recipeIngredients = computed( async () => {
  return await recipes.value.filter(item => {
    // Фильтруем только продукты, которые относятся к текущему рецепту
    return item.id.toString() === id;
  });
});

const heroSettings = {
  title: recipe.name,
  subtitle: recipe.description,
  image: recipe.image,

  button: {
    text: 'Изменить',
    link: '#',
    color: 'primary',
  },
  total_product_weight: recipe.total_product_weight,
  total_max_price: recipe.total_max_price,
  total_average_price: recipe.total_average_price,
  category: recipe.category,
}

const modalFormDetail = (id) => {
  console.log(id);
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

const addModalForm = () => {
  ingredient.value = {};
  formSettings.value.modalTitle = 'Добавить ингредиент';
  addIngredientSelectField();
  showModal.value = true;
}

const closeModal = () => {
  showModal.value = false;
}

const emitFormData = async (data) => {
  const res = await kitchenStore.addItem(data, 'ingredients');
  const recipeData = await kitchenStore.getItemById(id, 'cooking-recipe');
  recipeData.products.push(res.id);
  delete recipeData.image;
  await kitchenStore.updateItem(recipeData, id, 'cooking-recipe');
  showModal.value = false;
}
</script>


<style scoped>

</style>