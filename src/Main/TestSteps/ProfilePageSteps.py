from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.Main.PageObject.ProfilePage import *

import typing

class Profile:
  def __init__(self, driver):
    self.driver = driver
    self.element = ProfileElements(self.driver)
  
  def navigate_to(self, navlink:str) -> None: 
    result = self.element.nav_links
    links = {elem.text: elem for elem in result}

    self.driver.implicitly_wait(10)
    links[navlink].click()

  def open_card(self, Card:str) -> None:
    card_element = CardElements(self.driver, Card)
    card_element.open_module()

  def close_module(self) -> None:
    self.element.close_button

  def save_changes(self) -> None:
    self.element.save_button

  def fill_out_field(self, field:str, data) -> None:
    field_element = FieldElements(self.driver,field)
    field_element.send_input(data)

  
  def select_option(self,options) -> None:
    pass

  def is_save_button_enabled(self) -> bool:
    button = self.element.save_button
    return button.is_enabled()

  def field_has_validation(self, warning_type) -> bool:
    warning_element = self.element.invalid_format_warning

    if warning_element is not None:
      return warning_type in warning_element.text

    return False
