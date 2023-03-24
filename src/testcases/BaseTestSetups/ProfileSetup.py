import unittest
from selenium.webdriver.common.by import By
from src.Main.utils.DriverSetup import browser
from src.Main.TestSteps import AuthModuleSteps, ProfilePageSteps
from src.Main.TestData.secret_keys import SecretKeys as SKEYS

chrome_driver = browser()
driver = chrome_driver.get_driver()
steps = ProfilePageSteps.Profile(driver)

def setUpModule():
  driver.get('https://awork.ge/user/home')

  #close the popup, when page gets loaded
  driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()
  authmodule = AuthModuleSteps.authModule(driver)
  authmodule.open_auth_module()

  #provide your credentials here to authorize into system
  authmodule.send_credentials(login = SKEYS.login, password = SKEYS.Password)

  authmodule.click_authorize()
  driver.get("https://awork.ge/user/profile")


def tearDownModule():
  driver.quit()



