from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\Data\Python\SeleniumTraining\Drivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\Data\Python\SeleniumTraining\Drivers\geckodriver.exe")

driver.get("http://google.com/")
print(driver.current_url) # return the url of the page
print(driver.title) #title of the page

driver.close()