from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("Chrome opened")

driver.get("https://authorized-partner.vercel.app/")
print("Home page opened")
time.sleep(5)

driver.find_element(By.XPATH, "//a[@href='/login']").click()
print("Clicked Login")
time.sleep(5)

driver.find_element(By.XPATH, "//a[text()='Sign Up']").click()
print("Clicked Sign Up")
time.sleep(5)

print("Opened Register page")
time.sleep(5)

terms_element = driver.find_element(By.XPATH, "//*[contains(text(),'I agree')]")
driver.execute_script("arguments[0].click();", terms_element)
print("Terms accepted")
time.sleep(3)

driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()
print("Clicked Continue")
time.sleep(5)

print("Reached 'Set up your Account' page")

wait = WebDriverWait(driver, 20)

all_inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[not(@type='hidden')]")))

all_inputs[0].send_keys("Test")                     # First Name
all_inputs[1].send_keys("User")                     # Last Name
all_inputs[2].send_keys("testuser123@example.com")  # Email
all_inputs[3].send_keys("9855050277")               # Phone

driver.find_element(By.NAME, "password").send_keys("Test@1234")
driver.find_element(By.NAME, "confirmPassword").send_keys("Test@1234")

print("Account details filled")
time.sleep(5)

driver.find_element( By.XPATH, "//button[contains(text(),'Next')]").click()

print("Reached at Email Verification")

# NOTE:
# Automation stops here because email verification (OTP) requires access to a real email inbox.

time.sleep(120)

driver.quit()
