from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class MainPageLocators:
  VACANCY_INPUT: tuple = By.CLASS_NAME, 'form-control'
  CITY_INPUT: tuple = By.XPATH, "//div[contains(@class, 'search-panel')]/div[2]/div/input"
  VACANCY_SEARCH_BUTTON: tuple = By.XPATH, '//app-search-panel/div/div[3]/button'
  VACANCY_RESULT_NULL: tuple = By.XPATH, "//span[text()='შედეგი არ მოიძებნა']"
  VACANCY_INFO: tuple = By.XPATH, "(//vacancy-list)[1]/div/div/div/div[1]/vacancy-card/a/div/div[2]"

  POPUP: tuple = By.CLASS_NAME, 'btn.btn-medium'

  HAMBURGER_DROPDOWN: tuple = By.XPATH, "//div[contains(@class, 'header-content')]/div[2]/button"
  HAMBURGER_APPLICATION_SENT: tuple = By.XPATH, "//span[text() = 'გაგზავნილი აპლიკაციები']"
  SAVE_BOOKMARK: tuple = By.XPATH, "(//div[contains(@class, 'favorite-btn')])[2]"
  
