# todo-list_test_automation_with_python

This repository tests the To do list site https://todomvc.com/examples/vanilla-es6
This code tests the funcionalities of the To Do List such as? 
- Creation of new todo items.
- Delete items of the list.
- Check as completed option.
- Quantity is left items (X items left)
- The buttons: All, Active, Completed, Clear Completed

## Quick Start
- ##### Clone To Do List Automated Test into your repos folder.
    <pre>
    git clone https://github.com/VanderCaneppelle/todo-list_automated-test.git</pre>

- ##### Create and activate virtual environment and Install required Python Packages
    - Install pipenv
    <pre>
    pip install pipenv
    </pre>
    - Create a virtual environment and install the packages
    <pre>
    pipenv install
    </pre> 
    (This command will create a new environnment and install all the packages from pipfile)
    

- #### Running the script
- We can run the complete testing by using the below command
<pre>
pipenv run python -m pytest
</pre>
or just
<pre>
pytest
</pre>
- If you want to run in a different browser then you can add one more argument here like below.
<pre>
pytest --browser_name firefox
</pre>
- If you want to run in a HEADLESS mode, go to config.py file, set: then run the command pytest or pipenv run python -m pytest
<pre>
 HEADLESS = True
</pre>
- then run the command pytest or pipenv run python -m pytest
<

## Folder Structure
- todo-list-automated-tests
    - Locators 
    - src
        - Drivers 
        - logs
        - Reports
    - Tests
    - Config.py
    - Conftest.py

## todo-list-automated_tests:
### Folder Description
**Driver**
- As selenium supports different drivers for different browsers, this folder contains the web drivers that we are going to use on our project.
    Ex:- For chrome browser:- chomedriver.exe

**Locators**
- This foldes contains all the locator for the elements used on this test.

**Logs**
- Contains the test execution logs

**Reports**
- Contains the test case execution report file after test case execution.

**Tests**
- Contains test cases 
 
**Config.py**
- A config.py (configuration) file contains all the settings for the tests.


**Conftest.py**
- conftest is the test configuration file for pytest using which we can change the way pytest is working. From adding the setup and teardown to every test case to import external plugins or modules we can configure these easily.



