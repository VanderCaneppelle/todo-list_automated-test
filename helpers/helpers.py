
from selenium.webdriver.common.by import By
TODO_LIST = (By.CLASS_NAME, 'todo-list')
TODO_LIST_ITEMS =(By.CSS_SELECTOR,'[data-id]')
TODO_COUNT =(By.XPATH,'//span[@class="todo-count"]')
TODO_IDS = (By.TAG_NAME,'li')
TODO_COMPLETED_IDS = (By.CSS_SELECTOR,'li.completed')


# get all the to do task NAME and return in a list
def get_todo_items_list(self): 
    todo_items = []
    items = self.driver.find_elements(*TODO_LIST_ITEMS)
    for item in items:
        text = item.text
        todo_items.append(text)
             
    return todo_items


# get the text that is presetend on the bottom, with the items left information.
def get_item_left(self): 
    left = self.driver.find_element(*TODO_COUNT).text
    qty = left.split()[0]      
    return int(qty)


 # get a list of all IDS in a tab
def get_list_of_all_ids(self):
     id_list = []
     ids = self.driver.find_elements(*TODO_LIST_ITEMS)
     for id in ids:
        value = id.get_attribute("data-id")
        id_list.append(value)

     return id_list


# get a list of all completed ids in a tab
def get_list_of_completed_ids(self):
     completed_id_list = []
     completed_ids = self.driver.find_elements(*TODO_COMPLETED_IDS)
     for id in completed_ids:
        value = id.get_attribute("data-id")
        completed_id_list.append(value)

     return completed_id_list

def get_list_of_active_ids(self):
    active_ids = []
    all_ids = get_list_of_all_ids(self)
    completed_ids = get_list_of_completed_ids(self)

    for id in set(all_ids) - set(completed_ids):
        active_ids.append(id)
    
    return active_ids




