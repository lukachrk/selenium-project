from src.Main.PageObject.Elements.element import *
from src.Main.PageObject.Locators.Locators_ProfilePage import ProfileLocators, Module_locators



class ProfileElements:
  def __init__(self, driver):
    self.driver = driver

  nav_links = ClickablElement(ProfileLocators.NAVIGATION_LINKS, elements = True)
  upload_cv = ClickablElement(Module_locators.CV_UPLOAD)
  save_button = BasePageElement(ProfileLocators.SAVE_BUTTON)
  click_save = ClickablElement(ProfileLocators.SAVE_BUTTON)
  open_dropdown = ClickablElement(ProfileLocators.DROPDOWNS)
  check_label = ClickablElement(ProfileLocators.FORM_CHECK)
  close_button = ClickablElement(ProfileLocators.CLOSE_BUTTON)
  invalid_format_warning = BasePageElement(ProfileLocators.INVALID_FORMAT)
  mandatory_fields = ClickablElement(ProfileLocators.MANDATORY_FIELDS, elements=True)
  options_fields = ClickablElement(ProfileLocators.OPTION_FIELDS, elements=True)
  click_until_now = ClickablElement(ProfileLocators.OPTION_UNTIL_NOW)
  options_list = ClickablElement(ProfileLocators.OPTIONS_LIST)
  all_input_fields = ClickablElement(ProfileLocators.ALL_INPUT_FIELD, elements=True)
  mandatory_options_from = BasePageElement(ProfileLocators.MANDATORY_OPTION_FROM)
  mandatory_options_to = BasePageElement(ProfileLocators.MANDATORY_OPTION_TO)
  success_message = BasePageElement(ProfileLocators.SUCCCESS_ALERT)
  click_my_project_url = ClickablElement(ProfileLocators.MY_PROJECT_URL)


class CardElements:
  def __init__(self, driver, locator):
    self.driver = driver
    self.base_element = ClickablElement(locator)

  def open_module(self):
    return self.base_element.__get__(self, None)
    
class FieldElements:
  def __init__(self, driver, locator):
    self.driver = driver
    self.base_element = BasePageElement(locator)

  def send_input(self, value):
    return self.base_element.__set__(self, value)



  





  

  