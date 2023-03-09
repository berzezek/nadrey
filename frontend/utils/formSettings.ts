export const productAddFormSettings = {
  formAction: 'addProduct',
  buttonText: 'Добавить',
  modalTitle: 'Добавить продукт',
  formFields: [
    {title: 'Наименование', type: 'text', name: 'name', required: true, method: 'input'},
    {title: 'Описание', type: 'text', name: 'descriptions', required: false, method: 'textarea'},
    {
      title: 'Единица измерения', type: 'text', required: true, method: 'select', selectValue: [
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

export const propsFormSettings = {
  type: Object,
  required: false,
  default: () => ({
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
  }),
}