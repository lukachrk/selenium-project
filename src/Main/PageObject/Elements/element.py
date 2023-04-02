from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


#elements - a bool type that determines if we want to find single or many elements
class MainElement:
  def __init__(self, locator: tuple, wait: int = 10, elements: bool = False):
    self.locator = locator
    self.wait = wait
    self.elements = elements

class BasePageElement(MainElement):
  def __set__(self,obj,value):
    driver = obj.driver
    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      element.clear()
      element.send_keys(value)
    except NoSuchElementException:
      return None

  def __get__(self,obj,owner):
    driver = obj.driver
    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      return element
    except NoSuchElementException:
      return None

class ClickablElement(MainElement):
  def __get__(self,obj,value):
    driver = obj.driver

    #if elements bool is true, find all the elements and return them instead of clicking
    if(self.elements):
      try:
        element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_elements(*self.locator))
        return element
      except TimeoutException:
        pass

    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      element.click()
    except TimeoutException:
      pass

class UploadElement(MainElement):
  def __set__(self,obj,value):
    driver = obj.driver
    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      element.send_keys(value)
    except NoSuchElementException:
      return None