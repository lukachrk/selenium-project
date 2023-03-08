from selenium.webdriver.common.by import By
from locator import *
from element import BasePageElement, ClickablElement
from selenium.webdriver.support.wait import WebDriverWait

# super class for getting the driver in every subclass 
class BasePage:
  def __init__(self,driver):
    self.driver = driver

class MainPageElements(BasePage):
  Vacancy_input = BasePageElement(MainPageLocators.VACANCY_INPUT)
  no_vacancy_found = BasePageElement(MainPageLocators.VACANCY_RESULT_NULL)
  search_button = BasePageElement(MainPageLocators.VACANCY_SEARCH_BUTTON)

class MainPageButtons(BasePage):
  click_login_button = ClickablElement(authPageLocators.Login_button)

class MainPage:
  def __init__(self, driver):
    self.driver = driver

    self.page = MainPageElements(self.driver)

  def search_vacancy(self, text):
    self.page.Vacancy_input
    self.page.Vacancy_input = text
    self.page.search_button.click()
    result = self.page.no_vacancy_found
    return result


class authModule(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.buttons = MainPageButtons(self.driver)
    self.elements = MainPageElements(self.driver)

  def Open_Login(self):
    self.buttons.click_login_button

  def send_credentials(self):
    pass

