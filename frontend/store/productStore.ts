import {defineStore} from 'pinia'
import {BASE_API_URL} from '~/utils/constants'
import {IProduct} from "~/types";

export const useProductStore = defineStore('products', {
  state: () => ({
    products: [] as IProduct[],
    filteredProducts: [] as IProduct[],
    searchedProducts: [] as IProduct[],
    error: null as any,
    isFetching: false,
  }),
  getters: {
    getProductsByCategory: (state) => (category: number) => {
      if (category !== 0) {
        state.products.filter((product) => product.category === category)
      }
    },
    getProductsBySearch: (state) => (search: string) => {
      if (search !== '') {
        state.products.filter((product) => product.name.toLowerCase().includes(search.toLowerCase()))
      }
    }
  },
  actions: {
    async fetchProducts() {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product/`)
        this.products = await response.json();
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false
      }
    },
    async addProduct(product: IProduct) {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(product),
        })
        this.products.push(await response.json())
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false
      }
    }
  },
})
