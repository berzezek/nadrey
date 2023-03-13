// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@pinia/nuxt',
    '@nuxtjs/tailwindcss'
  ],
  pinia: {
    autoImports: [
      'defineStore',
    ]
  },
  // app: {
  //   head: {
  //     title: 'NApp',
  //     link: [
  //       {rel: 'stylesheet', href: 'https://unpkg.com/flowbite-datepicker/dist/flowbite-datepicker.css'},
  //     ],
  //     script: [
  //       {src: 'https://unpkg.com/flowbite-datepicker/dist/flowbite-datepicker.js', body: true},
  //     ]
  //   }
  // }
})
