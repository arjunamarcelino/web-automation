from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open the web
driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.tiket.com/")

# choose the trip
driver.find_element_by_xpath(
    "//*[@id='productWidget']/div[2]/div[1]/div[2]/div[1]/div/label").click()

# choose product
driver.find_element(By.ID, "productSearchFrom").send_keys("KNO")  # origin
driver.find_element_by_xpath("//*[@id='fromDropDownList-airport1']").click()
# driver.find_element_by_xpath("//*[@id='fromDropDownList-airport1']").click()
time.sleep(2)

# driver.find_element(By.ID, "productSearchTo").send_keys("CGK")  # dest

# driver.find_element_by_id("productSearchDeparture").clear()
# driver.find_element_by_id(
#     "productSearchDeparture").send_keys("Sen, 26 Jul 2021")

# driver.find_element_by_id("productSearchReturn").clear()
# driver.find_element_by_id("productSearchReturn").send_keys("Rab, 28 Jul 2021")


# submit product
# driver.find_element_by_xpath("//*[@id='productWidget']/div[2]/div[3]/button").click()


time.sleep(10)

# closes all the browsers
driver.quit()
