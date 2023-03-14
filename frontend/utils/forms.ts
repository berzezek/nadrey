export const productAddFormSettings = {
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
}

export const productCategoryAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить категорию',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},

  ],
};

export const stockAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить cклад',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},

  ],
};

export const productStockAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить продукт',
  formFields: [
    {title: 'Количество', type: 'number', name: 'quantity', required: true, method: 'input', step: 1},
    {
      title: 'Закупочная цена',
      type: 'number',
      name: 'price',
      required: false,
      method: 'input',
      step: 100
    },
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {
      title: 'Тип транзакции', type: 'text', name: 'transaction_type', required: false, method: 'select', selectValue: [
        {name: 'Приход', id: 'in'},
        {name: 'Расход', id: 'out'},
        {name: 'Перемещение', id: 'Перемещение'},
        {name: 'Списание', id: 'write_off'},
        {name: 'Списание по дате', id: 'data_off'},
      ]
    },
  ]
};

export const recipeCategoryAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить рецепт',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
  ]
};

export const recipeAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить рецепт',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
  ]
};

export const propsFormSettings = {
  formAction: '',
  buttonText: 'Добавить',
  formFields: [{
    name: '',
    title: '',
    type: 'text',
    method: 'input',
    required: false,
  }],
  addButton: {
    title: 'Добавить',
    required: false,
    method: 'add',
  }
}

