from tests import BaseClass
from selenium.webdriver.common.keys import Keys
import time
from locator.todo_homepage_locator import *
from helpers import helpers
# from locator.rb_plp_locator import *
# from locator.rb_pdp_locator import *
# from locator.rb_checkout_page_locator import *

class TestToDoList(BaseClass): # testsuite
    
    # TODO1 = "TODO1"
    # TODO2 = "TODO2"
    TODOS = ['Open a Jira ticket', 'Close Test Run', 'Smoke Test']
 
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
        
        #Ensure the list of TO DO items matches with the items entered.
        assert helpers.get_todo_items_list(self) == self.TODOS
        self.log().info("Todo List - Add New To Do - PASS")


    def test_2_items_left_all_tab(self):
         
         self.log().info("Todo List - Items Left ")
         
         items_left_text = helpers.get_item_left(self)
         list_of_active_items = helpers.get_todo_items_list(self)
         assert (len(list_of_active_items)) == items_left_text

         self.log().info("Todo List - Items Left - PASS ")


    def test_3_mark_item_as_completed_and_check_completed_tab(self):

         self.log().info("To Do list - Complete task")
         select_id = helpers.get_list_of_all_ids(self)[0]

         CHECKBOX = (By.CSS_SELECTOR, f'li[data-id="{select_id}"] input[type="checkbox"]')
         self.get_element(CHECKBOX).click()

         completed_items = helpers.get_list_of_completed_ids(self)
         active_items = len(helpers.get_list_of_active_ids(self))
         left_items_value = helpers.get_item_left(self)

         assert len(completed_items) == 1 and select_id in completed_items and  active_items == left_items_value

         self.get_element(COMPLETE_BTN).click()
         all_ids_from_completed_tab = helpers.get_list_of_all_ids(self) 
         completed_ids_from_completed_tab = helpers.get_list_of_completed_ids(self)

         assert len(all_ids_from_completed_tab) == 1 and all_ids_from_completed_tab == completed_ids_from_completed_tab and select_id in all_ids_from_completed_tab
         time.sleep(3)


        

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












