<template>
  <form @submit.prevent>
    <div class="relative z-0 w-full mb-6 group" v-for="field in formSettings.formFields" :key="field.name">

<!--      <img-->
<!--          v-if="field.method==='image'"-->
<!--          class="rounded-full w-24 h-24"-->
<!--          :src="field.name"-->
<!--          :alt="field.name"-->
<!--      >-->

      <input
          :type="field.type"
          :name="field.name"
          :id="field.name"
          :step="field.step"
          v-if="field.method === 'input'"
          v-model="formData[field.name]"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          :required="field.required"/>
      <textarea
          :name="field.name"
          :id="field.name"
          v-if="field.method === 'textarea'"
          v-model="formData[field.name]"
          class="block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer"
          :required="field.required"/>
      <select
          :name="field.name"
          :id="field.name"
          v-if="field.method === 'select'"
          v-model="formData[field.name]"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          :required="field.required">
        <option v-for="option in field.selectValue" :value="option.id" :key="option.id">
          {{ option.name }}
        </option>
      </select>
      <label
          :for="field.name"
          class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        {{ field.title }}</label>
    </div>
    <div v-if="props.formSettings.addMode">
      <flowbite-ui-button
          @click="addItem"
          :button-color="'blue'"
          :button-text="'????????????????'"
      />
    </div>
    <div v-else>
      <flowbite-ui-button
          @click="updateItem"
          :button-color="'blue'"
          :button-text="'??????????????????????????'"
      />
      <flowbite-ui-button
          @click="deleteItem"
          :button-color="'red'"
          :button-text="'??????????????'"
          class="md:ml-3"
      />
    </div>
  </form>
</template>

<script setup>

const props = defineProps({
  formSettings: {
    type: Object,
    required: false,
    default: () => {
      return {
        formFields: [],
        addMode: true,
      }
    },
  },
  fetchingData: {
    type: Object,
    required: false,
    default: () => {
      return {
        id: null,
      }
    },
  },
  editFormData: {
    type: Object,
    required: false,
    default: () => {
    },
  },
})

const emit = defineEmits(['emitFormData', 'emitFormData'])

const formData = ref(props.fetchingData)

const addItem = () => {
  emit('emitFormData', formData.value, 'addItem')
}

const updateItem = () => {
  emit('emitFormData', formData.value, 'updateItem')
}

const deleteItem = () => {
  emit('emitFormData', props.fetchingData.id, 'deleteItem')
}

</script>

<style scoped>

</style>