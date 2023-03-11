from selenium.webdriver.common.by import By
from PageObject.locator import *
from PageObject.element import BasePageElement, ClickablElement
from selenium.webdriver.support.wait import WebDriverWait


# super class for getting the driver in every subclass 
class BasePage:
  def __init__(self,driver):
    self.driver = driver

class MainPageElements(BasePage):
  Vacancy_input = BasePageElement(MainPageLocators.VACANCY_INPUT)
  no_vacancy_found = BasePageElement(MainPageLocators.VACANCY_RESULT_NULL)
  search_button = BasePageElement(MainPageLocators.VACANCY_SEARCH_BUTTON)

class AuthElements(BasePage):
  open_module = ClickablElement(authPageLocators.Login_button)
  login = BasePageElement(authPageLocators.EMAIL_INPUT)
  password = BasePageElement(authPageLocators.PASSWORD_INPUT)
  click_authorization = ClickablElement(authPageLocators.AUTHORIZATION_BUTTON)
  auth_alert = BasePageElement(authPageLocators.AUTHORIZATION_ALERT)

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
    self.elements = AuthElements(self.driver)

  def open_auth_module(self):
    self.elements.open_module

  def send_credentials(self, login, password):
    self.elements.login = login
    self.elements.password = password
  
  def click_authorize(self):
    self.elements.click_authorization
    response = self.elements.auth_alert
    return response
