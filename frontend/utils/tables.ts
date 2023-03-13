export const productTableSettings = {
  columns: [
    {name: 'Наименование'},
    {calories: 'Калорийность'},
    {description: 'Описание'}
  ]
}

export const productCategoryTableSettings = {
  columns: [
    {name: 'Наименование'},
    {description: 'Описание'}
  ]
}

export const stockTableSettings = {
  columns: [
    {name: 'Наименование'},
    {description: 'Описание'}
  ]
}

export const productStokeTableSettings = {
  columns: [
    {product: 'Наименование'},
    {quantity: 'Количество на складе'},
    {unit: 'Единица измерения'},
    {max_price: 'Максимальная цена'}
  ]
}
export const productStokeEditTableSettings = {
  columns: [
    {product_name: 'Наименование'},
    {quantity: 'Количество на складе'},
    {product_unit: 'Единица измерения'},
    {price: 'Цена'},
  ]
}