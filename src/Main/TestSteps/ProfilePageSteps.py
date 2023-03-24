from selenium.webdriver.common.by import By
from src.Main.PageObject.ProfilePage import ProfileElements
from src.Main.PageObject.locators.locator import ProfileLocators
import typing

class Profile:
  def __init__(self, driver):
    self.driver = driver
    self.elements = ProfileElements(self.driver)
  
  def navigate_to(self, navlink:str = None) -> None: 
    result = self.elements.nav_links
    links = {elem.text: elem for elem in result}

    self.driver.implicitly_wait(10)
    links[navlink].click()

  def open_module(self, module:str) -> None:
    self.driver.implicitly_wait(10)
    self.driver.find_element(By.XPATH, ProfileLocators.PROFILE_CARDS[module]).click()

  def close_module(self) -> None:
    self.elements.close_button

  def save_changes(self) -> None:
    self.elements.save_button

  def fill_out_field(self, module:str, field:str, data) -> None:
    locator = ProfileLocators.MODULE_ELEMENTS[module][field]
    element = self.driver.find_element(*locator)
    element.clear()
    element.send_keys(data)


  def fill_out_fields(self, module:str, data: str) -> None:
    locators = [value for value in ProfileLocators.MODULE_ELEMENTS[module].values()]

    for i in locators:
      self.driver.implicitly_wait(10)

      module_element = self.driver.find_element(*i)
      module_element.clear()
      module_element.send_keys(data)
  
  def select_option(self,options) -> None:
    pass

  def is_save_button_enabled(self) -> bool:
    button = self.elements.save_button
    return button.is_enabled()

  def field_has_validation(self):
    pass
    