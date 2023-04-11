from selenium.webdriver.common.by import By
from src.Main.PageObject.Elements.Elements_AuthModule import AuthElements
import time

class AuthModule:
  def __init__(self, driver):
    self.driver = driver
    self.elements = AuthElements(self.driver)

  def open_auth_module(self) -> None:
    self.elements.open_module

  def send_credentials(self, login, password) -> None:
    self.elements.login = login
    self.elements.password = password
  
  def click_authorize(self) -> None:
    self.elements.click_authorization
    time.sleep(2)