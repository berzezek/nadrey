<template>
  <div>
    <nuxt-layout>
      <nuxt-loading-indicator />
      <nuxt-page />
    </nuxt-layout>
  </div>
</template>

<script setup>
import {
  initAccordions,
  initCarousels,
  initCollapses,
  initDials,
  initDismisses,
  initDrawers,
  initDropdowns,
  initModals,
  initPopovers,
  initTabs,
  initTooltips,
} from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
  initAccordions()
  initCarousels()
  initCollapses()
  initDials()
  initDismisses()
  initDrawers()
  initDropdowns()
  initModals()
  initPopovers()
  initTabs()
  initTooltips()
})
</script>
