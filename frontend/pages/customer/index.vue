<template>
  <div class="">
    <flowbite-block-alert
        v-if="showAlert"
        @closeAlert="closeAlert"
        :alert-settings="alertSettings"
    />
    <h1 class="text-xl text-blue-800 text-center mb-4">Клиенты</h1>
    <flowbite-block-table
        :columnNames="clientTableSettings.columns"
        :columnValues="clients"
        @modalFormDetail="modalFormDetail"
        @addModalForm="addModalForm"
    />

    <div class="flex items-center">
      <flowbite-block-modal
          v-if="showModal"
          :formSettings="clientAddFormSettings"
          :fetchingData="client"
          @closeModal="closeModal"
          @addModalForm="addModalForm"
          @emitFormData="emitFormData"
      />
    </div>
  </div>
</template>

<script setup>
import {clientAddFormSettings} from "~/utils/forms";
import {clientTableSettings} from "~/utils/tables";
import {emitFormDataMixin} from "~/mixins/emitFormDataMixin";

import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();

const {data: clients} = await useLazyAsyncData('client', () => kitchenStore.fetchItems('client'));
const clientRefresh = () => refreshNuxtData('client')

const searchItems = (search) => {
  clients.value = kitchenStore.getItemsBySearch(search, 'name');
}

const showModal = ref(false);
const showAlert = ref(false);

const formSettings = ref(clientAddFormSettings);
const client = ref({});

const addModalForm = () => {
  client.value = {};
  formSettings.value.modalTitle = `Добавить клиента`;
  formSettings.value.addMode = true;
  showModal.value = true;
}
const closeModal = () => {
  clientRefresh();
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


const emitFormData = (data, action) => {
  emitFormDataMixin(
      data,
      action,
      'client',
      closeModal,
      alerting
  )
}
const closeAlert = () => {
  showAlert.value = false;
}

const modalFormDetail = (id) => {
  client.value = clients.value.find(client => client.id === id);
  formSettings.value.modalTitle = `Редактировать склад`;
  formSettings.value.addMode = false;
  formSettings.value.buttonText = `Редактировать`;
  showModal.value = true;
}

</script>

<style scoped>

</style>