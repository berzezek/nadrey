<template>
<!--  <section class="bg-gray-50 dark:bg-gray-900 p-3 sm:p-5">-->
<!--    <div class="mx-auto max-w-screen-xl px-4 lg:px-12">-->
      <!-- Start coding here -->
      <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
        <div class="flex flex-col md:flex-row items-center justify-between space-y-3 md:space-y-0 md:space-x-4 p-4">
          <div class="w-full md:w-1/2">
            <flowbite-ui-search/>
          </div>
          <div
              class="w-full md:w-auto flex flex-col md:flex-row space-y-2 md:space-y-0 items-stretch md:items-center justify-end md:space-x-3 flex-shrink-0">
            <flowbite-ui-button
                @click="addItem"
                :button-color="'blue'"
                :button-text="'Добавить'"
            />
            <div class="flex items-center space-x-3 w-full md:w-auto">
              <flowbite-ui-filter/>
            </div>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th class="px-2 py-3 text-center">#</th>
              <th
                  scope="col" class="px-4 py-3"
                  v-for="colName in columnNames"
                  :key="colName"
              >{{ Object.values(colName)[0] }}
              </th>
              <th scope="col" class="px-4 py-3">
                <span class="sr-only">Actions</span>
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="(colValue, index) in columnValues" :key="colValue.id"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 text-center py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {{ index + 1 }}
              </th>
              <td class="px-4 py-3 " v-for="colName in columnNames" :key="colName">
                <img v-if="Object.keys(colName) == 'image'" class="rounded-full w-12 h-12"
                     :src="colValue[Object.keys(colName)[0]]" :alt="colValue.name">
                <div
                    v-if="typeof colValue[Object.keys(colName)[0]] == 'boolean'"
                    class="flex items-center mb-4">
                  <input v-if="colValue[Object.keys(colName)[0]] === false" disabled id="disabled-checkbox" type="checkbox" value="true"
                         class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                  <input v-else disabled checked id="disabled-checked-checkbox" type="checkbox" value=""
                         class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">

                </div>
                <span v-else>{{ colValue[Object.keys(colName)[0]] }}</span>
              </td>
              <td class="px-4 py-3 flex items-center justify-end">
                <button id="apple-imac-27-dropdown-button" data-dropdown-toggle="apple-imac-27-dropdown"
                        class="inline-flex items-center p-0.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100"
                        type="button">
                  <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20"
                       xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z"/>
                  </svg>
                </button>
                <div id="apple-imac-27-dropdown"
                     class="hidden z-10 w-44 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600">
                  <ul class="py-1 text-sm text-gray-700 dark:text-gray-200"
                      aria-labelledby="apple-imac-27-dropdown-button">
                    <li>
                      <span
                          @click="showItem"
                          class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Show</span>
                    </li>
                    <li>
                      <span
                          @click="modalFormDetail(colValue.id)"
                          class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Edit</span>
                    </li>
                  </ul>
                  <div class="py-1">
                    <span
                        @click="deleteItem"
                        class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Delete</span>
                  </div>
                </div>
              </td>
            </tr>
            <div class="mt-20"></div>
            </tbody>
          </table>
        </div>
        <nav class="flex flex-col md:flex-row justify-between items-start md:items-center space-y-3 md:space-y-0 p-4"
             aria-label="Table navigation">
          <flowbite-ui-page-num/>
          <flowbite-ui-pagination/>
        </nav>
      </div>
<!--    </div>-->
<!--  </section>-->
</template>

<script setup>
const props = defineProps({
  columnNames: {
    type: Array,
    required: false,
    default: () => [],
  },
  columnValues: {
    type: Array,
    required: false,
    default: () => [],
  },
})

const emit = defineEmits(['emitFormData', 'modalFormDetail'])

const formData = ref(props.fetchingData)

const modalFormDetail = (id) => {
  emit('modalFormDetail', id)
}

const addItem = () => {
  // console.log('addItem')
  // emit('emitFormData', formData.value, 'addItem')
}

const updateItem = () => {
  emit('emitFormData', formData.value, 'updateItem')
}

const deleteItem = () => {
  emit('emitFormData', props.fetchingData.id, 'deleteItem')
}
const showItem = () => {
  console.log('showItem')
  // emit('emitFormData', props.fetchingData.id, 'showItem')
}
</script>

<style scoped>

</style>