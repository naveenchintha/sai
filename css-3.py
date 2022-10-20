import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\navee\Downloads\chromedriver_win32\chromedriver.exe.")
driver.get(r"https://www.facebook.com/login.php/")
time.sleep(5)
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input[placeholder=Email address or phone number]").send_keys("agga")
driver.find_element(By.CSS_SELECTOR,"[placeholder=Email address or phone number]").send_keys("agga")


time.sleep(10)