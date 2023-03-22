<template>
  <flowbite-block-hero
      :heroSettings="heroSettings"
  />
  <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Заказы</h1>
  <div class="mb-3 mx-auto">
    <flowbite-block-table
        :columnNames="orderTableSettings.columns"
        :columnValues="card.get_orders"
        @addModalForm="addModalForm"
        @modalFormDetail="modalFormDetail"
    />
    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="orderAddFormSettings"
          :fetchingData="order"
          @closeModal="closeModal"
          @emitFormData="emitFormData"
      />
    </div>
  </div>

</template>

<script setup>
import {useKitchenStore} from "~/store/kitchenStore";
import {orderTableSettings} from "~/utils/tables";
import {orderAddFormSettings} from "~/utils/forms";

const kitchenStore = useKitchenStore();
const router = useRouter();
const id = router.currentRoute.value.params.id;

const {data: recipes} = await useAsyncData('cooking-recipe', () => kitchenStore.fetchItems('cooking-recipe'));
const {data: orders} = await useAsyncData('order', () => kitchenStore.fetchItems('order'));
const {data: card} = await useAsyncData('card', () => kitchenStore.getItemById(id, 'card'));
const cardRefresh = () => refreshNuxtData('card');

const isPaid = () => {
  return card.value.is_paid ? 'Оплачено' : 'Не оплачено'
}

const heroSettings = {
  title: `Корзина № ${card.value.id} (${card.value.card_client}) - ${isPaid()}`,
  subtitle: card.value.description,

  button: {
    text: 'Изменить',
    link: '#',
    color: 'primary',
  },
}

const showModal = ref(false);

const formSettings = ref(orderAddFormSettings);

const order = ref({});

const addRecipeSelectField = () => {
  const recipeSelectField = {
    title: 'Рецепт',
    type: 'text',
    name: 'recipe',
    required: true,
    method: 'select',
    selectValue: recipes.value,
  }
  if (!formSettings.value.formFields.some(field => field.title === 'Рецепт')) {
    formSettings.value.formFields.unshift(recipeSelectField)
  }
}

const modalFormDetail = (id) => {
  order.value = orders.value.find(item => item.id === id);
  formSettings.value.modalTitle = `Редактировать заказ ${order.value.id}`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  addRecipeSelectField();
  showModal.value = true;
}

const addModalForm = () => {
  order.value = {};
  formSettings.value.modalTitle = 'Добавить заказ';
  formSettings.value.addMode = true;
  addRecipeSelectField();
  showModal.value = true;
}
//
const closeModal = () => {
  showModal.value = false;
}

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    const res = await kitchenStore.addItem(data, 'order');
    const cardData = await kitchenStore.getItemById(id, 'card');
    cardData.order.push(res.id);
    console.log(cardData)
    await kitchenStore.updateItem(cardData, id, 'card');
    cardRefresh();
    showModal.value = false;
  } else if (action === 'updateItem') {
    await kitchenStore.updateItem(data, data.id, 'order');
    cardRefresh();
    showModal.value = false;
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, 'order');
    cardRefresh();
    showModal.value = false;
  }
}
</script>


<style scoped>

</style>