<template>
  <div class="mt-6">
    <p
        v-for="description in descriptions"
        :key="description.link"
        class="text-purple-600 mb-2">{{ description.title }}
      <router-link :to="description.link" class="text-blue-600">
        {{ description.linkText }}
      </router-link>
    </p>
  </div>
</template>

<script setup>

const props = defineProps({
  descriptions: {
    type: Array,
    required: true,
    default: () => [
      {
        title: 'Здесь можно добавить',
        link: '/product-category',
        linkText: '"Категорию продуктов".',
      },
    ],
  },
});

</script>

<style scoped>

</style>