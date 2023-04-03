from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class RegistrationLocators:
  LOGIN_BUTTON: tuple = By.XPATH, "//button[text()=' შესვლა ']"
  REGISTRATION_BUTTON: tuple = By.XPATH, "//a[text() = ' გაიარე რეგისტრაცია და შექმენი პროფილი ']"
  PHONE_INPUT: tuple = By.XPATH, "(//form//input)[1]"
  PASSWORD_INPUT: tuple = By.XPATH, "(//form//input)[2]"
  NAME_SURNAME_INPUT: tuple = By.XPATH, "(//form//input)[3]"
  TERMS_CHECKBOX: tuple = By.XPATH, "(//form//input)[4]"
  CONTINUE_BUTTON: tuple = By.XPATH, "//button[text() = ' გაგრძელება ']"