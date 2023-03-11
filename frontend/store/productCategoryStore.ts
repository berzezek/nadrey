import {defineStore} from 'pinia'
import {BASE_API_URL} from '~/utils/constants'
import {IProductCategory} from "~/types";

export const useProductCategoryStore = defineStore('product-category', {
  state: () => ({
    productCategories: [] as IProductCategory[],
    error: null as any,
    isFetching: false,
  }),
  getters: {
    getProductCategoryBySearch: (state) => (search: string) => {
      if (search === '') {
        return state.productCategories;
      }
      return state.productCategories.filter((productCategory) => productCategory.name.toLowerCase().includes(search.toLowerCase()));
    }
  },
  actions: {
    async fetchProductCategories() {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product-category/`)
        this.productCategories = await response.json()
        return this.productCategories
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
      }
    },
    async updateProductCategory(productCategory: IProductCategory) {
      this.isFetching = true;
      try {
        const response = await fetch(`${BASE_API_URL}product-category/${productCategory.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(productCategory)
        })
        const data = await response.json()
        this.productCategories = this.productCategories.map((productCategory) => productCategory.id === data.id ? data : productCategory)
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async deleteProductCategory(id: number) {
      this.isFetching = true;
      try {
        await fetch(`${BASE_API_URL}product-category/${id}/`, {
          method: 'DELETE',
        })
        this.productCategories = this.productCategories.filter((productCategory) => productCategory.id !== id)
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false;
      }
    }
  },
})