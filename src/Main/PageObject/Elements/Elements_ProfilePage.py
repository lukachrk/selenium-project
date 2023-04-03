from src.Main.PageObject.Elements.element import *
from src.Main.PageObject.Locators.Locators_ProfilePage import ProfileLocators, Module_locators



class ProfileElements:
  def __init__(self, driver):
    self.driver = driver

  nav_links = ClickablElement(ProfileLocators.NAVIGATION_LINKS, elements = True)

  save_button = BasePageElement(ProfileLocators.SAVE_BUTTON)
  close_button = ClickablElement(ProfileLocators.CLOSE_BUTTON)

  click_save = ClickablElement(ProfileLocators.SAVE_BUTTON)
  click_until_now = ClickablElement(ProfileLocators.OPTION_UNTIL_NOW)
  click_my_project_url = ClickablElement(ProfileLocators.MY_PROJECT_URL)
  check_label = ClickablElement(ProfileLocators.FORM_CHECK)

  invalid_format_warning = BasePageElement(ProfileLocators.INVALID_FORMAT)
  success_message = BasePageElement(ProfileLocators.SUCCCESS_ALERT)

  all_input_fields = ClickablElement(ProfileLocators.ALL_INPUT_FIELD, elements=True)
  mandatory_fields = ClickablElement(ProfileLocators.MANDATORY_FIELDS, elements=True)

  options_fields = ClickablElement(ProfileLocators.OPTION_FIELDS, elements=True)
  option_field_items = ClickablElement(ProfileLocators.OPTION_FIELD_ITEMS, elements=True)
  options_field_names = ClickablElement(ProfileLocators.OPTION_FIELD_NAMES,elements=True)

  mandatory_options_from = BasePageElement(ProfileLocators.MANDATORY_OPTION_FROM)
  mandatory_options_to = BasePageElement(ProfileLocators.MANDATORY_OPTION_TO)

  youtube_url = BasePageElement(Module_locators.YOUTUBE_INPUT)
  video_upload = UploadElement(Module_locators.VIDEO_UPLOAD)

  add_skill = BasePageElement(Module_locators.SKILL_INPUT)
  skills_list = BasePageElement(Module_locators.SKILLS_LIST)

  certificate_name = BasePageElement(Module_locators.CERTIFICATE_INPUT)
  upload_certificate = UploadElement(Module_locators.CERTIFICATE_UPLOAD)

  user_registered_warning = BasePageElement(Module_locators.USER_ALREADY_REGISTERED)
  invalid_cv_warning = BasePageElement(Module_locators.INVALID_CV_WARNING)

  upload_cv = UploadElement(ProfileLocators.UPLOAD_CV)
  cv_document = BasePageElement(ProfileLocators.UPLOADED_CV)
  cv_uploaded_success_message = BasePageElement(ProfileLocators.CV_UPLOADED_SUCCESSFULY)
  delete_cv = ClickablElement(ProfileLocators.DELETE_CV)
  click_yes = ClickablElement(ProfileLocators.DELETE_CV_YES)

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



  





  

  