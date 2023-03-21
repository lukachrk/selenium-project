from selenium.webdriver.common.by import By
from src.Main.PageObject.AuthModule import AuthElements

class authModule:
  def __init__(self, driver):
    self.driver = driver
    self.elements = AuthElements(self.driver)

  def open_auth_module(self):
    self.elements.open_module

  def send_credentials(self, login, password):
    self.elements.login = login
    self.elements.password = password
  
  def click_authorize(self):
    self.elements.click_authorization
    response = self.elements.auth_alert
    return response