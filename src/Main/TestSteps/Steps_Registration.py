from src.Main.PageObject.Elements.Elements_Registration import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import typing
import time

class Registration:
  def __init__(self, driver):
    self.driver = driver
    self.element = RegistrationElements(self.driver)

  def navigate_to_registration(self):
    self.element.open_authentication
    time.sleep(2)
    self.element.click_register
  
  def fill_out_phone_number(self, number:str):
    self.element.input_phone_number = number  
    
  def fill_out_password(self, password:str):
    self.element.input_password = password 

  def fill_out_name_surname(self, name:str):
    self.element.input_name_surname = name

  def click_terms_checkbox(self):
    self.element.tick_terms_checkbox

  def click_continue(self):
    self.element.click_continue

  def got_warning(self, warningType: str):
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

  def field_is_mandatory(self, field:str):
    mandatory_fields = self.element.warning_field_required

    match field:
      case 'phone':
        return mandatory_fields[0].text
      case 'password':
        return mandatory_fields[1].text
      case 'name':
        return mandatory_fields[2].text
      case _:
        return False
