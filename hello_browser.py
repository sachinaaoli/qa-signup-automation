from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Script started...")

options = Options()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print("Chrome opened successfully")

driver.get("https://www.google.com")
print("Website opened")

time.sleep(15)  # <-- VERY IMPORTANT (15 seconds)

driver.quit()
print("Browser closed")
