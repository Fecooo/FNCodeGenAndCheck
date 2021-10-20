from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\Program Files (x86)\chromedriver.exe")
"""PATH = "C:\Program Files (x86)\chromedriver.exe"""
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://nitestats.com/codes-checker')
time.sleep(0.5)

sebesseg = driver.find_element(By.XPATH, '//*[@id="tab-1"]/div[1]/div[2]/div/div/div/div[2]/div/button[3]')
sebesseg.click()
time.sleep(0.5)

new_url = "https://fecooo.github.io/codegenpotty/"
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
time.sleep(0.5)

random = driver.find_element(By.XPATH, '//*[@id="random"]')
random.click()
time.sleep(0.5)

generate = driver.find_element(By.XPATH, '//*[@id="generate"]')
generate.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])

kod = driver.find_element(By.XPATH, '//*[@id="codesForm"]')
kod.send_keys(Keys.CONTROL, "v")
time.sleep(0.5)

start = driver.find_element(By.XPATH, '//*[@id="ccStart"]')
start.click()
time.sleep(65)

for i in range(19):
    driver.switch_to.window(driver.window_handles[0])

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.5)

    random.click()
    time.sleep(0.5)

    generate.click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])

    kod.send_keys(Keys.CONTROL, "v")
    time.sleep(0.5)

    start.click()
    time.sleep(65)
    
valid = driver.find_element(By.XPATH, '//*[@id="cc-tabs"]/ul/li[2]/a')
valid.click()

blur = driver.find_element(By.XPATH, '//*[@id="blurCodes2"]')
blur.click()
