from tests import BaseClass
from selenium.webdriver.common.keys import Keys
import time
from locator.rb_homepage_locator import *
from helpers import helpers
# from locator.rb_plp_locator import *
# from locator.rb_pdp_locator import *
# from locator.rb_checkout_page_locator import *

class TestToDoList(BaseClass): # testsuite
    
    # TODO1 = "TODO1"
    # TODO2 = "TODO2"
    TODOS = ['Open a Jira ticket', 'Close Test Run', 'Smoke Test']
    SEARCH_TEXT = "Bourbon"
    ENGRAVING_TEXT = "Engraving test"
    
    def test_1_add_new_todo_item(self):

        ''' This is a test case to test the add new todo item action. '''
        # Instantiating the logger
        self.log().info("Todo List - Add New To Do")
        # Opening ToDo Url
        self.driver.get('https://todomvc.com/examples/vanilla-es6')
        # add a new todo item
        self.get_element(NEW_TODO).send_keys(self.TODOS[0],Keys.RETURN)
        self.get_element(NEW_TODO).send_keys(self.TODOS[1],Keys.RETURN)
        self.get_element(NEW_TODO).send_keys(self.TODOS[2],Keys.RETURN)


        assert helpers.get_todo_items_list(self) == self.TODOS
        self.log().info("Todo List - Add New To Do - PASS")

    # def test_2_remove_todo_item(self):
        #   self.log().info("Todo List - Remove To Do Item ")
    #      self.get_element(SEARCH_BAR).click()
    #     self.get_element(SEARCH_INPUT).click()
    #     self.get_element(SEARCH_INPUT).send_keys(self.SEARCH_TEXT)
    #     self.get_element(SEARCH_BUTTON).submit()
    #     plp_title = self.get_element(PAGE_TITLE).text
    #     self.log().info("Reserve Bar - Search Bar query test >> PASS << ")
    #     assert  plp_title == self.SEARCH_TEXT

    # def test_3_select_product_from_plp(self):
    #     self.log().info("Reserve Bar - Select PLP item started ")
    #     plp_product_title = self.get_element(SELECT_ITEM).text
    #     self.get_element(SELECT_ITEM).click()
    #     pdp_product_title = self.get_element(PDP_PRODUCT_NAME).text
    #     self.log().info("Reserve Bar - Select PLP item  >> PASS <<")
    #     assert pdp_product_title.lower() == plp_product_title.lower()


    # def test_4_add_engraving_and_add_to_cart(self):
    #     self.log().info("Reserver Bar - Select ship delivery method started")
    #     self.get_element(SHIP).click()
    #     self.get_element(CUSTOM_ENGRAVING).click()
    #     self.get_element(ENGRAVING_INPUT).send_keys(self.ENGRAVING_TEXT)
    #     self.get_element(SAVE_ENGRAVING).click()
    #     self.get_element(ADD_TO_CART).click()
    #     engraving_cart = self.get_element(CART_ENGRAVING_INFO).text
    #     assert self.ENGRAVING_TEXT.lower() in engraving_cart.lower()
    #     self.log().info("Reserver Bar - Select ship delivery methodo>> PASS <<")


    # def test_5_go_checkout(self):
    #     self.log().info("Reserver Bar - Go to Checkout started")
    #     cart_info = self.cart_info(CART_PRODUCT,CART_PRICE,self.ENGRAVING_TEXT)
    #     self.get_element(CHECKOUT_BTN).click()
    #     checkout_info = self.checkout_info(CKT_PRODUCT,CKT_ENGRAVING_TEXT,CKT_PRICE)
    #     assert checkout_info == cart_info
    #     self.log().info("Reserver Bar - Go to Checkout >> PASS <<")
    #     self.log().info(checkout_info)
    #     self.log().info(cart_info)












