

from selenium.webdriver.common.by import By

# locators
NEW_TODO_LOCATOR = (By.CLASS_NAME, 'new-todo')
ALL_BTN =  (By.CSS_SELECTOR, 'a[href="#/"]')
ACTIVE_BTN = (By.CSS_SELECTOR, 'a[href="#/active"]')
DELETE_BTN = (By.CSS_SELECTOR,"button.destroy")
COMPLETE_BTN = (By.CSS_SELECTOR, 'a[href="#/completed"]')
CLEAR_COMPLETED_BTN = (By.CSS_SELECTOR, "button.clear-completed")
TODO_ITEMS_LEFT =(By.XPATH,'//span[@class="todo-count"]')
TODO_LIST = (By.CLASS_NAME, 'todo-list')
TODO_LIST_ITEMS =(By.CSS_SELECTOR,'[data-id]')
TODO_IDS = (By.TAG_NAME,'li')
TODO_COMPLETED_IDS = (By.CSS_SELECTOR,'li.completed')
CHECKBOX = (By.CSS_SELECTOR,'input[type="checkbox"]')
TOGGLE_ALL = (By.CLASS_NAME, 'toggle-all')

