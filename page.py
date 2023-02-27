from selenium.webdriver.common.by import By
from locator import *
from element import BasePageElement, ClickablElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchTextElement(BasePageElement):
  locator = MainPageLocators.vacancy_input


class BasePage:
  def __init__(self,driver):
    self.driver = driver


class MainPage(BasePage):
  send_input = SearchTextElement()

  def search_start(self):
    element = self.driver.find_elements(*MainPageLocators.vacancy_search_button)
    element[9].click()
    return WebDriverWait(self.driver, 400).until(EC.presence_of_element_located((By.XPATH,
      "//span[text()='შედეგი არ მოიძებნა']")))

class authModule(BasePage):
  send_input = SearchTextElement()

  def Open_Login(self):
    element  = self.driver.find_element(*authPageLocators.Login_button)

  def Password(self):
    pass

