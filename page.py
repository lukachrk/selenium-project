from selenium.webdriver.common.by import By
from locator import *
from element import BasePageElement, ClickablElement
from selenium.webdriver.support.wait import WebDriverWait

# super class for getting the driver in every subclass 
class BasePage:
  def __init__(self,driver):
    self.driver = driver
"""
subclass for finding every neccesary element on main page
class variables: when created, the BasePageElement __get__ descriptor takes the locator and automatically finds it
"""
class MainPageElements(BasePage):
  Vacancy_input = BasePageElement(MainPageLocators.VACANCY_INPUT)
  no_vacancy_found = BasePageElement(MainPageLocators.VACANCY_RESULT_NULL)
  search_button = BasePageElement(MainPageLocators.VACANCY_SEARCH_BUTTON)


class MainPage(BasePage):
  def search_start(self, text):
    page = MainPageElements(self.driver)
    page.Vacancy_input #find the vacancy_input element (__get__ method invoked)
    page.Vacancy_input = text #send the text argument to the element (__set__ method invoked)
    page.search_button
    page.search_button[9].click()
    result = page.no_vacancy_found
    return result

class authModule(BasePage):

  def Open_Login(self):
    element  = self.driver.find_element(*authPageLocators.Login_button)

  def Password(self):
    pass

