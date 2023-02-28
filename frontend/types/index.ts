export interface IProductCategory {
  id: number
  name: string
  description: string
}

export interface IProduct {
  id: number
  name: string
  description: string
  unit: string
  weight: number
  calories: number
  category: number
}