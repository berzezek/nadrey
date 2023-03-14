<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
      <div class="mr-auto place-self-center lg:col-span-7">
        <p class="max-w-2xl font-light text-gray-500 md:text-lg lg:text-xl dark:text-gray-400 text-end">{{ props.heroSettings.category }}</p>
        <h1 class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl dark:text-white">
          {{ props.heroSettings.title }}</h1>
        <p class="max-w-2xl mt-3 font-light text-gray-500 lg:my-2 md:text-lg lg:text-xl dark:text-gray-400">Рецепт</p>
        <pre class="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400">{{
            props.heroSettings.subtitle
          }}</pre>
        <p class="max-w-2xl font-light text-gray-500 dark:text-gray-400">Цена продуктов (усредненная) - {{ props.heroSettings.total_average_price }}</p>
        <p class="max-w-2xl font-light text-gray-500 dark:text-gray-400">Цена продуктов (максимальная) - {{ props.heroSettings.total_max_price }}</p>
        <p class="max-w-2xl font-light text-gray-500 dark:text-gray-400">Вес продуктов - {{ props.heroSettings.total_product_weight }} кг</p>
      </div>
      <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
        <img :src="props.heroSettings.image" :alt="props.heroSettings.title">
      </div>
    </div>
  </section>
</template>

<script setup>

const props = defineProps({
  heroSettings: {
    type: Object,
    default: () => {
      return {
        title: 'Payments tool',
        subtitle: 'From checkout to global sales tax compliance, companies around ...',
        image: 'https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/phone-mockup.png',
        button: {
          text: 'Get started',
          link: '#',
          color: 'primary',
        },
        total_product_weight: 0,
        total_max_price: 0,
        total_average_price: 0,
        category: ''
      }
    },
  },
});

// :heroTitle="recipe.value.name"
//     :heroSubtitle="recipe.value.description"
//     :heroImage="recipe.value.image"

</script>

<style scoped>

</style>