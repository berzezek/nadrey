<template>
  <div class="d-flex mt-5">
    <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Продукты</h1>
    <flowbite-block-table
        :columnNames="productTableColumnsNames"
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
          :editFormData="product"
          @emitFormData="emitFormData"
          @changeFormProps="changeFormProps"
          @closeModal="closeModal"
      />
      <flowbite-block-alert
          v-if="showAlert"
          @closeAlert="closeAlert"
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
import { productTableColumnsNames } from "~/utils/productTable";

const productStore = useProductStore();
const productCategoryStore = useProductCategoryStore();

productStore.fetchProducts();
productCategoryStore.fetchProductCategories();

const products = computed(() => productStore.products);
const productCategories = computed(() => productCategoryStore.productCategories);

const filterRadio = (categoryId) => {
  console.log(categoryId)

}

const searchItems = (search) => {
  console.log(search)
}


const showModal = ref(false);
const showAlert = ref(false);

let product = ref({
  name: '',
  descriptions: '',
  unit: '',
  category: '',
  price: '',
  id: ''
})

const modalFormDetail = (id) => {
  showModal.value = true;
  product.value = products.value.find((item) => item.id === id);
}

const modalForm = () => {
  showModal.value = true;
}

const closeModal = () => {
  showModal.value = false;
}

const productCategoriesSelect = computed(async () => {
  await productCategoryStore.fetchProductCategories()
  return productCategories.value.map((item) => {
    return {title: item.name, value: item.id}
  })
})


const formSettings = ref({
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
    productStore.addProduct(data);
    showModal.value = false;
    showAlert.value = true;

  } else if (action === 'addCategory') {
    console.log('addCategory', data);
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

const closeAlert = () => {
  showAlert.value = false;
}

</script>

<style scoped>

</style>