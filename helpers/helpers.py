
from selenium.webdriver.common.by import By
TODO_LIST = (By.CLASS_NAME, 'todo-list')
TODO_LIST_ITEMS =(By.CSS_SELECTOR,'[data-id]')

def get_todo_items_list(self): 
    todo_items = []
    # todo_list = self.driver.find_element_by_id(TODO_LIST)
    items = self.driver.find_elements(*TODO_LIST_ITEMS)
    for item in items:
        text = item.text
        todo_items.append(text)
             
    return todo_items