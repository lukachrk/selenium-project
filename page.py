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

class MainButtons(BasePage):
  click_search_button = ClickablElement(MainPageLocators.VACANCY_SEARCH_BUTTON)



class MainPage:
  def __init__(self, driver):
    self.driver = driver

    self.page = MainPageElements(self.driver)
    self.buttons = MainButtons(self.driver)

  def search_vacancy(self, text):
    self.page.Vacancy_input
    self.page.Vacancy_input = text
    self.page.search_button.click()
    result = self.page.no_vacancy_found
    return result


class authModule(BasePage):

  def Open_Login(self):
    element  = self.driver.find_element(*authPageLocators.Login_button)

  def Password(self):
    pass

