from selenium.webdriver.common.by import By

# locators
NEW_TODO_LOCATOR = (By.CLASS_NAME, 'new-todo')
COMPLETE_BTN = (By.CSS_SELECTOR, 'a[href="#/completed"]')
ACTIVE_BTN = (By.CSS_SELECTOR, 'a[href="#/active"]')
DELETE_BTN = (By.CSS_SELECTOR,"button.destroy")
ALL_BTN =  (By.CSS_SELECTOR, 'a[href="#/"]')
CLEAR_COMPLETED = (By.CSS_SELECTOR, "button.clear-completed")
TODO_COUNT =(By.XPATH,'//span[@class="todo-count"]')
TODO_LIST = (By.CLASS_NAME, 'todo-list')
TODO_LIST_ITEMS =(By.CSS_SELECTOR,'[data-id]')
TODO_IDS = (By.TAG_NAME,'li')
TODO_COMPLETED_IDS = (By.CSS_SELECTOR,'li.completed')


# def insert_id_into_selector(id):
#     CHECKBOX = (By.CSS_SELECTOR, f'li[data-id="{id}"] input[type="checkbox"]')

#     return CHECKBOX


# def item_to_delete(id):
#     delete =  (By.CSS_SELECTOR, f'li[data-id="{id}"] button.destroy')
#     return delete
