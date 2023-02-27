from selenium.webdriver.common.by import By

class authPageLocators:
  Login_button = (By.CLASS_NAME,'btn.color-base.login-btn.font-bold.ng-tns-c78-1.ng-star-inserted')

class MainPageLocators:
  vacancy_input = (By.CLASS_NAME,'form-control')
  vacancy_search_button = (By.TAG_NAME, 'button')
  vacancy_result = (By.TAG_NAME, 'vacancy-card')
  POPUP = (By.CLASS_NAME, 'btn.btn-medium')