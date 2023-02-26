from main import browser
from selenium.webdriver.common.by import By
from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
  locator = MainPageLocators.vacancy_input

class BasePage:
  def __init__(self,driver):
    self.driver = driver


class authModule(BasePage):

  send_input = SearchTextElement()

  def Open_Login(self):
    element  = self.driver.find_element(*authPageLocators.Login_button)

  def search_start(self):
    element = self.driver.find_element(*MainPageLocators.vacancy_search_button)
    element.click()

  def Password(self):
    pass

