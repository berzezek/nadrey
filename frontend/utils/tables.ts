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

export const productStockTableSettings = {
  columns: [
    {product: 'Наименование'},
    {quantity: 'Количество на складе'},
    {unit: 'Единица измерения'},
    {max_price: 'Максимальная цена'}
  ]
}
export const productStockEditTableSettings = {
  columns: [
    {product_name: 'Наименование'},
    {quantity: 'Количество на складе'},
    {product_unit: 'Единица измерения'},
    {transaction_type: 'Тип транзакции'},
    {price: 'Цена'},
  ]
}
export const recipeCategoryTableSettings = {
  columns: [
    {name: 'Наименование'},
    {description: 'Описание'},
  ]
}
export const recipeTableSettings = {
  columns: [
    {get_category: 'Категория'},
    {image: 'Изображение'},
    {name: 'Наименование'},
    {total_weight: 'Вес продуктов'},
    {weight: 'Фактический вес'},
    {total_price: 'Цена продуктов'},
    {price: 'Фактическая цена'},
  ]
}