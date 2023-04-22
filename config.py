import os
BASE_DIRECTORY = os.getcwd()
# BASE_URL = "https://www.google.com/"
BASE_URL ="https://todomvc.com/examples/vanilla-es6"
#DRIVER
DRIVER_PATH = os.path.join(BASE_DIRECTORY, 'src', 'drivers') #use os.path.join to create a path
WEB_DRIVER_WAIT = 30
HEADLESS = False
ACTION_DELAY = 1
DOWNLOAD_WAIT_TIME = 30
DOWNLOAD_FOLDER = os.path.join(BASE_DIRECTORY,'src', 'media','download')

#Reporting
REPORT_TITLE = "To Do list Testing"
REPORT_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'reports')
INDIVIDUAL_REPORT = False
LOG_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'logs')

