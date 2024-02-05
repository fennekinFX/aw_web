import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

web_link = "WEBSITE"

chrome_options = Options()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(executable_path=r"C:\Users\User\chromedriver.exe", options=chrome_options)
browser.maximize_window()

browser.get(web_link)
time.sleep(3)
im2 = pyautogui.screenshot('Screenshot-maker/my_screenshot.png')

im2
