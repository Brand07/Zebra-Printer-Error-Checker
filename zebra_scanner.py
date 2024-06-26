#import requests
#from bs4 import BeautifulSoup
#from datetime import datetime
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


acc_dsg = "http://10.10.113.236/"


driver = webdriver.Firefox()
driver.set_window_size(1024, 768) # Set the window size to 1920x1080

def check_for_printer_errors(printer, printer_name):
    try:
        driver.get(printer)
        # Check for the Serial number
        # To confirm connection to the printer
        serial_number = driver.find_element(By.XPATH, '/html/body/center[1]/h2').text
        print(f"Connection to {printer_name} successful. Serial Number: {serial_number}")
    except TimeoutException:
        print(f"Connection to {printer_name} failed. Unable to locate serial number.")
        return False
    
    try:
        # Check for any errors
        status_message = driver.find_element(By.XPATH, '/html/body/center[1]/h3[1]').text
        if status_message == "Status: READY":
            print("No errors found on printer.")
        else:
            print(f"Error found on {printer_name}: {status_message}")
            return True
    except:
        print(f"No errors found on {printer_name}.")
        return False
    driver.quit()

check_for_printer_errors(acc_dsg, "DSG Printer")

        



