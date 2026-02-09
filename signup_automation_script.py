from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20) 

driver.get("https://authorized-partner.vercel.app/")
print("Website opened successfully")

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()
print("Clicked on Login")

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign Up']"))).click()
print("Clicked on Sign Up")

terms_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'I agree')]")))
driver.execute_script("arguments[0].click();", terms_checkbox)
print("Accepted terms")

driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()

print("Fill user details")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Your First Name']"))).send_keys("QA")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Last Name']").send_keys("Test")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("testusers1@mailinator.com")
driver.find_element(By.XPATH, "//input[contains(@placeholder, '00-')]").send_keys("9855500111")
driver.find_element(By.NAME, "password").send_keys("QaTest@1")
driver.find_element(By.NAME, "confirmPassword").send_keys("QaTest@1")
print("Form filled")

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='one-time-code']")))
print("OTP page fully loaded")


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

driver.get("https://www.mailinator.com/v4/public/inboxes.jsp?to=testusers1")

time.sleep(5)

email_cell = wait.until(EC.element_to_be_clickable(( By.XPATH,"//td[contains(@onclick,'showTheMessage') and contains(text(),'no-reply')]")))
email_cell.click()
print("Opened OTP email")

wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "html_msg_body")))

otp_element = wait.until(EC.presence_of_element_located((By.XPATH,"//p[normalize-space() and string-length(normalize-space())=6]")))

otp_code = otp_element.text.strip()
print("OTP extracted:", otp_code)

print("OTP:", otp_code)

driver.switch_to.default_content()
driver.close()
driver.switch_to.window(driver.window_handles[0])

otp_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='one-time-code']"))
)
otp_input.send_keys(otp_code)
print("OTP entered successfully")
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Verify')]"))
).click()

print("OTP verified successfully")

print("Filling Agency Details")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Agency Name']"))).send_keys(" Vrit Technologies")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Role in Agency']").send_keys("QA")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Agency Email Address']").send_keys("vrit.tech@mailinator.com")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Agency Website')]").send_keys("www.vrittechnologies.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Agency Address']").send_keys("Kathmandu, Nepal")

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Your Region of Operation')]"))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, " //div[@role='option'][1]"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]"))).click()

print("Agency details submitted")
print("Filling Professional Experience")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Select Your Experience Level')]"))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option'][1]"))).click()

driver.find_element(By.NAME, "success_metrics").send_keys("90")
driver.find_element(By.NAME, "focus_area").send_keys("Undergraduate admissions to Canada")
driver.find_element(By.NAME, "number_of_students_recruited_annually").send_keys("50")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='checkbox']"))).click()

print("Professional Experience filled")

print("Filling Verification & Preferences")

driver.find_element(By.NAME, "business_registration_number").send_keys("123456789")

driver.find_element(By.XPATH, "//span[contains(text(),'Select Your Preferred Countries')]").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]"))).click()

driver.find_element(By.XPATH, "//button[@role='checkbox']").click()
driver.find_element(By.NAME, "certification_details").send_keys("ICEF Certified Education Agent")

file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
file_inputs[0].send_keys(r"C:\Users\sachi\Documents\company_registration.pdf")
file_inputs[1].send_keys(r"C:\Users\sachi\Documents\education_certificate.pdf")

print("Documents uploaded")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]"))).click()
print("Signup completed successfully")
time.sleep(5)
driver.quit()