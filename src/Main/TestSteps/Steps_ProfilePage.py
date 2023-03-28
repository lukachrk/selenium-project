from src.Main.PageObject.Elements.Elements_ProfilePage import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
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

  def fill_out_mandatory_fields(self, data) -> None:
    fields = self.element.mandatory_fields

    for i in fields:
      try:
        mandatory_text = i.find_element(By.XPATH, ".//small")
        if(mandatory_text):
          input_field = i.find_element(By.XPATH, ".//input")
          input_field.clear()
          input_field.send_keys(data)
      except NoSuchElementException:
        pass

  def select_option(self, Type:str, date:tuple):
    options = self.element.options_fields
    for i in options:
      try:
        option_label = i.find_element(By.XPATH, f"//div[text() = 'აირჩიე დაწყების {Type}']")
        if(option_label):
          i.click()
          self.driver.find_element(*date).click()
      except NoSuchElementException:
        pass

      
  def select_option(self,type:str) -> None:
    pass

  def is_save_button_enabled(self) -> bool:
    button = self.element.save_button
    return button.is_enabled()

  def field_has_validation(self, warning_type) -> bool:
    warning_element = self.element.invalid_format_warning

    if warning_element is not None:
      return warning_type in warning_element.text

    return False
