import {defineStore} from 'pinia'
import {BASE_API_URL} from '~/utils/constants'
import {IProduct} from "~/types";

export const useProductStokeStore = defineStore('productsStoke', {
  state: () => ({
    productsStoke: [] as IProduct[],
    productDetail: {} as IProduct,
    error: null as any,
    isFetching: false,
  }),
  getters: {
    // getProductsStokeByCategory: (state) => (categoryId: number) => {
    //   if (categoryId === 0) {
    //     return state.productsStoke;
    //   }
    //   return state.productsStoke.filter((product) => product.category === categoryId);
    // },
    // getProductsStokeBySearch: (state) => (search: string) => {
    //   if (search === '') {
    //     return state.productsStoke;
    //   }
    //   return state.productsStoke.filter((product) => product.name.toLowerCase().includes(search.toLowerCase()));
    // }
  },
  actions: {
    async fetchProductsStoke() {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}product-in-stoke/`)
        this.productsStoke = await response.json();
        return this.productsStoke
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false
      }
    },
    // async getProductStokeById(id: number) {
    //   this.isFetching = true;
    //   try {
    //     const response = await fetch(`${BASE_API_URL}product-in-store/${id}/`)
    //     this.productDetail = await response.json();
    //     return this.productDetail
    //   } catch (error) {
    //     console.log(error)
    //     this.error = error
    //   } finally {
    //     this.isFetching = false;
    //   }
    // },
    // async addProductStoke(product: IProduct) {
    //   this.isFetching = true;
    //   try {
    //     const response = await fetch(`${BASE_API_URL}product-in-store/`, {
    //       method: 'POST',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify(product)
    //     })
    //     return await response.json();
    //   } catch (error) {
    //     console.log(error)
    //     this.error = error
    //   } finally {
    //     this.isFetching = false;
    //   }
    // },
    // async updateProductStoke(product: IProduct) {
    //   this.isFetching = true;
    //   try {
    //     const response = await fetch(`${BASE_API_URL}product-in-store/${product.id}/`, {
    //       method: 'PUT',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify(product)
    //     })
    //     return await response.json();
    //   } catch (error) {
    //     console.log(error)
    //     this.error = error
    //   } finally {
    //     this.isFetching = false;
    //   }
    // },
    // async deleteProductStoke(id: number) {
    //   this.isFetching = true;
    //   try {
    //     await fetch(`${BASE_API_URL}product-in-store/${id}/`, {
    //       method: 'DELETE',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //     })
    //   } catch (error) {
    //     console.log(error)
    //     this.error = error
    //   } finally {
    //     this.isFetching = false;
    //   }
    // }
  },
})
