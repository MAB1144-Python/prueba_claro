from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

driver = webdriver.Chrome('./chromedriver')
sleep(1)
driver.get('https://dineshvelhal.github.io/testautomation-playground/login.html')
sleep(1)
name = driver.find_element('xpath','//*[@id="user"]')
name.send_keys('admin')
sleep(1)
passw = driver.find_element('xpath','//*[@id="password"]')
passw.send_keys('admin')
sleep(1)

#selección 1
login = driver.find_element('xpath','//*[@id="login"]')
login.click()
sleep(3)
cl= driver.find_element('xpath','//*[@id="rad_small"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="select_flavor"]/option[3]')
cl.click()
cl= driver.find_element('xpath','//*[@id="rad_barbeque"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="tomoto"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="quantity"]')
cl.send_keys('2')
cl= driver.find_element('xpath','//*[@id="submit_button"]')
cl.click()
sleep(10)

#selección 2
'''Pizza Size: Medium
Pizza Flavor: Pepperoni
Sauce: Barbeque
Toppings: Onions y Green Olive
Quantity: -21'''

cl= driver.find_element('xpath','//*[@id="rad_medium"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="select_flavor"]/option[2]')
cl.click()
cl= driver.find_element('xpath','//*[@id="rad_barbeque"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="tomoto"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="green_olive"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="onions"]')
cl.click()
cl= driver.find_element('xpath','//*[@id="quantity"]')
cl.send_keys('-21')
cl= driver.find_element('xpath','//*[@id="submit_button"]')
cl.click()

sleep(10)





