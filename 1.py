from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='D:/chromedriver/chromedriver.exe')
# driver.implicitly_wait(30) # 隐性等待，最长等30秒  
driver.get('https://huilansame.github.io')
locator = (By.LINK_TEXT, 'CSDN')
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
    print(driver.find_element_by_link_text('CSDN').get_attribute('href'))
finally:
    driver.close
