import {defineStore} from "pinia";
import {IProduct} from "~/types";
import {BASE_API_URL} from "~/utils/constants";

export const useProductStore = defineStore({
  id: 'product',
  state: () => ({
    products: [] as IProduct[],
    pendingProducts: true,
  }),
  getters: {},
  actions: {
    fetchProducts: async function () {
      try {
        const response = await fetch(`${BASE_API_URL}product/`)
        if (response.ok) {
          this.products = await response.json();
          this.pendingProducts = false;
        }
      } catch (error) {
        console.log(error);
      }
    },
  }
})