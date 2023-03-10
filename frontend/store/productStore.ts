import {defineStore} from 'pinia'
import {BASE_API_URL} from '~/utils/constants'
import {IProduct} from "~/types";

export const useProductStore = defineStore('products', {
  state: () => ({
    products: [] as IProduct[],
    productDetail: {} as IProduct,
    filteredProducts: [] as IProduct[],
    searchedProducts: [] as IProduct[],
    error: null as any,
    isFetching: false,
  }),
  getters: {
    getProductsByCategory: (state) => (categoryId: number) => {
      if (categoryId === 0) {
        return state.products;
      }
      return state.products.filter((product) => product.category === categoryId);
    },
    getProductsBySearch: (state) => (search: string) => {
      if (search === '') {
        return state.products;
      }
      return state.products.filter((product) => product.name.toLowerCase().includes(search.toLowerCase()));
    }
  },
  actions: {
    async fetchProducts() {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product/`)
        this.products = await response.json();
        return this.products
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false
      }
    },
    async getProductById(id: number) {
      this.isFetching = true;
      try {
        const response = await fetch(`${BASE_API_URL}product/${id}/`)
        this.productDetail = await response.json();
        return this.productDetail
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async addProduct(product: IProduct) {
      this.isFetching = true;
      try {
        const response = await fetch(`${BASE_API_URL}product/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(product)
        })
        return await response.json();
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async updateProduct(product: IProduct) {
      this.isFetching = true;
      try {
        const response = await fetch(`${BASE_API_URL}product/${product.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(product)
        })
        return await response.json();
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async deleteProduct(id: number) {
      this.isFetching = true;
      try {
        await fetch(`${BASE_API_URL}product/${id}/`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
        })
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    }
  },
})
