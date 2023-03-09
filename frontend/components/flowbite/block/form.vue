<template>
  <form @submit.prevent="emitFormData">
    <div class="relative z-0 w-full mb-6 group" v-for="field in formSettings.formFields" :key="field.name">
      <input :type="field.type" :name="field.name" :id="field.name" :step="field.step"
             v-if="field.method === 'input'"
             v-model="formData[field.name]"
             class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
             :required="field.required"/>
      <textarea :name="field.name" :id="field.name"
                v-if="field.method === 'textarea'"
                v-model="formData[field.name]"
                class="block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer"
                :required="field.required"/>
      <select :name="field.name" :id="field.name"
              v-if="field.method === 'select'"
              v-model="formData[field.name]"
              class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
              :required="field.required">
        <option v-for="option in field.selectValue" :value="option.id" :key="option.id">
          {{ option.name }}
        </option>
      </select>
      <label :for="field.name"
             class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        {{ field.title }}</label>
    </div>
    <button type="submit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
      {{ formSettings.buttonText }}
    </button>
    <button
        v-if="formSettings.deleteMode"
        class="md:mt-3 text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
      Удалить
    </button>
  </form>
</template>

<script setup>
import { propsFormSettings } from '~/utils/formSettings'

const props = defineProps({
  formSettings: propsFormSettings,
  fetchingData: {
    type: Object,
    required: false,
    default: () => {},
  },
  editFormData: {
    type: Object,
    required: false,
    default: () => {},
  },
})

const emit = defineEmits(['emitFormData'])

const formData = ref(props.fetchingData)

if (props.editFormData) {
  formData.value = props.editFormData
}

const emitFormData = () => {
  emit('emitFormData', formData.value, props.formSettings.formAction)
}


</script>

<style scoped>

</style>