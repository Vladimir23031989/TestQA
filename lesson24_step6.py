import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

button = browser.find_element(By.XPATH, '//*[@id="input_11_10"]')
button.click()
time.sleep(5)



time.sleep(20)
browser.quit()






