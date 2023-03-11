export const productStokeAlertSettings = {
  title: 'Успешно',
  text: 'Продукт успешно добавлен',
  type: 'success',
  icon: 'check-circle',
  iconColor: 'green-500'
}

export const productStokeDeleteAlertSettings = {
  title: 'Успешно',
  text: 'Продукт успешно удален',
  type: 'success',
  icon: 'check-circle',
  iconColor: 'red-500'
}

export const productStokeEditAlertSettings = {
  title: 'Успешно',
  text: 'Продукт успешно изменен',
  type: 'success',
  icon: 'check-circle',
  iconColor: 'red-500'
}

export const productStokeTableSettings = {
  columns: [
    {product_name: 'Наименование'},
    {quantity: 'Количество'},
    {price: 'Цена'}
  ]
}

export const productStokeAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить продукт',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {
      title: 'Единица измерения', type: 'text', name: 'unit', required: true, method: 'select', selectValue: [
        {name: 'кг', id: 'kg'},
        {name: 'гр', id: 'gr'},
        {name: 'л', id: 'l'},
        {name: 'мл', id: 'ml'},
        {name: 'шт', id: 'pcs'},
      ]
    },
    {title: 'Вес', type: 'number', name: 'weight', required: false, method: 'input', step: 0.01},
    {title: 'Калории', type: 'number', name: 'calories', required: false, method: 'input', step: 50},

  ],
  addButton: {
    title: 'Добавить категорию',
    method: 'addCategory',
    required: true,
  }
};
