<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
      <div class="mr-auto place-self-center lg:col-span-7">
        <p class="max-w-2xl font-light text-gray-500 md:text-lg lg:text-xl dark:text-gray-400 text-end">{{ props.heroSettings.category }}</p>
        <h1 class="max-w-2xl mb-4 text-2xl font-bold tracking-tight leading-none md:text-3xl xl:text-4xl dark:text-white">
          {{ props.heroSettings.title }}</h1>
        <p class="max-w-2xl font-light text-gray-500 dark:text-gray-400" v-for="option in props.heroSettings.options" :key="option.title">
          {{ option.title }} - {{ option.value }}</p>
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
        options: [{
          title: 'Payments tool',
          value: 'payments-tool'
        }],
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