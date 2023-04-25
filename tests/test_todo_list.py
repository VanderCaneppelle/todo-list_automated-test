from selenium.webdriver.common.keys import Keys
import time
from locator.todo_homepage_locator import *
#from helpers.helpers import *
from selenium.webdriver.common.action_chains import ActionChains
from tests.base_class import BaseClass

class TestToDoList(BaseClass, BaseClass.ToDoList): # testsuite

     NEW_ITEMS = ['Open a Jira ticket', 'Close Test Run', 'Smoke Test']
 
     def test_1_add_new_todo_item(self):
          self.log().info("Todo List - Add New To Do / Items Left ")                             
          self.add_new_todo_items(NEW_TODO_LOCATOR,*self.NEW_ITEMS)                     # Receive the locator and list of items and add to the To Do List
          expected_left_items_qty = self.list_of_active_ids_all_tab()      # Get the qty of active items to compare with the left itmes info
         
          self.assertAddNewItems(self.NEW_ITEMS, expected_left_items_qty) 

          self.log().info("Todo List - Add New To Do - PASS")
          self.log().info("Todo List - Items Left - PASS ")

     
     def test_2_mark_item_as_completed_and_test_left_items(self):
          select_id = self.list_of_active_ids_all_tab()[0]  # Select an ID to be marked as completed, will be use to build the selector
          element = self.get_element(self.selector_builder(select_id))      # Build a selector and store it on element
          element.find_element(*CHECKBOX).click()                           # Click on the checkbox of the element selected.
               
          self.AssertItemIsChecked(select_id) # Ensure selected ID  
 
         
     def test_3_completed_tab(self):
         
          select_id = self.list_of_completed_ids_all_tab()   # get the completed IDS from ALL TAB, to check if its the same on COMPLETED TAB
          self.get_element(COMPLETE_BTN).click()             # click on COMPLETED button

          self.AssertCompletedTabInfo(select_id)            # Ensure the ID checked as completed in ALL TAB is the only ID displayed on COMPLETED TAB
          

     def test_4_active_tab(self):
          self.get_element(ALL_BTN).click()                           # Go to ALL TAB to get the list of items
          active_ids_from_all_tab = self.list_of_active_ids_all_tab() # Get active items frmo ALL TAB, to compare with active item from ACTIVE TAB.
          self.get_element(ACTIVE_BTN).click()                        # Click on ACTIVE
          active_ids_from_active_tab = self.list_of_all_ids_all_tab()  # Get list of all ids from ACTIVE TAB

          self.AssertActiveTabItems(active_ids_from_all_tab, active_ids_from_active_tab)   # Ensure the active items on ACTIVE tab are the same presented on ALL tab


     def test_5_delete_todo(self):
          actions = ActionChains(self.driver)                                             # instantiating the ActionsChains C
          id_selection = self.list_of_all_ids_current_tab()[1]             # select the ID to be deleted. Will be used to build the selector and to check if the right ID wa deleted.
          element_locator = self.get_element(self.selector_builder(id_selection))         # build the selector using the ID selected
          actions.move_to_element(element_locator).perform()                                      # hover over the selected item
          element_locator.find_element(*DELETE_BTN).click()                                       # locate and click on DELETE button
         
          assert id_selection  not in self.list_of_active_ids_active_tab()      # Ensure deleted ID is not present on ACTIVE tab.
          self.get_element(ALL_BTN).click()                                                                      
          assert id_selection not in self.list_of_active_ids_active_tab()       # Ensure deleted ID is not present on ALL tab.
          
     
     def test_6_clear_completed_btn(self):

          self.get_element(CLEAR_COMPLETED_BTN).click()                                        # Locate the CLEAR COMPLETED button and click
          all_tab_completed_id = self.list_of_completed_ids_completed_tab()    # Get all the completed ID from ALL tab
          self.get_element(COMPLETE_BTN).click()                                               # Go to COMPLETE tab
          completed_tab_all_ids = self.list_of_all_ids_current_tab()            # Get all IDS from COMPLETE tab

          assert len(all_tab_completed_id) == 0        # Ensure the  ALL tab has no completed item on it
          assert len(completed_tab_all_ids)  == 0      # Ensure the COMPLETE tab is empty 
       
     














