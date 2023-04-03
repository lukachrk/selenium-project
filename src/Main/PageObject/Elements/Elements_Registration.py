from src.Main.PageObject.Elements.element import *
from src.Main.PageObject.Locators.Locators_Registration import RegistrationLocators

class RegistrationElements:
  def __init__(self, driver):
    self.driver = driver

  open_authentication = ClickablElement(RegistrationLocators.LOGIN_BUTTON)
  click_register = ClickablElement(RegistrationLocators.REGISTRATION_BUTTON)
  input_phone_number = BasePageElement(RegistrationLocators.PHONE_INPUT)
  input_password = BasePageElement(RegistrationLocators.PASSWORD_INPUT)
  input_name_surname = BasePageElement(RegistrationLocators.NAME_SURNAME_INPUT)
  tick_terms_checkbox = BasePageElement(RegistrationLocators.TERMS_CHECKBOX)
  click_continue = ClickablElement(RegistrationLocators.CONTINUE_BUTTON)