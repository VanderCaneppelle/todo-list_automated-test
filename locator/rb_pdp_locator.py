from selenium.webdriver.common.by import By


SHIP = (By.ID, 'rb_shipping')
CUSTOM_ENGRAVING = (By.ID, 'customEngraving')
ENGRAVING_INPUT = (By.ID,'engraving1')
SAVE_ENGRAVING = (By.ID, 'btnSaveEngraving')
ADD_TO_CART = (By.CLASS_NAME, 'cart-and-ipay')
CART_ENGRAVING_INFO = (By.CLASS_NAME, 'engraving-line')
CHECKOUT_BTN = (By.CSS_SELECTOR, '[data-testid="checkoutBtn"]')
PDP_PRODUCT_NAME =(By.CSS_SELECTOR,'[data-testid="productName"]')
PRODUCT = (By.CSS_SELECTOR, '.card-body .line-item-name')
CART_PRICE = (By.CSS_SELECTOR, '[data-testid="cartProductPrice"]')
CART_PRODUCT = (By.CSS_SELECTOR, "[data-testid='productName']")
