<template>
  <h1 class="text-xl text-gray-900 dark:text-white text-center mb-4">Заказы</h1>
  <flowbite-block-table
      :columnNames="cardTableSettings.columns"
      :columnValues="cards"
      @addModalForm="addModalForm"
      @modalFormDetail="modalFormDetail"
      @emitFormData="emitFormData"
  />
  <div class="flex items-center">
    <flowbite-block-modal
        v-if="showModal"
        :formSettings="cardAddFormSettings"
        :fetchingData="card"
        @closeModal="closeModal"
        @emitFormData="emitFormData"
    />

  </div>
</template>

<script setup>
import {cardTableSettings} from "~/utils/tables";
import {cardAddFormSettings} from "~/utils/forms";
import {useKitchenStore} from "~/store/kitchenStore";

const router = useRouter();
const kitchenStore = useKitchenStore();
const {data: clients} = await useLazyAsyncData('client', () => kitchenStore.fetchItems('client'));
const {data: cards} = await useAsyncData('cards', () => kitchenStore.fetchItems('card'));
const cardsRefresh = () => refreshNuxtData('cards')

const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(cardAddFormSettings);
const card = ref({});

const closeModal = () => {
  showModal.value = false;
  cardsRefresh();
}

const alertSettings = ref({});

const alerting = (data) => {
  alertSettings.value = data
  showAlert.value = true;
  setTimeout(() => {
    showAlert.value = false;
  }, 5000)

}
const closeAlert = () => {
  showAlert.value = false;
}

const addCardSelect = () => {

  const clientSelectField = {
    title: 'Клиент',
    type: 'text',
    name: 'client',
    required: true,
    method: 'select',
    selectValue: clients.value,
  }
  if (!formSettings.value.formFields.find(field => field.name === 'client')) {
    formSettings.value.formFields.unshift(clientSelectField);
  }
}

const modalFormDetail = (id) => {
  card.value = cards.value.find(card => card.id === id);
  card.value.date_created = new Date(card.value.date_created).toLocaleDateString('ru-RU')
  formSettings.value.modalTitle = `Корзина №${card.value.id} от ${card.value.date_created}`;
  formSettings.value.addMode = false;
  addCardSelect();
  showModal.value = true;
}

const addModalForm = () => {
  card.value = {};
  formSettings.value.modalTitle = `Добавить корзину`;
  addCardSelect();
  formSettings.value.addMode = true;
  showModal.value = true;
}

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    data.products = []
    const addCard = await kitchenStore.addItem(data, 'card');
    closeModal();
    router.push(`/card/${addCard.id}`);
  } else if (action === 'updateItem') {
    const editCard = await kitchenStore.updateItem(data, data.id, 'card');
    closeModal();
    router.push(`/card/${editCard.id}`);
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, 'card');
    closeModal();
  }
}

</script>

<style scoped>

</style>