from src.Main.PageObject.Elements.Elements_MainPage import MainPageElements
from selenium.webdriver.common.by import By
import time
from typing import Any

class MainPage:
	def __init__(self, driver):
		self.driver = driver
		self.element = MainPageElements(self.driver)

	def return_to_main_page(self) -> None:
		self.driver.get('https://awork.ge/user/home')

	def search_vacancy(self, text: str, city:str) -> None:
		self.element.Vacancy_input = text
		self.element.city_input = city
		self.element.search_button.click()

	#helper function for below methods
	def get_saved_vacancy_info(self) -> tuple[str, str]:
		vacancy = self.element.get_vacancy_info

		vacancy_title = vacancy.find_element(By.TAG_NAME, 'h6').text
		company_name = vacancy.find_element(By.TAG_NAME, 'p').text
		return (vacancy_title, company_name)

	def save_vacancy(self) -> tuple[str, str]:
		self.driver.execute_script("window.scrollTo(0, 1200)") 
		self.element.set_bookmark
		time.sleep(0.5)

		vacancy_info = self.get_saved_vacancy_info()
		return vacancy_info


	def check_for_saved_vacancy(self) -> tuple[str, str]:
		self.driver.get('https://awork.ge/user/profile?nav=saved')
		vacancy_info = self.get_saved_vacancy_info()
		return vacancy_info


	def vacancy_not_found(self) -> Any:
		warning = self.element.no_vacancy_found

		if(warning is not None):
			return warning.text
		else:
			return False
		