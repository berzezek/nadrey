<template>

  <div class="relative overflow-x-auto">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
      <tr>
        <th class="px-6 py-3 text-center">#</th>
        <th scope="col" class="px-6 py-3" v-for="colName in columnNames" :key="colName">
          {{ Object.values(colName)[0] }}
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(colValue, index) in columnValues" :key="colValue.id"
          @click="modalFormDetail(colValue.id)"
          class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
        <th class="px-6 py-3 text-center">{{ index + 1 }}</th>
        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
            v-for="colName in columnNames" :key="colName">
          {{ colValue[Object.keys(colName)[0]] }}
        </th>
      </tr>
      </tbody>
    </table>
  </div>
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

const emit = defineEmits([
  'modalFormDetail',
])
const modalFormDetail = (id) => {
  emit('modalFormDetail', id)
}

</script>

<style scoped>

</style>