import unittest
from selenium.webdriver.common.by import By
from src.Main.utils.DriverSetup import browser
from src.Main.TestSteps import Steps_Authentication, Steps_ProfilePage
from src.Main.TestData.secret_keys import SecretKeys as SKEYS
import time

chrome_driver = browser()
driver = chrome_driver.get_driver()
steps = Steps_ProfilePage.Profile(driver)

def setUpModule():
  driver.get('https://awork.ge/user/home')

  #close the popup, when page gets loaded
  driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()
  authmodule = Steps_Authentication.AuthModule(driver)
  authmodule.open_auth_module()

  #provide your credentials here to authorize into system
  authmodule.send_credentials(login = SKEYS.login, password = SKEYS.Password)

  authmodule.click_authorize()
  time.sleep(3)
  driver.get("https://awork.ge/user/profile")


# def tearDownModule():
#   driver.quit()

if __name__ == '__main__':
  unittest.main()

