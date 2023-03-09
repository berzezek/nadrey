<template>

  <!-- Main modal -->
  <div class="fixed z-50 w-full p-4 overflow-y-auto h-modal md:h-full">
    <div class="relative w-full h-full max-w-2xl md:h-auto">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <!-- Modal header -->
        <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ formSettings.modalTitle }}
          </h3>
          <button
              @click="closeModal"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                    clip-rule="evenodd"></path>
            </svg>
          </button>
        </div>
        <!-- Modal body -->
        <div class="p-6 space-y-6 shadow-xl">

          <flowbite-block-form
              :formSettings="formSettings"
              :fetchingData="fetchingData"
              @emitFormData="emitFormData"
              @changeFormProps="changeFormProps"
              @closeModal="closeModal"
          />

        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
import { propsFormSettings } from '~/utils/formSettings'

const props = defineProps({
  buttonText: {
    type: String,
    default: 'Open modal'
  },
  addForm: {
    type: Boolean,
    default: false
  },
  formSettings: propsFormSettings,
  fetchingData: {
    type: Boolean,
    required: false,
    default: () => {}
  }
})

const emit = defineEmits(['emitFormData', 'changeFormProps', 'closeModal'])

const emitFormData = (data, action) => {
  emit('emitFormData', data, action)
}

const changeFormProps = (data) => {
  emit('changeFormProps', data)
}

const closeModal = () => {
  emit('closeModal')
}

</script>

<style scoped>

</style>