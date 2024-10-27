import _thread
import time
import threading

from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("www.google.com")

time.sleep(3)

driver.refresh()

TOGGLE_KEY = KeyCode(char="t")
clicking = False
mouse = Controller()


def clicker():
    count = 0;
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            count += 1
            if count > 5000:
                driver.refresh()
                count = 0
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
