from src.Main.PageObject.Elements.Elements_Registration import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import Any 
import time

class Registration:
  def __init__(self, driver):
    self.driver = driver
    self.element = RegistrationElements(self.driver)

  def navigate_to_registration(self) -> None:
    self.element.open_authentication
    time.sleep(0.5)
    self.element.click_register
  
  
  def fill_out_phone_number(self, number:str) -> None:
    self.element.input_phone_number = number  
    

  def fill_out_password(self, password:str) -> None:
    self.element.input_password = password 


  def fill_out_name_surname(self, name:str)  -> None:
    self.element.input_name_surname = name


  def click_terms_checkbox(self) -> None:
    self.element.tick_terms_checkbox


  def click_continue(self) -> None:
    self.element.click_continue


  def got_warning(self, warningType: str) -> Any:
    warning  = None

    match warningType:
      case 'number':
        warning = self.element.warning_invalid_phone_number
      case 'password':
        warning = self.element.warning_invalid_password
      case 'name':
        warning = self.element.warning_invalid_name_surname
      case 'user':
        warning = self.element.warning_user_already_registered

    if(warning):
      return warning.text
    else:
      return False

  def field_is_mandatory(self) -> list[str]:
    input_fields = self.element.all_inputs

    for i in input_fields:
      time.sleep(1)
      i.clear()
      i.send_keys(1)
      i.send_keys(Keys.CONTROL, 'a')
      i.send_keys(Keys.BACKSPACE)

    mandatory_fields = self.element.warning_field_required
    return [warning.text for warning in mandatory_fields]
