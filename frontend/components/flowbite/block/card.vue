<template>
<div class="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-2xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700 mx-auto">
    <img class="object-cover w-full rounded-t-lg h-192 md:h-auto md:w-192 md:rounded-none md:rounded-l-lg" :src="props.cardValue.image" alt="">
    <div class="flex flex-col justify-between p-4 leading-normal">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ props.cardValue.name }}</h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ props.cardValue.description }}</p>
    </div>
</div>
  {{props.cardValue}}
</template>

<script setup>
const props = defineProps({
  cardValue: {
    type: Object,
    required: false,
    default: () => {
      return {
        image_url: '',
        name: '',
        description: '',
      }
    },
  }
})


</script>

<style scoped>

</style>