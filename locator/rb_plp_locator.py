from selenium.webdriver.common.by import By


RESULT_TITLES = (By.CLASS_NAME, 'pdp-link')
PAGE_TITLE = (By.CSS_SELECTOR, '[data-testid="plp-top-title"]')
SELECT_ITEM = (By.PARTIAL_LINK_TEXT ,'Woodford Reserve Double')