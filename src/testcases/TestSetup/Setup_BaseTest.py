import unittest
from src.Main.utils.DriverSetup import browser
from selenium.webdriver.common.by import By

class BaseSetupClass(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    chrome_driver = browser()
    cls.driver = chrome_driver.get_driver()
    cls.driver.get('https://awork.ge/user/home')

    #close the popup, when page gets loaded
    cls.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

