import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://clown-fish.ru/katalog-ribki"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

button = browser.find_element(By.XPATH, '//*[@id="rec389440883"]/div/div/div[1]/div[2]/div/div[3]')
button.click()
time.sleep(5)

b1 = browser.find_element(By.XPATH, '//*[@id="rec389109335"]/div[1]/div/div[3]/div[2]/a/div[1]/img[1]')
browser.execute_script ("return arguments[0].scrollIntoView(true);", b1)
time.sleep(5)

h1 = browser.find_element(By.XPATH, '//*[@id="rec389109335"]/div[1]/div/div[3]/div[2]/a/div[2]/div[1]')
text_h1 = h1.text
print(text_h1)

assert 'Гурами - Мрамор' == text_h1
print('Good')

time.sleep(20)
browser.quit()





