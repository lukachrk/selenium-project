from selenium.webdriver.common.by import By

class authPageLocators:
  Login_button = (By.CLASS_NAME,'btn.color-base.login-btn.font-bold.ng-tns-c78-1.ng-star-inserted')

class MainPageLocators:
  VACANCY_INPUT = (By.CLASS_NAME,'form-control')
  VACANCY_SEARCH_BUTTON = (By.XPATH, '//app-search-panel/div/div[3]/button')
  VACANCY_RESULT_NULL = (By.XPATH,"//span[text()='შედეგი არ მოიძებნა']")
  POPUP = (By.CLASS_NAME, 'btn.btn-medium')