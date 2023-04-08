from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class RegistrationLocators:
  LOGIN_BUTTON: tuple = By.XPATH, "//button[text()=' შესვლა ']"
  REGISTRATION_BUTTON: tuple = By.XPATH, "//a[text() = ' გაიარე რეგისტრაცია და შექმენი პროფილი ']"
  PHONE_INPUT: tuple = By.XPATH, "(//form/div/input)[1]"
  PASSWORD_INPUT: tuple = By.XPATH, "(//form/div/input)[2]"
  NAME_SURNAME_INPUT: tuple = By.XPATH, "(//form/div/input)[3]"
  TERMS_CHECKBOX: tuple = By.XPATH, "(//form//input)[4]"
  CONTINUE_BUTTON: tuple = By.XPATH, "//button[text() = ' გაგრძელება ']"
  INVALID_PHONE_FORMAT: tuple = By.XPATH, "//small[text() = ' მობილურის ნომრის ფორმატი არ არის სწორი, გთხოვთ გადაამოწმოთ ']"
  INVALID_PASSWORD: tuple = By.XPATH, "//small[text() = ' პაროლი უნდა შედგებოდეს მინიმუმ 8 სიმბოლოსგან ']"
  INVALID_NAME_SURNAME: tuple = By.XPATH, "//small[text() = ' სახელი უნდა შედგებოდეს მინიმუმ ორი სიტყვისგან ']"
  MANDATORY_FIELD: tuple = By.XPATH, "//small[contains(text(), 'სავალდებულოა')]"
  USER_ALREADY_EXITS: tuple = By.XPATH, "//div[text() =  ' ასეთი მომხმარებელი უკვე არსებობს ']"
  ALL_INPUT_FIELD: tuple = By.XPATH, "//input[contains(@id, 'floatingInput')]"