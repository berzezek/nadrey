<template>
  <flowbite-block-hero :heroSettings="heroSettings"/>
  <h1 class="text-xl text-blue-800 text-center mb-4">Заказы</h1>
  <div class="mb-3 mx-auto">
    <flowbite-block-table
        :columnNames="orderTableSettings.columns"
        :columnValues="card.get_orders"
        @addModalForm="addModalForm"
        @modalFormDetail="modalFormDetail"
        @search="searchItems"
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
import {useKitchenStore} from '~/store/kitchenStore'
import {orderTableSettings} from '~/utils/tables'
import {orderAddFormSettings} from '~/utils/forms'

const kitchenStore = useKitchenStore()
const router = useRouter()
const id = router.currentRoute.value.params.id

const {data: card} = await useAsyncData('card', () =>
    kitchenStore.getItemById(id, 'card')
)
const {data: orders} = await useAsyncData('order', () =>
    kitchenStore.fetchItems('order')
)
const {data: recipes} = await useAsyncData('cooking-recipe', () =>
    kitchenStore.fetchItems('cooking-recipe')
)

const cardRefresh = () => refreshNuxtData('card')
const orderRefresh = () => refreshNuxtData('order')
const recipeRefresh = () => refreshNuxtData('cooking-recipe')

const isPaid = computed(() => {
  if (card.value.is_paid) {
    return 'Оплачено'
  } else {
    return 'Не оплачено'
  }
})

const searchItems = (searchText) => {
  recipes.value = kitchenStore.getItemsBySearch(searchText, 'name')
}

const heroSettings = {
  title: `Корзина № ${card.value.id}`,
  subtitle: `${card.value.card_client} - от ${card.value.date_created}: ${isPaid}`,

  button: {
    text: 'Изменить',
    link: '#',
    color: 'primary',
  },
  options: [{
    title: 'Клиент',
    value: card.value.card_client
  }, {
    title: 'Сумма заказа',
    value: computed(() => card.value.total_price)
  }, {
    title: 'Дата создания',
    value: new Date(card.value.date_created).toLocaleString()
  }, {
    title: 'Оплачено',
    value: isPaid
  }],
}

const showModal = ref(false)
const formSettings = ref(orderAddFormSettings)
const order = ref({})

const addRecipeSelectField = () => {
  const recipeSelectField = {
    title: 'Рецепт *',
    type: 'text',
    name: 'recipe',
    required: true,
    method: 'select',
    selectValue: recipes.value,
  }
  if (!formSettings.value.formFields.find(field => field.name === 'recipe')) {
    formSettings.value.formFields.unshift(recipeSelectField)
  }
}

const modalFormDetail = (id) => {
  order.value = orders.value.find((item) => item.id === id)
  formSettings.value.modalTitle = `Редактировать заказ ${order.value.id}`
  formSettings.value.addMode = false
  formSettings.value.buttonText = `Редактировать`
  addRecipeSelectField()
  showModal.value = true
}

const addModalForm = () => {
  order.value = {}
  formSettings.value.modalTitle = 'Добавить заказ'
  formSettings.value.addMode = true
  addRecipeSelectField()
  showModal.value = true
}
const closeModal = () => {
  cardRefresh()
  orderRefresh()
  recipeRefresh()
  showModal.value = false
}

const emitFormData = async (data, action) => {
  if (action === 'addItem') {
    const res = await kitchenStore.addItem(data, 'order')
    const cardData = await kitchenStore.getItemById(id, 'card')
    cardData.order.push(res.id)
    await kitchenStore.updateItem(cardData, id, 'card')
    closeModal();
  } else if (action === 'updateItem') {
    await kitchenStore.updateItem(data, data.id, 'order')
    closeModal();
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, 'order')
    closeModal();
  }
}
</script>

<style scoped></style>
