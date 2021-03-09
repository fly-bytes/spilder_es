from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#selenium dom等待
def wait(driver, dom=By.ID, data='myDynamicElement'):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((dom, data))
        )
    finally:
        driver.quit()
