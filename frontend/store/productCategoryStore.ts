import {defineStore} from 'pinia'
import {BASE_API_URL} from '~/utils/constants'
import {IProductCategory} from "~/types";
export const useProductCategoryStore = defineStore('product-category', {
  state: () => ({
    productCategories: [] as IProductCategory[],
    error:  null as any,
    isFetching: false,
  }),
  getters: {
    getProductCategories(state) {
      return state.productCategories
    }
  },
  actions: {
    async fetchProductCategories() {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product-category/`)
        this.productCategories = await response.json()
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false
      }
    },
    async addProductCategory(productCategory: IProductCategory) {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product-category/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(productCategory)
        })
        const data = await response.json()
        this.productCategories.push(data)
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false;
        alert('Категория добавлена')
      }
    }
  },
})