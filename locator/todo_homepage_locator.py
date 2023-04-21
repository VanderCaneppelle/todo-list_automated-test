from selenium.webdriver.common.by import By

# locators
NEW_TODO = (By.CLASS_NAME, 'new-todo')
COMPLETE_BTN = (By.CSS_SELECTOR, 'a[href="#/completed"]')
ACTIVE_BTN = (By.CSS_SELECTOR, 'a[href="#/active"]')
DELETE_BTN = (By.CSS_SELECTOR,"button.destroy")
ELEMENT = (By.CSS_SELECTOR, "li[data-id='1682082599179']")
ALL_BTN =  (By.CSS_SELECTOR, 'a[href="#/"]')
CLEAR_COMPLETED = (By.CSS_SELECTOR, "button.clear-completed")

def element_id(id):
    DELETE = (By.CSS_SELECTOR, f'li[data-id="{id}"]')
    
    return DELETE


def checkbox(id):
    CHECKBOX = (By.CSS_SELECTOR, f'li[data-id="{id}"] input[type="checkbox"]')

    return CHECKBOX


def item_to_delete(id):
    delete =  (By.CSS_SELECTOR, f'li[data-id="{id}"] button.destroy')
    return delete
