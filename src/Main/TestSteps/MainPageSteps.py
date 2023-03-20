from selenium.webdriver.common.by import By
from src.Main.PageObject.MainPage import MainPageElements

class MainPage:
  def __init__(self, driver):
    self.driver = driver
    self.page = MainPageElements(self.driver)

  def search_vacancy(self, text: str):
    #basepageelement class __get__ method invoked
    self.page.Vacancy_input

    #BasePageElement class __set__ method invoked
    self.page.Vacancy_input = text

    self.page.search_button.click()
    result = self.page.no_vacancy_found
    return result