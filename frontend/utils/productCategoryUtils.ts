export const productCategoryAlertSettings = {
  title: 'Успешно',
  text: 'Продукт успешно добавлен',
  type: 'success',
  icon: 'check-circle',
  iconColor: 'green-500'
}

export const productCategoryDeleteAlertSettings = {
  title: 'Успешно',
  text: 'Продукт успешно удален',
  type: 'success',
  icon: 'check-circle',
  iconColor: 'red-500'
}

export const productCategoryEditAlertSettings = {
  title: 'Успешно',
  text: 'Продукт успешно изменен',
  type: 'success',
  icon: 'check-circle',
  iconColor: 'yellow-500'
}

export const productCategoryTableSettings = {
  columns: [
    {name: 'Наименование'},
    {description: 'Описание'}
  ]
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