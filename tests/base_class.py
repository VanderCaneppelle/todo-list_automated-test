import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import config, pytest, time
from selenium.webdriver.common.keys import Keys


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
        # add New items to TO DO LIST
        def add_new_todo_items(self,element,*items): 
            for item in items:
                self.get_element(element).send_keys(item,Keys.RETURN)


        # get all the to do task NAME and return in a list
        def todo_name_list(self,TODO_LIST_ITEMS): 
            todo_items = []
            items = self.driver.find_elements(*TODO_LIST_ITEMS)
            for item in items:
                text = item.text
                todo_items.append(text)
                    
            return todo_items


        # get the quantity that is presetend on the bottom ->  "x items left"
        def left_items(self,TODO_ITEMS_LEFT ): 
            left = self.driver.find_element(*TODO_ITEMS_LEFT).text
            qty = left.split()[0]      
            return int(qty)


        # Get a list of all IDS in ALL tab
        def list_of_all_ids(self,TODO_LIST_ITEMS, BTN_TO_CLICK):
            id_list = []
            self.get_element(BTN_TO_CLICK).click()
            ids = self.driver.find_elements(*TODO_LIST_ITEMS)
            for id in ids:
                value = id.get_attribute("data-id")
                id_list.append(value)

            return id_list
        
        # Get a list of all IDS from the current tab
        def list_of_all_ids_current_tab(self,TODO_LIST_ITEMS):
            id_list = []
        
            ids = self.driver.find_elements(*TODO_LIST_ITEMS)
            for id in ids:
                value = id.get_attribute("data-id")
                id_list.append(value)

            return id_list


        # get a list of all COMPLETED IDS from current tab
        def list_of_completed_ids_current_tab(self,TODO_COMPLETED_IDS):
            completed_id_list = []
            completed_ids = self.driver.find_elements(*TODO_COMPLETED_IDS)
            for id in completed_ids:
                value = id.get_attribute("data-id")
                completed_id_list.append(value)

            return completed_id_list
        

        # Get a list o ACTIVE IDS from current tab 
        def list_of_active_ids_current_tab(self,TODO_COMPLETED_IDS,TODO_LIST_ITEMS):
            active_ids = []
            all_ids = self.list_of_all_ids_current_tab(TODO_LIST_ITEMS)
            completed_ids = self.list_of_completed_ids_current_tab(TODO_COMPLETED_IDS)

            for id in set(all_ids) - set(completed_ids):
                active_ids.append(id)
            
            return active_ids
        
        # Build a specific selector, get an ID and add to selector.
        def selector_builder(self,id):
            selector = (By.CSS_SELECTOR, f'li[data-id="{id}"]')
    
            return selector
        

        def assertNewItems(self, expected_todo_items, expected_items_list):

            assert self.todo_name_list(self.TODO_LIST_ITEMS) == self.NEW_ITEMS                                       # Ensure the list of TO DO text matches with the text entered.          
            assert self.left_items(self.TODO_ITEMS_LEFT) == len(self.list_of_all_ids_current_tab(self.TODO_LIST_ITEMS))
