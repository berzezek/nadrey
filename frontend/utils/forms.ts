export const productAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить продукт',
  formFields: [
    {title: 'Наименование *', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {
      title: 'Единица измерения *', type: 'text', name: 'unit', required: true, method: 'select', selectValue: [
        {name: 'кг', id: 'kg'},
        {name: 'гр', id: 'gr'},
        {name: 'л', id: 'l'},
        {name: 'мл', id: 'ml'},
        {name: 'шт', id: 'pcs'},
      ]
    },
    {title: 'Вес', type: 'number', name: 'weight', required: false, method: 'input', step: 0.01},
    {title: 'Калории', type: 'number', name: 'calories', required: false, method: 'input', step: 50},
    {title: 'Категория *', type: 'text', name: 'category', required: true, method: 'select', selectValue: []},
  ],
}

export const productCategoryAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  addMode: true,
  modalTitle: 'Добавить категорию',
  formFields: [
    {title: 'Наименование *', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
  ],
};

export const stockAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить cклад',
  formFields: [
    {title: 'Наименование *', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},

  ],
};

export const productStockAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить продукт',
  formFields: [
    {title: 'Количество *', type: 'number', name: 'quantity', required: true, method: 'input', step: 1},
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
    {
      title: 'Продукт *',
      type: 'text',
      name: 'product',
      required: true,
      method: 'select',
      selectValue: [],
    },
    {
      title: 'Склад *',
      type: 'text',
      name: 'store',
      required: true,
      method: 'select',
      selectValue: [],
    }
  ]
};

export const recipeCategoryAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить рецепт',
  formFields: [
    {title: 'Наименование *', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
  ]
};

export const recipeIngredientAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить рецепт',
  formFields: [
    {title: 'Наименование *', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {title: 'Цена', type: 'number', name: 'price', required: false, method: 'input', step: 100},
    {title: 'Фактический вес', type: 'number', name: 'weight', required: false, method: 'input', step: 0.1},
  ]
};

export const ingredientsAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  formFields: [
    {title: 'Количество *', type: 'number', name: 'quantity', required: true, method: 'input', step: 0.01},
    {title: 'Продукт *', type: 'text', name: 'product', required: true, method: 'select', selectValue: []}
  ]
};

export const clientAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить клиента',
  formFields: [
    {title: 'Имя *', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {title: 'Контакты *', type: 'text', name: 'phone', required: true, method: 'input'},
    {title: 'Почта', type: 'email', name: 'email', required: false, method: 'input'},
    {title: 'Дата рождения', type: 'date', name: 'birthday', required: false, method: 'input'},
    {title: 'Адрес', type: 'text', name: 'address', required: false, method: 'input'},
  ]
};

export const orderAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить заказ',
  formFields: [
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {title: 'Количество *', type: 'number', name: 'quantity', required: true, method: 'input', step: 0.1},
    {title: 'Готов', type: 'checkbox', name: 'is_completed', required: false, method: 'checkbox'},
  ]
};

export const cardAddFormSettings = {
  formAction: 'addItem',
  buttonText: 'Добавить',
  modalTitle: 'Добавить корзину',
  formFields: [
    {title: 'Описание', type: 'text', name: 'description', required: false, method: 'textarea'},
    {title: 'Оплачен', type: 'checkbox', name: 'is_paid', required: false, method: 'checkbox'},
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

