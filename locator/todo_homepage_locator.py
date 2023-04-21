from selenium.webdriver.common.by import By

# locators
# ADDRESS_INPUT= (By.ID, 'header-address-select')
NEW_TODO = (By.CLASS_NAME, 'new-todo')
COMPLETE_BTN = (By.CSS_SELECTOR, 'a[href="#/completed"]')
ACTIVE_BTN = (By.CSS_SELECTOR, 'a[href="#/active"]')


def checkbox(id):
    CHECKBOX = (By.CSS_SELECTOR, f'li[data-id="{id}"] input[type="checkbox"]')

    return CHECKBOX
