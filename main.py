from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from colorama import Fore
from colored import fg
from dhooks import Webhook
import time

"""tim = time.localtime()
current_time = time.strftime("%H:%M:%S", tim)"""
zold=fg('green')
# kérdések blokk
PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.add_argument('--log-level=3')

print("")
print(Fore.WHITE + " --> " + Fore.GREEN + "Mekkora adag kódokat szeretnél vizsgáltatni? (Minél nagyobb mennyiség annál lassabb lesz egy idő után)")
print(Fore.WHITE + " --> " + Fore.LIGHTBLUE_EX + "1 " + Fore.GREEN + "- 2500 " + Fore.LIGHTRED_EX + "(kb. 6 perc)")
print(Fore.WHITE + " --> " + Fore.LIGHTBLUE_EX + "2 " + Fore.GREEN + "- 5000 " + Fore.LIGHTRED_EX + "(kb. 11 perc)")
print(Fore.WHITE + " --> " + Fore.LIGHTBLUE_EX + "3 " + Fore.GREEN + "- 7500 " + Fore.LIGHTRED_EX + "(kb. 17 perc)")
print(Fore.WHITE + " --> " + Fore.LIGHTBLUE_EX + "4 " + Fore.GREEN + "- 10000 " + Fore.LIGHTRED_EX + "(kb. 22 perc)")
adag = int(input(Fore.WHITE + " --> " + Fore.GREEN + "Adag: " + Fore.LIGHTBLUE_EX + ""))

ismetles = 0
if adag == 1:
    ismetles = 4
elif adag == 2:
    ismetles = 9
elif adag == 3:
    ismetles = 14
elif adag == 4:
    ismetles = 19
else:
    print(Fore.RED + "Na fussunk neki mégegyszer.")

print("")
print(Fore.WHITE + " --> " + Fore.GREEN + "Hányszor vizsgálnád ezt az adagot?")
vizsgalas = int(input(Fore.WHITE + " --> " + Fore.GREEN + "Vizsgálás száma: " + Fore.LIGHTBLUE_EX + ""))

print("")
print(Fore.WHITE + " --> " + Fore.GREEN + "A bot képes Discord webhook-al üzenetet küldeni az eredményekről")
print(Fore.WHITE + " --> " + Fore.GREEN + "Szeretnéd használni ezt a funkciót? " + Fore.LIGHTBLUE_EX + "(i / n)")
valasz = input(Fore.WHITE + " --> " + Fore.GREEN + "Választásod: " + Fore.LIGHTBLUE_EX + "")
print("")

if valasz == "i":
    webhook = input(Fore.WHITE + " --> " + Fore.GREEN + "Add meg a DC webhook linkjét: " + Fore.LIGHTBLUE_EX + "")
    hook = Webhook(webhook)
    time.sleep(0.5)

    print(Fore.WHITE + " --> " + Fore.RED + "A bot munkára indul!" + Fore.WHITE + "")
    time.sleep(0.5)

    print("")
    print("= " * 50)
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.maximize_window()
    time.sleep(2)
    print("")
    print("= " * 50)
elif valasz == "n":
    print(Fore.WHITE + " --> " + Fore.GREEN + "Nem igényelted ezt a funkciót. " + Fore.RED + "A bot munkára indul!" + Fore.WHITE + "")
    time.sleep(0.5)
    
    print("")
    print("= " * 50)
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.maximize_window()
    time.sleep(2)
    print("")
    print("= " * 50)
else:
    print(Fore.WHITE + " --> " + Fore.RED + "Nem tudom értelmezni")

# automata vizsgálás blokk
if valasz == "i" or valasz == "n":
    idokezdet = time.time()
    driver.get('https://nitestats.com/codes-checker')
    time.sleep(0.5)

    new_url = "https://fecooo.github.io/codegenhu/"
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.get(new_url)
    time.sleep(0.5)

    for i in range(vizsgalas):
        def program():
            driver.switch_to.window(driver.window_handles[0])

            for k in range(3):
                le = driver.find_element(By.TAG_NAME, 'html')
                le.send_keys(Keys.ARROW_DOWN)
            
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

            for j in range(ismetles):
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
            
            if valasz == "i":
                print("")
                print(Fore.WHITE + " --> " + Fore.LIGHTGREEN_EX + "Érvényes kódok száma: " + Fore.CYAN + validsz.text)
                print(Fore.WHITE + " --> " + Fore.LIGHTYELLOW_EX + "Használt kódok száma: " + Fore.CYAN + used.text)
                print(Fore.WHITE + " --> " + Fore.LIGHTRED_EX + "Hibás kódok száma: " + Fore.CYAN + error.text)

                hook.send("Érvényes kódok száma: " + "**" + validsz.text + "**")
                hook.send("Használt kódok száma: " + "**" + used.text + "**")
                hook.send("Hibás kódok száma: " + "**" + error.text + "**")
            elif valasz == "n":
                print("")
                print(Fore.WHITE + " --> " + Fore.LIGHTGREEN_EX + "Érvényes kódok száma: " + Fore.CYAN + validsz.text)
                print(Fore.WHITE + " --> " + Fore.LIGHTYELLOW_EX + "Használt kódok száma: " + Fore.CYAN + used.text)
                print(Fore.WHITE + " --> " + Fore.LIGHTRED_EX + "Hibás kódok száma: " + Fore.CYAN + error.text)
            else:
                print("")
                print(Fore.WHITE + " --> " + Fore.RED + "Valami hiba történt.")

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

                if valasz == "i":
                    print("")
                    print(Fore.WHITE + " --> " + Fore.LIGHTGREEN_EX + "Érvényes kód: " + Fore.CYAN + validkod.text + Fore.BLUE + "")
                    hook.send("Érvényes kód: " + validkod.text)
                elif valasz == "n":
                    print(Fore.WHITE + " --> " + Fore.LIGHTGREEN_EX + "Érvényes kód: " + Fore.CYAN + validkod.text + Fore.BLUE + "")
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            time.sleep(2)
        program()

        idoveg = time.time()
        temp = idoveg-idokezdet-5

        hours = temp // 3600
        temp = temp - 3600 * hours
        minutes = temp // 60
        seconds = temp - 60 * minutes

        print("")
        print(Fore.WHITE + " --> " + Fore.GREEN + "A folyamat hossza: " + Fore.LIGHTBLUE_EX + '%02d:%02d:%02d' %(hours, minutes, seconds) + Fore.WHITE + "")
else:
    print(Fore.WHITE + " --> " + Fore.RED + "A bot nem indul el, mert nem adtál meg helyes adatot")