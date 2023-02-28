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
  getters: {},
  actions: {
    async fetchProducts() {
      this.isFetching = true
      console.log('fetching products...')
      try {
        const response = await fetch(`${BASE_API_URL}product/`)
        this.products = await response.json();
        this.filteredProducts = this.products;
        this.searchedProducts = this.filteredProducts;
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false
      }
    },
    getProductsByCategory(categoryId: number) {
      if (categoryId === 0) {
        this.filteredProducts = this.products;
        this.searchedProducts = this.filteredProducts; // сохранить результаты фильтрации в поисковом массиве
        return;
      }
      try {
        this.getProductsBySearch(''); // сбросить поиск
        this.filteredProducts = this.products.filter((product) => product.category === categoryId);
        this.searchedProducts = this.filteredProducts; // сохранить результаты фильтрации в поисковом массиве
      } catch (error) {
        console.log(error)
        this.error = error
      }
    },
    getProductsBySearch(search: string) {
      try {
        this.searchedProducts = this.filteredProducts.filter((product) => product.name.toLowerCase().includes(search.toLowerCase()))
      } catch (error) {
        console.log(error)
        this.error = error
      }
    }
  },
})
