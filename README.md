# automation_testing_with_python

This is a framework that will make your life easier in the field of automation testing. The goal of this framework is to making automation testing as easier as python that any one can learn and start using easily. your support will be highly appriciated in this process of making this as the easiest and effective framework in the field of automation testing. Please join us by contributing your inputs and giving this repo a star.  

https://user-images.githubusercontent.com/50165036/154853172-5a883d20-1fc3-4fbc-a4f8-7411dab2954c.mp4

#### Below are few useful features of this framework
- Modular Design.
- Report generation.
- Mailer to send the report.
- Events Log.
#### Prerequisite
- High learning sprit towards automation
- Basic knowledge in python

## Quick Start
- ##### Clone To Do List Automated Test into your repos folder.
    <pre>
    git clone https://github.com/VanderCaneppelle/todo-list_automated-test.git</pre>

- ##### Create and activate virtual environment and Install required Python Packages
    <pre>
    Open the project in your IDE
    Install pipenv -> pip install pipenv
    Create a virtual environment and install the packages - > pipenv install 
    This command will create a new environnment and install all the packages from pipfile
    </pre>

- #### Running the script
We can run the complete testing by using the below command
<pre>
pipenv run python -m pytest
or just 
pytest
</pre>
If you want to run in a different browser then you can add one more argument here like below.
<pre>
pytest --browser_name firefox
</pre>
If you want to run in a HEADLESS mode, go to config.py file, set HEADLESS = True then run the command pytest or pipenv run python -m pytest
</pre>

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



