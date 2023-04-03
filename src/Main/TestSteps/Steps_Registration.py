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
    self.element.click_register
  
  def fill_out_phone_number(self, number:str):
    self.element.input_phone_number = number  
    
  def fill_out_password(self, password:str):
    self.element.input_phone_number = password 

  def fill_out_name_surname(self, name:str):
    self.element.input_phone_number = name

  def click_terms_checkbox(self):
    self.element.tick_terms_checkbox

  def click_continue(self):
    self.element.click_continue

