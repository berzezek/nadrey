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
              <input v-if="colValue[Object.keys(colName)[0]] === false" disabled id="disabled-checkbox" type="checkbox"
                     value="true"
                     class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
              <input v-else disabled checked id="disabled-checked-checkbox" type="checkbox" value=""
                     class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">

            </div>
            <span v-else>{{ colValue[Object.keys(colName)[0]] }}</span>
          </td>
          <td class="px-4 py-3 flex items-center justify-end">
            <div class="dropdown">
              <button @click="toggleDropdown(index)">{{ selectedOption[index] }}</button>
              <ul v-if="isOpen[index]" class="dropdown-menu">
                <li v-for="(option, index) in options" :key="index" @click="selectOption(index)">{{ option }}</li>
              </ul>
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
})

const isOpen = ref(props.columnValues.map(() => false))
const selectedOption = ref(props.columnValues.map(() => 'Выберите опцию'))
const options = ref(['Показать', 'Редактировать', 'Удалить'])

function toggleDropdown(index) {
  isOpen.value[index] = !isOpen.value[index]
}

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

const selectOption = (index) => {
  if (options.value[index] === 'Показать') {
    console.log('showItem')
    // showItem()
  } else if (options.value[index] === 'Редактировать') {
    console.log('updateItem')
    // modalFormDetail(props.fetchingData.id)
  } else if (options.value[index] === 'Удалить') {
    console.log('deleteItem')
    // deleteItem()
  }
  isOpen.value = false
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