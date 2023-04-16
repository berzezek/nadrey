import {defineStore} from 'pinia'

const BASE_API_URL = 'http://nadrey.tw1.su/api/v1/';
console.log(BASE_API_URL)

export const useKitchenStore = defineStore('kitchen', {
  state: () => ({
    items: [],
    item: {},
    error: null as any,
    isFetching: false,
  }),
  getters: {
    getItemsById: (state) => (id: number | string, param: string) => {
      if (id === 0 || id === '0' || id === '') {
        return state.items;
      }
      return state.items.filter((item) => item[param] === id);
    },
    getItemsBySearch: (state) => (search: string, param: keyof typeof state.item) => {
      if (search === '') {
        return state.items;
      }
      return state.items.filter((item: string) => item[param]?.toLowerCase().includes(search.toLowerCase()));
    }
  },
  actions: {
    async fetchItems(url: string) {
      this.isFetching = true
      try {
        const response = await fetch(`${BASE_API_URL}${url}/`)
        this.items = await response.json();
        return this.items
      } catch (error) {
        this.error = error
      } finally {
        this.isFetching = false
      }
    },
    async getItemById(id: number, url: string) {
      this.isFetching = true;
      console.log(`${BASE_API_URL}${url}/${id}/`)
      try {
        const response = await fetch(`${BASE_API_URL}${url}/${id}/`)
        this.item = await response.json();
        return this.item
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async addItem(data: {}, url: string) {
      this.isFetching = true;
      try {
        const response = await fetch(`${BASE_API_URL}${url}/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        return await response.json();
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async updateItem(data: {}, id: number | string, url: string ) {
      this.isFetching = true;
      try {
        const response = await fetch(`${BASE_API_URL}${url}/${id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        return await response.json();
      } catch (error) {
        console.log(error)
        this.error = error
      } finally {
        this.isFetching = false;
      }
    },
    async deleteItem(id: number, url: string) {
      this.isFetching = true;
      try {
        await fetch(`${BASE_API_URL}${url}/${id}/`, {
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
