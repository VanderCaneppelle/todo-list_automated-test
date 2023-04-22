from selenium.webdriver.common.keys import Keys
import time
from locator.todo_homepage_locator import *
from helpers.helpers import *
from selenium.webdriver.common.action_chains import ActionChains
from tests.base_class import BaseClass

class TestToDoList(BaseClass, BaseClass.ToDoList): # testsuite
    

     NEW_ITEMS = ['Open a Jira ticket', 'Close Test Run', 'Smoke Test', 'onemore']
 
     def test_1_add_new_todo_item(self):
          self.log().info("Todo List - Add New To Do / Items Left ")   # Instantiating the logger
          
          self.add_new_todo_items(NEW_TODO_LOCATOR,*self.NEW_ITEMS)    # add a new todo item
          assert self.all_todo_items_list(TODO_LIST_ITEMS) == self.NEW_ITEMS       # Ensure the list of TO DO items matches with the items entered.          
          assert self.items_left(TODO_COUNT) == len(self.list_of_all_ids(TODO_LIST_ITEMS)) # Ensure the items left information matches with the qty of active items.
       
          self.log().info("Todo List - Add New To Do - PASS")
          self.log().info("Todo List - Items Left - PASS ")

     
     def test_2_mark_item_as_completed_on_all_tab_and_check_completed_tab(self):
        # get the first ID of the To Do list items, for later use this ID to mark as complete.
          self.select_id = self.list_of_all_ids(TODO_LIST_ITEMS)[0]
        # Pass the selected ID to the selector function, this will ensure that the checkbox  checked is always the one that is set on select_id
          checkbox_locator = self.insert_id_into_selector(self.select_id)
          # Logger instantianting 
          self.log().info("To Do list - All task")
          # click on checkbox to complete
          self.get_element(checkbox_locator).click()
          self.active_ids_from_all_tab = self.list_of_active_ids_current_tab(TODO_COMPLETED_IDS,TODO_LIST_ITEMS)
          self.completed_ids_from_all_tab= self.list_of_completed_ids_current_tab(TODO_COMPLETED_IDS)
          left_items_value = self.items_left(TODO_COUNT)
          # assert there is only 1 item marked as checked, and that this item is the one that meant to be, and test if the left items value changed accordingly when the checkbox was completed.
          assert len(self.completed_ids_from_all_tab) == 1 
          assert self.select_id in self.completed_ids_from_all_tab 
          assert len(self.active_ids_from_all_tab) == left_items_value
          # Ensure the completed item is presented on COMPLETED tab.
          self.log().info("To Do list - All tab - PASS")
     '''    
     def test_4_completed_tab(self):
         self.log().info("To Do list - Completed task tab")
         
         self.get_element(COMPLETE_BTN).click()
         all_ids_from_completed_tab = get_list_of_all_ids(self) 
         assert len(all_ids_from_completed_tab) == 1 and all_ids_from_completed_tab == completed_ids_from_all_tab and select_id in all_ids_from_completed_tab
         
         self.log().info("To Do list - Completed task tab - PASS")


   
  
    def test_5_active_tab(self):
          self.log().info("To Do list - Active tab test")
          self.get_element(ACTIVE_BTN).click()
          active_list = get_list_of_all_ids(self)
          active_set = set(active_list)
          active_ids_set = set(active_ids_from_all_tab)
          assert active_set == active_ids_set
          # assert active_list  in  active_ids_from_all_tab
          self.log().info("To Do list - Active tab test")

     def test_6_delete_todo(self):
          actions = ActionChains(self.driver)
          self.log().info("To Do list - Detele To Do button test")
          id_selection = list_of_active_ids(self)[1]
          element = self.get_element(element_id(id_selection))

          # Passe o mouse sobre o elemento
          actions.move_to_element(element).perform()

          # Localize e clique no botão "destroy"
          btn_delete = element.find_element(*DELETE_BTN)
          btn_delete.click()
          assert id_selection  not in list_of_active_ids(self)
          
          self.log().info("To Do list - Delete To Do button test")


     def test_7_clear_completed_btn(self):
          self.log().info("To Do list -Clear Completed Test")
          btn_all = self.get_element(ALL_BTN)
          btn_all.click()
          self.get_element(CLEAR_COMPLETED).click()
          all_tab_completed_id = get_list_of_completed_ids(self)
          self.get_element(COMPLETE_BTN).click()
          completed_tab_ids = get_list_of_all_ids(self)

          assert len(all_tab_completed_id) == 0 and len(completed_tab_ids) == 0
     '''














