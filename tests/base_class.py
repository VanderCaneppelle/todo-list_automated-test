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
        
        def add_new_todo_items(self,element,*items):
            for item in items:
                self.get_element(element).send_keys(item,Keys.RETURN)


        # get all the to do task NAME and return in a list
        def all_todo_items_list(self,TODO_LIST_ITEMS): 
            todo_items = []
            items = self.driver.find_elements(*TODO_LIST_ITEMS)
            for item in items:
                text = item.text
                todo_items.append(text)
                    
            return todo_items


        # get the text that is presetend on the bottom, with the items left information.
        def items_left(self,TODO_COUNT ): 
            left = self.driver.find_element(*TODO_COUNT).text
            qty = left.split()[0]      
            return int(qty)


        # get a list of all IDS in a tab
        def list_of_all_ids(self,TODO_LIST_ITEMS):
            id_list = []
            ids = self.driver.find_elements(*TODO_LIST_ITEMS)
            for id in ids:
                value = id.get_attribute("data-id")
                id_list.append(value)

            return id_list


        # get a list of all completed ids in a tab
        def list_of_completed_ids_current_tab(self,TODO_COMPLETED_IDS):
            completed_id_list = []
            completed_ids = self.driver.find_elements(*TODO_COMPLETED_IDS)
            for id in completed_ids:
                value = id.get_attribute("data-id")
                completed_id_list.append(value)

            return completed_id_list

        def list_of_active_ids_current_tab(self,TODO_COMPLETED_IDS,TODO_LIST_ITEMS):
            active_ids = []
            all_ids = self.list_of_all_ids(TODO_LIST_ITEMS)
            completed_ids = self.list_of_completed_ids_current_tab(TODO_COMPLETED_IDS)

            for id in set(all_ids) - set(completed_ids):
                active_ids.append(id)
            
            return active_ids
        
        def insert_id_into_selector(self,id):
            CHECKBOX = (By.CSS_SELECTOR, f'li[data-id="{id}"] input[type="checkbox"]')

            return CHECKBOX