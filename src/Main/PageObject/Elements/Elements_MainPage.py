from src.Main.PageObject.Elements.element import *
from src.Main.PageObject.Locators.Locators_MainPage import MainPageLocators

class MainPageElements:
  def __init__(self, driver):
    self.driver = driver
    
  Vacancy_input = BasePageElement(MainPageLocators.VACANCY_INPUT)
  city_input = BasePageElement(MainPageLocators.CITY_INPUT)

  no_vacancy_found = BasePageElement(MainPageLocators.VACANCY_RESULT_NULL)

  search_button = BasePageElement(MainPageLocators.VACANCY_SEARCH_BUTTON)
  open_hamburger = ClickablElement(MainPageLocators.HAMBURGER_DROPDOWN)
  set_bookmark = ClickablElement(MainPageLocators.SAVE_BOOKMARK)
  get_vacancy_info = BasePageElement(MainPageLocators.VACANCY_INFO)