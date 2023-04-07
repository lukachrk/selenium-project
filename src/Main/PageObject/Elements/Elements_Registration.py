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
  all_inputs = ClickablElement(RegistrationLocators.ALL_INPUT_FIELD, elements=True)

  tick_terms_checkbox = ClickablElement(RegistrationLocators.TERMS_CHECKBOX)

  click_continue = ClickablElement(RegistrationLocators.CONTINUE_BUTTON)

  warning_invalid_phone_number = BasePageElement(RegistrationLocators.INVALID_PHONE_FORMAT)
  warning_invalid_password = BasePageElement(RegistrationLocators.INVALID_PASSWORD)
  warning_invalid_name_surname = BasePageElement(RegistrationLocators.INVALID_NAME_SURNAME)
  warning_field_required  = ClickablElement(RegistrationLocators.MANDATORY_FIELD, elements=True)
  warning_user_already_registered = BasePageElement(RegistrationLocators.USER_ALREADY_EXITS)