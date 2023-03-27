from src.Main.PageObject.Elements.element import *
from src.Main.PageObject.Locators.Locators_MainPage import MainPageLocators

class MainPageElements:
  def __init__(self, driver):
    self.driver = driver
    
  Vacancy_input = BasePageElement(MainPageLocators.VACANCY_INPUT)
  no_vacancy_found = BasePageElement(MainPageLocators.VACANCY_RESULT_NULL)
  search_button = BasePageElement(MainPageLocators.VACANCY_SEARCH_BUTTON)