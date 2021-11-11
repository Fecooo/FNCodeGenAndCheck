from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dhooks import Webhook
import time

tim = time.localtime()
current_time = time.strftime("%H:%M:%S", tim)
"""print(current_time)"""


s = Service("C:\Program Files (x86)\chromedriver.exe")

print(current_time, "- A bot képes Discord webhook-al üzenetet küldeni az eredményekről")
print("Szeretnéd használni ezt a funkciót?")
print("igen")
print("nem")
valasz = input("Választásod: ")
print(".")
print("Hányszor tízezer kódot akarsz megvizsgáltatni?")
darabszam = int(input("Döntésed: "))

if valasz == "igen":
    webhook = input("Add meg a DC webhook linkjét: ")
    hook = Webhook(webhook)
    time.sleep(2)
    print("A bot munkára indul!")
    time.sleep(0.5)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
elif valasz == "nem":
    print("Nem igényelted ezt a funkciót. A bot munkára indul!")
    time.sleep(0.5)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
else:
    print("Nem tudom értelmezni")

if valasz == "igen" or valasz == "nem":
    driver.get('https://nitestats.com/codes-checker')
    time.sleep(0.5)

    new_url = "https://fecooo.github.io/codegenhu/"
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.get(new_url)
    time.sleep(0.5)

    for i in range(darabszam):
        def program():
            driver.switch_to.window(driver.window_handles[0])

            sebesseg = driver.find_element(By.XPATH, '//*[@id="tab-1"]/div[1]/div[2]/div/div/div/div[2]/div/button[3]')
            sebesseg.click()
            time.sleep(0.5)

            driver.switch_to.window(driver.window_handles[1])

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

            for j in range(19):
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
            time.sleep(1)

            blur = driver.find_element(By.XPATH, '//*[@id="blurCodes2"]')
            blur.click()
            time.sleep(1)

            validsz = driver.find_element(By.XPATH, '//*[@id="validData"]')
            used = driver.find_element(By.XPATH, '//*[@id="inactiveData"]')
            error = driver.find_element(By.XPATH, '//*[@id="errorData"]')
            
            if valasz == "igen":
                print("Érvényes kódok száma: ", validsz.text)
                print("Használt kódok száma: ", used.text)
                print("Hibás kódok száma: ", error.text)

                hook.send("Érvényes kódok száma: " + "**" + validsz.text + "**")
                hook.send("Használt kódok száma: " + "**" + used.text + "**")
                hook.send("Hibás kódok száma: " + "**" + error.text + "**")
            elif valasz == "nem":
                print("Érvényes kódok száma: ", validsz.text)
                print("Használt kódok száma: ", used.text)
                print("Hibás kódok száma: ", error.text)
            else:
                print("Valami hiba történt.")

            if validsz.text == "1" or validsz.text == "2" or validsz.text == "3":
                copy = driver.find_element(By.XPATH, '//*[@id="copy-valid"]')
                copy.click()

                cucc = "https://fecooo.github.io/KodGyujto/"
                driver.execute_script("window.open('');")

                driver.switch_to.window(driver.window_handles[2])
                driver.get(cucc)
                time.sleep(0.5)

                mezo = driver.find_element(By.XPATH, '//*[@id="cuccos"]')
                mezo.send_keys(Keys.CONTROL, "v")

                add = driver.find_element(By.XPATH, '//*[@id="add"]')
                add.click()
                time.sleep(2)

                validkod = driver.find_element(By.XPATH, '//*[@id="panel"]/div')
                time.sleep(3)

                if valasz == "igen":
                    print("Érvényes kód: ", validkod.text)
                    hook.send("Érvényes kód: " + validkod.text)
                elif valasz == "nem":
                    print("Érvényes kód: ", validkod.text)
                else:
                    print("Sajnos nem találtam érvényes kódot. 🙁")
            else:
                print("Sajnos nem találtam érvényes kódot. 🙁")
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            time.sleep(10)
        program()
else:
    print("A bot nem indul el, mert nem adtál meg helyes adatot")