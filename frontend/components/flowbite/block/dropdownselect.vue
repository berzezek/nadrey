<template>
  <div>

    <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio"
            @click="changeSelect(0)"
            class="inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
            type="button">
      <svg class="w-4 h-4 mr-2 text-gray-400" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
           xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
              clip-rule="evenodd"></path>
      </svg>
      {{ selectText }}
      <svg class="w-3 h-3 ml-2" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24"
           xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
      </svg>
    </button>
    <div id="dropdownRadio"
         class="z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600"
         data-popper-reference-hidden="" data-popper-escaped="" data-popper-placement="top"
         style="position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 3847.5px, 0px);">
      <ul class="p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownRadioButton">
        <li v-for="select in selectValue" :key="select.id">
          <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
            <input id="filter-radio-example-1" type="radio" value="" name="filter-radio"
                   @input="changeSelect(select.id)"
                   class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
            <label for="filter-radio-example-1"
                   class="w-full ml-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">
              {{ select.name }}
            </label>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useKitchenStore } from "~/store/kitchenStore";

const kitchenStore = useKitchenStore()

const props = defineProps({
  selectText: {
    type: String,
    default: 'Выбрать'
  },
  searchSelect: {
    type: String,
    default: ''
  }
})

const {data: selectValue} = await useLazyAsyncData(props.searchSelect, () => kitchenStore.fetchItems(props.searchSelect));

const emit = defineEmits(['changeSelect'])

const changeSelect = (id) => {
  emit('changeSelect', id)
}
</script>

<style scoped>

</style>