from src.Main.PageObject.locators.element import *
from src.Main.PageObject.locators.locator import authPageLocators

class AuthElements:
  def __init__(self, driver):
    self.driver = driver

  open_module = ClickablElement(authPageLocators.Login_button)

  login = BasePageElement(authPageLocators.EMAIL_INPUT)
  password = BasePageElement(authPageLocators.PASSWORD_INPUT)

  click_authorization = ClickablElement(authPageLocators.AUTHORIZATION_BUTTON)
  auth_alert = BasePageElement(authPageLocators.AUTHORIZATION_ALERT)