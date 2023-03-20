from src.Main.PageObject.locators.element import *
from src.Main.PageObject.locators.locator import ProfileLocators

class ProfileElements:
  def __init__(self, driver):
    self.driver = driver
    
  nav_links = ClickablElement(ProfileLocators.NAVIGATION_LINKS, elements = True)

  upload_cv = ClickablElement(ProfileLocators.MY_CV)
  click_save = ClickablElement(ProfileLocators.SAVE_BUTTON)
  open_dropdown = ClickablElement(ProfileLocators.DROPDOWNS)
  check_label = ClickablElement(ProfileLocators.FORM_CHECK)