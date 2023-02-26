from selenium.webdriver.support.wait import WebDriverWait
"""
the selenium pageobject documentation is outdated and doesn't work
my solution: decosntructing instance variable self.locator as a tuple from locator module
since the driver.get_element_by_name has been removed from
"""
class BasePageElement:
  def __set__(self,obj,value):
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element(*self.locator))
    driver.find_element(*self.locator).clear()
    driver.find_element(*self.locator).send_keys(value)

  def __get__(self,obj,owner):
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element(*self.locator))
    element = driver.find_element(*self.locator)
    return element
