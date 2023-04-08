from src.Main.PageObject.Elements.Elements_MainPage import MainPageElements
import time

class MainPage:
	def __init__(self, driver):
		self.driver = driver
		self.element = MainPageElements(self.driver)

	
	def search_vacancy(self, text: str):
		self.element.Vacancy_input = text
		self.element.search_button.click()

	def vacancy_not_found(self):
		warning = self.element.no_vacancy_found

		if(warning is not None):
			return warning.text
		else:
			return False