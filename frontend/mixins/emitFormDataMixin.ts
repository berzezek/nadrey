import {itemAlertSettings, itemDeleteAlertSettings, itemEditAlertSettings} from "~/utils/alerts";
import { useKitchenStore } from "~/store/kitchenStore";
const kitchenStore = useKitchenStore();

export const emitFormDataMixin = async (
  data: any,
  action: string,
  final_url: string,
  closeModal: Function,
  alerting: Function
) => {
  if (action === 'addItem') {
    await kitchenStore.addItem(data, final_url);
    closeModal();
    alerting(itemAlertSettings);
  } else if (action === 'updateItem') {
    console.log(data)
    await kitchenStore.updateItem(data, data.id, final_url);
    closeModal();
    alerting(itemEditAlertSettings);
  } else if (action === 'deleteItem') {
    await kitchenStore.deleteItem(data, final_url);
    closeModal();
    alerting(itemDeleteAlertSettings);
  }
}