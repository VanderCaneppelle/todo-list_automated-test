from tests import BaseClass
from selenium.webdriver.common.keys import Keys
import time
from locator.todo_homepage_locator import *
from helpers import helpers
# from locator.rb_plp_locator import *
# from locator.rb_pdp_locator import *
# from locator.rb_checkout_page_locator import *

class TestToDoList(BaseClass): # testsuite
    

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
         list_of_active_items = helpers.get_list_of_active_ids(self)
         assert (len(list_of_active_items)) == items_left_text

         self.log().info("Todo List - Items Left - PASS ")


    def test_3_mark_item_as_completed_on_all_tab_and_check_completed_tab(self):
        # get the first ID of the To Do list items
         select_id = helpers.get_list_of_all_ids(self)[0]
        # Pass the selected ID to the selector function, this will ensure that the checkbox  checked is always the one that is set on select_id
         checkbox_to_complete = checkbox(select_id)
          # Logger instantianting 
         self.log().info("To Do list - Complete task")
          # click on checkbox to complete
         self.get_element(checkbox_to_complete).click()
          # get lists of active, completed items, and also the left items information.
         completed_ids_from_all_tab= helpers.get_list_of_completed_ids(self)
         active_ids_form_completed_tab = helpers.get_list_of_active_ids(self)
         left_items_value = helpers.get_item_left(self)
          # assert there is only 1 item marked as checked, and that this item is the one that meant to be, and test if the left items value changed accordingly when the checkbox was completed.
         assert len(completed_ids_from_all_tab) == 1 and select_id in completed_ids_from_all_tab and  len(active_ids_form_completed_tab) == left_items_value
          # Ensure the completed item is presented on COMPLETED tab.
         self.get_element(COMPLETE_BTN).click()
         all_ids_from_completed_tab = helpers.get_list_of_all_ids(self) 
         assert len(all_ids_from_completed_tab) == 1 and all_ids_from_completed_tab == completed_ids_from_all_tab and select_id in all_ids_from_completed_tab
         
         self.log().info("To Do list - Completed task tab - PASS")


    def test_4_active_tab(self):
          self.log().info("To Do list - Active tab test")
          self.get_element(ACTIVE_BTN).click()


    #     self.get_element(CUSTOM_ENGRAVING).click()
    #     self.get_element(ENGRAVING_INPUT).send_keys(self.ENGRAVING_TEXT)
    #     self.get_element(SAVE_ENGRAVING).click()
    #     self.get_element(ADD_TO_CART).click()
    #     engraving_cart = self.get_element(CART_ENGRAVING_INFO).text
    #     assert self.ENGRAVING_TEXT.lower() in engraving_cart.lower()
          self.log().info("To Do list - Active tab test")



    # def test_5_go_checkout(self):
    #     self.log().info("Reserver Bar - Go to Checkout started")
    #     cart_info = self.cart_info(CART_PRODUCT,CART_PRICE,self.ENGRAVING_TEXT)
    #     self.get_element(CHECKOUT_BTN).click()
    #     checkout_info = self.checkout_info(CKT_PRODUCT,CKT_ENGRAVING_TEXT,CKT_PRICE)
    #     assert checkout_info == cart_info
    #     self.log().info("Reserver Bar - Go to Checkout >> PASS <<")
    #     self.log().info(checkout_info)
    #     self.log().info(cart_info)












