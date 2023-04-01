export const productTableSettings = {
  columns: [
    {name: 'Наименование'},
    {unit_russian: 'Единица измерения'},
    {category_name: 'Категория'},
    {calories: 'Калорий на ед.'},
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
    {average_price: 'Средняя цена'}
  ]
}

export const productStockEditTableSettings = {
  columns: [
    {product_name: 'Наименование'},
    {quantity: 'Количество'},
    {product_unit: 'Единица измерения'},
    {transaction_type_russian: 'Тип транзакции'},
    {price: 'Цена'},
  ]
}

export const recipeCategoryTableSettings = {
  columns: [
    {name: 'Наименование'},
    {description: 'Описание за ед.'},
  ]
}
export const recipeTableSettings = {
  columns: [
    {category: 'Категория'},
    // {image: 'Изображение'},
    {name: 'Наименование'},
    {total_product_weight: 'Вес продуктов'},
    {weight: 'Фактический вес'},
    {total_average_price: 'Средняя цена  *'},
    {total_max_price: 'Максимальная цена  *'},
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
    {quantity: 'Количество'},
    {is_completed: 'Готов'},
    {description: 'Описание'}
  ]
}

export const cardTableSettings = {
  columns: [
    {card_client: 'Клиент'},
    {date_created: 'Дата создания'},
    {is_paid: 'Оплачен'},
  ]
}
