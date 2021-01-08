from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#this one is for identyfing the wen elements
from selenium.webdriver.common.by import By
# this is for checking for some conditions on the driver like if the required elements have laoded or not
from selenium.webdriver.support import expected_conditions as EC

# this one if for the driver to wait for specified time
from selenium.webdriver.support.ui import WebDriverWait

# this one is for selecting the elements in the drop down list
from selenium.webdriver.support.ui import Select

#for the mouse action we need to import hte below packages
from selenium.webdriver import ActionChains

#for UnitTesting Framework
import unittest


#for logging
import logging


import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("pref",{"download_default_directory":"C:\Download"})

#to send the logging to the log file and u can sepcify the level of logging to be considered
logging.basicConfig(filename="test.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %P'  ,level=logging.DEBUG)
#logging
logging.debug("This is debug log")
logging.info("This is info log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")


driver = webdriver.Chrome(executable_path="C:\Data\Python\SeleniumTraining\Drivers\chromedriver.exe",chrome_options=chromeOptions)

#this will make the transaction to wait
# impicit wait is applicable to all the elements in the page
# This has to be speciified only 1  time and it has to be in the begining of the code

driver.implicitly_wait(5)
# to maximize the window size
driver.maximize_window()



"""

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_url)
print(driver.title)
# for getting the xpath

#   driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)
driver.get("https://scientificgames.com")
driver.back()
print(driver.current_url)
print(driver.title)

driver.forward() # NAvigationg from previous page to the current page like formward button on the browset
print(driver.title)

time.sleep(5)
#Conditional Commands
# is_enabled and is_displayed can be used for any kind of web elements
# is_selected is used for check boxes and radio buttons

driver.get("http://advantageonlineshopping.com/")
time.sleep(3)
print(driver.current_url)
print(driver.title)
elem = driver.find_element_by_id("loginMiniTitle")
print(elem.is_enabled())
print(elem.is_displayed())
print(elem.is_selected())

user_elem =  driver.find_element_by_name("username")
print(elem.is_enabled())
print(elem.is_displayed())
pwd_elem =  driver.find_element_by_name("password")
print(elem.is_enabled())
print(elem.is_displayed())
#user_elem.send_keys("test123@test.com")
#pwd_elem.send_keys("Abc@123")
#driver.find_element_by_xpath("//*[@id='sign_in_btnundefined']").click()

"""
driver.get("https://www.expedia.com/")
driver.find_element(By.XPATH , "//*[@id='uitk-tabs-button-container']/li[2]/a/span").click()

#explciit wait
# WebDriverWait wil lwait for the number of seconds that is specified if the page open before then it is comes out if not will wait for the time specified
# Excpicit wait is based on condition and not on time, so it based on the element
#

wait = WebDriverWait(driver,10)
time.sleep(5)

# selecting the drop down list of items
#elemt = driver.find_element() #find the element of the dropdown list
#drp = Select(elemt) # to get all the items in the drop down list
# drp.select_by_visisble_text('') #thsi will list all the options to select based on the needs

#driver.close() # will only close the  currently focused browser
driver.quit() # will clsoe all the browesers that are opened by the application


