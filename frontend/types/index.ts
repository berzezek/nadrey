import {RuntimeConfig} from "@nuxt/schema";

export interface IrunTimeConfig extends  RuntimeConfig {
  apiBase?: string
  localeApiBase?: string
}

interface Item {
  id: number
  name: string
  description: string
}

export interface IProductCategory extends Item {
}

export interface IProduct extends Item {
  unit: string
  weight: number
  calories: number
  category: number
}