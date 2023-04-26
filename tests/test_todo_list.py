from tests.base_class import BaseClass
from selenium.webdriver.common.by import By
from locator.todo_homepage_locator import *
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException



class TestToDoList(BaseClass, BaseClass.ToDoList): 

     new_items = ['Open a Jira ticket', 'Close Test Run', 'Smoke Test', 'Close Sprint']
 
     def test_1_add_new_todo_items(self):  # this test cover the all tab also.

          # self.log().info("Todo List - Add New To Do / Items Left ")                             
          self.add_new_todo_items(*self.new_items)                                  # Receive a list of items and add to the To Do List
          expected_left_items_qty = self.list_of_active_ids_all_tab()               # Get the qty of active items to compare with the left itmes info
         
          self.assert_correct_items_added(self.new_items, expected_left_items_qty)  # Ensure the items were added and the items left info is correct
     
     
     def test_2_mark_item_as_complete(self):
          selected_id = self.list_of_active_ids_all_tab()[0]     # Select an ID to be marked as completed, will be use to build the selector
          self.click_checkbox(selected_id)                       # Build the selector and select the specific checkbox 
          self.assert_item_is_checked(selected_id)               # Ensure there is only 1 ID completed, as I only checked 1 item as completed
     
     def test_3_mark_item_as_active(self):
          selected_id = self.list_of_completed_ids_all_tab()[0]  # Select an ID to be marked as completed, will be use to build the selector
          self.click_checkbox(selected_id)                       # Build the selector and select the specific checkbox 
          
          self.assert_item_is_unchecked()     # Ensure there is no item checked on all page
          self.go_to_completed_tab()
          self.assert_complete_tab_is_empty() # Ensure complete tab is empty


     def test_4_completed_tab_displays_correct_info(self):
          self.go_to_all_tab()
          select_id = self.list_of_all_ids_all_tab()[0]                           # Select an ID to be marked as completed
          self.click_checkbox(select_id)                                          # Check item as complete
          completed_ids_from_all_tab = self.list_of_completed_ids_all_tab()       # get the completed IDS from ALL TAB, to check if its the same on COMPLETED TAB       
          self.go_to_completed_tab()
          self.assert_complete_tab_shows_correct_info(completed_ids_from_all_tab) # Ensure the ID checked as completed in ALL TAB is the only ID displayed on COMPLETED TAB
          

     def test_5_active_tab_displays_correct_info(self):
          self.go_to_all_tab()
          active_ids_from_all_tab = self.list_of_active_ids_all_tab()     # Get active items frmo ALL TAB, to compare with active item from ACTIVE TAB.
          self.go_to_active_tab()
          active_ids_from_active_tab = self.list_of_all_ids_active_tab()  # Get list of all ids from ACTIVE TAB

          self.assert_active_tab_shows_correct_info(active_ids_from_all_tab, active_ids_from_active_tab)   # Ensure the active items on ACTIVE tab are the same presented on ALL tab


     def test_6_delete_todos(self):
          selected_id = self.list_of_all_ids_current_tab()[1]         # select the ID to be deleted. 
          self.delete_selected_id(selected_id)                        # hover over the delete item
          self.assert_deleted_id_not_in_active_tab(selected_id)       # Ensure deleted ID is not present on ACTIVE TAB.
          self.go_to_all_tab()                                                                
          self.assert_deleted_id_not_in_all_tab(selected_id)          # Ensure deleted ID is not present on ALL TAB.

     
     def test_7_clear_completed_todos(self):
          self.clear_completed()
          completed_ids_from_all_tab = self.list_of_completed_ids_all_tab() # Get all the completed ID from ALL tab
          self.go_to_completed_tab()                                 
          completed_tab_all_ids = self.list_of_all_ids_current_tab()        # Get all IDS from COMPLETE TAB
          self.assert_all_completed_ids_are_deleted(completed_ids_from_all_tab,completed_tab_all_ids) 


     def test_8_complete_active_all(self):
          self.go_to_all_tab()
          all_ids_all_tab = self.list_of_all_ids_all_tab()      # get list of all ids from ALL TAB
          self.click_toggle_all()                           # complete all
          self.assert_all_todos_are_completed(all_ids_all_tab)  # Ensure all items are comleted
          self.click_toggle_all()                           # active all 
          self.assert_all_todos_are_active(all_ids_all_tab)     # Ensure all items are active

     # def test_9_edit_todo(self):

     #      selected_id = self.list_of_active_ids_all_tab()[0]
     #      actions =ActionChains(self.driver)
     #      element = self.get_element(self.selector_builder(selected_id))      # Build a selector and store it on element
     #      actions.double_click(element).perform()
     #      time.sleep(2)
     #      # edit_field = self.driver.switch_to.active_element
     #      edit_field.clear()
  
     #      edit_field.send_keys("todo edited",Keys.RETURN)
     #      assert "todo edited" in self.todo_name_list()
     #      time.sleep(5)

     # def test_9_edit_todo(self):
     #      selected_id = self.list_of_active_ids_all_tab()[0]
     #      actions = ActionChains(self.driver)
     #      element = self.get_element(self.selector_builder(selected_id))
     #      actions.double_click(element).perform()
     #      time.sleep(2)
     #      edit_field = self.driver.switch_to.active_element  # obter o elemento de edição de tarefa novamente
     #      edit_field.clear()
     #      edit_field.send_keys("todo edited", Keys.RETURN)
     #      assert "todo edited" in self.todo_name_list()
     #      time.sleep(5)



     def test_9_edit_todo(self):
           selected_id = self.list_of_active_ids_all_tab()[0]
           actions = ActionChains(self.driver)
           element = self.get_element(self.selector_builder(selected_id))
           actions.double_click(element).perform()
           element.find_element(*EDIT_TODO).send_keys(Keys.CONTROL + "a")
           element.find_element(*EDIT_TODO).send_keys(Keys.BACKSPACE)
           element.find_element(*EDIT_TODO).send_keys("edited todo",Keys.RETURN)
           assert "edited todo" in self.todo_name_list()
           time.sleep(3)

       
     














