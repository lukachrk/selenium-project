from src.Main.PageObject.Elements.element import *
from src.Main.PageObject.Locators.Locators_AuthModule import AuthModuleLocators

class AuthElements:
  def __init__(self, driver):
    self.driver = driver

  open_module = ClickablElement(AuthModuleLocators.Login_button)

  login = BasePageElement(AuthModuleLocators.EMAIL_INPUT)
  password = BasePageElement(AuthModuleLocators.PASSWORD_INPUT)

  click_authorization = ClickablElement(AuthModuleLocators.AUTHORIZATION_BUTTON)
  auth_alert = BasePageElement(AuthModuleLocators.AUTHORIZATION_ALERT)