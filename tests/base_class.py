import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import config, pytest, time
from selenium.webdriver.common.keys import Keys
from locator.todo_homepage_locator import *
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def log(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(f'{config.LOG_FOLDER}/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_element(self, element):
        ''' Returns the element by finding from the page
        Parameters:
        element: The element finder tuple eg: (By.NAME,'ELEMENT_NAME') '''
        time.sleep(config.ACTION_DELAY)
        myElem = WebDriverWait(self.driver, config.WEB_DRIVER_WAIT).until(EC.presence_of_element_located(element))
        return myElem

    class ToDoList:

        def go_to_completed_tab(self):
            self.get_element(COMPLETE_BTN).click() 
            

        def go_to_all_tab(self):
            self.get_element(ALL_BTN).click() 

        
        def go_to_active_tab(self):
            self.get_element(ACTIVE_BTN).click() 

        
        def clear_completed(self):
            self.get_element(CLEAR_COMPLETED_BTN).click()       

 
        # add New items to TO DO LIST
        def add_new_todo_items(self,*items): 
            for item in items:
                self.get_element(NEW_TODO_LOCATOR).send_keys(item,Keys.RETURN)


        # get all the to do task NAME and return in a list
        def todo_name_list(self): 
            todo_items = []
            items = self.driver.find_elements(*TODO_LIST_ITEMS)
            for item in items:
                text = item.text
                todo_items.append(text)
                    
            return todo_items


        # get the quantity that is presetend on the bottom ->  "x items left"
        def left_items(self ): 
            left = self.driver.find_element(*TODO_ITEMS_LEFT).text
            qty = left.split()[0]      
            return int(qty)


        # Get a list of all IDS in ALL tab
        def list_of_all_ids_all_tab(self):
            id_list = []
            ids = self.driver.find_elements(*TODO_LIST_ITEMS)
            for id in ids:
                value = id.get_attribute("data-id")
                id_list.append(value)

            return id_list
        
        # Get a list of all IDS from the current tab
        def list_of_all_ids_current_tab(self):
            id_list = []
        
            ids = self.driver.find_elements(*TODO_LIST_ITEMS)
            for id in ids:
                value = id.get_attribute("data-id")
                id_list.append(value)

            return id_list


        # get a list of all COMPLETED IDS from current tab
        def list_of_completed_ids_all_tab(self):
            completed_id_list = []
            completed_ids = self.driver.find_elements(*TODO_COMPLETED_IDS)
            for id in completed_ids:
                value = id.get_attribute("data-id")
                completed_id_list.append(value)


            return completed_id_list
        def list_of_completed_ids_completed_tab(self):
            completed_id_list = []
            completed_ids = self.driver.find_elements(*TODO_COMPLETED_IDS)
            for id in completed_ids:
                value = id.get_attribute("data-id")
                completed_id_list.append(value)

            return completed_id_list
        

        def list_of_completed_ids_active_tab(self):
            completed_id_list = []
            completed_ids = self.driver.find_elements(*TODO_COMPLETED_IDS)
            for id in completed_ids:
                value = id.get_attribute("data-id")
                completed_id_list.append(value)

            return completed_id_list
        

        # Get a list o ACTIVE IDS from current tab 
        def list_of_active_ids_all_tab(self):
            active_ids = []
            all_ids = self.list_of_all_ids_all_tab()
            completed_ids = self.list_of_completed_ids_all_tab()

            for id in set(all_ids) - set(completed_ids):
                active_ids.append(id)
            
            return active_ids
        


        def list_of_active_ids_active_tab(self):
            active_ids = []
            all_ids = self.list_of_all_ids_current_tab()
            completed_ids = self.list_of_completed_ids_active_tab()

            for id in set(all_ids) - set(completed_ids):
                active_ids.append(id)
            
            return active_ids
        
        
        def list_of_all_ids_active_tab(self):
            id_list = []
            ids = self.driver.find_elements(*TODO_LIST_ITEMS)
            for id in ids:
                value = id.get_attribute("data-id")
                id_list.append(value)

            return id_list

        
        # Build a specific selector, get an ID and add to selector.
        def selector_builder(self,id):
            selector = (By.CSS_SELECTOR, f'li[data-id="{id}"]')
    
            return selector
        
        def click_checkbox(self, select_id):
            element = self.get_element(self.selector_builder(select_id))      # Build a selector and store it on element
            element.find_element(*CHECKBOX).click() 
        

        def delete_selected_id(self, id_selection):
            actions = ActionChains(self.driver)                                             # instantiating the ActionsChains C
            element_locator = self.get_element(self.selector_builder(id_selection))         # build the selector using the ID selected
            actions.move_to_element(element_locator).perform()
            element_locator.find_element(*DELETE_BTN).click()          
        

        def assert_correct_items_added(self, expected_todo_items, expected_items_left): 
            assert self.todo_name_list() == expected_todo_items      # Ensure the list of TO DO text matches with the text entered.
            assert self.left_items() == len(expected_items_left)          # Ensure the items left information matches with the qty of active items.
    

        def assert_complete_tab_shows_correct_info(self,select_id):
            all_ids_from_completed_tab = self.list_of_all_ids_current_tab()  # get all ids present on COMPLETED tab.
            assert len(all_ids_from_completed_tab) == 1     # Ensure there is only one item present on completed tab
            assert all_ids_from_completed_tab == select_id  # Ensure the item presented on COMPLETED tab is the same present on ALL tab


        def assert_active_tab_shows_correct_info(self, active_ids_from_all_tab, active_ids_from_active_tab):
            assert sorted(active_ids_from_all_tab) == sorted(active_ids_from_active_tab)


        def assert_delete_id_not_in_active_tab(self, id_selection):
            assert id_selection  not in self.list_of_active_ids_active_tab()


        def assert_delete_id_not_in_all_tab(self, id_selection):
            assert id_selection not in self.list_of_active_ids_all_tab()


        def assert_all_completed_ids_are_deleted(self,completed_ids_all_tab,completed_tab_all_ids):    
            assert len(completed_ids_all_tab) == 0      # Ensure the  ALL TAB has no completed item on it
            assert len(completed_tab_all_ids) == 0      # Ensure the COMPLETE tab is empty 
       
       
        def assert_item_is_unchecked(self):
            assert len(self.list_of_completed_ids_all_tab()) == 0               # Ensure there is only 1 ID completed, as I only checked 1 item as completed    
            assert len(self.list_of_active_ids_all_tab()) == self.left_items() # Ensure the ID completed is the one that supposed to be
     

        def assert_item_is_checked(self,expected_id):
            assert len(self.list_of_completed_ids_all_tab()) == 1               # Ensure there is only 1 ID completed, as I only checked 1 item as completed
            assert expected_id in self.list_of_completed_ids_all_tab()            # Ensure the ID completed is the one that supposed to be
            assert len(self.list_of_active_ids_all_tab()) == self.left_items()   # Ensure "left items" qty has decreased after the item was completed
        
       
        def assert_complete_tab_is_empty(self):
            assert len(self.list_of_all_ids_current_tab()) == 0

    