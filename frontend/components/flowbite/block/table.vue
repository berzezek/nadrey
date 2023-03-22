<template>
  <!--  <section class="bg-gray-50 dark:bg-gray-900 p-3 sm:p-5">-->
  <!--    <div class="mx-auto max-w-screen-xl px-4 lg:px-12">-->
  <!-- Start coding here -->
  <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
    <div class="flex flex-col md:flex-row items-center justify-between space-y-3 md:space-y-0 md:space-x-4 p-4">
      <div class="w-full md:w-1/2">
        <flowbite-ui-search
            @search="search"
        />
      </div>
      <div
          class="w-full md:w-auto flex flex-col md:flex-row space-y-2 md:space-y-0 items-stretch md:items-center justify-end md:space-x-3 flex-shrink-0">
        <flowbite-ui-button
            @click="addModalForm"
            :button-color="'blue'"
            :button-text="'Добавить'"
        />
        <flowbite-ui-button
            v-if="newButton"
            @click="newButtonClick"
            :button-color="newButton.color"
            :button-text="newButton.text"
        />
        <div class="flex items-center space-x-3 w-full md:w-auto">
          <flowbite-ui-filter
              :filters="filters"
              @filter="filter"
          />
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
        </tr>
        </thead>
        <tbody>
        <tr
            v-for="(colValue, index) in columnValues" :key="colValue.id"
            @click="modalFormDetail(colValue.id)"
            class="border-b dark:border-gray-700">
          <th scope="row" class="px-2 text-center py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            {{ index + 1 }}
          </th>
          <td class="px-4 py-3 " v-for="colName in columnNames" :key="colName">
            <div v-if="Object.keys(colName) == 'image'">

              <img class="rounded-full w-12 h-12"
                   :src="colValue[Object.keys(colName)[0]]" :alt="colValue.name">
            </div>
            <div
                v-if="typeof colValue[Object.keys(colName)[0]] == 'boolean'"
                class="flex items-center mb-4">
              <input v-if="colValue[Object.keys(colName)[0]] === false" disabled id="disabled-checkbox" type="checkbox"
                     value="true"
                     class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
              <input v-else disabled checked id="disabled-checked-checkbox" type="checkbox" value=""
                     class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">

            </div>
            <div v-else>

              <span>{{ colValue[Object.keys(colName)[0]] }}</span>
            </div>
          </td>
        </tr>
        </tbody>
      </table>
      <div class="mt-20"></div>
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
  newButton: {
    type: Object,
    required: false,
    default: () => {
    },
  },
  filters: {
    type: Array,
    default: () => [],
  },
})

const emit = defineEmits([
  'emitFormData',
  'modalFormDetail',
  'addModalForm',
  'newButtonClick',
  'search',
  'filter'
])

const modalFormDetail = (id) => {
  emit('modalFormDetail', id)
}

const addModalForm = () => {
  emit('addModalForm')
}

const newButtonClick = () => {
  emit('newButtonClick')
}

const deleteItem = (id) => {
  emit('emitFormData', id, 'deleteItem')
}
const showItem = () => {
  console.log('showItem')
  // emit('emitFormData', props.fetchingData.id, 'showItem')
}

const search = (searchText) => {
  emit('search', searchText)
}

const filter = (filter) => {
  emit('filter', filter)
}

</script>

<style scoped>
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown button {
  background-color: #fff;
  color: #333;
  border: 1px solid #ccc;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 5px;
  list-style: none;
  margin: 0;
  z-index: 1;
}

.dropdown-menu li {
  padding: 5px;
  cursor: pointer;
}

.dropdown-menu li:hover {
  background-color: #f2f2f2;
}
</style>