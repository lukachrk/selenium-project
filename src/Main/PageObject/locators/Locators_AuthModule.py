from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class AuthModuleLocators:
  Login_button: tuple = By.XPATH, "//button[text()=' შესვლა ']"

  EMAIL_INPUT: tuple = By.ID, 'floatingInput1'
  PASSWORD_INPUT: tuple = By.ID, 'floatingInput2'
  
  AUTHORIZATION_BUTTON: tuple = By.XPATH, "//button[text()=' ავტორიზაცია ']"
  AUTHORIZATION_ALERT: tuple = By.XPATH, "//div[text()=' ავტორიზაცია წარმატებულია ' or  text()=' მობილურის ნომერი ან პაროლი არასწორია ']"

