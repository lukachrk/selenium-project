from selenium.webdriver.common.by import By
from src.Main.PageObject.ProfilePage import ProfileElements
from src.Main.PageObject.locators.locator import ProfileLocators

class Profile:
  def __init__(self, driver):
    self.driver = driver
    self.elements = ProfileElements(self.driver)
  
  def navigate_to(self, navlink:str = None): 
    result = self.elements.nav_links
    links = {elem.text: elem for elem in result}

    self.driver.implicitly_wait(10)
    links[navlink].click()

  def open_module(self, module:str):
    self.driver.implicitly_wait(10)
    self.driver.find_element(By.XPATH, ProfileLocators.PROFILE_CARDS[module]).click()


  def fill_out(self, module:str, data: tuple):
    module_dicts = ProfileLocators.MODULE_ELEMENTS[module]
    #nested for loop list comprehention to get locators from module dict keys
    module_locators = [value for dicts in module_dicts for value in dicts.values()]

    for i in range(len(module_locators)):
      self.driver.implicitly_wait(10)

      module_element = self.driver.find_element(*module_locators[i])
      module_element.clear()
      module_element.send_keys(data[i])
  
  def is_button_enabled(self):
    button = self.elements.save_button
    return button.is_enabled()
    
  def select_option(self,options):
    pass