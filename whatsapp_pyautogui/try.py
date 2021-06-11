import threading
import time


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def execute(amount, adressed, message):
    # profile_path = "user-data-dir=/home/daniel/.config/google-chrome/storing"
    #
    # options = webdriver.ChromeOptions()
    # options.add_argument(profile_path)
    # browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
    browser.set_window_size(1,1)
    browser.set_window_position(10, (position*100))
    browser.get("https://web.whatsapp.com")

    time.sleep(5)
    search = WebDriverWait(browser, 500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#side > div.SgIJV > div > label > div > div._2_1wd.copyable-text.selectable-text")))
    search.send_keys(adressed)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    send = WebDriverWait(browser, 500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                              "#main > footer > div.vR1LG._3wXwX.copyable-area > div._2A8P4._2A1WX > div > div._2_1wd.copyable-text.selectable-text")))

    for i in range(amount):
        send.send_keys(message)
        send.send_keys(Keys.ENTER)

moin = (1000, 'Hyhf', 'Hallo')

threads = []
for x in range(2):
    profile_path = f"user-data-dir=/home/daniel/.config/google-chrome/storing{x}"

    options = webdriver.ChromeOptions()
    options.add_argument(profile_path)
    browser = webdriver.Chrome(executable_path="./chromedriver", options=options)

    position = x
    f1 = threading.Thread(target=execute, args=moin,)
    f1.start()
    threads.append(f1)


for thread in threads:
    thread.join()

print('Hello')