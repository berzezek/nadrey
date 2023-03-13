<template>
  <h1>Рецепт № {{ $router.currentRoute.value.params.id }}</h1>
  <flowbite-block-card
    :cardValue="recipe"
  />
</template>

<script setup>
import {useKitchenStore} from "~/store/kitchenStore";

const kitchenStore = useKitchenStore();
const router = useRouter();

const {data: recipe} = await useAsyncData('recipe', () => kitchenStore.getItemById(
    'cooking-recipe', router.currentRoute.value.params.id));
</script>

<style scoped>

</style>