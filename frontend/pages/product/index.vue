<template>
  <div class="d-flex mt-5">
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Продукты</h1>
    <flowbite-block-table
        :columnNames="propsTableNames"
        :columnValues="products"
        :searchSelect="productCategories"
        @modalForm="modalForm"
        @modalFormDetail="modalFormDetail"
        @filterRadio="filterRadio"
        @searchItems="searchItems"
    />

    <div class="mt-4">

      <flowbite-block-modal
          v-if="showModal"
          :button-text="'Добавить продукт'"
          :addForm="true"
          :modal-title="'Добавить продукт'"
          :modal-footer="false"
          :form-settings="formSettings"
          @emitFormData="emitFormData"
          @changeFormProps="changeFormProps"
      />
      <flowbite-block-alert
          v-if="showAlert"
      />
      <button type="button"
              @click="modalForm"
              class="ml-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Добавить продукт
      </button>

    </div>
  </div>
</template>

<script setup>
import {useProductStore} from "~/store/productStore";
import {useProductCategoryStore} from "~/store/productCategoryStore";

const productStore = useProductStore();
const productCategoryStore = useProductCategoryStore();

productStore.fetchProducts();
productCategoryStore.fetchProductCategories();

const products = computed(() => productStore.searchedProducts);
const productCategories = computed(() => productCategoryStore.productCategories);

const propsTableNames = [
  {name: 'Наименование'},
  {'descriptions': 'Описание'},
  {'calories': 'Калории'}
]

const filterRadio = (categoryId) => {
  productStore.getProductsByCategory(categoryId);
}

const searchItems = (search) => {
  productStore.getProductsBySearch(search);
}


const showModal = ref(false);
const showAlert = ref(false);

const modalFormDetail = (id) => {
  console.log(id)
  showModal.value = true;
}

const modalForm = () => {
  showModal.value = true;
}

const productCategoriesSelect = computed(async () => {
  await productCategoryStore.fetchProductCategories()
  return productCategories.value.map((item) => {
    return {title: item.name, value: item.id}
  })
})


const formSettings = reactive({
  formAction: 'addProduct',
  buttonText: 'Добавить продукт',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'descriptions', required: false, method: 'textarea'},
    {
      title: 'Единица измерения', type: 'text', required: true, method: 'select', selectValue: [
        {title: 'кг', value: 'kg'},
        {title: 'гр', value: 'gr'},
        {title: 'л', value: 'l'},
      ]
    },
    {title: 'Вес', type: 'number', name: 'weight', required: false, method: 'input'},
    {title: 'Калории', type: 'number', name: 'calories', required: false, method: 'input'},
    {
      title: 'Категория',
      type: 'text',
      name: 'category',
      required: true,
      method: 'select',
      selectValue: await productCategoriesSelect.value
    },
  ],
  addButton: {
    title: 'Добавить категорию',
    method: 'addCategory',
    required: true,
  }
})


const emitFormData = (data, action) => {
  if (action === 'addProduct') {
    console.log(productStore.isFetching);
    console.log('addProduct', data);

  } else if (action === 'addCategory') {
    // productCategoryStore.addProductCategory(data);
  }
}

const changeFormProps = (method) => {
  if (method === 'addCategory') {
    formSettings.formAction = 'addCategory';
    formSettings.buttonText = 'Добавить категорию';
    formSettings.formFields = [
      {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
      {title: 'Описание', type: 'text', name: 'descriptions', required: false, method: 'textarea'},
    ],
        formSettings.addButton = {
          required: false,
        }

  }
}

</script>

<style scoped>

</style>