from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.data.go.kr/index.do"
driver.get(url)

element = driver.find_element(By.CLASS_NAME, 'input-text')
element.send_keys('학자금지원정보')
element.send_keys(Keys.ENTER)

file = driver.find_element(By.CLASS_NAME, "result-list").find_element(By.CSS_SELECTOR, "ul > li > div.bottom-area > a")
file.click()

time.sleep(5)