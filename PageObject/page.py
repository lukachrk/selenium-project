from selenium.webdriver.common.by import By
from PageObject.locator import *
from PageObject.element import BasePageElement, ClickablElement
from selenium.webdriver.support.wait import WebDriverWait


# super class for getting the driver in every subclass 
class BasePage:
  def __init__(self,driver):
    self.driver = driver


class MainPageElements(BasePage):
  Vacancy_input = BasePageElement(MainPageLocators.VACANCY_INPUT)
  no_vacancy_found = BasePageElement(MainPageLocators.VACANCY_RESULT_NULL)
  search_button = BasePageElement(MainPageLocators.VACANCY_SEARCH_BUTTON)


class AuthElements(BasePage):
  open_module = ClickablElement(authPageLocators.Login_button)

  login = BasePageElement(authPageLocators.EMAIL_INPUT)
  password = BasePageElement(authPageLocators.PASSWORD_INPUT)

  click_authorization = ClickablElement(authPageLocators.AUTHORIZATION_BUTTON)
  auth_alert = BasePageElement(authPageLocators.AUTHORIZATION_ALERT)

  

class ProfileElements(BasePage):
  nav_links = ClickablElement(ProfileLocators.NAVIGATION_LINKS, elements = True)

  upload_cv = ClickablElement(ProfileLocators.MY_CV)
  click_save = ClickablElement(ProfileLocators.SAVE_BUTTON)
  open_dropdown = ClickablElement(ProfileLocators.DROPDOWNS)
  check_label = ClickablElement(ProfileLocators.FORM_CHECK)




class MainPage:
  def __init__(self, driver):
    self.driver = driver
    self.page = MainPageElements(self.driver)

  def search_vacancy(self, text: str):
    #basepageelement class __get__ method invoked
    self.page.Vacancy_input

    #BasePageElement class __set__ method invoked
    self.page.Vacancy_input = text

    self.page.search_button.click()
    result = self.page.no_vacancy_found
    return result


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
  

  def select_option(self,options):
    pass

  