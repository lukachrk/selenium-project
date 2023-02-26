from selenium.webdriver.common.by import By

class authPageLocators:
  Login_button = (By.NAME,'შესვლა')

class MainPageLocators:
  vacancy_input = (By.CLASS_NAME,'form-control')
  vacancy_search_button = (By.XPATH, "//div[contains(@class,'div.form-group.search-form.ng-tns-c80-2')]/button")