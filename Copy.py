# Open Browser
# Selenium 4
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Go to WebPage

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("username")

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Push Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_locator.click()

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
assert text_locator == "Logged In Successfully"

# Verify button Log out is displayed on the new page
log_out_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_locator.is_displayed()
