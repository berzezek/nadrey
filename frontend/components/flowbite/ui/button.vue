<template>
  <button
      :type="buttonType"
      :class="buttonClass"
      @click="clickButton"
  >
    {{ buttonText }}
  </button>
</template>

<script setup>
const props = defineProps({
  buttonType: {
    type: String,
    default: 'button',
  },
  buttonColor: {
    type: String,
    default: 'blue',
  },
  buttonText: {
    type: String,
    default: 'Добавить',
  },
})
const buttonClass = ref('')
buttonClass.value = `ml-3 text-white
bg-${props.buttonColor}-700
hover:bg-${props.buttonColor}-800 focus:ring-4 focus:outline-none
focus:ring-${props.buttonColor}-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2 text-center
dark:bg-g${props.buttonColor}600
dark:hover:bg-${props.buttonColor}-700
dark:focus:ring-${props.buttonColor}-800`

const emit = defineEmits([
  'click',
])
const clickButton = (data) => {
  if (data) {
    emit('click', data)
  } else {
    emit('click')
  }
}
</script>

<style scoped>

</style>