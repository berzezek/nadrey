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
    {product__name: 'Наименование'},
    {product_quantity: 'Количество на складе'},
    {unit: 'Единица измерения'},
    {max_price: 'Максимальная цена'},
    {average_price: 'Усредненная цена'}
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
    {category: 'Категория'},
    // {image: 'Изображение'},
    {name: 'Наименование'},
    {total_product_weight: 'Вес продуктов'},
    {weight: 'Фактический вес'},
    {total_average_price: 'Средняя цена *'},
    {total_max_price: 'Максимальная цена *'},
    {price: 'Фактическая цена'},
  ]
}
export const recipeIngredientsTableSettings = {
  columns: [
    {name: 'Наименование'},
    {quantity: 'Количество'},
    {unit: 'Ед'},
    {unit_weight: 'Вес продукта'},
    {max_price: 'Максимальная цена'},
    {average_price: 'Средняя цена'},
  ]
}

export const clientTableSettings = {
  columns: [
    {name: 'Наименование'},
    {phone: 'Телефон'},
    {email: 'Email'},
    {address: 'Адрес'},
    {birthday: 'Дата рождения'},
    {description: 'Описание'},
  ]
}

export const orderTableSettings = {
  columns: [
    {recipe_name: 'Рецепт'},
    {description: 'Описание'},
    {quantity: 'Количество'},
    {is_completed: 'Готов'}
  ]
}

export const cardTableSettings = {
  columns: [
    {card_client: 'Клиент'},
    {is_paid: 'Оплачен'},
  ]
}
