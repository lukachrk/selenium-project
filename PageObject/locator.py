from selenium.webdriver.common.by import By

class authPageLocators:
  Login_button = (By.CLASS_NAME, 'btn.color-base.login-btn.font-bold.ng-tns-c78-1.ng-star-inserted')

  EMAIL_INPUT = (By.ID, 'floatingInput1')
  PASSWORD_INPUT = (By.ID, 'floatingInput2')
  
  AUTHORIZATION_BUTTON = (By.XPATH, "//button[text()=' ავტორიზაცია ']")
  AUTHORIZATION_ALERT = (By.XPATH, 
  "//div[text()=' ავტორიზაცია წარმატებულია ' or  text()=' მობილურის ნომერი ან პაროლი არასწორია ']")


class MainPageLocators:
  VACANCY_INPUT = (By.CLASS_NAME, 'form-control')
  VACANCY_SEARCH_BUTTON = (By.XPATH, '//app-search-panel/div/div[3]/button')
  VACANCY_RESULT_NULL = (By.XPATH, "//span[text()='შედეგი არ მოიძებნა']")

  POPUP = (By.CLASS_NAME, 'btn.btn-medium')
  NAVIGATION_LINKS = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), ' nav-item')]")

  HAMBURGER_DROPDOWN = (By.XPATH, "//div[contains(@class, 'header-account')]")
  HAMBURGER_PROFILE = (By.XPATH, "//div[contains(@class,'nav-item') ]/a")
  HAMBURGER_APPLICATION_SENT = (By.XPATH, "//span[text() = 'გაგზავნილი აპლიკაციები']")


class ProfileLocators:
  NAVIGATION_LINKS = (By.XPATH, 
  "//div[contains(concat(' ', normalize-space(@class), ' '), ' profile-nav-link')]")