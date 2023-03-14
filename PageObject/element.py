from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePageElement:
  def __init__(self,locator: tuple, wait: int = 100):
    self.locator = locator
    self.wait = wait

  def __set__(self,obj,value):
    driver = obj.driver
    WebDriverWait(driver, self.wait).until(
      lambda driver: driver.find_element(*self.locator))
    driver.find_element(*self.locator).clear()
    driver.find_element(*self.locator).send_keys(value)

  def __get__(self,obj,owner):
    driver = obj.driver
    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      return element
    except NoSuchElementException:
      return None

class ClickablElement:
  def __init__(self, locator: tuple, wait: int = 10):
    self.locator = locator
    self.wait = wait

  def __get__(self,obj,value):
    driver = obj.driver
    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      element.click()
    except TimeoutException:
      pass