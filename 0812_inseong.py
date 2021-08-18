from selenium import webdriver
import time

url = 'https://www.phone-direct.co.kr/shop/item.php?it_id=1606021985'

driver = webdriver.Chrome()
driver.get(url)

print(driver.window_handles)
time.sleep(5)