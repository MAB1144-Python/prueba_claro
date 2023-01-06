from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import numpy as np
import random
#JuanAutoO
driver = webdriver.Chrome('./chromedriver')
sleep(1)
driver.get('https://dineshvelhal.github.io/testautomation-playground/advanced.html')
sleep(1)
rating = driver.find_element('xpath','/html/body/div/div/div[2]/div/div[1]/table/tbody/tr/td[2]/label')
print("disculpas no logre extraer el rating")
print(rating.find_element(By.NAME('element')))

print("error")

passw = driver.find_element('xpath','//*[@id="txt_rating"]')
passw.send_keys(rating.get_attribute('element'))
cl= driver.find_element('xpath','//*[@id="check_rating"]')
cl.click()
sleep(10)
