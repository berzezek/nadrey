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
  app: {
    head: {
      title: 'NApp',
      // favicon: 'https://nuxtjs.org/favicon.ico',
      link: [
        // {rel: 'icon', type: 'image/png', href: '.favicon.png'},
        ],
    }
  },
  runtimeConfig: {
    public: {
      apiBase: "http://nadrey.tw1.su/api/v1/",
      localeApiBase: "http://localhost:8000/api/v1/",
    }
  }
})
