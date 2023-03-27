from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class MainPageLocators:
  VACANCY_INPUT: tuple = By.CLASS_NAME, 'form-control'
  VACANCY_SEARCH_BUTTON: tuple = By.XPATH, '//app-search-panel/div/div[3]/button'
  VACANCY_RESULT_NULL: tuple = By.XPATH, "//span[text()='შედეგი არ მოიძებნა']"

  POPUP: tuple = By.CLASS_NAME, 'btn.btn-medium'
  NAVIGATION_LINKS: tuple = By.XPATH, 
  "//div[contains(@class, 'profile-nav-link')]/span[contains(@class, 'd-md-inline')]"

  HAMBURGER_DROPDOWN: tuple = By.XPATH, "//div[contains(@class, 'header-account')]"
  HAMBURGER_APPLICATION_SENT: tuple = By.XPATH, "//span[text() = 'გაგზავნილი აპლიკაციები']"

