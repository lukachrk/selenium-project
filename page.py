from main import browser
from selenium.webdriver.common.by import By
from locator import *

class BasePage:
  def __init__(self):
    self.Browser = browser()
    self.driver  = self.Browser.get_driver()


class authModule(BasePage):
  def Open_Login(self):
    element  = self.driver.find_element(*authPageLocators.Login_button)

  def Password(self):
    pass
