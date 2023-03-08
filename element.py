from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

"""
the selenium pageobject documentation is outdated and doesn't work
my solution: decosntructing instance variable self.locator as a tuple from locator module
since the driver.get_element_by_name has been removed 
"""

"""
update: class elements take locator as an argument, thus removing the neccesity to inherit them into sub classes
and reducing amount of sub classes we make for every element we want to find on the page
"""


class BasePageElement:
  def __init__(self,locator, wait = 100):
    self.locator = locator
    self.wait = wait

  def __set__(self,obj,value):
    driver = obj.driver
    WebDriverWait(driver, self.wait).until(
      lambda driver: driver.find_element(*self.locator))
    driver.find_element(*self.locator).click()
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
  def __init__(self, locator, wait = 10):
    self.locator = locator
    self.wait = wait

  def __get__(self,obj,value):
    driver = obj.driver
    try:
      element = WebDriverWait(driver, self.wait).until(lambda driver: driver.find_element(*self.locator))
      element.click()
    except TimeoutException:
      pass